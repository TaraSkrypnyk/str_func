try:
    def shchaslyve():
        n = int(input('Введіть шестизначне додатнє число: '))
        rez = False
        if n<100000 or n>999999:
            n = int(input('Введіть шестизначне додатнє число: '))
        sum1 = int(n % 10) + int((n % 100)/10) + int((n % 1000)/100)
        print(sum1)
        sum2 = int((n % 10000)/1000) + int((n % 100000)/10000) + int(n / 100000)
        print(sum2)
        if sum1 == sum2:
            rez = True
        print(rez)
    shchaslyve()

except Exception as e:
    print(e)