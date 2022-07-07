with open("D:/numpy_book/data/hokkaido_raw.txt",encoding = "utf-8") as fp:#
  text = fp.readlines()#ファイル全体を行単位で区切ってリスト化できる
hokkaido = []
for tx in text:
  item = tx.replace("\n","").split(",")
  item.insert(2,item[1][-1])
  item[-1] = int(item[-1])
  hokkaido.append(item)
print(hokkaido)