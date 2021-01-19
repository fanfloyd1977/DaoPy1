"""
#1
String1 = "Twinkle, twinkle, little star,"
String2 = "        How I wonder what you are!"
String3 = "                Up above the world so high,"
String4 = "                Like a diamond in the sky."
String5 = "Twinkle, twinkle, little star,"
String6 = "        How I wonder what you are"


Strings = [String1, String2, String3, String4, String5, String6]
for i in Strings:
    print(i)

######################
#2

import sys
print(sys.version)

######################
#3
from datetime import date
today = date.today()
print(today)

######################
#4
Radius = float(input("Please enter Radius : "))
Circle_Area = 3.141592653589793238 * pow(Radius,2)
Round = round(Circle_Area,5)
print("Circle Area is : " + str(Round))


######################
#5

Firstname = input("Pleae Enter Firstname : ")
Lastname = input("Please Enter Lastname : " )
List_Firstname = list(Firstname)
List_Lastname = list(Lastname)

Lf = len(List_Firstname)
Ll = len(List_Lastname)
i = 0
while i < Lf:
    print(List_Firstname[Lf-1-i], end = " ")
    i = i+1
i = 0
while i < Ll:
    print(List_Lastname[Ll-1-i], end = " ")
    i = i+1
#print(f"{list(Firstname.strip())}")


#########################
#5
Firstname = input("Pleae Enter Firstname : ")
Lastname = input("Please Enter Lastname : " )
print(Lastname +" "+ Firstname)


#6
Numbers = input("Please enter a list of numbers : ")
List_Numbers = list(Numbers)
L = len(List_Numbers)

for i in List_Numbers:
    if i == ",":
        List_Numbers.remove(i)
for j in List_Numbers:
    if j == " ":
        List_Numbers.remove(j)

# List = Numbers.split(",")
# print(List)

print(List_Numbers)
Tuple_Numbers = tuple(List_Numbers)
print(Tuple_Numbers)


########
#7
Filename = input("Please enter your filename : ")
File_Name = list(Filename)
Filename_Index = File_Name.index(".")
#print(Filename_Index)
i = Filename_Index
#print(len(File_Name))
while i >= Filename_Index and i <= len(File_Name)-1:
    print(File_Name[i], end = "")
    i = i+1


########
#8
TRed = "\x1b[31m"
TBlack = "\x1b[30m"
Color_List = ["Red","Green","White" ,"Black"]
print(TRed + Color_List[0], TBlack + Color_List[3])


########
#9

exam_st_date = (11, 12, 2014)
print("The examination will start from : " + str(exam_st_date[0]) + " / " + str(exam_st_date[1]) + " / " + str(exam_st_date[2]))


########
#10

N = int(input("Please enter N : "))
TwoN = int(str(N) + str(N))
ThreeN = int(str(N) + str(N) + str(N))
Total = N + TwoN + ThreeN
print(Total)


########
#11
Function = input("Please enter function : ")
print(Function.__doc__)


########
#12

import calendar
Year = int(input("Enter Year : "))
Month = int(input("Enter Month : "))
print(calendar.month(Year,Month))


########
#13
print("a string that you " + '"don' + "'" + "t" + '"' + "have to escape")
print("This")
print("is a ........ multi-line")
print("heredoc string ---------> example")


########
#14

import calendar

print("(YYYY,MM,DD)")

First = input("Enter first date : ")
Second = input("Enter second date : ")

First = First.split(",")
Second = Second.split(",")
print(First)

First_Month_range = calendar.monthrange(int(First[0]),int(First[1]))
print(First_Month_range)
I = int(input("Enter I : "))
Diff = First_Month_range[1] - I
print(Diff)

Date1 = calendar.weekday(int(First[0]),int(First[1]),int(First[2]))
Date2 = calendar.weekday(int(Second[0]),int(Second[1]),int(Second[2]))
Day = Date1 - Date2
print(Day)


########
#14
from datetime import date
First = input("Enter first date : ")
First = First.split(",")
Second = input("Enter Second date : ")
Second = Second.split(",")

d1 = date(int(First[0]),int(First[1]),int(First[2]))
d2 = date(int(Second[0]),int(Second[1]),int(Second[2]))

print(d2-d1)



########
#15

Radius = float(input("Enter Radius : "))
Volume_Sphere = 4/3 * 3.1416 * pow(Radius,3)
print(Volume_Sphere)



########
#16

Number = int(input("Enter number : "))

if Number > 17:
    print((Number-17)*2)
else:
    print(abs(Number-17))


########
#18

N1 = float(input("Enter N1 : "))
N2 = float(input("Enter N2 : "))
N3 = float(input("Enter N3 : "))

if (N1 != N2) or (N2 != N3):
    print(N1+N2+N3)
else:
    print(3*(N1+N2+N3))


########
#19

String = input("Enter String : ")
String = String.split(" ")
if String[0] == "Is":
    for i in String:
        print(i, end = " ")
elif String[0] != "Is":
        i = 0
        print("Is", end = " ")
        while i < len(String):
            print(String[i], end = " ")
            i = i+1


########
#20
String = str(input("Enter String : "))
N = int(input("Enter Number of copies : "))

i = 1
while i <= abs(N):
    print(String, end = "")
    i = i+1



########
#21

Number = int(input("Enter number : "))
print(Number/2)
Div = float(Number/2)

Divided = list(str(Div))
print(Divided)
if Divided[2] == "5":
    print("Odd")
else:
    print("Even")

#21
Number = int(input("Enter number : "))
Mod = Number % 2
if Mod == 0:
    print("Even")
else:
    print("Odd")


###############################
#22

Number = input("Enter Number : ")
List = list(Number)
print(List)
j = 0
for i in List:
    if i == "4":
        j = j+1

print("Number 4 in given list is = " + str(j))


###############################
#23

String = input("Enter String : ")
N = int(input("Enter Number : "))
List = list(String)

if len(List) >= 2:
    i = 1
    while i <= N:
        print(String[0], end = "" + String[1])
        i = i+1

else:
    i = 1
    while i <= N:
        print(String[0], end="")
        i = i + 1


###############################
#24

Tub = ("a","e","i","o","u")
Letter = str(input("Enter letter : "))

if Letter == Tub[0] or Letter == Tub[1] or Letter == Tub[2] or Letter == Tub[3] or Letter == Tub[4]:
    print("It is vowel")
else:
    print("It is NOT vowel")


###################################################################################
#25


Number = int(input("Enter Number : "))

SV = [1,5,8,3]

if Number not in SV:
    print("False")
else:
    print("True")



#########################
#26

LOI = input("Enter list of Integer : ")
List = LOI.split(",")
print(List)

for i in List:
    x = 1
    while x <= int(i):
        print("@" , end = "")
        x = x +1
    print("\n")



##############
#27

List = input("Enter String : ")
List = List.split(",")
print(List)

for i in List:
    print(i, end = "")


##############
#28

numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527
    ]



for j in numbers:
    if j == 237:
        print(j)
        break
    if j != 237:
        mod = j % 2
        if mod == 0:
            print(j , end = ",")


##############
#29

List1 = ["White", "Black", "Red", "Yellow", "Green"]
List2 = ["Red", "Green"]

for i in List1:
    if i not in List2:
        print(i)


##############
#30

Base = float(input("Enter Base : "))
Height = float(input("Enter Height : "))

Area = (Base*Height)/2
print(Area)

"""














































































