anko_a_name = ["こしあん","ごまあん","栗あん","かぼちゃあん"]
anko_b_name = ["大福","大福","あんぱん","あんぱん"]
anko_b = []

for a,b in zip(anko_a_name,anko_b_name):
    anko_b.append([a,b])

for anko in anko_b:
    for item in anko[::-1]:
        print(item[::-1],end=" ")
    print()
