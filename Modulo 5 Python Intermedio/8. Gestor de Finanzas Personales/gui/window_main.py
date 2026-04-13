import FreeSimpleGUI as sg
from services.storage_service import calculate_totals, load_transactions


def main_window():
    sg.theme("GrayGrayGray")

    headings = ["Type", "Title", "Amount", "Category", "Date", "Description"]
    
    # load data from csv and convert to list for the table
    transactions = load_transactions()
    data = [t.to_csv_row() for t in transactions]
    
    income, expenses, balance = calculate_totals()

    layout = [
        [sg.Text("Finance Manager", font=("Segoe UI", 18, "bold"), justification="center", expand_x=True)],
        [sg.HorizontalSeparator()],

        # display total income, expenses and balance
        [
            sg.Text(f"Income: ${income:.2f}", key="total_income", text_color="green", font=("Segoe UI", 12, "bold")),
            sg.Push(),
            sg.Text(f"Expense: ${expenses:.2f}", key="total_expense", text_color="red", font=("Segoe UI", 12, "bold")),
            sg.Push(),
            sg.Text(f"Balance: ${balance:.2f}", key="total_balance", text_color="blue", font=("Segoe UI", 12, "bold")),
        
        ],

        [sg.HorizontalSeparator()],
        
        # display transactions in a table
        [sg.Table(
            values=data,
            headings=headings,
            key="table",
            auto_size_columns=False,
            col_widths=[10, 20, 10, 15, 12, 30],
            justification="left",
            expand_x=True,
            expand_y=True,
            alternating_row_color="#E8E8E8"
        )],

        [sg.HorizontalSeparator()],

        # buttons
        [
            sg.Push(),
            sg.Button("Add Transaction", size=(15, 1)),
            sg.Button("Export CSV", size=(15, 1)),
            sg.Push()]
    ]
    return sg.Window("Personal Finance Manager", layout, finalize=True, resizable=True)