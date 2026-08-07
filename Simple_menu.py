# Match-case

def simple_menu(choice):
    match choice:
        case 1:
            return "Login selected"
        case 2:
            return "Register selected"
        case 3:
            return "Good-bye"
        case _:
            return "Invalid choice"



print("=== MENU ===")
print("1. Login")
print("2. Register")
print("3. Exit")

print (simple_menu( choice = int(input("Select the menu : "))))
