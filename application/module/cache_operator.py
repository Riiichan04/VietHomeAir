# import os, json, time
#
#
# # Tìm cache data, nếu không tìm đc thì tạo 1 file mới
# def find_cache_data(directory_path):
#     cache_path = directory_path + "/cache_data.json"
#     if not os.path.exists(cache_path):  # Nếu như chưa có file thì tạo
#         open(cache_path, encoding='utf-8', mode='w+')
#         with open(cache_path, 'w') as f:
#             json.dump({}, f)  # Viết thông tin mặc định vào file
#     return json.load(open(cache_path, encoding='utf-8'))  # Trả về 1 json
#
#
# # Kiểm tra xem có cần phải gọi API không
# def is_need_renew_weather_cache_data(json_file):
#     return True if not 'weather_data' in json_file else\
#         int(time.time()) - json_file['weather_data']["upload_time"] >= 3600