def display_title():
    print("\n==============================")
    print("  Disneyland Reviews Explorer")
    print("==============================\n")

def display_main_menu():
    print("Main Menu:")
    print("A - View Data")
    print("B - View Visual Data")
    print("C - Export Data")
    print("EXIT - Exit the Program")
    return input("Enter your choice: ").strip().upper()

def display_view_data_menu():
    print("\nView Data Menu (A):")
    print("1 - View all reviews for a specific park")
    print("2 - Count reviews from a specific location for a specific park")
    print("3 - Show average rating for a park in a specific year")
    print("4 - Back to Main Menu")
    return input("Enter your choice (1–4): ").strip()