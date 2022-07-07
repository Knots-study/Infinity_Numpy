anko_list = ["こしあん","ごまあん","栗あん","かぼちゃあん"]
print(sorted(anko_list))
print(anko_list)#sortedは非破壊的メゾッド
anko_list.sort()
print(anko_list)#sortは破壊的メゾッド