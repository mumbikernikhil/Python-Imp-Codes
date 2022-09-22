punct = ''' `!@#$%^&*()-_+=~',"<.>?/:;\* '''
a = input("Enter a string: ")
no_punct = ""

for char in a:
    if char not in punct:
        no_punct = no_punct + char
print(no_punct)