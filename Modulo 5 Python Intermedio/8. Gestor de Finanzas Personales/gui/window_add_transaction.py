import FreeSimpleGUI as sg
from services.transaction_service import save_transaction
from services.category_service import get_categories, add_category

def window_add_transaction():
    sg.theme("GrayGrayGray")

    label_size = (10, 1)   # mismo ancho para todos los labels
    input_size = (30, 1)   # mismo ancho para todos los inputs de una línea

    layout = [
        [sg.Text("Add Transaction", key="title",
                font=("Segoe UI", 16, "bold"),
                justification="center",
                expand_x=True)],
        [sg.HorizontalSeparator()],

        # Type
        [
            sg.Text("Type:", size=label_size, justification="right"),
            sg.Radio("Income", "TYPE", key="radio_income", enable_events=True),
            sg.Radio("Expense", "TYPE", key="radio_expense", enable_events=True),
        ],

        # Title
        [
            sg.Text("Title:", size=label_size, justification="right"),
            sg.Input(key="tx_title", size=input_size),
        ],

        # Amount
        [
            sg.Text("Amount:", size=label_size, justification="right"),
            sg.Input(key="amount", size=input_size, enable_events=True),
        ],

        # Category
        [
            sg.Text("Category:", size=label_size, justification="right"),
            sg.Combo(get_categories(), key="category", readonly=True, size=(input_size[0]-4, 1)),
            sg.Button("+", key="add_category", size=(3, 1))
        ],

        # Date
        [
            sg.Text("Date:", size=label_size, justification="right"),
            sg.Input(key="date", size=input_size, readonly=True, enable_events=True),
            sg.Button("📅", key="pick_date", size=(4, 1))
        ],

        # Description
        [
            sg.Text("Description:", size=label_size, justification="right", pad=((0, 5), (4, 4))),
            sg.Multiline(key="description", size=(input_size[0], 5)),
        ],

        [sg.HorizontalSeparator()],
        [sg.Push(), sg.Button("Save", size=(10, 1)), sg.Button("Cancel", size=(10, 1)), sg.Push()],
    ]

    window = sg.Window("New Transaction", layout, modal=True, finalize=True)

    window["amount"].bind("<FocusOut>", "_FOCUS_OUT")
    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, "Cancel"):
            window.close()
            break

        # add new category
        if event == "add_category":
            new_category = sg.popup_get_text("Enter new category:")
            if new_category:
                add_category(new_category)
                window["category"].update(values=get_categories())

        # change title based on type
        if event == "radio_income":
            window["title"].update("Add Income")

        if event == "radio_expense":
            window["title"].update("Add Expense")

        # amount input validation: only allow numbers and one dot
        if event == "amount":
            actual_value = values["amount"]
            
            filtered = "".join([c for c in actual_value if c.isdigit() or c == '.'])
            #avoid multiple dots
            if filtered.count(".") > 1:
                parts = filtered.split(".")
                filtered = parts[0] + "." + "".join(parts[1:])

            if filtered != actual_value:
                window["amount"].update(filtered)

        # add .00 on focus out
        if event == "amount" + "_FOCUS_OUT":
            raw = values["amount"].strip()
            if raw == "":
                raw = "0"
            value_float = float(raw)
            amount_formatted = f"{value_float:.2f}"
            window["amount"].update(amount_formatted)
        
        # open date picker and format date to MM/DD/YYYY
        if event == "pick_date":
            date_tuple = sg.popup_get_date(
                title="Select Date",
                no_titlebar=False,
                keep_on_top=True,
                location=(None, None),
                close_when_chosen = True,
                arrow_font=("Segoe UI", 12),
            )
            if date_tuple:
                month, day, year = date_tuple 
                formatted = f"{month:02d}/{day:02d}/{year:04d}"
                window["date"].update(formatted)

        if event == "Save":
            success, errors = save_transaction(values)

            if not success:
                sg.popup_error("\n".join(errors), title="Validation Errors")
                continue

            sg.popup("Transaction saved successfully!", title="Success")
            window.close()
            break

    return window