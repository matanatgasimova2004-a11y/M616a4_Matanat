# # Dərs 3 · Blok 1 — Python-un 10 kərpici
# # İşə salma (de-praktikum qovluğundan): python src/l3_basics_start.py
# # Dərsdə hər kərpicin kodunu slayddan öz bölməsinə yazırıq.
# # Hər bölmə əvvəlcə öz başlığını çap edir — terminalda həmişə
# # ən aşağıdakı bölməyə baxın. Tam kod dərsdən sonra Teams-də olacaq.

# print("=== Kərpic 1 ===")   # Proqram — əmrlər ardıcıllığı
# # TODO: print(...) ilə 4 sətir (slayd «Kərpic 1»)
# print("Salam, data mühəndisliyi!")
# print("Baza stansiyası:", "BAK-0207")
# print(2+3)
# print("2+3")
# print("=== Kərpic 2 ===")   # Dəyişən — adı olan qutu
# # TODO: cell, rsrp, drops
# cell= "BAK-0207"
# rsrp=-95.5
# print(cell, rsrp)
# rsrp=-108.1
# print(cell, rsrp)
# drops=2
# drops=drops+1
# print("drops=",drops)
# name="Matanat"
# age=22
# print("Mənim adım",name , "." , "Mənim ", age , "yaşım var.")
# print("=== Kərpic 3 ===")   # Tiplər: int, float, str, bool, None
# # TODO: type(...) və «mətn ≠ ədəd»
# name=input("please enter your name")
# age=int(input("please eter your age"))
# print(f"ad {name}, yas {age+1}")
# print(age<25)
# print(age>25)
print("=== Kərpic 6 ===")
row={"cell_id": "BAK-0207","region":"Yasamal","rsrp_dbm": -108.1}
print(row["region"])
print(row["rsrp_dbm"])
row["band"]="LTE800"
print(row)
row["region"]="Nasimi"
print(row)
row["region"]=input("please enter new region")
print(row)
print("=== Kərpic 6 ===")
rsrp_list=[-91.5,-108.1,-86.2,-103.3,-110.4]
for v in rsrp_list:
    print(v)
    deyer=int(input("* = "))
    print(v*deyer)







