def init_database():
    names = ["Picard", "Riker", "Data", "Worf"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
    divs = ["Command", "Command", "Operations", "Security"]
    ids = ["1", "2", "3", "4"]
    return names, ranks, divs, ids
    

def display_menu():
    user_name = input("Enter your full name: ")
    print("\n--- MENU ---")
    print(user_name, "Has sucessfully logged in!")
    print("1. Add member")
    print("2. Remove member")
    print("3. Update rank")
    print("4. Display roster")
    print("5. Search crew")
    print("6. Filter by division")
    print("7. Calculate payroll")
    print("8. Count officers")
    print("9. Exit")

    option = input("Choose an option: ")
    return option
def main():
    names, ranks, divs, ids = init_database()
    print(names, ranks, divs, ids)
    option = display_menu()





main()

