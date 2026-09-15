"""Audited allowlist for a fresh, single-purpose Python production process.

This guards ordinary Python file APIs and imports, including os.open and resolved
symlinks. It is an accidental-leakage boundary, not a sandbox for hostile native
extensions. Only reviewed runtime modules and model code may execute inside it.
"""
from __future__ import annotations
import os
from pathlib import Path
import sys

_ACTIVE = None
_INSTALLED = False


class ReadGuard:
    def __init__(self, *, files=(), directories=(), writable=(), denied=(), source_directory=None):
        self.files = {Path(p).resolve() for p in files}
        self.directories = tuple(Path(p).resolve() for p in directories)
        self.writable = tuple(Path(p).resolve() for p in writable)
        self.denied = tuple(Path(p).resolve() for p in denied)
        self.reads = []
        self.source_directory = Path(source_directory).resolve() if source_directory else None

    def check(self, value, write=False):
        if isinstance(value, int):
            # The worker starts with close_fds=True and no inherited data handles.
            return
        path = Path(os.fsdecode(value)).resolve()
        if any(path == p or p in path.parents for p in self.denied):
            raise PermissionError('Phase 5 denied path')
        roots = self.writable if write else self.directories + self.writable
        if (not write and path in self.files) or any(path == p or p in path.parents for p in roots):
            if not write:
                self.reads.append(str(path))
            return
        raise PermissionError('Phase 5 path outside allowlist: ' + str(path))

    def __enter__(self):
        global _ACTIVE, _INSTALLED
        if _ACTIVE is not None:
            raise RuntimeError('nested production guard')
        if self.source_directory:
            for module in tuple(sys.modules.values()):
                location = getattr(module, '__file__', None)
                if location:
                    path = Path(location).resolve()
                    if path.parent == self.source_directory and path not in self.files:
                        raise PermissionError('unapproved module already imported into production')
        if not _INSTALLED:
            sys.addaudithook(_audit)
            _INSTALLED = True
        _ACTIVE = self
        return self

    def __exit__(self, *args):
        global _ACTIVE
        _ACTIVE = None


def _audit(event, args):
    if _ACTIVE is None:
        return
    if event == 'open':
        mode, flags = args[1], args[2]
        write = (isinstance(mode, str) and any(c in mode for c in 'wax+')) or bool(flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC))
        _ACTIVE.check(args[0], write)
    elif event in ('os.listdir', 'os.scandir'):
        path = Path(os.fsdecode(args[0])).resolve() if not isinstance(args[0], int) else None
        if path is None or not any(p.parent == path for p in _ACTIVE.files):
            _ACTIVE.check(args[0])
    elif event == 'import' and args[1]:
        _ACTIVE.check(args[1])
    elif event in ('subprocess.Popen', 'os.system', 'os.posix_spawn', 'os.fork'):
        raise PermissionError('production child processes are forbidden')
    elif event in ('os.remove', 'os.rmdir', 'os.mkdir', 'os.chmod'):
        _ACTIVE.check(args[0], True)
    elif event in ('os.rename', 'os.link', 'os.symlink'):
        raise PermissionError('production aliases/replacement are forbidden')


def block_network():
    """Permanent process-wide transport gate, installed before application imports."""
    counts = {'blocked_network_attempts': 0, 'network_calls': 0}
    def hook(event, args):
        if event in ('socket.connect', 'socket.connect_ex', 'socket.getaddrinfo', 'socket.sendto', 'http.client.connect', 'urllib.Request'):
            counts['blocked_network_attempts'] += 1
            raise PermissionError('Phase 5 offline network guard')
    sys.addaudithook(hook)
    os.environ.update(HF_HUB_OFFLINE='1', TRANSFORMERS_OFFLINE='1', HF_HUB_DISABLE_TELEMETRY='1', PYTHONDONTWRITEBYTECODE='1')
    sys.dont_write_bytecode = True
    return counts
