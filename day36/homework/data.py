a = input("type in anything :")
for i in a:
    if "e" == i or "E" == i:
        break
    print(i)


b = input("type whatever you want :")
for i in b:
    if "bad" in b:
        print("აკრძალულუ სიტყვა")
        break
    else:
        print("ყველაფერი კარგადაა")
        break


c = input("type it out :")
for i in c:
    if i == " ":
        continue
    print(i)


d = input("aba tu magari xar xmovnebi dawere :")
for i in d:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        continue
    print(i)


e = int(input("enter 1st number :"))
f = int(input("enter 2nd number :"))
for i in range(e,f):
    if i % 15 == 0:
        print(i)
        break


g = input("enter (python is the best) :")
while g != "python is the best":
    print("you should learn python")
    g = input("enter (python is the best) :")


r = 0
h = int(input("enter 1st number :"))
j = int(input("enter 2nd number :"))
for i in range(h,j):
    if i % 3 == 0:
        r += 1
    if r == 3:
        print(i)
        break


