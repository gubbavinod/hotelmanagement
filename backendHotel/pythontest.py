import csv

# Replace 'menu.csv' with the path to your CSV file
file_path = '/Users/santhoshnama/Desktop/React/Project/hotelmanagement/backendHotel/meal_info.csv'

def get_unique_cuisines(csv_file):
    cuisines = set()

    with open(csv_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cuisines.add(row['cuisine'])

    return cuisines

unique_cuisines = get_unique_cuisines(file_path)
print("Different types of cuisines available:")
for cuisine in unique_cuisines:
    print(cuisine)
