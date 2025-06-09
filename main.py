from process import load_data
from tui import display_title, display_main_menu, display_view_data_menu
from visual import (
    show_reviews_pie_chart,
    show_avg_rating_per_park,
    show_top_locations_by_park,
    show_monthly_avg_rating
)

def main():
    display_title()

    # Load data
    data = load_data("Disneyland_reviews.csv")
    if not data:
        print("❌ No data found.")
        return

    print(f"✅ {len(data)} reviews loaded.\n")

    # Main menu loop
    while True:
        choice = display_main_menu()

        if choice == "A":
            # View Data menu
            while True:
                sub_choice = display_view_data_menu()

                if sub_choice == "1":
                    park = input("Enter park name (e.g., Disneyland_Paris): ").strip()
                    matches = [row for row in data if row['Branch'] == park]
                    if matches:
                        print(f"\n{len(matches)} reviews for {park}:\n")
                        for review in matches[:5]:
                            print(review)
                    else:
                        print("No reviews found for that park.")

                elif sub_choice == "2":
                    park = input("Enter park name: ").strip()
                    location = input("Enter reviewer location (e.g., UK): ").strip()
                    count = sum(1 for row in data if row['Branch'] == park and row['Reviewer_Location'] == location)
                    print(f"{count} review(s) for {park} from {location}")

                elif sub_choice == "3":
                    park = input("Enter park name: ").strip()
                    year = input("Enter year (e.g., 2023): ").strip()
                    ratings = [
                        int(row['Rating']) for row in data
                        if row['Branch'] == park and row['Year_Month'].startswith(year)
                    ]
                    if ratings:
                        avg = sum(ratings) / len(ratings)
                        print(f"Average rating for {park} in {year}: {avg:.2f}")
                    else:
                        print("No reviews found for that park in that year.")

                elif sub_choice == "4":
                    print("Returning to Main Menu...\n")
                    break
                else:
                    print("Invalid input. Please enter 1, 2, 3, or 4.")

        elif choice == "B":
            # Visual Data menu
            while True:
                print("\nView Visual Data (B):")
                print("1 - Pie chart: Number of reviews per park")
                print("2 - Bar chart: Average review score per park")
                print("3 - Bar chart: Top 10 locations with highest average rating for a park")
                print("4 - Bar chart: Average monthly rating per park")
                print("5 - Back to Main Menu")

                b_choice = input("Enter your choice: ").strip()

                if b_choice == "1":
                    show_reviews_pie_chart(data)
                elif b_choice == "2":
                    show_avg_rating_per_park(data)
                elif b_choice == "3":
                    show_top_locations_by_park(data)
                elif b_choice == "4":
                    show_monthly_avg_rating(data)
                elif b_choice == "5":
                    print("Returning to Main Menu...\n")
                    break
                else:
                    print("Invalid input. Please enter a number from 1 to 5.")

        elif choice == "C":
            print("💾 Export Data (Menu C) - Not attempted")

        elif choice == "EXIT":
            print("👋 Goodbye!")
            break

        else:
            print("⚠️ Invalid input. Please try again.")

if __name__ == "__main__":
    main()