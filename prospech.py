import json
with open('data.json', encoding='utf-8') as soubor:
    prospech = json.load(soubor)
print(prospech)
dal_nedal = {} 
for name, points in prospech.items():
    if points >= 60 :
        dal_nedal[name] = "prospel"
    else : 
        dal_nedal[name] = "neprospel"
with open("prospech.json", mode="w", encoding="utf-8") as vystupni_soubor:
    json.dump(dal_nedal, vystupni_soubor, ensure_ascii=False)
# Bonusovy ukol
with open('data1.json', encoding='utf-8') as soubor:
    body = json.load(soubor)
total_grade = {}
for name, bonus_points in body.items():
    prospech[name] += bonus_points
for name, total_points in prospech.items():
    if total_points >= 90 :
        total_grade[name] = 1
    elif total_points >= 70 :
        total_grade[name] = 2
    elif total_points >= 50 :
        total_grade[name] = 3
    elif total_points >= 30 :
        total_grade[name] = 4
    else :
        total_grade[name] = 5
with open("znamky.json", mode="w", encoding="utf-8") as vystupni_soubor:
    json.dump(total_grade, vystupni_soubor, ensure_ascii=False)