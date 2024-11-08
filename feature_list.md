### List tính năng
- Quản lý dịch vụ
- Hệ thống account
- Tìm kiếm dịch vụ
- Đánh giá dịch vụ
- Gợi ý tour du lịch
- Sắp xếp đánh giá dịch vụ
- Thống kê dịch vụ: Theo đánh giá, rating,...

---
### Chi tiết tính năng
#### Homepage (Thông)
- Dịch vụ có rating cao nhất
- Hiển thị một vài địa điểm có dịch vụ + tour phổ biến nhất 
- Hiển thị category
- Hiển thị chọn dựa theo tiện ích
- Hiển thị tất cả dịch vụ
- Tìm kiếm: Theo tên dịch vụ/ theo danh mục

### Trang kết quả tìm kiếm (Loan)
- Hiển thị kết quả
- Bộ lọc: Theo danh mục, theo vị trí, theo tiện ích, theo rating, theo giá/đêm

### Trang danh mục (Loan)
- Hiển thị dịch vụ
- Bộ lọc: Theo danh mục, theo vị trí, theo tiện ích, theo rating, theo giá/đêm

#### Thông tin dịch vụ bnb
- Tên dịch vụ
- List hình ảnh
- Thông tin dịch vụ: Có mấy phòng,...
- Tiện ích đi kèm
- Chủ nhà/Người tổ chức
- Mô tả dịch vụ
- Thông tin phụ
- Thời gian booking
- Danh mục: Loại nhà
-> (Thông)

- Danh sách yêu thích, chia sẻ, báo cáo
- Giá tiền
- Đánh giá: Rating + Số lượt rating
-> (Thịnh)

- Bình luận + Rating
- Có phân loại đánh giá: sạch sẽ, chủ nhà,...
- Nơi sẽ đến (Cụ thể = map)
-> (Thư)

- Mô tả nơi đến + (Có thể thêm mô tả tiện ích xung quanh)
- Mô tả tour du lịch ở khu vực đó (nếu có)
- Card thông tin chủ nhà
- Nội quy của dịch vụ
- Gợi ý các dịch vụ khác
-> (Loan)
#### Tài khoản
* 3 loại tài khoản: Admin, user, chủ nhà 
-> Mỗi loại account có 1 trang tương ứng

- Admin: (Thư)
  - Quản lý dịch vụ: CRUD dịch vụ
  - Thống kê: 
    - Rating của dịch vụ
    - Số lượt checkin của dịch vụ
    - Khu vực: Số lượt checkin, dịch vụ khác ở khu vực,...
  - Quản lý tài khoản user và chủ nhà

- User (Thư)
  - Chia sẻ
  - Danh sách yêu thích
  - Báo cáo dịch vụ
  - Lịch sử truy cập
  - Lịch sử đặt phòng

- Chủ nhà (Thịnh)
  - Cung cấp thông tin liên lạc
  - Quản lý dịch vụ của mình: CRUD
  - Hệ thống rating (Optional)
  - Số lượt đánh giá (Optional)
  - Cung cấp thông tin chủ nhà

### Trang đăng ký, đăng nhập, quên mật khẩu (Thịnh)

#### Thành phần phụ (base.html) (Thông)
- Header
- Footer:
  - About us
  - Contact us
  - Privacy policy

### DB:
- Account:
  - id*
  - username*
  - email
  - passwd
  - phone
  - type
  - gender

- History:
  - hid*
  - account_id
  - sid
   
- Favorite:
  - bid*
  - sid*
  - account_id

- ServiceOwner:
  - id*
  - rating
  - count_rating
  - count_report   

- Service:
  - sid*
  - oid 1Table?
  - cid 1Table?
  - address_id 1Table?
  - name
  - detail
  - description
  - place
  - status
  - price
  - time 
  - count_report
  - capacity

- ServiceImage:
  - image_id*
  - sid*
  - url

- ServiceRule:
  - sid*
  - rule
  - description
  
- ServiceRating:
  - rating_id*
  - sid
  - rating
  - comment
  - rating_at

- ServiceRatingType !!
  - rating_id*
  - type_name

- Address: !!
  - address_id*
  - province
  - location

- Post !!
  - pid*
  - sid
  - oid
  - title
  - post_description
  - upload_date
  - edit_date

- Category
  - cid
  - name

- ServiceExtension:
  - seid*
  - sid

- Extension:
  - eid*
  - name

- Tour:
  - tid*
  - address_id
  - name
  - description
  - image

**s: service
**p: post
**o: owner
**c: category
**e: extension
**t: tour

~~=> Config Django + Config View: (Thông)~~
=> Phần DB Service + Tour + Extension + Post: (Loan + Thông)
=> Phần account (Thư)
=> Cào data: Thịnh
=> AI: (optional)
  - Gợi ý service (Loan + Thịnh)
  - Gợi ý tour (Thư + Thông)