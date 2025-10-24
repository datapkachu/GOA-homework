for i in range(1,50):
    if i % 2 == 0:
        print(f"ლუწი {i}")
    elif i % 2 == 1:
        print(f"კენტი {i}")
    elif i == 0:
        print(f"ნული {i}")


for i in range(20):
    if i % 15 == 0:
        print(f"იყოფა 3-ზე და 5-ზე{i}")
    elif i % 3 == 0:
        print(f"იყოფა 3-ზე {i}")
    elif i % 5 == 0:
        print(f"იყოფა 5-ზე{i}")
    elif i % 15 == 0:
        print(f"იყოფა 3-ზე და 5-ზე{i}")
    else:
        print(f"არ იყოფა არცერთზე {i}")


x=0
y=0
f=int(input("enter any number :"))
for i in range(f):
    if i % 2 == 0:
        x += 1
    elif i % 2 != 0:
        y += 1
print(x)
print(y)



a=[10, 25, 33, 47, 80, 99]
for i in range(6):
    if a[i] > 50:
        print("მეტი 50-ზე")
    elif a[i] <50:
        print("ნაკლები 50-ზე")


sum=0
for i in range(100):
    if i % 2 == 0:
        print(i)
        sum += i
print(f"ლუწი რიცხვების ჯამია: {sum}")


c=["avarage","cool","under","apple"]
for i in c:
    if i[0] == "a":
        print(i)


for i in range(20):
    if i % 2 == 0:
        print("ლუწი")
    elif i % 2 == 1:
        print("კენტი")
    elif i == 0:
        print("ნული")


b=[5, 15, 25, 35, 45, 55]
for i in range(6):
    print(b[i])


c = input("eneter any word:")
for i in c:
    print(i)


total = 0
for i in range(1,10):
    total += i
print(f"ჯამი არის: {total}")
