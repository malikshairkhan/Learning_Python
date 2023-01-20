my_small_list = ["a","b","c","d","e"]
case_changer = lambda my_small_list : my_small_list.upper()

final_value = map(case_changer,my_small_list)
print(list(final_value))

