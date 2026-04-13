import FreeSimpleGUI as sg
from gui.window_main import main_window
from gui.window_add_transaction import window_add_transaction
from services.storage_service import calculate_totals, load_transactions
from services.export_service import export_to_csv


def main():
    window = main_window()

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        if event == 'Add Transaction':
            # open the add transaction window
            window_add_transaction()
            
            # after closing the add transaction window, refresh the table data
            transactions = load_transactions()
            updated_data = [t.to_csv_row() for t in transactions]
            window["table"].update(values=updated_data)

            # also refresh the totals
            income, expenses, balance = calculate_totals()
            window["total_income"].update(f"Income: ${income:.2f}")
            window["total_expense"].update(f"Expense: ${expenses:.2f}")
            window["total_balance"].update(f"Balance: ${balance:.2f}")

        if event == 'Export CSV':
            save_path = sg.popup_get_file(
                "Save CSV",
                save_as=True,
                default_extension=".csv",
                file_types=(("CSV Files", "*.csv"),)
            )
            if save_path:
                export_to_csv(save_path)
                sg.popup("Exported successfully!", title="Success")

        if event == 'Back':
            window.close()
            window = main_window()

    window.close()

if __name__ == "__main__":
    main()
