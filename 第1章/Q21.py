anko_list = ["こしあん","ごまあん","栗あん","かぼちゃあん"]
anko_char = []
for anko in anko_list:
  for chara in anko:
    anko_char.append(chara)

print(anko_char)

anko_char.clear()
for anko in anko_list:
  print(list(anko))
  anko_char += anko#これでも可能(ankoがリスト型にキャストされた)
print(anko_char)