# PythonProgramming_Project
Đồ án nhóm 14 - Lập trình Python - NLU 2024-2025 - Weather Center

#### Lưu ý: Repo này chỉ mới config cơ bản, chưa hề config phần csdl, phân trang và model

### Cách chạy code:
1. Clone repo này về 
2. Mở repo = IDE/Text Editor
3. Với Pycharm:
   - Cách 1:Chỉ cần click run là được
   - Cách 2: Mở terminal gõ: `python manage.py runserver`
4. Với VSCode:
   1. Mở terminal gõ: `.venv\Scripts\Activate.ps1`
   2. Gõ lệnh: `python manage.py runserver`

### Cách config Django:
1. Gõ: `python -m venv .venv` để tạo Virtual Environment
2. Gõ `.venv\Scripts\Activate.ps1` để bật venv
3. Gõ `python pip install Django` để cài Django vào venv
4. Gõ `django-admin startproject tên_pj .` để tạo project, dấu . để cho biết là cài ngay ở cd (Ở Python_WeatherCenter)
5. Có thể cài thêm mọi thứ tùy ý
6. Gõ `python manage.py runserer` để chạy server


### Ghi chú:
- Version Python là: 3.10
- Version Django là: 5.1.2
- Version pip (bộ cài đặt thư viện,...) là: 24.2