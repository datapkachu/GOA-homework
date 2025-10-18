a=[1,2,3,4,5,6]
a[2:4]=[10,20,30]
print(a)


b=["apple", "banana", "cherry", "kiwi", "mango"]
b[:2]=["pear", "plum"]
print(b)


c=["a", "b", "c", "d", "e", "f"]
c[-3:]=["x", "y", "z"]
print(c)


d=["გიორგი" , "ირმა" , "საბა" ]
d=["red", "green", "blue", "yellow", "black", "white"]
print(d)


e=input("enter any number:")
if int(b) % 2 == 0:
    print("Even")
else:
    print("Odd")


f=[1,2,3,4,5]
if f[3]%2 == 0:
    print("Even number")
else:
    print("Odd number")


g=[1,2,3,4,5,6,7,8,9,51]
if g[-1] > 50 and g[-1] % 2 == 0:
    print("ეს რიცხვი არის ლუწი და მეტი 50 ზე")
elif g[-1] < 50 and g[-1] % 2 != 0:
    print("ეს რიცხვი არის კენტი და ნაკლები 50 ზე")
elif g[-1] % 2 == 0:
    print("ეს რიცხვი არის ლუწი")
elif g[-1] % 2 != 0:
    print("ეს რიცხვი არის კენტი")


h=[1,2,3,4,5,6,7,8,9,10]
if h[5] % 2 == 0 or h[5] > 100:
    print("even or more than 100")
elif h[3] % 2 != 0 or h[3] < 100:
    print("odd or less than 100")


i="data"
j="data"
if i != j:
    print(True)
else:
    print(False)


