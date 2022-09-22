# Write a Python program to find the list of words that
# are longer than n from a given list of words

txt = "The quick brown fox jumps over the lazy dog"
x = txt.split()
b = []
for i in x:
    if len(i) > 3:
        b.append(i)
print(b)