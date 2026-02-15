def init_database():
    names = ["Picard", "Riker", "Data", "Worf", "Spock"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Cadet"]
    divs = ["Command", "Command", "Operations", "Security", "Sciences"]
    ids = ["1", "2", "3", "4", "5"]
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

def add_member(names, ranks, divs, ids):


    new_member = input("Enter the new members name: ")
    new_rank = input("Choose your rank: ")
    new_divs = input("Choose your division: ")
    new_ids = input("Choose your ID: ")


    validate_ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Cadet"]
    if new_rank in validate_ranks:
        names.append(new_member)
        ranks.append(new_rank)
        divs.append(new_divs)
        ids.append(new_ids)
        print("New member has successfully been added! ")
    else:
        print("This rank is invalid. Please choose another rank. ")

        
    

    if new_ids in ids:
       print("This ID cannot be used, please choose a different one.")
       return

def remove_member(names, ranks, divs, ids):
    user_id = input("Enter the ID that you would like to remove? ")

    if user_id not in ids:
        print("This id does not exist! ")
        return
    rem = ids.index(user_id)
    names.pop(rem)
    ranks.pop(rem)
    divs.pop(rem)
    ids.pop(rem)
    print("This member has sucessfully been removed! ")
    
def update_rank(names, ranks, ids):
    member_id = input("Enter the id of the rank that you would like to update: ")
    if member_id not in ids:
        print("This user id does not exist! ")
        return
    update = ids.index(member_id)
    rank_update = input("Please enter your new rank: ")
    ranks[update] = rank_update
    print("Your rank has successfully been updated! ")

def display_roster(names, ranks, divs, ids):
     print("\n--- Roster ---")
     print("name", end= "           ")
     print("rank", end="            ")
     print("division", end= "           ")
     print("ID")

     for i in range(len(names)):
         print(names[i], end= "         ")
         print(ranks[i], end= "         ")
         print(divs[i], end= "         ")
         print(ids[i])

def search_crew(names, ranks, divs, ids):
    search_term = input("Enter the name that you would like to search: ")
    for i in range(len(names)):
        if search_term in names[i]:
            print("Name", names[i])
            print("Rank", ranks[i])
            print("Division", divs[i])
            print("ID", ids[i])
        
            
            




    
    
        



    


def main():
    names, ranks, divs, ids = init_database()
    print(names, ranks, divs, ids)
    option = display_menu()
    if option == "1":
        add_member(names, ranks, divs, ids)
    elif option == "9":
        print("You have successfully logged out! ")
    
    elif option == "2":
        remove_member(names, ranks, divs, ids)
    elif option == "3":
        update_rank(names, ranks, ids)
    elif option == "4":
        display_roster(names, ranks, divs, ids)
    elif option == "5":
        search_crew(names, ranks, divs, ids)

    




main()

