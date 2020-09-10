'''
author =
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]


#| USER |   PASSWORD  |
#-----------------------
#| bob  |     123     |
#| ann  |    pass123  |
#| mike | password123 |
#| liz  |    pass123  |

user_dic = dict()
user1 = {"name" : "bob", "pass" : "123"}
user2 = {"name" : "ann", "pass" : "pass123"}
user3 = {"name" : "mike", "pass" : "password123"}
user4 = {"name" : "liz", "pass" : "pass123"}
user_dic[user1["name"]] = user1
user_dic[user2["name"]] = user2
user_dic[user3["name"]] = user3
user_dic[user4["name"]] = user4

set_user_dic = set(user_dic.keys())

print("="*20, """
        WELCOME
""" ,"="*20)

#Vložení login a jeho kontrola
log_user = input("Login: ")
set_log_user = {log_user}
if not set_log_user.isdisjoint(set_user_dic) == 0:
    print("Invalid user login. Program is closed.")
    exit()
else:
    print("Login is OK, continue.")

#Vložení hesla a jeho kontrola vůči zadanému loginu
log_pass = input("Password: ")
if user_dic[log_user]["pass"] == log_pass:
    print("Password is OK. Continue.")
else:
    print("Invalid user password. Program is closed")
    exit()

