from mind import DigitalMind

mind = DigitalMind()

print("Welcome to Digital Mind Simulator")

while True:
    mind.status()

    print("\nChoose an action:")
    print("1. Work")
    print("2. Eat")
    print("3. Sleep")
    print("4. Relax")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        mind.work()
    elif choice == "2":
        mind.eat()
    elif choice == "3":
        mind.sleep()
    elif choice == "4":
        mind.relax()
    elif choice == "5":
        print("Exiting simulation...")
        break
    else:
        print("Invalid choice")