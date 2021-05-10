import math

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
    # Get total withdrawn from each category
    total_withdrawals = []
    for category in categories:
        total = 0
        for entry in category.ledger:
            if int(entry["amount"]) < 0:
                total += int(entry["amount"])
            total_withdrawals.append(total)
    # Get total_spend
    total_spend = sum(total_withdrawals)
    # Calculate each category as rounded % of total_spend
    # percent_spends = []
    # for item in total_withdrawals:

    title = "Percentage spent by category"

    # Build bars
    # Loop over categories, if category == %, add o
    upper_chart = ""
    total = 100
    while total > 0:
        row = f"{total}|"
        for category in total_withdrawals:
            if round_down(category/total_spend) == total:
                row = row + " o"
                
            
    
    # Print lines
    # lines = "    -" + ("-" * (len(categories) * 3))

    # Print category names
    # Loop over categories
    # 
    return chart
    
def round_down(n, decimals=-1):
    multiplier = 10 ** decimals
    return int(math.floor(n * multiplier) / multiplier)

print(round_down(55//60))