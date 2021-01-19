# Dao Exercise
Unit = "Start"
while (Unit != "K" and Unit != "L" and Unit != "k" and Unit != "l"):
    TGreen = "\033[32m"
    TRed = "\x1b[31m"

    Weight = input("Please enter your weight : ")
    Unit = input("K(Kg.) or L(Pound) : ")
    if Unit == "K" or Unit == "k" :
        Weight = float(Weight) * 2.2
        print ("Your weight in Pound = " + str(Weight))
    elif Unit == "L" or Unit == "l" :
        Weight = float(Weight) / 2.2
        print("Your weight in Kg. = " + str(Weight))
#    else:
#        print(TRed + "Enter wrong Unit, pls run again " + TGreen + "Good Luck !")


