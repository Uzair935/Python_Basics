"""def check_no():
    while True:
        try:
            Num = int(input("Enter a number to check wheather it's positive,negative,zero: "))
            break
        except ValueError:
            print("INVALID INPUT!")

    if Num>0 :
        print("It's positive")
    elif Num<0 :
        print("It's negative")
    else:
        print("It's zero")
check_no()"""

def vowel_check():
    while True:
        var = str(input("Enter alphabet to check wheather it is a vowel or not: "))
        if len(var)==1:
            break
        else:
            print("INPUT IS TOO LONG!")

    Vowels = ["a","e","i","o","u"]
    if var.lower() in Vowels:
        print(f"{var} is a vowel")
    else:
        print(f"{var} is not a vowel")
vowel_check()