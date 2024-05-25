# 15 lessons Lug'atlar bilan ishlash

# items()

# talaba_0 = {
#     "ism": "Umidbek",
#     "familya": "Hajiboyev",
#     "from": "Xanqa",
#     "Job": "Web developer",
# }

# for kalit, qiymat in talaba_0.items():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat}")


# Keys

vegetables = {
    "olma": 10000,
    "banana": 17000,
    "gilos": 11000,
    "uzum": 14000,
}

# for meva in vegetables_0:
#     print(meva.title())

bozorlik = ["anor", "uzum", "non", "baliq"]

for buyum in bozorlik:
    if buyum not in vegetables:
        print(f"iltimos do'koninggizga {buyum} ham olib keling")
