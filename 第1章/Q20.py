num_list = [i+10 for i in range(10)]
print(num_list[7::-3])
print(num_list[1:8:3][::-1])#こっちの方がわかりやすいかも(スライスは2つにまたがって表示可能)