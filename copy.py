list1 = [7,8,9]
list2 = list(list1)

print(id(list1), id(list2))

list1[0] = 10
list2[1] = 15

print(list1, list2)


# Python代码
listA = [1,2,3]
listB = listA


print(id(listA), id(listB))

listA[0] = 4
listB[1] = 5

print(listA, listB)
