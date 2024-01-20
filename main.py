try:
    def line():
        lenght = int(input('Введіть довжину лінії: '))
        if lenght<0:
            lenght = int(input('Введіть довжину лінії: '))
        nap = int(input('Якщо ви хочете горизонтальну лінію введіть 1. Якщо вихочете вертикальну лінію введіть 2: '))
        if nap != 1 and nap != 2:
            nap = int(
                input('Якщо ви хочете горизонтальну лінію введіть 1. Якщо вихочете вертикальну лінію введіть 2: '))
        sign = str(input('Введіть символ з якого хочетет отримати лінію: '))
        i = 0
        if nap == 1:
            while i < lenght:
                print(sign, end='')
                i +=1
        elif nap == 2:
            while i < lenght:
                print(sign)
                i +=1


    line()

except Exception as e:
    print(e)