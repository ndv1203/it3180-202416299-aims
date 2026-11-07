# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.1] - 2026-11-07
### Fixed
- Sửa `search_by_title()` không phân biệt hoa thường (#20).

## [1.0.0] - 2026-11-07
### Added
- `Cart.print_cart()` hiển thị chi tiết các đĩa DVD trong giỏ hàng (#3).
- `search_by_title()` tìm kiếm đĩa DVD theo tiêu đề (#4).
- `Cart.total_cost_with_discount()` tính tổng tiền sau khi giảm giá (#8, #9).
- Thông báo tiếng Việt khi thêm đĩa vào giỏ hàng (#10).
- Mẫu Pull Request `.github/pull_request_template.md` (#2) và sơ đồ Use Case `docs/use-case.md` (#5).

### Fixed
- Sửa lỗi giỏ hàng nhận đĩa thứ 21 vượt quá `MAX_NUMBERS_ORDERED = 20` (#6, #7).
