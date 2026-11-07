# Câu hỏi thảo luận – Lab 05

## 1. Ưu, nhược điểm của `upstream first` (sửa trên `master` trước) so với `release first` (sửa trên `release/*` trước)?
- **Release first (sửa trên `release/*` trước, dùng trong học phần)**:
  - *Ưu điểm*: Vá ngay đúng phiên bản đang chạy ngoài thực tế (`v1.0.0`), không bị vướng các thay đổi/tính năng mới chưa ổn định trên `master`; phát hành bản vá `v1.0.1` nhanh chóng.
  - *Nhược điểm*: Cần kỷ luật cherry-pick bản sửa ngược về `master` và các nhánh `release/*` khác đang hoạt động để tránh tái phát lỗi (regression) ở phiên bản sau.
- **Upstream first (sửa trên `master` trước)**:
  - *Ưu điểm*: Đảm bảo lỗi luôn được triệt tiêu trên nhánh phát triển chính trước tiên, không lo lỗi bị bỏ sót ở các bản phát hành tương lai.
  - *Nhược điểm*: Khi cherry-pick lùi về nhánh `release/*` cũ có thể gặp xung đột nếu mã nguồn trên `master` đã thay đổi cấu trúc nhiều so với bản cũ.

## 2. Nếu quên lan truyền bản sửa sang `release/lab05`, lệnh nào ở Phần F sẽ phát hiện?
- Lệnh kiểm toán commit tương đương:
  ```bash
  git cherry -v origin/release/lab05 origin/release/lab04
  ```
  Commit sửa lỗi (`fix: make search_by_title case-insensitive`) sẽ mang dấu `+` (chưa có mặt trên `release/lab05`) thay vì dấu `-`.
- Ngoài ra, vòng lặp kiểm tra hành vi thực tế trên 3 phiên bản (`for ref in v1.0.1 v1.1.0 master; do ...`) sẽ in ra `0` thay vì `1` tại `v1.1.0`.
