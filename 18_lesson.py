#  17 Lesson While

# input

# ism = input("Enter your name? ")
# print(ism)
# savol = f"Salom {ism.title()}. Yoshingiz nechida? "
# yosh = input(savol)

# height = input("Enter your height? ")

# height = float(height)

#  while
# son = 1
# while son <= 10:
#     print(son, end="")
#     son = son + 1

print("Dastur tugadi")

# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' yozing): "
# qiymat = ""

# while qiymat != "exit":
#     qiymat = input(savol)
#     if qiymat != "exit":
#         print(float(qiymat) ** 2)
# print("Dastur tugadi")


#  ishora
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtashish uchun 'exit' deb yozing) "
# ishora = True

# while ishora:
#     qiymat = input(savol)
#     if qiymat == "exit":
#         ishora = False
#     else:
#         print(float(qiymat) ** 2)
# print("Dastur tugadi!!")


# break

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtashish uchun 'exit' deb yozing) "


# while True:
#     qiymat = input(savol)
#     if qiymat == "exit":
#         break
#     else:
#         print(float(qiymat) ** 2)
# print("Dastur tugadi!!")

# sonlar = list(range(1, 11))
# for son in sonlar:
#     if son == 5:
#         break
#     print(f"{son} ning kvadrati {son ** 2} ga teng")


# Continue
# sonlar = list(range(1, 11))
# for son in sonlar:
#     if son == 5:
#         continue
#     print(f"{son} ning kvadrati {son ** 2} ga teng")

# Continue while
# son = 0
# while son < 10:
#     son += 1
#     if son % 2 == 0:
#         continue
#     else:
#         print(son)


# Amaliyot

# savol = "Yaxshi ko'rgan kitoblariz kiriting!"
# while True:
#     kitob = input(savol)
#     if kitob == "stop":
#         break

# print("Raxmat")


#  2

savol = "Yoshingiz kiriting!!"

while True:
    qiymat = input(savol)
    if qiymat == "exit" or "quit":
        break
    yosh = int(qiymat)

    if yosh < 7:
        narx = 2000
    elif 7 <= yosh < 18:
        narx = 3000
    elif 18 <= 65:
        narx = 10000
    else:
        narx = 0
    if narx == 0:
        print("Sizga chipta bepul")
    else:
        print(f"Chipta {narx} som")
