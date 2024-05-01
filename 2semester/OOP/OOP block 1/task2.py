import datetime as dt
import time


class Person:
    def __init__(self, name, birth_country, birth_date):
        self.name = name
        self.birth_country = birth_country
        self.birth_date = birth_date

    def age(self):
        now = dt.date.fromtimestamp(time.time())
        bd = dt.date.fromisoformat(self.birth_date)
        age = now - bd
        return age.days // 365


human = Person('Alex', 'Russia', '1911-11-01')
print('{} is {} years old'.format(human.name, human.age()))
