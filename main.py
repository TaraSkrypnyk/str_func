try:
    text = str(input('Vvedit text: '))
    filter_text = text.lower()
    slova = str(input("Vvedit zarezervovani slova: ")).lower()
    if slova in filter_text:
        print('Vashe slovo znaydene: ' + text.replace(slova, slova.upper()))
    else:
        print('Vashe slovo ne znaydene')

except Exception as e:
    print(e)