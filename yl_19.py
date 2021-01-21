text = "Kuressaare Hunjakool"
wovels = ["a", "e", "i", "o", "u", "õ", "ä", "ö", "ü"]

i = 0
for c in text:
    if c in wovels:
        i += 1
        print(c)


print(i)