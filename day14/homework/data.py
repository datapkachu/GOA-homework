balance=2000
name=input("hello what is your name?:")
answer=input(f"hi {name} would u like to sign in?:")
if answer=="yes":
    pin=input("enter yout pin:")
else:
    print("why are u here?")
if pin=="123456":
    a=print("pin is correct!")
    print(f"your balance is ${balance}")
    a=input("do you want to withdrow money?:")
    if a=="yes":
        n=int(input("how much do u want to withdrow:"))
        if balance<0:
            print("you cant do that buddy...")
        else:
            print(balance-n)
        print("is your balance")
    else:
        print("have a nice day sir")
else:
    print("pin is incorrect")



