from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools/validation"))

from validate_generation_eval import validate


class GenerationEvaluationValidationTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / "annotation/generation/generation_eval_v0.json").read_text(encoding="utf-8"))
        self.v1 = json.loads((ROOT / "annotation/generation/generation_eval_v1.json").read_text(encoding="utf-8"))
        verified_path = ROOT / "eval-sets/generation/generation_eval_v1_verified.json"
        self.verified = json.loads(verified_path.read_text(encoding="utf-8")) if verified_path.exists() else None
        self.retrieval = ROOT / "eval-sets/retrieval/retrieval_eval.jsonl"
        self.corpus = ROOT / "data/versions/corpus-v0.1/chunks.jsonl"

    def run_validation(self, data):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "dataset.json"
            path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
            return validate(path, self.retrieval, self.corpus)

    def point(self, **changes):
        point = {"point_id": "P1", "description": "A corpus-grounded legal requirement.", "importance": "required", "supporting_chunk_ids": ["134-2025-QH15_dieu-9_khoan-1_diem-a"]}
        point.update(changes)
        return point

    def as_draft_with_point(self, data):
        data["dataset_status"] = "draft"
        data["items"][0]["annotation_status"] = "draft"
        data["items"][0]["required_points"] = [self.point()]

    def test_current_template_is_valid(self):
        self.assertEqual(self.run_validation(self.data), [])

    def test_v1_dataset_is_valid(self):
        self.assertEqual(self.run_validation(self.v1), [])
        self.assertEqual(len(self.v1["items"]), 31)
        self.assertEqual(sum(len(item["required_points"]) for item in self.v1["items"]), 102)
        self.assertTrue(all(item["annotation_status"] == "draft" for item in self.v1["items"]))

    def test_v1_verified_dataset_is_valid(self):
        self.assertIsNotNone(self.verified)
        self.assertEqual(self.run_validation(self.verified), [])
        self.assertEqual(self.verified["dataset_status"], "verified")
        self.assertEqual(len(self.verified["items"]), 31)
        self.assertTrue(all(item["annotation_status"] == "verified" for item in self.verified["items"]))

    def test_duplicate_query_id_is_rejected(self):
        data = copy.deepcopy(self.data); data["items"][1]["query_id"] = data["items"][0]["query_id"]
        self.assertTrue(any("duplicate query_id" in e for e in self.run_validation(data)))

    def test_query_mismatch_is_rejected(self):
        data = copy.deepcopy(self.data); data["items"][0]["query"] = "changed"
        self.assertTrue(any("query differs" in e for e in self.run_validation(data)))

    def test_invalid_answerability_is_rejected(self):
        data = copy.deepcopy(self.data); data["items"][0]["answerability"] = "unknown"
        self.assertTrue(any("invalid answerability" in e for e in self.run_validation(data)))

    def test_invalid_importance_is_rejected(self):
        data = copy.deepcopy(self.data); self.as_draft_with_point(data); data["items"][0]["required_points"][0]["importance"] = "optional"
        self.assertTrue(any("invalid importance" in e for e in self.run_validation(data)))

    def test_empty_point_description_is_rejected(self):
        data = copy.deepcopy(self.data); self.as_draft_with_point(data); data["items"][0]["required_points"][0]["description"] = ""
        self.assertTrue(any("description is empty" in e for e in self.run_validation(data)))

    def test_duplicate_point_id_is_rejected(self):
        data = copy.deepcopy(self.data); self.as_draft_with_point(data); data["items"][0]["required_points"].append(self.point())
        self.assertTrue(any("duplicate point_id" in e for e in self.run_validation(data)))

    def test_nonexistent_chunk_is_rejected(self):
        data = copy.deepcopy(self.data); self.as_draft_with_point(data); data["items"][0]["required_points"][0]["supporting_chunk_ids"] = ["not-a-chunk"]
        self.assertTrue(any("nonexistent corpus chunk" in e for e in self.run_validation(data)))

    def test_non_gold_chunk_is_rejected(self):
        data = copy.deepcopy(self.data); self.as_draft_with_point(data); data["items"][0]["required_points"][0]["supporting_chunk_ids"] = ["134-2025-QH15_dieu-4_khoan-2"]
        self.assertTrue(any("not retrieval gold" in e for e in self.run_validation(data)))

    def test_verified_record_requires_answer_and_points(self):
        data = copy.deepcopy(self.data); data["dataset_status"] = "verified"; data["items"][0]["annotation_status"] = "verified"
        data["items"][0]["required_points"] = []; data["items"][0]["reference_answer"] = ""
        self.assertTrue(any("verified records require" in e for e in self.run_validation(data)))


if __name__ == "__main__":
    unittest.main()
