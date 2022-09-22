# Concatenate two lists in the following order
# Expected output:
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
lst3 = []
for i in list1:
    for j in list2:
        lst3.append(i+j)
print(lst3)
