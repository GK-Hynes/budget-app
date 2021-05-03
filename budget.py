class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __repr__(self):
	    pass

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        vals = [i["amount"] for i in self.ledger]
        balance = sum(vals)
        return balance

    def transfer(self, amount, other_category):
        pass
    
    def check_funds(self, amount):
        balance = self.get_balance()
        if amount > balance:
            return False
        return True



def create_spend_chart(categories):
    pass