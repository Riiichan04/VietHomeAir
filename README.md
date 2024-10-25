# Weather Center - Đồ án môn Lập trình Python - Nhóm 14 - NLU 2024-2025

#### Lưu ý: Repo này chỉ mới config cơ bản, chưa hề config phần csdl, phân trang và model

---
### Cách chạy code:
#### Cách 1: Chạy thông qua Virtual Environment
1. Clone repo này về 
2. Mở repo = IDE/Text Editor
3. Gõ: `python -m venv .venv` để tạo Virtual Environment
4. Mở terminal gõ: `.venv\Scripts\Activate.ps1`
5. Gõ `python pip install Django`
6. Với Pycharm:
   - Cách 1:Chỉ cần click run là được
   - Cách 2: Mở terminal gõ: `python manage.py runserver`
7. Với VSCode:
   - Gõ lệnh: `python manage.py runserver`

#### Cách 2: Chạy trực tiếp
1. Clone repo này về
2. Mở terminal của pj này và gõ `python pip install Django`
3. Gõ `python manage.py runserver`

---
### Các library cần cài để dùng:
1. **Django**: `python pip install Django`
2. **requests**: `python pip install requests`

---
### Cách config Django:
1. Gõ: `python -m venv .venv` để tạo Virtual Environment
2. Gõ `.venv\Scripts\Activate.ps1` để bật venv
3. Gõ `python pip install Django` để cài Django vào venv
4. Gõ `django-admin startproject tên_pj .` để tạo project, dấu . để cho Python biết là cài ngay ở current dir (Ở Python_WeatherCenter)
5. Gõ `python manage.py startapp tên_app` để tạo 1 app
6. Add dòng `tên_app.apps.TênAppConfig` vào file `setting.py` trong project
7. Tạo 1 directory tên là `templates` để chứa các file html/Jinja2, tạo các file html tùy ý
8. Mở `views.py` trong app tạo class View với `template_name = tênfile.html`
9. Mở `urls.py` trong project, trong `urlpatterns` thêm: `path('tên_sub_page, TênClassView.as_views(), name='tên_sub_page')` 
10. Gõ `python manage.py runserer` để chạy server

---
### Ghi chú:
- Version Python là: 3.10
- Version Django là: 5.1.2
- Version requests là 2.32.3 (Dùng để fetch api của bên thứ 3)
- Version pip (bộ cài đặt thư viện,...) là: 24.2

---
### Lưu ý với Pycharm:
- Nên tạo 1 project Django rồi đưa code vào
- Có thể setup cho Pycharm thủ công để nó detect ra đây là project Django