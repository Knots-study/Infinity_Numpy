anko_list = ["こしあん","ごまあん","栗あん","かぼちゃあん"]
anko_char = []
for anko in anko_list:
  anko_char += anko
anko_char.remove("栗")
print(anko_char)