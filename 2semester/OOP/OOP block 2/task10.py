class KgToPounds:
    def __init__(self, kg):
        self._kg = kg

    @property
    def kg(self):
        return self._kg

    @kg.setter
    def kg(self, value):
        if value < 0:
            raise ValueError(
                "Количество килограмм должно быть неотрицательным")
        self._kg = value

    def to_pounds(self):
        return self._kg * 2.20462


# Пример использования
weight_converter = KgToPounds(10)
print("Текущее количество килограмм:", weight_converter.kg)
print("Текущее количество фунтов:", weight_converter.to_pounds())

# Установка нового значения килограмм
weight_converter.kg = 20
print("Новое количество килограмм:", weight_converter.kg)
print("Новое количество фунтов:", weight_converter.to_pounds())
