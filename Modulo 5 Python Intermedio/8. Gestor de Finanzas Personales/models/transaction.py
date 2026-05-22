import datetime

class Transaction:
    def __init__(self, transaction_type, title, amount, category, date, description):
        self.transaction_type = transaction_type
        self.title = title
        self.amount_raw = amount
        self.category = category
        self.date = date
        self.description = description

        self.amount = None

    # ------------------------------------------------------------
    # Converts a CSV row (list of strings) to a Transaction object
    # ------------------------------------------------------------
    @classmethod
    def from_csv_row(cls, row):
        obj = cls(
            transaction_type=row[0],
            title=row[1],
            amount=row[2],
            category=row[3],
            date=row[4],
            description=row[5]
        )
        obj.amount = float(row[2])
        return obj
    
    # ------------------------------------------------------------
    # Converts a Transaction object to a CSV row (list of strings)
    # ------------------------------------------------------------
    def to_csv_row(self):
        return [
            self.transaction_type,
            self.title,
            f"{self.amount:.2f}",
            self.category,
            self.date,
            self.description.replace("\n", " ")
        ]
    
    # ------------------------------------------------------------
    # validations
    # ------------------------------------------------------------
    def validations(self):
        errors = []

        # Title
        if not self.title.strip():\
            errors.append("Title cannot be empty.")

        # Amount empty or not a number
        if not str(self.amount_raw).strip():
            errors.append("Amount cannot be empty.")
        else:
            try:
                value = float(self.amount_raw)
                if value <= 0:
                    errors.append("Amount must be greater than 0.00.")
                else:
                    self.amount = value
            except ValueError:
                errors.append("Amount must be a number.")

        #category
        if not self.category.strip():
            errors.append("Category must be selected.")

        #Date (MM/DD/YYYY)
        try:
            date_obj = datetime.datetime.strptime(self.date, "%m/%d/%Y").date()
            today = datetime.date.today()

            if date_obj > today:
                errors.append("Date cannot be in the future.")
                
        except ValueError:
            errors.append("Date must be in format MM/DD/YYYY.")

        return errors
