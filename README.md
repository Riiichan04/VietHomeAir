# Weather Center - Đồ án môn Lập trình Python - Nhóm 12 - NLU 2024-2025

#### Lưu ý: Repo này chỉ mới config cơ bản, chưa config csdl và model

---

### Cách chạy code:

#### Cách 1: Chạy thông qua Virtual Environment

1. Clone repo này về
2. Mở repo = IDE/Text Editor
3. Gõ: `python -m venv .venv` để tạo Virtual Environment
4. Mở terminal gõ: `.venv\Scripts\Activate.ps1`
5. Gõ `pip install Django`
6. Với Pycharm:
    - Cách 1:Chỉ cần click run là được
    - Cách 2: Mở terminal gõ: `python manage.py runserver`
7. Với VSCode:
    - Gõ lệnh: `python manage.py runserver`
8. Cài thêm các thư viện hỗ trợ:
    - **requests**: `pip install requests`
    - **python-dotenv**: `pip install python-dotenv`

[//]: # (9. Tạo 1 file tên là `.env` và đặt trong project với thông tin như sau:)

[//]: # ()
[//]: # (```)

[//]: # (OPEN_WEATHER="Open Weather API Key")

[//]: # (```)

#### Cách 2: Chạy trực tiếp

1. Clone repo này về
2. Mở terminal của pj này và gõ `pip install Django`
3. Gõ `python manage.py runserver`
4. Cài thêm các thư viện hỗ trợ:
    - **requests**: `pip install requests`
    - **python-dotenv**: `pip install python-dotenv`

[//]: # (5. Tạo 1 file tên là `.env` và đặt trong project với thông tin như sau:)

[//]: # ()
[//]: # (```)

[//]: # (OPEN_WEATHER="Open Weather API Key")

[//]: # (```)

---

### Các library cần cài để dùng:

1. **Django**: `pip install Django`
2. **requests**: `pip install requests`
3. **python-dotenv**: `pip install python-dotenv`

---

### Cách config Django:

1. Gõ: `python -m venv .venv` để tạo Virtual Environment
2. Gõ `.venv\Scripts\Activate.ps1` để bật venv
3. Gõ `python pip install Django` để cài Django vào venv
4. Gõ `django-admin startproject tên_pj .` để tạo project, dấu . để cho Python biết là cài ngay ở current dir (Ở
   Python_WeatherCenter)
5. Gõ `python manage.py startapp tên_app` để tạo 1 app
6. Add dòng `tên_app.apps.TênAppConfig` vào file `setting.py` trong project
7. Tạo 1 directory tên là `templates` để chứa các file html/Jinja2, tạo các file html tùy ý
8. Mở `views.py` trong app tạo class View với `template_name = tênfile.html`
9. Mở `urls.py` trong project, trong `urlpatterns` thêm:
   `path('tên_sub_page, TênClassView.as_views(), name='tên_sub_page')`
10. Gõ `python manage.py runserer` để chạy server

---

### Ghi chú:

- Version Python là: 3.10
- Version Django là: 5.1.2
- Version requests là 2.32.3 (Dùng để fetch api của bên thứ 3)
- Version python-dotenv là 1.0.1
- Version pip (bộ cài đặt thư viện,...) là: 24.2
- Các biến môi trường (.env) sử dụng (tạo 1 file tên .env trong project):
    - OpenWeather API Key

---

### Lưu ý với Pycharm:

- Nên tạo 1 project Django rồi đưa code vào
- Có thể setup cho Pycharm thủ công để nó detect ra đây là project Django

---

### Giải thích Cấu trúc Project: (Quickguide về Django)

![project_explorer.png](https://cdn.discordapp.com/attachments/1083971658055942167/1303773919974658169/image.png?ex=672cf995&is=672ba815&hm=39fb74d961a77fb8510d0b03f157d753ffe00a059897f67b51854a6db4c5ed91&)

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