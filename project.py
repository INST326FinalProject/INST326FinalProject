import datetime

class Expense:
    """Class to represent an expense
    """
    def __init__(self, amount, category, description):
        """Initialize an expense object
        
        Args:
            amount (float): the amount of the expense
            category (str): the category of the expense
            description (str): description of the expense
        """
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.datetime.now()