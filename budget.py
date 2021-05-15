import math

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __repr__(self):
        # Generate title
        # stars = '*'*((30 - len(self.name)) // 2)
        # title = f"{stars}{self.name}{stars}\n"

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

    def get_withdrawls(self):
        total= 0
        for item in self.ledger:
            if item["amount"] < 0:
                total += item["amount"]
        return total


def create_spend_chart(categories):
    # Get total withdrawn from each category
    # total_withdrawals = []
    # for category in categories:
    #     total = 0
    #     for entry in category.ledger:
    #         if int(entry["amount"]) < 0:
    #             total += int(entry["amount"])
    #         total_withdrawals.append(total)
    # # Get total_spend
    # total_spend = sum(total_withdrawals)
    # Calculate each category as rounded % of total_spend
    # percent_spends = []
    # for item in total_withdrawals:

    # Generate chart title
    chart_title = "Percentage spent by category\n"

    # Generate upper chart
    # Loop over categories, if category == %, add o
    upper_chart = ""
    percentage = 100
    totals = getTotals(categories)
    while percentage >= 0:
        category_bars = " "
        for total in totals:
            if total * 100 >= percentage:
                category_bars += "o  "
            else:
                category_bars += "   "
        upper_chart += str(percentage).rjust(3) + "|" + category_bars + "\n"
        percentage -= 10
        
                
    # Generate lines
    lines = "-" + "---"*len(categories)
    lines = lines.rjust(len(lines)+4) + "\n"

    # Generate category names
    names = []
    x_axis = ""
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

        x_axis += name_str


    chart = chart_title + upper_chart + lines + x_axis
    print(chart)
    return chart

def truncate(n):
    multiplier = 10
    return int(n + multiplier) / multiplier

def getTotals(categories):
    total = 0
    breakdown = []
    for category in categories:
        total += category.get_withdrawls()
        breakdown.append(category.get_withdrawls())
    rounded = list(map(lambda x: truncate(x/total), breakdown))
    return rounded