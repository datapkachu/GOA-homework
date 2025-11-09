a = input("enter your name :")
print(a.upper())


b = input("enetr your name :")
print(b.lower())


c = input("enter your name :")
print(c.capitalize())


d = ["data","nika","luka","dachi","sandro"]
for i in d:
    print(i.upper())


e = ["DATA","NIKA","LUKA","DACHI","SANDRO"]
for i in e:
    print(i.lower())


f = ["data","nika","luka","dachi","sandro"]
for i in f:
    print(i.capitalize())


g = [2,4,6,8,10,12,14,16,18,20]
print(len(g))


print(len("ალექსანდრე"))


j = 1
h = [3,6,9,12,15,18,21,24,27,30]
for i in h:
    if i % 2 == 0:
        print(j)
        j += 1


l = 1
k = [3,6,9,12,15,18,21,24,27,30]
for i in k:
    if i % 2 != 0:
        print(l)
        l += 1


m = input("enter first number :")
n = input("enter second number :")
o = 0
for i in range(int(m),int(n)):
    if i % 2 == 0:
        o += 1
        print(i)
