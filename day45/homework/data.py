# a = [1,2,3,4,5,6,7,8,9]
# b = []
# for i in a:
#     if i % 2 == 0:
#         b.append(i)
# print(b)


# c = [1,2,3,4,5,6,7,8,9]
# d = []
# for i in c:
#     if i % 2 != 0:
#         d.append(i)
# print(d)


# e = ["data" , "nika" , "goga" , "giorgi" , "levani" , "gogi"]
# for i in e:
#     if "g" in i[0] and "i" in i[-1]:
#         e.remove(i)
# print(e)

# e1 = ["data" , "nika" , "goga" , "giorgi" , "levani" , "gogi"]
# g = 0
# for i in e1:
#     g += 1
#     if "g" in i[0] and "i" in i[-1]:
#         e1.pop(g-1)
# print(e1)


# k = ["data" , "nika" , "GOGA" , "giorgi" , "levani" , "GOGI"]
# for i in k:
#     if "G" in i[0] and i[-2] == i[-2].upper() and i[-1] == i[-1].upper():
#         k.remove(i)
# for i in range(len(k)):
#     k[i]= k[i].upper()
# print(k)


l = [1,2,3,4,5,6,7,8,9]
m = ["data" , "nika" , "GOGA" , "giorgi" , "levani" , "GOGI"]
for i in l:
    if i % 2 == 0 and i != 0:
        l.remove(i)
print(l)
