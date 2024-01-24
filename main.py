try:
    num_list= list(map(int, input("Введіть список чисел через пробіл").split()))
    x = int(input("Введіть число для пошуку в списку"))
    print(num_list.count(x))
except Exception as e:
    print(e)