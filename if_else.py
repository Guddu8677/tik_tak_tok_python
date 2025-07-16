#if else statement  decision control system
#email guddukumardas121@gmail.com
#password Guddu121@

email=input("Enter your email")
if '@' in email:
    password =input("Enter you password")
    if email =="guddukumardas121@gmail.com" and password =="Guddu121@":
        print("Welcome sucessfull")
    elif email=="guddukumardas121@gmail.com" and password != "Guddu121@":
        print("Password incrrocet")
        password=input("Enter again your password")
        if password == "Guddu121@":
            print("finally correct")
        else:
                print("Still incorrect")
    else:
        print("incorrect credential")
else:
    print("email is worng correct it")
        
