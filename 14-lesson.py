# Lug'atlar bilan ishlash "Dictionary"
# car_0 = {"model": "Gentra", "rang": "black"}
# print(car_0["model"])

# uz_en = {"apple": "olma", "bannena": "banan"}
# print(uz_en["apple"])
# print(uz_en)

# fruits = {"apple": "10000", "tarvuz": "20000", "mandarin": "14000"}
# print(f"Mandarin narhi {fruits["mandarin"]} so'm")

# talaba_0 = {"name": "xajiboyev umidbek", "age": "16", "yil": "2008"}
# talaba_0["kurs"] = 3
# talaba_0["fakultet"] = "informatika"
# talaba_0["name"] = "salim"

# print(
#     f"{talaba_0['name'].title()},\
#   {talaba_0['age']} yoshda,\
#   {talaba_0['yil']}-yilda tugulgan,\
#   {talaba_0['kurs']}, kurs,\
#   {talaba_0['fakultet']}, boyicha o'qiydi"
# )

# Bo'sh lug'at
# talaba_1 = {}

# talaba_1["Name"] = "umidbek"
# talaba_1["Age"] = "16"
# print(f"Talaba {talaba_1['Name']}, {talaba_1['Age']} yosh")

# Malumotlarni ochirish "DEL"
# cars = {}
# cars["Name"] = "Gentra"
# cars["Color"] = "Qora"
# print(f"Bu mashina nomi {cars['Name']}, rangi esa {cars ['Color']}")
# del cars["Name"]
# print(cars)

# Lug'atlarni bir nechta qatorda yozish
telefonlar = {
    "salim": "iphone 14 pro",
    "orif": "Redmi 12 pro",
    "sardor": "Samsung A72",
    "matrasul": "Nokia 3310",
}
# print(telefonlar["salim"])
# print(telefonlar["matrasul"])


# Amaliyot

# phone = telefonlar.get("umka", "Bunday ism mavjud emas")
# print(phone)
otam = {"Name": "Ulug'bek", "Age": "1980", "manzili": "Xanqa"}
tyil = otam["Age"]
vil = otam["manzili"]
print(f"Otamning ismi {otam['Name']}, {tyil} yilda tugilgan, {vil} viloyatida tugilgan")

food = {"salim": "shashlik", "umidbek": "burger", "doniyor": "gamburger", "ali": "osh"}
print(f"Ali sevimli taomi {food['ali']}")
