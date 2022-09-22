myDict = {"Pankha":"Fan", "Pustak":"Book", "Gadi":"Car", "Vastu":"Object"}
print(myDict.keys())
ui = input("Enter word: ").capitalize()

print(f"The meaning of {ui} is {myDict[ui]}")