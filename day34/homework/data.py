a=["tbilisi","batumi","moskov","berlin","NewYork"]
for i in range(len(a)):
    if len(a[i]) > 6:
        print(a[i])


b=["duck","cool","Congratulations","piegon","garbage","Acknowledgement"]
for i in b:
    if len(i) % 15 == 0:
        print(i)


d = 1
c = [234,54,51354,654,547,56,23,54,257,467,10231]
for i in c:
    print(d)
    d += 1


e = ["garbage","Chair","uncool","Bread"]
for i in range(len(e)):
    if len(e[i]) == 5:
        print(e[i])


g = 0
b= 0
f = input("enter any word :")
print(len(f))
for i in range(len(f)):
    if f[i] == "a":
        g+=1
    if f[i] == "A":
        b+=1
print(g)
print(b)


j = 0
h = ["data","nika","luka","dachi","goga","gabrieli","sandro"]
for i in range(len(h)):
    if len(h[i]) > len(h[i-1]):
        j=h[i]
print(j)
