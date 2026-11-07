# Câu hỏi thảo luận – Lab 04

## 1. Vì sao chuẩn bị phát hành trên `master` trước, không sửa trực tiếp trên nhánh `release/*`?
Nhánh `release/*` được tạo ra để đóng băng baseline phát hành và bị khóa bởi Branch Protection. Nếu sửa số phiên bản và `CHANGELOG.md` trên `master` trước (qua PR), thì khi tách `release/lab04` từ `master`, cả `master` và `release/lab04` đều có sẵn lịch sử chuẩn bị phát hành đồng nhất mà không phải merge ngược từ `release/*` về `master`.

## 2. Vì sao `release/*` không bao giờ merge ngược vào `master`? So sánh với GitFlow.
- Trong **Release Flow**, `release/*` là dòng bảo trì riêng của một phiên bản đã phát hành (có thể chứa commit nâng phiên bản PATCH như `1.0.1`), trong khi `master` đã tiến lên phiên bản mới (`1.1.0`). Nếu merge cả nhánh `release/*` vào `master` sẽ gây xung đột số phiên bản và kéo các thay đổi chỉ dành cho dòng cũ vào `master`. Thay vào đó, chỉ các commit sửa lỗi mới được lan truyền bằng `cherry-pick`.
- So với **GitFlow** (duy trì song song hai nhánh dài hạn `main` và `develop`, và merge `release/*` vào cả hai), Release Flow gọn nhẹ hơn: chỉ có một nhánh tích hợp chính `master` và các nhánh `release/*` tách ra khi phát hành.

## 3. Vì sao lên phiên bản `1.0.0` mà không phải `0.4.0`?
Theo **Semantic Versioning (SemVer)**:
- Dải `0.y.z` (`v0.1.0`..`v0.3.0` ở Lab 01–03) dùng cho giai đoạn phát triển ban đầu khi tính năng và giao diện chưa ổn định.
- Khi phần mềm đã hoàn thiện các tính năng cốt lõi, vượt qua kiểm thử và sẵn sàng công bố bản phát hành ổn định chính thức đầu tiên làm baseline cam kết, phiên bản được nâng lên `1.0.0`.
