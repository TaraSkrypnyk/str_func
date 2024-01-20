try:
    def neparny_chysla():
        num1 = n1 = int(input('Vvedit pershe chyslo: '))
        if num1 < 0:
            num1 = n1 = int(input('Vvedit dodatne chyslo: '))
        num2 = n2 = int(input('Vvedit druhe chyslo: '))
        if num2 < 0:
            num2 = n2 =int(input('Vvedit dodatne chyslo: '))
        if num2 > num1:
            if (n1 % 2) == 0:
                n1 += 1
                while n1 < n2:
                    print(n1," ", end="")
                    n1 += 2
            elif (n1 % 2) == 1:
                n1 += 2
                while n1 < n2:
                    print(n1," ", end="")
                    n1 += 2
        elif num1 > num2:
            n1 = num2
            n2 = num1
            if (n1 % 2) == 0:
                n1 += 1
                while n1 < n2:
                    print(n1," ", end="")
                    n1 += 2
            elif (n1 % 2) == 1:
                n1 += 2
                while n1 < n2:
                    print(n1," ", end="")
                    n1 += 2

    neparny_chysla()

except Exception as e:
    print(e)