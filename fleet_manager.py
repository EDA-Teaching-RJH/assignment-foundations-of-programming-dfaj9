def init_database():
    n = ["Picard", "Riker", "Data", "Worf"]
    r = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
    d = ["Command", "Command", "Operations", "Security"]
    ids = ["1", "2", "3", "4"]
    return n, r, d, ids
    
def main():
    n, r, d, ids = init_database()
    print(n, r, d, ids)
main()
