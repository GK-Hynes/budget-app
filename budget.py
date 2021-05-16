import math

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __repr__(self):
        # Generate title
        title = f"{self.name}".center(30,"*") + "\n" 

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

        # Now build table
        output = title + entries + total
        return output

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

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

    def get_withdrawals(self):
        total= 0
        for item in self.ledger:
            if item["amount"] < 0:
                total += item["amount"]
        return total


def create_spend_chart(categories):
    # Helper function for formatting totals
    def round_down(n):
        multiplier = 10
        return int(n * multiplier) / multiplier

    # Get total withdrawn from each category
    total = 0
    withdrawals = []
    for category in categories:
        total += category.get_withdrawals()
        withdrawals.append(category.get_withdrawals())
    total_withdrawals = list(map(lambda x: round_down(x/total), withdrawals))
    
    # Generate chart title
    chart_title = "Percentage spent by category\n"

    # Generate upper chart
    # Loop over categories, if category == percentage, add o
    upper_chart = ""
    percentage = 100
    while percentage >= 0:
        category_bars = " "
        for total in total_withdrawals:
            if total * 100 >= percentage:
                category_bars += "o  "
            else:
                category_bars += "   "
        upper_chart += str(percentage).rjust(3) + "|" + category_bars + ("\n")
        percentage -= 10
        
    # Generate lines
    lines = "-" + "---"*len(categories)
    lines = lines.rjust(len(lines)+4) + "\n"

    # Generate category names
    names = []
    category_names = ""
    for category in categories:
        names.append(category.name)
    
    max_length = max(names, key=len)
    
    for x in range(len(max_length)):
        name_str = "     "
        for name in names:
            if x >= len(name):
                name_str += "   "
            else:
                name_str += name[x] + "  "

        if (x != len(max_length) -1):
            name_str += "\n"

        category_names += name_str

    # Put it all together
    chart = chart_title + upper_chart + lines + category_names
    return chart