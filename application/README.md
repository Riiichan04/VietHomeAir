## Đây là một cái quickguide về cách phần Views hoạt động trong Django

1. Tạo 1 class trong `views.py`
2. Set `template_name = tên_file.html`
3. Override function `get_context_data(self, **kwargs)`. Mục đích là **mỗi khi gọi view** (Tức là khi gọi đến trang tương ứng) thì **function này được gọi đầu tiên**. Trong function này:
4. Dòng đầu: `context = super().get_context_data(**kwargs)`
5. Các dòng kế: xử lý thông tin
6. `context['kết_quả'] = biến_kết_quả_từ_phần_xử_lý`
7. Dòng cuối: `return context`
8. Sau đó, hiện kết quả trong html bằng cách gõ: `{{ kết_quả }}` (kết_quả là tên thuộc tính tương ứng khi ta add vào context ở bước 6)