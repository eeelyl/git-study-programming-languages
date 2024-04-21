import os
import random
from PIL import Image, ImageDraw  # pip install pillow


def figure_gen(num_circles=100):
    try:
        # Создаем директорию Circles, если она не существует
        if not os.path.exists('Circles'):
            os.makedirs('Circles')

        for i in range(num_circles):
            # Создаем белое изображение с размерами 600x600
            image = Image.new("RGB", (600, 600), "white")
            draw = ImageDraw.Draw(image)

            # Генерируем случайный цвет для круга
            color = (random.randint(0, 255), random.randint(
                0, 255), random.randint(0, 255))

            # Рисуем круг радиусом 300 пикселей в случайном месте
            x = random.randint(0, 300)
            y = random.randint(0, 300)
            draw.ellipse((x, y, x + 300, y + 300), fill=color)

            # Сохраняем изображение в формате JPEG с именем circle_i.jpg, где i - номер круга
            image.save(f'Circles/circle_{i + 1}.jpg', 'JPEG')
    except Exception as e:
        print(f"Произошла ошибка: {e}")


# Вызываем функцию с количеством кругов по умолчанию (100)
figure_gen()
