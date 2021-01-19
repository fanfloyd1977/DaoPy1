def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = int(result)*int(base_num)
    return result

base_num = int(input("Please enter base value : "))
pow_num = int(input("Please enter power value : "))
print (raise_to_power(base_num,pow_num))

def translate(phase):
    translation = ""
    for letter in phase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("Please enter Phase : ")))



]

