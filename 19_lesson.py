#  19 Dars While va Ro'yhatlar

# print("Yaqin dostlaringiz ro'yxatini tuzamiz")
# ismlar = []
# n = 1
# while True:
#     savol = f"{n} dostlaringiz ismini kiriting!"
#     ism = input(savol)
#     ismlar.append(ism)
#     takrorlash = input("Yana dostlar qoshasizmi?(ha/yo'q)")
#     n += 1
#     if takrorlash != "ha":
#         break
# print("Dostlaringiz ro'yxati")
# for ism in ismlar:
#     print(ism.title())
# dostlar = {}
# ishora = True

# while ishora:
#     ism = input("Dostlaringiz ismini kiriting!!")
#     yosh = input(f"{ism} yoshini kiriting")
#     dostlar[ism] = int(yosh)

#     javob = input("yana malumot qoshasizmi (ha/yo'q)")
#     if javob == "yo'q":
#         ishora = False

# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")

#  Remove While

# cars = ["nexia", "gentra", "audi", "malibu", "gentra", "gentra"]

# while "gentra" in cars:
#     cars.remove("gentra")
# print(cars)

# talabalar = ["husan", "hasan", "salim", "umid"]
# baholangan_talabalar = {}

# while talabalar:
#     talabalar = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = int(baho)
