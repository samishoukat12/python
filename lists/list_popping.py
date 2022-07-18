my_list=["sami","ali","hamza"]




my_new_list=["david"]

my_new_list.append(my_list.pop(2))
print(my_new_list)


my_new_list.insert(0,my_list.pop(1))

print(my_new_list)


my_new_list.insert(0,my_list.pop())

print(my_new_list)



#slice method
my_new_list_try=["ahmad"]

my_new_list_try.insert(0,my_new_list[1:4])
print(my_new_list_try)


