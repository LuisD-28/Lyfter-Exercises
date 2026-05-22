import csv
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
CSV_PATH = os.path.join(DATA_DIR, "categories.csv")

DEFAULT_CATEGORIES = ["Food", "Transport", "Entertainment", "Utilities", "Salary"]

def ensure_categories_csv():
    #create a csv file and add header if it doesn't exist
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    if not os.path.isfile(CSV_PATH):
        with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            for cat in DEFAULT_CATEGORIES:
                writer.writerow([cat])


def get_categories():
    ensure_categories_csv()

    categories = []
    with open(CSV_PATH, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            categories.append(row[0])

    return categories


def add_category(name):
    ensure_categories_csv()

    categories = get_categories()
    if name not in categories:
        with open(CSV_PATH, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([name])
    