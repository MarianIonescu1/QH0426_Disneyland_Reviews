import csv

# Example Disneyland reviews
rows = [
    ["Review_ID", "Rating", "Year_Month", "Reviewer_Location", "Branch"],
    [1, 5, "2023-08", "UK", "Disneyland_Paris"],
    [2, 4, "2022-06", "USA", "Disneyland_California"],
    [3, 3, "2023-05", "Japan", "Disneyland_HongKong"],
    [4, 4, "2023-04", "France", "Disneyland_Paris"],
    [5, 5, "2023-01", "Canada", "Disneyland_California"],
    [6, 2, "2022-12", "Germany", "Disneyland_Paris"],
    [7, 3, "2022-11", "UK", "Disneyland_HongKong"],
    [8, 4, "2023-07", "USA", "Disneyland_California"],
    [9, 5, "2023-06", "Italy", "Disneyland_HongKong"],
    [10, 1, "2022-09", "India", "Disneyland_Paris"]
]

# Create and save the CSV file
with open("Disneyland_reviews.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

print("✅ Disneyland_reviews.csv file has been created with sample data.")