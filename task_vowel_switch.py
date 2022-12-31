vowel = input("Enter any alphabet to check if its vowel or not:")
match vowel.lower():
    case "a":
        print("it is vowel")
    case "e":
        print("it is vowel")
    case "i":
        print("it is a vowel")
    case "o":
        print("it is a vowel")
    case "u":
        print("it is vowel")
    case _:
        print("it is not vowel")