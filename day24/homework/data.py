a=[1,2,3,4,5,6,7]
print(a[-1]*a[-7])
print(a[2])
print(a[-5])


b=("apple","banana","cherry","grape","kiwi","orange")
print(b[2] , b[3])
print(b[-3] , b[-4])


c=(3,4,5,6,7,1,2,9,8,11)
d=int(input("აირჩიე ციფრი 1 ადნ 10 მდე:"))
if d >= 0 and d < 10:
    print(c[d])
elif d >= 10 or d < 0:
    print("you entered negative or more than number 10")


e=["dog" ," most" ,"is" ,"angry" ,"running"  , "forest", "fast", "in" , "cat" ,"human", "very"]
print(e[0] , e[2] , e[4] , e[-4] , e[-6] , e[-1] , e[-5])


f=["dog", "cat", "horse", "cow", "sheep", "goat"]
g=input("do u prefer a cat or a gaot:")
if g == f[1]:
    print("your choice was a cat")
elif g == "goat":
    print("your choice was a goat")
else:
    print("you chose another animal")


h=("tbilisi","batumi","new york","tokyo","moscow","baku")
i=int(input("pick a number between 0 to 5:"))
j=int(input("pick another number between 0 to 5:"))
if i < j:
    print(h[i] , h[j])
elif i > j:
    print(h[j] , h[i])
elif i == j:
    print(h[i])


k=input("type something:")
if k[0] == "a" and k[-1] != "z":
    print("სიტყვა იწყება a-თი")
elif k[-1] == "z" and k[0] != "a":
    print("სიტყვა მთავრდება z-ით")
elif k[0] == "a" and k[-1] == "z":
    print("ეს სიტყვა იწყება a-თი და მთავრდება z-თი")
else:
    print("სიტყვა არც a-თი იწყება და არც z-ით მთავრდება")


l=input("type anything:")
if l[0] == l[-1]:
    print("პირველი და ბოლო ერთნაირია")
else:
    print("პირველი და ბოლო განსხვავებულია")


m="agivorsbgitr"
print(m[-4] + m[4] + m[-4] +m[0])
print(m[-6] + m[0] + m[-5] +m[0])
print(m[-5] + m[0] + m[-2] +m[2] , m[3] + m[0] + m[-1])


n="giorgi"
o=0
while o < 6:
    print(n[o])
    o+=1 

p="giorgi"
for q in range(6):
    print(p[q])