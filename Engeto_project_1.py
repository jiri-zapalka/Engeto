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

# | USER |   PASSWORD  |
# -----------------------
# | bob  |     123     |
# | ann  |    pass123  |
# | mike | password123 |
# | liz  |    pass123  |
credentials = {"bob": "123", "ann": "pass123", "mike": "password123",
               "liz": "pass123"}
print("-" * 20, """
        WELCOME
""", "-" * 20)
# Vložení login a jeho kontrola
log_user = input("Login: ")
log_password = input("Password: ")
log_credentials = {log_user: log_password}
for user, password in credentials.items():
    if user in log_credentials.keys() and password == log_credentials.get(log_user):
        break
    else:
        print("Invalid Login name or Password")
        exit()
# výběr z připravených textů
print("-" * 40, """
We have 3 texts to be analyzed.
""")
vol_text = int(input("Enter a number btw. 1 and 3 to select: ")) - 1
print(TEXTS[vol_text])
# základní statistika
print("-" * 40)
# příprava seznamu, bez mezer a jiných znaků

work_text = TEXTS[vol_text].split()
# 1
print("There are ", len(work_text), " words in the selected text")
# 2
slova2 = []
while work_text:
    if work_text[0].istitle():
        slova2.append(work_text[0])
    work_text = work_text[1:]
print("There are ", len(slova2), " titlecase word")
# 3
work_text = TEXTS[vol_text].split()
slova3 = []
while work_text:
    if work_text[0].isupper():
        slova3.append(work_text[0])
    work_text = work_text[1:]
print("There are ", len(slova3), " uppercase words")
# 4
work_text = TEXTS[vol_text].split()
slova4 = []
while work_text:
    if work_text[0].islower():
        slova4.append(work_text[0])
    work_text = work_text[1:]
print("There are ", len(slova4), " lowercase words")
# 5
work_text = TEXTS[vol_text].split()
slova5 = []
while work_text:
    if work_text[0].isdigit():
        slova5.append(work_text[0])
    work_text = work_text[1:]
print("There are ", len(slova5), " numeric strings")
# analýza délky slov a jejich četnosti v textu
work_text = TEXTS[vol_text].split()
print("-" * 40,)
delka_slov = {}
for slovo in work_text:
    delka_slov[len(slovo)] = delka_slov.setdefault(len(slovo), 0) + 1
    # seřazení slovníku
sort_delka_slov = sorted(delka_slov.items())
for key, value in sort_delka_slov:
    print(key, ':', value * "*", value)
    # součet všech čísel v textu
print("-" * 40)
prevodnik = [int(x) for x in slova5]
print("If we summed all the numbers in this text we would get: ",
      sum(prevodnik))
print("-" * 40,)
