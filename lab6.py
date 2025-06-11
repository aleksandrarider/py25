

#1
def div3():
    d = int(input("введите число"))
    if d % 3 == 0:
        result = "число делится на 3"
    else:
        result = "число не делится на 3"
    return result


#2
def div100():
    try:
        n = int(input("введите число"))
        itog = 100 / n
    except ValueError:
        print("введите число еще раз")
        itog = 0
    except ZeroDivisionError:
        itog = 0
    return itog


#3
def magic_date():
    date = input("введите дату")
    date_list = date.split(".")
    date_list[2] = date_list[2][2:]
    int_date_list = [int(i) for i in date_list]
    if int_date_list[0] * int_date_list[1] == int_date_list[2]:
        return True
    else:
        return False



#4
def lucky_number():
    number= str(input("введите номер"))
    if len(number)%2==0:
        list_1 = list(number[:(len(number)//2)])
        list_2 = list(number[(len(number)//2):])
        list_1 = list(map(int, list_1))
        list_2 = list(map(int, list_2))
        sum1 = sum(list_1)
        sum2 = sum(list_2)
        if sum1 == sum2:
            result = "номер счастливый"
        else:
            result = "номер не счастливый"
    else:
        result = "длина номера должна быть четной"
    return result

x = int(input("введите номер задания(1, 2, 3 , 4)"))
if x == 1:
    print(div3())
elif x == 2:
    print(div100())
elif x == 3:
    print(magic_date())
elif x == 4:
    print(lucky_number())
else:
    print("неверный номер")