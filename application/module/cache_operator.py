import os, json, time

def is_need_renew_weather_cache_data(json_file):
    return True if not 'weather_data' in json_file else int(time.time()) - json_file['weather_data']["upload_time"] >= 3600
