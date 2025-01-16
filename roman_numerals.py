#convert roman numbers to numerals

numeral_input = input("Enter a roman numeral you want to convert: ")

def roman_to_int(numeral):
    final_ans = 0
    if "CM" in numeral:
        final_ans +=900
        numeral = numeral.replace("CM", "")

    if "CD"in numeral:
        final_ans +=400
        numeral = numeral.replace("CD", "")
    
    if "XC" in numeral:
        final_ans +=90
        numeral = numeral.replace("XC", "")
    
    if "XL" in numeral:
        final_ans +=40
        numeral = numeral.replace("XL", "")

    if "IX" in numeral:
        final_ans +=9
        numeral = numeral.replace("IX", "")

    if "IV" in numeral:
        final_ans +=4
        numeral = numeral.replace("IV", "")

    for i in numeral:
        if i == "M":
            final_ans += 1000
        elif i =="D":
            final_ans +=500
        elif i == "C":
            final_ans +=100
        elif i == "L":
            final_ans +=50
        elif i == "X":
            final_ans +=10
        elif i == "V":
            final_ans +=5
        elif i == "I":
            final_ans +=1




    print("The roman numerals you wanted to translates tO: " + str(final_ans)+ "!!")

roman_to_int(numeral_input)
