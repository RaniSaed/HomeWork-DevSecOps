list1 = list(map(int, input("Enter numbers for list 1, separated by spaces: ").split()))

list2 = list(map(int, input("Enter numbers for list 2, separated by spaces: ").split()))

max_list1 = max(list1)
max_list2 = max(list2)

count_list1 = 0
for num in list1:
    if num > max_list2:
        count_list1 += 1

count_list2 = 0
for num in list2:
    if num > max_list1:
        count_list2 += 1

if count_list1 > count_list2:
    print("List 1 contains more large numbers.")
elif count_list2 > count_list1:
    print("List 2 contains more large numbers.")
else:
    print("Both lists contain the same number of large numbers.")