try:
    num_list = list(map(int, input("Введіть список чисел через пробіл").split()))
    def listsum(numList):
        Sum = 0
        for i in numList:
            Sum = Sum + i
        return Sum
    print("Сума всіх елементів списку: ", listsum(num_list))
    print("Середнє арефметичне всіх елементів списку: ", listsum(num_list)/len(num_list))

except Exception as e:
    print(e)