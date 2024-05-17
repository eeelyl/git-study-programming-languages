import random


def move_cars(car_positions):
    """Обновляет позиции автомобилей."""
    return [pos + 1 if random.random() > 0.3 else pos for pos in car_positions]


def draw_car(position):
    """Печатает позицию одного автомобиля."""
    return f'Start|{"-" * position}'


def run_step_of_race(car_positions):
    """Вычисляет позиции автомобилей в следующий момент времени."""
    return move_cars(car_positions)


def draw(car_positions):
    """Выводит позиции всех автомобилей."""
    return '\n'.join(draw_car(pos) for pos in car_positions)


def race(time, car_positions):
    """Запускает гонку автомобилей."""
    if time == 0:
        return car_positions
    print('_________________________')
    car_positions = run_step_of_race(car_positions)
    print(draw(car_positions))
    return race(time - 1, car_positions)


# Начальные параметры
initial_time = 5
initial_car_positions = [0, 0, 0]

# Запуск гонки
race(initial_time, initial_car_positions)
