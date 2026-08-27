cars = {}
while True:
    print("\n 1.' Add car' ,\n 2.'Book service',\n 3.' view cars',\n  4.'Search cars' ,\n 5.'Update car',\n 6.' Generate Bill',\n 7.'Exit'")
    ch= input("choice:")
    
    if ch =="1":
        id= input("car ID:")
        cars[id] = {
            "name": input("customer:"),
            "car": input("car model:"),
            "service": "Not Booked",
            "status": "pending",
            "bill": 0
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
        id = input("car Id:")
        
        if id in cars:
            print(cars[id])
        else:
            print("car not found!")
            
    elif ch =="5":
        id = input("car ID:")
        
        if id in cars:
            cars[id]["status"]= input("status:")
            print("status updated!")
            
        else:
            print("car not found!")
            
    elif ch =="5":
        id = input("Car Id:")
        
        if id in cars:
            print("Customer:",cars[id]["name"])
            print("Service:",cars[id]["service"])
            print("Total Bill: Rs.",cars[id]["bill"])
            
    elif ch =="7":
        print("Thank you!")
        break
    
    else:
        print("Invalid choice!")
        
print("visit Again!")