import matplotlib.pyplot as plt
from collections import Counter, defaultdict

# Option 1: Pie chart – number of reviews per park
def show_reviews_pie_chart(data):
    park_names = [row['Branch'] for row in data]
    counts = Counter(park_names)
    labels = counts.keys()
    sizes = counts.values()

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title("Number of Reviews per Park")
    plt.show()

# Option 2: Bar chart – average review score per park
def show_avg_rating_per_park(data):
    park_scores = defaultdict(list)
    for row in data:
        park = row['Branch']
        score = int(row['Rating'])
        park_scores[park].append(score)

    parks = list(park_scores.keys())
    averages = [sum(scores) / len(scores) for scores in park_scores.values()]

    plt.figure(figsize=(8, 5))
    plt.bar(parks, averages)
    plt.title("Average Review Score per Park")
    plt.xlabel("Park")
    plt.ylabel("Average Score")
    plt.ylim(0, 5)
    plt.show()

# Option 3: Bar chart – top 10 locations with highest average rating for a park
def show_top_locations_by_park(data):
    park = input("Enter park name (e.g., Disneyland_Paris): ").strip()
    location_scores = defaultdict(list)

    for row in data:
        if row['Branch'] == park:
            location = row['Reviewer_Location']
            score = int(row['Rating'])
            location_scores[location].append(score)

    if not location_scores:
        print("No data found for that park.")
        return

    avg_by_location = {loc: sum(scores) / len(scores) for loc, scores in location_scores.items()}
    top_10 = sorted(avg_by_location.items(), key=lambda x: x[1], reverse=True)[:10]

    locations = [loc for loc, _ in top_10]
    scores = [score for _, score in top_10]

    plt.figure(figsize=(10, 5))
    plt.bar(locations, scores)
    plt.title(f"Top 10 Locations by Avg Rating for {park}")
    plt.xlabel("Location")
    plt.ylabel("Average Rating")
    plt.ylim(0, 5)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Option 4: Bar chart – average monthly rating per park
def show_monthly_avg_rating(data):
    park = input("Enter park name (e.g., Disneyland_Paris): ").strip()
    monthly_scores = defaultdict(list)

    for row in data:
        if row['Branch'] == park:
            month = row['Year_Month'][5:]  # Get MM from YYYY-MM
            score = int(row['Rating'])
            monthly_scores[month].append(score)

    if not monthly_scores:
        print("No data found for that park.")
        return

    month_order = ['01', '02', '03', '04', '05', '06',
                   '07', '08', '09', '10', '11', '12']
    averages = []
    for m in month_order:
        if m in monthly_scores:
            avg = sum(monthly_scores[m]) / len(monthly_scores[m])
        else:
            avg = 0
        averages.append(avg)

    plt.figure(figsize=(10, 5))
    plt.bar(month_order, averages)
    plt.title(f"Average Monthly Rating for {park}")
    plt.xlabel("Month")
    plt.ylabel("Average Rating")
    plt.ylim(0, 5)
    plt.show()