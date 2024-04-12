# Напишите функцию search_substr(subst, st), которая принимает 2 строки и определяет, имеется ли подстрока subst в строке st.
# В случае нахождения подстроки, возвращается фраза «Есть контакт!», а иначе «Мимо!».
# Должно быть найдено совпадение независимо от регистра обеих строк.

def search_substr(subst, st):
    if st.lower().find(subst.lower()) != -1:
        return "Есть контакт!"
    else:
        return "Мимо!"


string = input("Введите строку: ")
substring = input("Введите подстроку: ")
print(search_substr(substring, string))
