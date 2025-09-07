print(2122+2)
print(43+64)
print(3+9)

print(12/4)
print(7/3)
print(8/5)

print(2*8)
print(4*75)
print(9*12)

print(12//4)
print(3//2)
print(60//31)

print(7**2)
print(5**4)
print(10**3)

print(10%4)
print(90%70)
print(54%7)


# დღეს ვისწავლეთ % , // , ** მათემატიკური ოპერატორები...
# % პირველი რიცხვის მეორეზე გაყოფისას გამოგვიტანს დარჩენილ ნაშთს.
# // გვაჩვენებს თუ მეორე რიცხვი პირველში რამდენჯერ მოთავსდება.
# ** პირველ რიცხვს მეორეზე ახარისხებს.

print(12//5)
print(3//5)
print(8//3)
print(71//54)
print(7//3)

print(7**2)
print(80**12)
print(17**6)
print(5**4)
print(3**14)

print(6%4)
print(74%7)
print(9%6)
print(4%2)
print(12%5)


# 15 / 3 = 5
# 20 / 4 = 5
# 100 / 20 = 5

# 15 // 10 = 1
# 10 // 7 = 1
# 40 // 12 = 3

# 4 * 3 = 12
# 40 * 3 = 120
# 120 * 3 = 360

# 4 ** 3 = 64
# 10 ** 3 = 1000
# 2 ** 6 = 64
# 3 ** 4 = 81

# 10 % 7 = 3
# 3 % 2 = 1
# 50 % 25 = 0
# 14 % 11 = 3
# 110 % 50 = 10


# სიები და ცვლადები ერთმანეთისგან იმით განსხვავდებიან, რომ სიაში ბევრი მნიშვნელობის, ხოლო ცვლადში ერთი მნიშვნელობის ჩაწერა შეიზლება
# სიას იყენებენ ერთ ცვლადში ბევრი რამის შესანახად


names=["data" , "nika" , "luka" , "temo"]
numbers=[12 , 30 , 40 , 54]
floats=[5.7 , 7.8 , 80.23 , 76.32]
boolean=[True , False]
everything=[True , 4.6 , 15 , "data12345"]


a=float(input("enter first number:"))
b=float(input("enter second numer:"))
print(a**b)
print(a//b)
print(a%b)


c=int(input("რამდენ ხინკალს შეჭამდი:"))
if c >= 30 and c <=99:
    print("between 30 and 100")
elif c >= 100 and c <= 200:
    print("between 100 and 200")
else:
    print("other number")


d=12
e=3.6
f=True
g="data"
h=False
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))


i = 50
while i != 100:
    print(i)
    i = i + 5


for j in range(40,90,3):
    print(j)


for k in range(15):
    print("დათა საკანდელიზე")

me = 1
while me != 15:
    print("დათა საკანდელიზე")
    me = me + 1


l=input("enter your name:")
if l == "data":
    m=input("enter your surname:")
    if m == "sakandelidze":
        print("same name and same surname")
    else:
        print("same name but different surname")
else:
    print("aqedan moshordi")


password="data123"
m=input("enter password:")
while m != password:
    m=input("enter password:")
    if m == password:
        print("გამოიცანი")
