# PythonProgramming_Project
Đồ án nhóm 14 - Lập trình Python - NLU 2024-2025 - Weather Center

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
### Cách config Django:
1. Gõ: `python -m venv .venv` để tạo Virtual Environment
2. Gõ `.venv\Scripts\Activate.ps1` để bật venv
3. Gõ `python pip install Django` để cài Django vào venv
4. Gõ `django-admin startproject tên_pj .` để tạo project, dấu . để cho Python biết là cài ngay ở current dir (Ở Python_WeatherCenter)
5. Có thể cài thêm mọi thứ tùy ý
6. Gõ `python manage.py runserer` để chạy server

---
### Ghi chú:
- Version Python là: 3.10
- Version Django là: 5.1.2
- Version pip (bộ cài đặt thư viện,...) là: 24.2