### Giải thích Cấu trúc Project: (Quickguide về Django)

![project_explorer.png](https://drive.google.com/file/d/1biOhy-sPQgzju1H9VmgApabemLP7-Ho_/view?usp=drive_link)

- **.venv**: Chứa Virtual Environment, dùng để cài library và chạy code trong môi trường ảo mà không làm ảnh hưởng đến máy thật. Được tạo ra bằng lệnh `python -m venv tên_directory_venv`


- **application**: Chứa phần ứng dụng. Là nơi làm việc chính của Django, mọi code để chạy web đều được đặt ở đây. Được tạo ra sau khi chạy lệnh `python manage.py startapp tên_application`. Trong đó:

    - **migrations**: <em><u>Directory mặc định</u></em> chứa module liên quan đến csdl
    - **module**: Chứa các function và class hỗ trợ cho việc xử lý
    - **static**: Chứa các phần tĩnh của web (gồm CSS và JS, hình ảnh, video,...):
        - **scripts**: Nơi chứa các file JS
        - **style**: Nơi chứa các file CSS
        - **image**: Nơi chứa hình ảnh
        - **favicon.ico**: Icon của web
    - **templates**: Nơi chứa các file HTML (html trong Django sử dụng định dạng **Jinja2**) và file Jinja2
    - **models**: Là directory chứa các file model của web, dùng để thay thế file **models.py**
    - **views**: Là directory chứa các file view của web, dùng để thay thế file **views.py**
    - **\__init\__.py**: <em><u>File mặc định</u></em> dùng để cho python biết rằng thư mục chứa nó (application) là 1 module
    - **admin.py**: <em><u>File mặc định</u></em> chứa thông tin liên quan đến tài khoản admin (Dùng để truy cập vào model/database)
    - **tests.py**: <em><u>File mặc định</u></em> chứa phần Testcase của app
    - ~~**models.py**: <em><u>File mặc định</u></em> chứa phần Model của app. Đây cũng là nơi thao tác trực tiếp với phần Database~~
    - ~~**views.py**: <em><u>File mặc định</u></em> chứa phần View của app. Đây cũng là nơi thao tác với các API của bên thứ 3 trong app~~


- **bed_and_breakfast**: Đây là directory chứa các thông tin về project:

    - **\__init\__.py**: <em><u>File mặc định</u></em> dùng để cho python biết rằng thư mục chứa nó (weather_center) là 1 module
    - **asgi.py**: <em><u>File mặc định</u></em>, đây là file dùng để thực hiện Asynchronous Server Gateway Interface (Xem ở Google).
    - **settings.py**: <em><u>File mặc định</u></em> dùng để chứa các setting của project
    - **urls.py**: <em><u>File mặc định</u></em> dùng để đăng ký url (1 trang mới) trên web
    - **wsgi.py**: <em><u>File mặc định</u></em>, đây là file dùng để thực hiện Web Server Gateway Interface (Xem ở Google).


- **.env**: Đây là 1 file đặc biệt chứa các biến môi trường của project (là các biến mà chỉ hoạt động ở máy này nhưng không thể hoạt động ở máy khác, hoặc dùng để chứa thông tin private của project - Xem ở Google)


- **db.sqlite3**: <em><u>Đây là 1 file mặc định</u></em> được tạo ra khi chạy `python manage.py runserver` nếu chưa config database cho project (Mặc định Django dùng Sqlite)


- **manage.py**: <em><u>Đây là 1 file mặc định</u></em> dùng để chạy code (Tương tự 1 file có main() trong Java dùng để chạy code)