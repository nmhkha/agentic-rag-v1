const form = document.querySelector("#query-form");
const queryInput = document.querySelector("#query");
const submitButton = document.querySelector("#submit");
const loading = document.querySelector("#loading");
const errorBox = document.querySelector("#error");
const resultPanel = document.querySelector("#result");
const answerBox = document.querySelector("#answer");
const statusBadge = document.querySelector("#status");
const latencyBox = document.querySelector("#latency");
const citationList = document.querySelector("#citations");
const emptyState = document.querySelector("#empty-state");
const statusLabels = {
  success: "Đã hoàn tất",
  insufficient_evidence: "Chưa đủ căn cứ",
  incomplete_answer: "Cần bổ sung thông tin",
  citation_check_failed: "Cần kiểm tra nguồn",
};

function setLoading(active) {
  submitButton.disabled = active;
  form.setAttribute("aria-busy", String(active));
  loading.classList.toggle("hidden", !active);
}

function renderCitations(citations) {
  citationList.replaceChildren();
  if (!citations.length) {
    const item = document.createElement("li");
    item.className = "no-sources";
    item.textContent = "Không có nguồn tham chiếu hợp lệ.";
    citationList.append(item);
    return;
  }
  for (const citation of citations) {
    const item = document.createElement("li");
    item.className = "source-item";
    const badge = document.createElement("span");
    badge.className = "evidence-id";
    badge.textContent = `[${citation.evidence_id}]`;
    const body = document.createElement("div");
    body.className = "source-body";
    const location = [
      citation.document_number,
      citation.article && `Điều ${citation.article}`,
      citation.clause && `Khoản ${citation.clause}`,
      citation.point && `Điểm ${citation.point}`,
    ].filter(Boolean).join(" · ");
    const title = document.createElement("strong");
    title.className = "source-title";
    title.textContent = citation.document_title || citation.chunk_id;
    body.append(title);
    if (location) {
      const detail = document.createElement("p");
      detail.className = "source-location";
      detail.textContent = location;
      body.append(detail);
    }
    if (citation.source_url) {
      const link = document.createElement("a");
      link.href = citation.source_url;
      link.target = "_blank";
      link.rel = "noreferrer";
      link.className = "source-link";
      link.textContent = "Xem nguồn chính thức ↗";
      body.append(link);
    }
    item.append(badge, body);
    citationList.append(item);
  }
}

function renderResult(payload, httpLatencyMs) {
  answerBox.textContent = payload.answer;
  statusBadge.textContent = statusLabels[payload.status] || payload.status;
  statusBadge.title = payload.status;
  statusBadge.dataset.status = payload.status;
  latencyBox.replaceChildren();
  for (const [label, value] of [["RAG", payload.rag_latency_ms], ["HTTP end-to-end", httpLatencyMs]]) {
    const metric = document.createElement("span");
    metric.textContent = `${label}: ${(value / 1000).toLocaleString("vi-VN", {minimumFractionDigits: 2, maximumFractionDigits: 2})} giây`;
    metric.title = `${value.toFixed(1)} ms`;
    latencyBox.append(metric);
  }
  renderCitations(payload.citations);
  resultPanel.classList.remove("hidden");
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  errorBox.classList.add("hidden");
  resultPanel.classList.add("hidden");
  emptyState.classList.add("hidden");
  setLoading(true);
  const started = performance.now();
  try {
    const response = await fetch("/api/v1/answers", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({query: queryInput.value}),
    });
    const payload = await response.json();
    const httpLatencyMs = performance.now() - started;
    if (!response.ok) throw new Error("request_failed");
    renderResult(payload, httpLatencyMs);
  } catch (error) {
    errorBox.textContent = "Chưa thể xử lý câu hỏi lúc này. Vui lòng thử lại sau và kiểm tra kết nối nếu lỗi tiếp tục xảy ra.";
    errorBox.classList.remove("hidden");
  } finally {
    setLoading(false);
  }
});
