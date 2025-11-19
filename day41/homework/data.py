# .append() ფუნქცია სიის ბოლოში ამატებს ელემენტს
# .insert() ფუნქცია სადაც გინდა იქ ამატებს ელემენტს
# .pop() ფუნქცია სიიდან აშორებს ნებისმიერ 1 ელემენტს ინდექსების გამოყენებით
# .remove() ფუნქცია სიიდან აშორებს ნებისმიერ 1 ელემენტს, ელემენტის სახელის გამოყენებით


a = [1,2,3,4,5,6,7,8,9]
a.append(10)
print(a)


b = ["goga","dachi","luka","zaza","girogi"]
b.append("data")
print(b)


d = ["goga","dachi","luka","zaza","girogi"]
e = input("enter your name :")
d.append(e)
print(d)


f = ["goga","dachi","luka","zaza","girogi"]
f.insert(3 , "data")
print(f)


g = input("enter your name :")
h = input("enter a number between 0 to 6 :")
i = ["goga","dachi","luka","zaza","girogi","zuka"]
i.insert(int(h) , g)
print(i)


fruits = ["apple", "banana"]
fruits.insert(1 , "orange")
print(fruits)


names = ["goga", "saba", "luka"]
names.insert(-1 , "irakli")
print(names)


foods = ["bread", "milk", "cheese"]
foods.insert(0 , "water")
print(foods)


numbers = [5, 10, 15]
numbers.pop(-1)
print(numbers)


fruits = ["apple", "banana", "orange"]
fruits.pop(1)
print(fruits)


names = ["goga", "saba", "luka"]
names.pop(1)
print(names)


colors = ["red", "green", "blue" , "yellow" , "black" , "purple"]
colors.pop(0)
print(colors)
colors.pop(2)
print(colors)


j = input("eneter a number between 0 to 4 :")
tems = ["pen", "pencil", "book", "eraser"]
tems.pop(int(j))
print(tems)


fruits = ["apple", "banana", "orange"]
fruits.remove("banana")
print(fruits)


nums = [3, 5, 3, 7]
nums.remove(3)
print(nums)


colors = ["red", "blue", "green"]
colors.remove("blue")
print(colors)


names = ["goga", "saba", "luka"]
print(names)
k = input("pick a name from the list above :")
names.remove(k)
print(names)


items = ["pen", "pencil", "book", "pencil"]
items.remove("pencil")
print(items)