import csv
import os
from services.storage_service import load_transactions, calculate_totals


def export_to_csv(output_path):
    transactions = load_transactions()
    income, expenses, balance = calculate_totals()

    with open(output_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        # Header
        writer.writerow(["Personal Finance Report"])
        writer.writerow(["Date", "Title", "Amount", "Category", "Type", "Description"])

        # Rows
        for t in transactions:
            amount = t.amount if t.transaction_type == "Income" else -t.amount
            writer.writerow([
                t.date,
                t.title,
                amount,
                t.category,
                t.transaction_type,
                t.description.replace("\n", " ")
            ])

        # Summary
        writer.writerow([])
        writer.writerow(["Summary"])
        writer.writerow(["Total Income", f"${income:.2f}"])
        writer.writerow(["Total Expenses", f"${expenses:.2f}"])
        writer.writerow(["Balance", f"${balance:.2f}"])
        
            