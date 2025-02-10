# VietHomeAir - Đồ án môn Lập trình Python - Nhóm 12 - NLU 2024-2025

--- 
Đồ án môn Lập trình Python - Nhóm 12 - NLU 2024-2025. VietHomAir - Website cung cấp dịch vụ Bed and Breakfast

## Mục lục

* [Tính năng](#tính-năng)
* [Cách chạy code](#cách-chạy-code)
* [Các thư viện đã dùng](#các-thư-viện-đã-dùng)
* [Tính năng dự kiến](#tính-năng-dự-kiến)
* [Ghi chú](#ghi-chú)

---
### Tính năng:
1. **Trang chủ**: Hiển thị các danh mục bnb có thể chọn, hiển thị các bnb HOT (có lượt xem nhiều) và các bnb có đánh giá cao. Bên cạnh đó, cũng có thể hiển thị tất cả các bnb hiện có.
2. **Danh mục**: Hiển thị các bnb thuộc danh mục đã chọn, bên cạnh đó cũng có một bản đồ hiển thị vị trí chi tiết, giá tiền và popup chứa các thông tin cơ bản của bnb.
3. **Chi tiết bnb**: Hiển thị thông tin chi tiết bnb, vị trí của bnb trên bản đồ. Bên cạnh đó cũng có thể đặt phòng nhanh trong trang này.
4. ***Đặt phòng***: Sau khi đã đăng nhập, người dùng chọn ngày checkin và checkout của bnb đã chọn và nhập thêm các thông tin khác như liên hệ, ghi chú,.... Sau đó, sẽ gửi các thông tin này đến chủ bnb. Tuy nhiên hiện tại, người đặt phòng chỉ có thể gửi thông tin đặt phòng cho chủ bnb xét duyệt. Còn phần thanh toán và các chính sách thanh toán liên quan sẽ do người dùng và chủ bnb thỏa thuận.
5. ***Đánh giá bnb:***: Sau khi checkout. Người dùng có thể đánh giá bnb. Đánh giá này sẽ được phân tích qua 2 bước: Lọc các đánh giá spam và phân tích cảm xúc tích cực/tiêu cực của bình luận để phân loại và hiển thị trên trang thông tin bnb.
6. **Quản lý bnb**: Các account có role là chủ bnb có thể quản lý các bnb của mình. Có thể xem và thay đổi thông tin của bnb (trừ vị trí). Bên cạnh đó, cũng có thể xét duyệt các yêu cầu đặt phòng.
7. **Tìm kiếm bnb**: Có thể tìm kiếm bnb dựa theo một từ khóa trong tên bnb.

---
### Cách chạy code:
- Nếu không biết dùng Docker thì có thể dùng các lệnh sau:
1. Mở terminal của repo sau khi clone.
2. `docker build -t your-app-name .`: Để tiến hành build Docker Image. Với `your-app-name` là tên application muốn đặt.
3. `docker run -d -p 8000:8000 --name your-container-name your-app-name`: Dùng để chạy Container từ Image đã tạo với `your-container-name` là tên Container muốn đặt.
4. Mở `localhost:8000/` để sử dụng web.

---
### Tính năng dự kiến
*Dù báo cáo xong, nhưng project này vẫn sẽ được tiếp tục phát triển và hoàn thiện*
1. **Thanh toán**: Thay vì để người dùng và chủ nhà tự thỏa thuận, sẽ thêm tính năng thanh toán hoàn chỉnh.
2. **Trang tìm kiếm**: Cập nhật giao diện, thêm bộ lọc và phần phân trang cho kết quả tìm kiếm.
3. **Trang chủ**: Thêm infinite scrolling cho phần `tất cả Bnb`.
4. **Trang người dùng**: Bổ sung thêm các tính năng cần thiết khác cho trang người dùng.
5. **Xác thực người dùng**: Thêm phần xác thực tài khoản mới thông qua gửi một email hoặc OTP về số điện thoại đã đăng ký.
6. **Hệ thống đánh giá chủ nhà**: Dựa trên đánh giá của người dùng về chủ nhà, hệ thống sẽ đưa ra một xếp hạng đánh giá cho chủ nhà.

---
### Ghi chú:
- Repo này sử dụng Python 3.10


##### Đã báo cáo vào ngày 10/1/2025