mesto = int(input("введите номер места"))
if 1<=mesto<=36:
    if mesto % 2==0:
        tip_mesta = "верхнее, купе"
    else:
        tip_mesta = "нижнее, купе"
elif 37<=mesto<=54:
    if mesto % 2==0:
        tip_mesta = "верхнее боковое"
    else:
        tip_mesta = "нижнее боковое"
else:
    tip_mesta = "ошибка"

print(tip_mesta)