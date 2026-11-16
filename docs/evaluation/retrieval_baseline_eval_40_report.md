# Bộ Dữ Liệu Đánh Giá Baseline Retrieval: `baseline_eval_40.jsonl`

---

## 1. Tổng quan bộ 40 queries

File lưu trữ: [baseline_eval_40.jsonl](file:///home/minhkha/kk/TTTN/legal-agentic-rag-next/eval-sets/retrieval/baseline_eval_40.jsonl)

| Tiêu chí | Thông số |
|---|---|
| **Tổng số queries** | **40** queries |
| **Nguồn** | 10 legacy (chắt lọc từ `retrieval_eval.jsonl`) + 30 mới thiết kế |
| **Độ phủ văn bản** | **17/17 văn bản** trong `corpus-v0.2` (100% độ phủ) |
| **Độ phủ chunk** | **128 gold chunks** (trung bình 3.2 chunks/query, min 1, max 9) |
| **Tính hợp lệ chunk** | **100% chunk_id** đã được kiểm chứng tồn tại thực tế trong corpus |
| **Độ khó** | Dễ (13), Trung bình (19), Khó (8) |
| **Phân loại query** | Trách nhiệm chủ thể (8), Điều kiện áp dụng (7), Trình tự thủ tục (7), Hành vi cấm (4), Phân loại (3), Cơ chế thử nghiệm (2), Chính sách (2), Thẩm quyền (2), Minh bạch (1), Quản trị dữ liệu (1), Khu vực công (1), Trách nhiệm giải trình (1), Nguyên tắc (1) |

---

## 2. Ma trận độ phủ 17 văn bản trong `corpus-v0.2`

Legacy set (`retrieval_eval.jsonl`) trước đây **chỉ phủ 3/17 văn bản** (Luật AI, Nghị định AI, Thông tư AI). Bộ 40 query này phủ toàn diện cả 17 văn bản:

| Mã văn bản | Tên văn bản pháp lý | Lĩnh vực | Số chunks corpus | Queries legacy | Queries mới | Tổng queries |
|---|---|---|---:|---:|---:|---:|
| `134-2025-QH15` | Luật Trí tuệ nhân tạo | AI | 206 | 5 | 0 | **5** |
| `142-2026-ND-CP` | Nghị định hướng dẫn Luật Trí tuệ nhân tạo | AI | 503 | 4 | 0 | **4** |
| `05-2026-TT-BKHCN` | Khung đạo đức trí tuệ nhân tạo quốc gia | AI | 28 | 1 | 0 | **1** |
| `367-2026-QD-TTG` | Kế hoạch triển khai thi hành Luật AI | AI | 3 | 0 | 1 | **1** |
| `91-2025-QH15` | Luật Bảo vệ dữ liệu cá nhân | Dữ liệu cá nhân | 261 | 0 | 4 | **4** |
| `356-2025-ND-CP` | Nghị định hướng dẫn Luật BVDLCN | Dữ liệu cá nhân | 339 | 0 | 3 | **3** |
| `116-2025-QH15` | Luật An ninh mạng | An ninh mạng | 435 | 0 | 2 | **2** |
| `122-2025-QH15` | Luật Thương mại điện tử | Thương mại điện tử | 267 | 0 | 2 | **2** |
| `248-2026-ND-CP` | Nghị định hướng dẫn Luật TMĐT | Thương mại điện tử | 389 | 0 | 2 | **2** |
| `148-2025-QH15` | Luật Chuyển đổi số | Chuyển đổi số | 265 | 0 | 2 | **2** |
| `224-2026-ND-CP` | Nghị định hướng dẫn Luật Chuyển đổi số | Chuyển đổi số | 851 | 0 | 2 | **2** |
| `20-2023-QH15` | Luật Giao dịch điện tử | GD điện tử | 271 | 0 | 2 | **2** |
| `20-2026-VBHN-VPQH`| Luật Công nghiệp công nghệ số | CN công nghệ số | 255 | 0 | 2 | **2** |
| `47-2026-VBHN-VPQH`| Luật Bảo vệ quyền lợi người tiêu dùng | BV người tiêu dùng| 511 | 0 | 2 | **2** |
| `29-2026-VBHN-BCT` | Nghị định hướng dẫn Luật BVQLNTD | BV người tiêu dùng| 130 | 0 | 2 | **2** |
| `60-2024-QH15` | Luật Dữ liệu | Quản trị dữ liệu | 247 | 0 | 2 | **2** |
| `67-2026-VBHN-VPQH`| Luật Sở hữu trí tuệ | Sở hữu trí tuệ | 1,161 | 0 | 2 | **2** |
| **Tổng** | **17 văn bản** | **10 lĩnh vực** | **6,122** | **10** | **30** | **40** |

---

## 3. Danh sách 10 Legacy Queries được chắt lọc

Được lựa chọn từ [retrieval_eval.jsonl](file:///home/minhkha/kk/TTTN/legal-agentic-rag-next/eval-sets/retrieval/retrieval_eval.jsonl) theo tiêu chí: trạng thái đã xác minh (`verified`), gold chunks rõ ràng, đa dạng độ khó và chủ đề:

1. **`eval001`**: *Các mức phân loại rủi ro của hệ thống trí tuệ nhân tạo gồm những mức nào?* (Dễ, 3 chunks, `134-2025-QH15`)
2. **`eval004`**: *Nhà cung cấp hệ thống AI rủi ro cao phải duy trì những biện pháp quản lý nào?* (Trung bình, 6 chunks, `142-2026-ND-CP`)
3. **`eval007`**: *Nội dung do AI tạo ra phải được thông báo hoặc gắn nhãn như thế nào?* (Khó, 9 chunks, `142-2026-ND-CP`)
4. **`eval009`**: *Hệ thống AI tương tác trực tiếp với con người phải được thiết kế theo yêu cầu gì?* (Dễ, 1 chunk, `134-2025-QH15`)
5. **`eval011`**: *Cơ chế thử nghiệm có kiểm soát cho phép tổ chức, cá nhân được hưởng những cơ chế gì trong phạm vi thử nghiệm?* (Trung bình, 2 chunks, `134-2025-QH15`)
6. **`eval013`**: *Việc phân loại cấp độ thử nghiệm có kiểm soát dựa trên những tiêu chí nào?* (Trung bình, 5 chunks, `142-2026-ND-CP`)
7. **`eval019`**: *Cơ sở dữ liệu quốc gia phục vụ trí tuệ nhân tạo được tổ chức theo những nguyên tắc nào?* (Dễ, 1 chunk, `134-2025-QH15`)
8. **`eval024`**: *Những hành vi nào liên quan đến AI bị nghiêm cấm khi lợi dụng nhóm người dễ bị tổn thương?* (Dễ, 1 chunk, `134-2025-QH15`)
9. **`eval025`**: *Khi ứng dụng AI trong quản lý nhà nước, cơ quan vận hành phải đánh giá tác động trong trường hợp nào?* (Khó, 7 chunks, `142-2026-ND-CP`)
10. **`eval028`**: *Tổ chức phát triển hoặc triển khai AI cần bảo đảm trách nhiệm giải trình ra sao?* (Khó, 2 chunks, `05-2026-TT-BKHCN`)

---

## 4. Danh sách 30 New Queries thiết kế trải đều corpus

Tất cả 30 query được xây dựng dựa trên các điều khoản cụ thể, bám sát các câu hỏi tra cứu thực tế của doanh nghiệp và chuyên gia pháp lý:

| Query ID | Câu hỏi | Văn bản | Điều | Số chunks | Độ khó |
|---|---|---|---|---:|---|
| `new001` | Chủ thể dữ liệu cá nhân phải được cung cấp những thông tin gì trước khi đồng ý cho xử lý dữ liệu? | `91-2025-QH15` | Đ.9 | 3 | Dễ |
| `new002` | Trong trường hợp nào dữ liệu cá nhân được xử lý mà không cần sự đồng ý của chủ thể? | `91-2025-QH15` | Đ.19 | 3 | Trung bình |
| `new003` | Khi nào bên kiểm soát dữ liệu phải xóa hoặc hủy dữ liệu cá nhân? | `91-2025-QH15` | Đ.14 | 4 | Trung bình |
| `new004` | Hệ thống trí tuệ nhân tạo phải tuân thủ những yêu cầu bảo vệ dữ liệu cá nhân nào? | `356-2025-ND-CP` | Đ.10 | 4 | Khó |
| `new005` | Bên kiểm soát dữ liệu phải đáp ứng điều kiện gì khi chuyển giao dữ liệu cá nhân ra nước ngoài? | `356-2025-ND-CP` | Đ.7 | 4 | Khó |
| `new006` | Những hành vi nào bị nghiêm cấm trên không gian mạng theo Luật An ninh mạng? | `116-2025-QH15` | Đ.7 | 4 | Trung bình |
| `new007` | Chủ quản hệ thống thông tin phải thực hiện biện pháp bảo vệ an ninh mạng nào? | `116-2025-QH15` | Đ.26 | 4 | Khó |
| `new008` | Sàn giao dịch thương mại điện tử phải đáp ứng những nghĩa vụ gì đối với người tiêu dùng? | `122-2025-QH15` | Đ.14 | 3 | Trung bình |
| `new009` | Hoạt động quảng cáo trong thương mại điện tử phải tuân thủ những quy định nào? | `122-2025-QH15` | Đ.18 | 2 | Trung bình |
| `new010` | Thương nhân nước ngoài cung cấp dịch vụ thương mại điện tử tại Việt Nam phải đáp ứng điều kiện gì? | `248-2026-ND-CP` | Đ.5 | 3 | Trung bình |
| `new011` | Nền tảng số trung gian phải lưu trữ thông tin giao dịch trong thời hạn bao lâu? | `248-2026-ND-CP` | Đ.10 | 2 | Dễ |
| `new012` | Cơ quan nhà nước phải đảm bảo những yêu cầu gì khi cung cấp dịch vụ công trực tuyến? | `148-2025-QH15` | Đ.22 | 3 | Trung bình |
| `new013` | Chính sách phát triển kinh tế số bao gồm những nội dung chính nào? | `148-2025-QH15` | Đ.6 | 3 | Dễ |
| `new014` | Nền tảng số quy mô lớn phải đáp ứng những nghĩa vụ quản trị nào? | `224-2026-ND-CP` | Đ.10 | 3 | Khó |
| `new015` | Hoạt động quảng cáo trên nền tảng số phải tuân thủ những quy định gì? | `224-2026-ND-CP` | Đ.20 | 3 | Trung bình |
| `new016` | Chữ ký điện tử có giá trị pháp lý khi đáp ứng những điều kiện gì? | `20-2023-QH15` | Đ.22 | 3 | Trung bình |
| `new017` | Hợp đồng điện tử được giao kết theo trình tự nào? | `20-2023-QH15` | Đ.34 | 2 | Dễ |
| `new018` | Nhà nước hỗ trợ hoạt động nghiên cứu và phát triển sản phẩm công nghệ số bằng những biện pháp gì? | `20-2026-VBHN-VPQH` | Đ.16 | 3 | Dễ |
| `new019` | Cơ sở dữ liệu công nghiệp công nghệ số được thu thập và quản lý theo trách nhiệm của ai? | `20-2026-VBHN-VPQH` | Đ.35 | 3 | Trung bình |
| `new020` | Tổ chức kinh doanh phải thực hiện những trách nhiệm gì khi bán hàng trực tuyến cho người tiêu dùng? | `47-2026-VBHN-VPQH` | Đ.22 | 3 | Trung bình |
| `new021` | Trách nhiệm thu hồi sản phẩm khuyết tật của tổ chức kinh doanh được quy định như thế nào? | `47-2026-VBHN-VPQH` | Đ.36 | 3 | Trung bình |
| `new022` | Tổ chức quản lý chợ và trung tâm thương mại có trách nhiệm gì với người tiêu dùng? | `29-2026-VBHN-BCT` | Đ.5 | 3 | Trung bình |
| `new023` | Những hành vi nào bị nghiêm cấm trong quản lý và sử dụng dữ liệu? | `60-2024-QH15` | Đ.10 | 4 | Dễ |
| `new024` | Dữ liệu quan trọng và dữ liệu cốt lõi phải được bảo vệ theo yêu cầu nào? | `60-2024-QH15` | Đ.20 | 3 | Trung bình |
| `new025` | Tác phẩm nào không thuộc đối tượng bảo hộ quyền tác giả? | `67-2026-VBHN-VPQH` | Đ.15 | 3 | Dễ |
| `new026` | Hành vi nào bị coi là xâm phạm quyền sở hữu công nghiệp đối với nhãn hiệu? | `67-2026-VBHN-VPQH` | Đ.130 | 3 | Khó |
| `new027` | Kế hoạch triển khai thi hành Luật Trí tuệ nhân tạo giao cho các bộ ngành những nhiệm vụ gì? | `367-2026-QD-TTG` | Đ.1 | 1 | Dễ |
| `new028` | Nguyên tắc bảo vệ dữ liệu cá nhân theo Luật Bảo vệ dữ liệu cá nhân gồm những nội dung gì? | `91-2025-QH15` | Đ.3 | 3 | Dễ |
| `new029` | Cơ quan nhà nước phải lưu trữ hồ sơ đánh giá tác động bảo vệ dữ liệu cá nhân trong bao lâu? | `356-2025-ND-CP` | Đ.14 | 3 | Trung bình |
| `new030` | Doanh nghiệp phải giải quyết khiếu nại trực tuyến của người tiêu dùng trong thời hạn bao lâu? | `29-2026-VBHN-BCT` | Đ.15 | 3 | Trung bình |

---

## 5. Hướng dẫn chạy đánh giá Metric Baseline

Cấu trúc mỗi dòng trong `baseline_eval_40.jsonl` tương thích trực tiếp với hàm `retrieval_query_metrics` trong [metrics.py](file:///home/minhkha/kk/TTTN/legal-agentic-rag-next/src/legal_rag/evaluation/metrics.py):

```python
from legal_rag.evaluation.metrics import retrieval_query_metrics, aggregate_retrieval

# Với mỗi query:
row_metric = retrieval_query_metrics(
    gold_chunk_ids=item["gold_chunk_ids"],
    gold_article_ids=item["gold_article_ids"],
    retrieved_chunk_ids=retrieved_chunks_top_k,
    retrieved_article_ids=retrieved_articles_top_k,
)

# Tổng hợp toàn bộ:
summary = aggregate_retrieval(all_rows)
# Trả về: hit@1, hit@3, hit@5, recall@5, recall@10, mrr@10 ở cả chunk_level & article_level
```
