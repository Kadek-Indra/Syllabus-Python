list_number = {"a" : 4,
               "b" : 10,
               "c" : 10,
               "e" : 9}

correct_number = sorted(set(list_number.values()), reverse=True)[:2]


print (correct_number)

