# Câu hỏi thảo luận – Lab 01

## 1. Vì sao dùng `git mv` thay vì xóa rồi tạo lại tệp?
`git mv` giúp Git ghi nhận thao tác đổi tên/di chuyển tệp trong staging area ngay lập tức, bảo toàn lịch sử thay đổi của tệp qua các commit (có thể truy vết bằng `git log --follow`). Trên Pull Request (tab Files changed), tệp được hiển thị là `renamed` thay vì bị xóa toàn bộ và thêm mới, giúp việc review rõ ràng và chính xác hơn.

## 2. `release/lab01` có phải baseline không?
Có. `release/lab01` đóng vai trò là một **baseline** – một trạng thái cấu hình đã được thống nhất và đóng băng tại thời điểm kết thúc Lab 01 để phục vụ việc nộp bài và kiểm toán cấu hình. Từ thời điểm này, không được commit trực tiếp lên `release/lab01`.

## 3. Vì sao không commit thẳng lên `master` dù làm một mình?
- Tuân thủ quy trình kiểm soát thay đổi (Change Control) trong SCM: mọi thay đổi đều đi qua nhánh riêng và Pull Request để có cơ hội tự kiểm tra toàn bộ diff trước khi tích hợp.
- Giữ nhánh `master` luôn ở trạng thái ổn định, chạy được.
- Tạo thói quen làm việc nhất quán giữa làm cá nhân và làm việc nhóm, sẵn sàng tích hợp với Branch Protection và CI/CD.
