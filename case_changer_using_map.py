#chnage the lower case character into uper case using function
my_small_list = ["a","b","c","d","e"]
def character_changer(character_value):
    return character_value.upper()

final = map(character_changer,my_small_list)
print(list(final))
