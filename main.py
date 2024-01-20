try:
    sl1 = str(input('Vvedit slovo: ')).lower()
    sl2 = sl1[::-1]
    if sl2 == sl1:
        print('Vashe slovo palindrom')
    else:
        print('Vashe slovo ne palindrom')
except Exception as e:
    print(e)