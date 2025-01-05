import csv
import json
# Sẽ xóa
with open('../static/data.json', 'r', encoding='utf-8') as file:
    list_data = json.load(file)

for data in list_data:
    # data.pop('description')
    for index in range(len(data['policy'])):
        data['policy'][index] = data['policy'][index].replace('Nội quy nhà\n', '').replace('\nHiển thị thêm', '')


with open('../static/convert_data.csv', 'w', encoding='utf-8', newline='') as csv_file:
    fieldnames = ['title', 'description' , 'imageUrl', 'listService', 'price', 'comment', 'policy']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(list_data)