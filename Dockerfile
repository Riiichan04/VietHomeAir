# Chọn image python 3.10
FROM python:3.10-slim

# Set workdir trong container
WORKDIR /app

# Copy requirements vào container
COPY requirements.txt .

# Cài các thư viện từ requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ code vào container
COPY . .

# Mở cổng 8000 để chạy
EXPOSE 8000

# Chạy Django
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000