import csv
import datetime
import time

def create_csv(file_name):
    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['№', 'Секунда', 'Микросекунда']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for i in range(1, 101):
            current_time = datetime.datetime.now()
            writer.writerow({
                '№': i,
                'Секунда': current_time.second,
                'Микросекунда': current_time.microsecond
            })
            time.sleep(0.02)

# Создаем CSV-файл
create_csv('file_row_100.csv')
