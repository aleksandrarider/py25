def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year%400==0:
        print("Год ", year, " високосный")
    else:
        print("этот год не високосный")

year = int(input("введите номер года"))
leap_year(year)
