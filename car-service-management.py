cars = {}
while True:
    print("\n 1.' Add car' ,\n 2.'Book service',\n 3.' view',\n  4.'Exit'")
    ch= input("choice:")
    
    if ch =="1":
        id= input("car ID:")
        cars[id] = {
            "name": input("customer:"),
            "car": input("car model:")
        }
        print("car added!")
        
    elif ch =="2":
        id = input("car ID:")
        if id in cars:
            cars[id]["service"]= input("service:")
            cars[id]["bill"]= int(input("Bill:"))
            print("Service booked!")
            
        else:
            print("car not found!")
            
    elif ch =="3":
        for id, data in cars.items():
            print(id,data)
            
    elif ch =="4":
        print("Thank you!")
        break
    
    else:
        print("Invalid choice!")
        
print("visit Again!")