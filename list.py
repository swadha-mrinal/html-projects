lst = ['apple','guava','mango','banana','kiwi']

print("length of list:", len(lst))
print("first element:",lst[0])
print("last element:", lst[-1])

lst.append('papaya')
print("updated list:", lst)

lst.remove('kiwi')
print("updated list:", lst)

lst.sort()
print("sorted ist:", lst)

lst.pop(1)
print("updated list:", lst)

lst.reverse()
print("Reversed list:", lst)

print("Multiplication on list:", lst*2)

lst = lst[:4]
print("sliced list:", lst)

lst.clear()
print("updated list:", lst)