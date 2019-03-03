squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)
#不使用局部变量/临时变量square
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

#列表解析
squares = [value**2 for value in range(1,11)]
print(squares)

million = 0
for value in range(1,1000001):
    million = value + million
print(million)
print(min(range(1,1000001)))
print(max(range(1,1000001)))
print(sum(range(1,1000001)))


qishu = [i for i in range(1,21,2)]
print(qishu)

chuyi3 = []
for i in range(0,46):
    if i%3 == 0:
        chuyi3.append(i)
print(chuyi3)


lifang = [value**3 for value in range(1,11)]
print(lifang)