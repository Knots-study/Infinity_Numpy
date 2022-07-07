anko_list = ["こしあん","ごまあん","栗あん","かぼちゃあん"]
anko_char = [];x = []
for anko in anko_list:
  anko_char += anko
for an in anko_char:
  if(an != "あ" and an != "ん"):
    x.append(an)
x.remove("栗")
print(x)