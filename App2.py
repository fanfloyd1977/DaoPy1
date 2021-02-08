
#import pandas as pd

#Say = input(">>")

#data = pd.read_excel(r"C:\Users\Kirara\PycharmProjects\DaoPy1\Book.xls")

#row = data.shape[0]


#for i in range(row):
#    if Say == data["Question"].values[i]:
#        print(data["Answer"].values[i])
        
"""
import re
list = ["guru99 get", "guru99 give", "guru Selenium"]

for element in list:
    z = re.match("(g\w+)\W(g\w+)", element)
    if z:
        print((z.groups()))




x = [low.lower() for low in list1]
print(x)

list1 = ["How are you?", "How r u?","Im fine, Thanks you and you", "I want to fly away", "Someday, I will fly", "I'm doing well", "I miss you"]
list2 = "doing well"
List3 = ["It is a good day"]
res = [j for j in list1 if any(k.casefold() in j.casefold() for k in list2)]

if res:
    print("yes")
else:
    print("No")




import re



list1 = "how "'" is everthing going"
word = ":)"
if word in list1.split():
    print("ok")

r = input("enter : ")
s = "I\'m not feeling well"

if r.lower()==s.lower():
    print(s)

"""
list1 = ["How are you?",
list2 = "how are"
List3 = ["It is a good day"]

res = [j for j in list1 if any(k.casefold() in j.casefold() for k in list2)]

if res:
    print("yes")
else:
    print("No")