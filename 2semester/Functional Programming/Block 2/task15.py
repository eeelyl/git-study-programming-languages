import asyncio

# Исходные данные
data = [{'name': 'wonderful sunset on the volga', 'country': 'UK', 'active_state': False},
        {'name': 'fantastic sunrise in .crimea. ',
            'country': 'Germany', 'active_state': False},
        {'name': 'good rain in Vladivostok.', 'country': 'Spain', 'active_state': True}]

# Корутин для установки страны


async def set_new_country(next_coroutine):
    while True:
        band = await next_coroutine()
        band['country'] = 'Russia'
        await next_coroutine.send(band)

# Корутин для исправления имени


async def correct_name(next_coroutine):
    while True:
        band = await next_coroutine()
        band['name'] = band['name'].replace('.', '').title()
        await next_coroutine.send(band)

# Корутин для переключения активного состояния


async def toggle_active_state(next_coroutine):
    while True:
        band = await next_coroutine()
        band['active_state'] = not band['active_state']
        await next_coroutine.send(band)

# Конечная корутина


async def final_coroutine():
    while True:
        band = await asyncio.Future()
        return band

# Корутин pipeline для обработки данных


async def pipeline(data, *coroutines):
    # Запуск всех корутин и связывание их вместе
    next_coroutine = final_coroutine()
    for coroutine in reversed(coroutines):
        next_coroutine = coroutine(next_coroutine)

    # Передача данных в цепочку корутин
    for band in data:
        await next_coroutine.send(band)

# Основная функция для запуска корутина pipeline


async def main(data):
    await pipeline(data, set_new_country, correct_name, toggle_active_state)

# Запуск основного корутина
asyncio.run(main(data))

# Вывод результата
print(data)
