# Count the number of strings where the string length is 2 or more and
# the first and last character are same from a given list of strings

lst = ['abc', 'xyz', 'aba', '1221']

ctr = 0
for i in lst:
    if len(lst) > 1 and i[0] == i[-1]:
        ctr += 1
print(ctr)
