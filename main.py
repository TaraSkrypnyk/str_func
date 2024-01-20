try:
    text = str(input('Vvedit text: '))
    sign_for_search = str('.')
    if sign_for_search in text:
        print('V vashomu texti ' , text.count(sign_for_search) , 'rechen')
    else:
        print('V vashomu texti 1 rechennya')
except Exception as e:
    print(e)