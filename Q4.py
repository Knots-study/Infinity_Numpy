anko_a_name = ["こしあん","ごまあん","栗あん","かぼちゃあん"]

for anko in anko_a_name:
    if(len(anko) == 4):
        print(anko + "　価格：{}円".format(100))
    else:
        print(anko + "　価格：{}円".format(150))
    