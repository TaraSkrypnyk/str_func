try:
    def sum():
        num1 = int(input('Vvedit pershe chyslo: '))
        num2 = int(input('Vvedit druhe chyslo: '))
        rez = 0
        if num2 > num1:
            while num1<num2-1:
                num1 += 1
                rez = rez + num1
            print(rez)
        elif num1 > num2:
            while num2 < num1-1:
                num2 += 1
                rez = rez + num2
            print(rez)
    sum()
except Exception as e:
    print(e)