!git clone https://github.com/koshian2/numpy_book
#指定されたディレクトリに元のリポジトリと同じものを複製複製
#git clone [リポジトリ] [ディレクトリ]
#git clone [リポジトリ]　ディレクトリが指定されていない場合直下にクローンされる
with open("numpy_book/data/hokkaido_raw.txt") as fp:
  text = fp.readlines()#ファイル全体を行単位で区切ってリスト化できる
print(text)