# Câu hỏi thảo luận – Lab 02

## 1. Vì sao phải đồng bộ `master` trước khi gửi PR?
Khi phát triển song song, nhánh `master` có thể đã tiến thêm các commit mới từ PR của thành viên khác. Đồng bộ `origin/master` vào nhánh tính năng trước khi gửi PR giúp phát hiện sớm xung đột (conflict) và kiểm tra tích hợp ngay tại máy cá nhân (chạy thử chương trình/test), đảm bảo PR khi merge vào `master` không làm hỏng hệ thống.

## 2. Khi nào không được dùng `rebase`?
Không được `rebase` các commit đã được đẩy lên nhánh dùng chung (`master`, `release/*`) hoặc nhánh mà nhiều người đang cùng làm việc, vì `rebase` viết lại lịch sử (tạo mã SHA mới cho commit), gây lệch lịch sử và buộc người khác phải xử lý phân nhánh phức tạp.

## 3. `feature/*` khác `topic/*` ra sao?
- `feature/*`: Dùng cho việc phát triển chức năng/tính năng nghiệp vụ mới của sản phẩm (ví dụ: `feature/cart-print`, `feature/search-by-title`).
- `topic/*`: Dùng cho các công việc hỗ trợ quanh dự án như tài liệu, cấu hình kho chứa, template, chuẩn bị phát hành hoặc CI (ví dụ: `topic/pr-template`, `topic/use-case-diagram`).
