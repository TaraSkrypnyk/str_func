try:
    def max():
        num1 = int(input('Введіть перше число: '))
        num2 = int(input('Введіть друге число: '))
        num3 = int(input('Введіть третє число: '))
        num4 = int(input('Введіть четверте число: '))
        if num1>num2 and num1>num3 and num1>num4:
            print('Найбільше число: ', num1)
        elif num2>num1 and num2>num3 and num2>num4:
            print('Найбільше число: ', num2)
        elif num3>num1 and num3>num2 and num3>num4:
            print('Найбільше число: ', num3)
        else:
            print('Найбільше число: ', num4)
    max()

except Exception as e:
    print(e)