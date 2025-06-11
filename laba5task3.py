n = int(input("введите количество слов"))
for i in range(n):
    word = input("введите слово").lower()
    if "ф" in word:
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")

