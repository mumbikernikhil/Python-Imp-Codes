# pass if total is 40% and min 33% in each subject

a = int(input("Enter marks scored in English: "))
b = int(input("Enter marks scored in Maths: "))
c = int(input("Enter marks scored in Hindi: "))

# if (a+b+c)/3 > 40 and (a>33 and b>33 and c>33):
#     print("You are Passed")
# else:
#     print("You are failed")

if(sub1<33 or sub2<33 or sub3<33):
    print("You are fail because you have less than 33% in one of the subjects")
elif(sub1+sub2+sub3)/3 < 40:
    print("You are fail due to total percentage less than 40")
else:
    print("Congatulations! You passed the exam")