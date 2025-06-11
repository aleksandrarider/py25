import random
p_ans = 0
e = 0
while e <3:
    a = random.randint(0,9)
    b = random.randint(0, 9)
    p = a + b
    primer = str(a) + "+" + str(b) + "="
    answer = int(input(primer))
    if answer == p:
        print("Правильно!")
        p_ans +=1
    else:
        print("Ответ неверный")
        e += 1
print("Игра окончена. Правильных ответов: ", p_ans)
