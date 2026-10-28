rsrp_dbm=-95
p_mw=10**(rsrp_dbm/10)
print(f"{rsrp_dbm} dBm= {p_mw:.2e} mW")
value=[-85,-97,-110,-102,-118]
for v in value:
    if v<-105:
        print(v, "dBm - zəif siqnal")
    else:
        print(v, "dBm - normal")
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
print("=== Kərpic 7 ===")
rsrp_list=[-91.5,-108.1,-86.2,-103.3,-110.4]
weak=0
for v in rsrp_list:
    if v<-105:
        print(v, "->zeif")
        weak=weak+1
    else:
        print(v,"->normal")
print("Zeif olcme sayi:"), weak
n=int(input())
if n<7:
    print(n,"kicikdir 7")
elif  n==7:
    print(n,"beraberdir 7")
elif n%7==0:
    print(n,"7ye tam bolunur")
else:
    print(n,"boyukdur")


