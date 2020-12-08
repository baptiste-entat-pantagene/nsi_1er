lyceens = {"lyceen_1" : 13 , "lyceen_2" : 17 , "lyceen_3" : 9 , "lyceen_4" : 15 , "lyceen_5" : 8 , "lyceen_6" : 14 , "lyceen_7" : 16 , "lyceen_8" : 12 ,"lyceen_9" : 13 , "lyceen_10" : 15 , "lyceen_11" : 14 , "lyceen_12" : 9 , "lyceen_13" : 10 , "lyceen_14" : 12 , "lyceen_15" : 13 , "lyceen_16" : 7 ,"lyceen_17" : 12 , "lyceen_18" : 15 , "lyceen_19" : 9 , "lyceen_20" : 17}
lyceenAdmis = {}
lyceenNonAdmis = {}

for k, v in lyceens.items():
    if v < 10: lyceenNonAdmis[k] = v
    else: lyceenAdmis[k] = v

print("admis -->", lyceenAdmis)
print("\nnon admis -->", lyceenNonAdmis)