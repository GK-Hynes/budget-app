class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __repr__(self):
        # Generate title
        stars = '*'*((30 - len(self.name)) // 2)
        title = f"{stars}{self.name}{stars}\n"

        # Generate entries
        entry_list = []
        for i in self.ledger:
            description = i["description"][:23]
            amount = "{:.2f}".format(i["amount"])
            space = " "*(30 - (len(description) + len(amount)))
            entry_list.append(f"{description}{space}{amount}")
        entries = "\n".join(entry_list) + "\n"

        # Generate total
        total = f"Total: {self.get_balance()}"

        output = title + entries + total
        return output


# *************Food*************
# initial deposit        1000.00
# groceries               -10.15
# restaurant and more foo -15.89
# Transfer to Clothing    -50.00
# Total: 923.96


    def deposit(self, amount, description=""):
        self.ledger.append({"amount": float(amount), "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        vals = [i["amount"] for i in self.ledger]
        balance = sum(vals)
        return balance

    def transfer(self, amount, other_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other_category.name}")
            other_category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
    
    def check_funds(self, amount):
        balance = self.get_balance()
        if amount > balance:
            return False
        return True


def create_spend_chart(categories):
    pass
