# son = -50
# if son<0:
#     print('Manfiy son')
# else:
#     print('Musbat son')

# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#     print('Sizga kirish bepul')
# elif yosh<=12:
#     print('Sizga kirish 5000 so\'m')
# else:
#     print('Sizga kirish 10000 so\'m')

# kun = input("Bugun nima kun?>>>")
# if kun.lower() == "shanba" or kun.lower() == "yakshanba":
#     print("Bugun dam olish kuni")
# else:
#     print("Bugun ish kuni")

# kun = input("Bugun nima kun? ")
# harorat = float(input("Havo hararati qanday? "))
# if (kun.lower() == "yakshanba" or kun.lower() == "shanba") and harorat >= 30:
#     print("Ketdik cho'milishga")
# elif (kun.lower() == "yakshanba" or kun.lower() == "shanba") and harorat < 30:
#     print("Bormaymiz")

# boolean
# narx = 10000
# salat = True
# olma = True

# if salat:
#     print("Sotib oldi")
#     narx = narx + 2000

# in operatori
menu = ["somsa", "shashlik", "palov", "norin"]
ovqat = input("Nima buyurtma berasiz?>>>  ")
if ovqat.lower() in menu:
    print('Buyurtma qabul qilindi')
else:
    print("Buyurtma qabul qilinmadi")