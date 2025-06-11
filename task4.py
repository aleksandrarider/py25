color1 = input("введите первый цвет(красный, синий или желтый) ")
color2 = input("введите второй цвет(красный, синий или желтый) ")
if color1 != "желтый" and color1 != "синий" and color1 != "красный":
    print("неверный цвет")
if color2 != "желтый" and color2 != "синий" and color2 != "красный":
    print("неверный цвет")

if color1 == "желтый":
    if color2 == "желтый":
        print("желтый")
    elif color2 == "синий":
        print("зеленый")
    elif color2 == "красный":
        print("оранжевый")
elif color1 == "синий":
    if color2 == "синий":
        print("синий")
    elif color2 == "красный":
        print("фиолетовый")
    elif color2 == "желтый":
        print("зеленый")
elif color1 == "красный":
    if color2 == "красный":
        print("красный")
    elif color2 == "синий":
        print("фиолетовый")
    elif color2 == "желтый":
        print("оранжевый")