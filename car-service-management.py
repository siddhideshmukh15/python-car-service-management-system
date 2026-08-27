cars = {}

while True:
    print("\n===== CAR SERVICING MANAGEMENT SYSTEM =====")
    print("1. Add Car")
    print("2. Book Service")
    print("3. View Cars")
    print("4. Search Car")
    print("5. Update Service Status")
    print("6. Generate Bill")
    print("7. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        id = input("Car ID: ")

        if id in cars:
            print("Car already exists!")
        else:
            cars[id] = {
                "name": input("Customer Name: "),
                "car": input("Car Model: "),
                "service": "Not Booked",
                "status": "Pending",
                "bill": 0
            }
            print("Car added successfully!")

    elif ch == "2":
        id = input("Car ID: ")

        if id in cars:
            print("\nAvailable Services")
            print("1. Oil Change - Rs.1500")
            print("2. General Service - Rs.2500")
            print("3. Brake Service - Rs.3000")
            print("4. AC Service - Rs.2000")

            service = input("Choose service: ")

            if service == "1":
                cars[id]["service"] = "Oil Change"
                cars[id]["bill"] = 1500
            elif service == "2":
                cars[id]["service"] = "General Service"
                cars[id]["bill"] = 2500
            elif service == "3":
                cars[id]["service"] = "Brake Service"
                cars[id]["bill"] = 3000
            elif service == "4":
                cars[id]["service"] = "AC Service"
                cars[id]["bill"] = 2000
            else:
                print("Invalid service!")
                continue

            cars[id]["status"] = "Pending"
            print("Service booked successfully!")

        else:
            print("Car not found!")

    elif ch == "3":
        if not cars:
            print("No cars available!")
        else:
            for id, data in cars.items():
                print("\nCar ID:", id)
                print("Customer:", data["name"])
                print("Car Model:", data["car"])
                print("Service:", data["service"])
                print("Status:", data["status"])
                print("Bill: Rs.", data["bill"])

    elif ch == "4":
        id = input("Car ID: ")

        if id in cars:
            print("\n--- Car Details ---")
            print("Car ID:", id)
            print("Customer:", cars[id]["name"])
            print("Car Model:", cars[id]["car"])
            print("Service:", cars[id]["service"])
            print("Status:", cars[id]["status"])
            print("Bill: Rs.", cars[id]["bill"])
        else:
            print("Car not found!")

    elif ch == "5":
        id = input("Car ID: ")

        if id in cars:
            print("\n1. Pending")
            print("2. In Service")
            print("3. Completed")

            status = input("Choose status: ")

            if status == "1":
                cars[id]["status"] = "Pending"
            elif status == "2":
                cars[id]["status"] = "In Service"
            elif status == "3":
                cars[id]["status"] = "Completed"
            else:
                print("Invalid status!")
                continue

            print("Status updated!")
        else:
            print("Car not found!")

    elif ch == "6":
        id = input("Car ID: ")

        if id in cars:
            if cars[id]["service"] == "Not Booked":
                print("No service booked!")
            else:
                print("\n========== BILL ==========")
                print("Customer:", cars[id]["name"])
                print("Car Model:", cars[id]["car"])
                print("Service:", cars[id]["service"])
                print("Status:", cars[id]["status"])
                print("Total Bill: Rs.", cars[id]["bill"])
                print("==========================")
        else:
            print("Car not found!")

    elif ch == "7":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")

print("Visit Again!")