#Write a Python program to create a new dictionary by extracting 
# the mentioned keys from the below dictionary.


sampleDict = { 
  "name": "Kelly",
  "age":25, 
  "salary": 8000, 
  "city": "New york" }

keys = ["name", "salary"]

# newDict = {k: sampleDict[k] for k in keys}
# print(newDict)

# new dict
res = dict()

for k in keys:
    # add current key with its va;ue from sample_dict
    res.update({k: sampleDict[k]})
print(res)