import os, json, time

def is_need_renew_weather_cache_data(json):
    return True if not 'weather' in json else int(time.time()) - json['weather_data']["upload_time"] >= 3600
