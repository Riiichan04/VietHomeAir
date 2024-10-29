# Danh sách tính năng

## Xem thời tiết trong vòng 24h

- Nhiệt độ trong ngày.
- Khả năng mưa ngày hôm đó.

## Xem tin tức thời tiết trong ngày hôm đó.

- Tổng hợp từ các trang báo lớn (VNExpress)
- Cập nhật các thiên tai, áp thấp nhiệt đới,... nếu có.

## Cảnh báo mưa lớn, gợi ý vật dụng cần thiết khi ra ngoài hoặc cách phòng tránh thiên tai

- Nhận feedback của người dùng về thời tiết, từ đó lấy dữ liệu để train cho hệ thống gợi ý.

## Vẽ biểu đồ phân bố lượng mưa từng vùng trong khu vực lân cận.

- Lấy dữ liệu từ các bài báo, API thời tiết.

## Vẽ biểu đồ biến đổi nhiệt độ/lượng mưa/UV/Gió/Độ ẩm/Sương mù/Ô nhiễm không khí trong ngày.

- Lấy dữ liệu từ API thời tiết.

## Chế độ Dark/Light Mode cho thiết bị.

- Chuyển đổi chế độ sáng/tối.

## Chuyển đổi đơn vị đo lường nhiệt độ cho từng quốc gia.

- Tùy mỗi quốc gia sẽ có đơn vị đo nhiệt độ khác nhau.

## Dự báo thời tiết cho 1 tuần.

- Kèm chức năng coi thời tiết trong 24h, xem tin tức, cảnh báo/gợi ý, vẽ biểu đồ.

## Có thể lưu khu vực người dùng mong muốn theo dõi thời tiết hằng ngày.

- Tiện lợi cho người đi làm, đi học, hoạt động xa nơi sinh hoạt.

## Phân trang

1. ***Cho n trang hiển thị thông tin thòi tiết cơ bản của n location khác nhau. Trong đó:***
    - Tên chỗ vị trí hiện tại.
    - Nhiệt độ hiện tại.
    - High-low temperature.
    - Cảnh báo mưa trong khoảng thời gian nào.
    - Danh sách khung giờ + khả năng mưa (24H).
    <div><strong>Người thực hiện: Thông</strong></div>

    - Dự báo 10 ngày tiếp theo.
    - Danh sách các thành phố đã lưu.
    - Cảnh báo/gợi ý vật dụng ra ngoài.
    - Tin tức trong ngày.
    - Bản đồ nhiệt độ toàn khu vực.
    <div><strong>Người thực hiện: Thư</strong></div> 


2. ***Ứng với mỗi trang ở 1. thì sẽ có 1 trang chứa mọi biểu đồ tương ứng của location đó như sau:***
    - Đối với nhiệt độ: Biểu đồ biến động nhiệt độ.
    - Đối với UV: Biểu đồ biến động UV.
    - Đối với lượng mưa: Biểu đồ phần trăm khả năng mưa.
    - Đối với độ ẩm/sương mù: Biến đổi độ ẩm (%)
    - Đối với ô nhiễm không khí: Biến đổi lượng CO2.
    <div><strong>Người thực hiện: Loan</strong></div> 


3. ***Ứng với mỗi location thì sẽ có 1 trang chứa các thông tin chi tiết và thống kê của từng location như sau:***
    - Tên trang (Nhiệt độ/Lượng mưa/UV/Gió/Độ ẩm/Sương mù/Ô nhiễm không khí).
    - Danh sách ngày (thứ + ngày) (10 ngày)
    - Thông tin ngày được chọn.
    - Trạng thái thông tin ở thời điểm hiện tại.
    - Thông tin về Nhiệt độ/Lượng mưa/UV/Gió/Độ ẩm/Sương mù/Ô nhiễm không khí
    <div><strong>Người thực hiện: Thịnh</strong></div> 


4. ***Về Django:***
    - Config View
    - Config Model
    - Config Database
    - Config connect to OpenWeather API

5. *(Optional)* ***Tính năng AI về Cảnh báo/gợi ý vật dụng ra ngoài.***

6. Database