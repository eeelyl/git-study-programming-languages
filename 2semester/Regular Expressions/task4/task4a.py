import re


def remove_leading_zeros(ip_address):
    cleaned_ip = re.sub(r'\b0+(\d)', r'\1', ip_address)
    return cleaned_ip


# Пример использования:
ip_address = "192.168.001.001"
print(remove_leading_zeros(ip_address))  # Выведет: 192.168.1.1
