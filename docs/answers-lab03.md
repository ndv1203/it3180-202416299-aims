# Câu hỏi thảo luận – Lab 03

## 1. Merge base là gì?
**Merge base** là commit tổ tiên chung gần nhất (best common ancestor) của hai nhánh cần hợp nhất. Git thực hiện **3-way merge** bằng cách so sánh 3 trạng thái: `merge base`, đầu nhánh hiện tại (`HEAD`), và đầu nhánh cần hợp nhất. Nếu một dòng chỉ thay đổi ở một phía so với `merge base`, Git tự động lấy thay đổi đó; nếu cả hai phía cùng sửa một vùng so với `merge base`, xung đột (merge conflict) sẽ xảy ra.

## 2. Vì sao trên `master` và `release/*` phải dùng `git revert` thay vì `git reset`?
`master` và `release/*` là các nhánh dùng chung, lịch sử đã được chia sẻ cho toàn bộ nhóm (và gắn với PR, tag, bản phát hành).
- `git reset` dời con trỏ nhánh lùi lại và viết lại lịch sử (xóa commit khỏi nhánh), đòi hỏi `push --force` – điều này bị chặn bởi Branch Protection và sẽ làm hỏng kho chứa của các thành viên khác.
- `git revert` tạo một **commit mới** có nội dung đảo ngược thay đổi của commit cũ, giữ nguyên lịch sử và cho phép hoàn tác an toàn thông qua Pull Request.
