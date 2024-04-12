from collections import Counter


def top3(st):
    st = st.replace(" ", "")
    return dict(Counter(st).most_common(3))


text3 = input("Введите текст: ")
print(top3(text3))