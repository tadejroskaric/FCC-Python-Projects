class Category:
    # Creating an empty ledger with balance 0
    def __init__(self, category):
        self.ledger = []
        self.balance = 0
        self.name = category

    # String representation
    def __str__(self):
        total = 0
        title_line = self.name.center(30, "*") + "\n"
        lines = ""
        for item in self.ledger:
            # Calculate total amount
            total += item['amount']
            # Formatting the numbers
            item['amount'] = "{:.2f}".format(item['amount'])
            # Formatting the output
            line = f"{item['description'][:23]}" +\
                   f"{str((item['amount']))[:7].rjust(30-len(item['description'][:23]))}"
            # Create last line and break loop on last item
            if item == self.ledger[-1]:
                lines += line
                break
            lines += line + "\n"

        return title_line + lines + "\n" f"Total: {total}"

    # Depositing money to ledger
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    # Withdrawing money from ledger
    def withdraw(self, amount, description=""):
        # Checking if we have enough funds
        if self.check_funds(amount):
            self.ledger.append({"amount": -1 * amount, "description": description})
            self.balance -= amount
            return True
        else:
            return False

    # Get current balance
    def get_balance(self):
        return self.balance

    # Transfer funds to another category
    def transfer(self, amount, category2):
        # Check if enough funds
        if self.check_funds(amount):
            self.withdraw(amount, description=f"Transfer to {category2.name}")
            category2.deposit(amount, description=f"Transfer from {self.name}")
            return True
        else:
            return False

    # Check if we have enough funds to make transaction
    def check_funds(self, amount):
        # Is given amount bigger than the current balance?
        if amount > self.balance:
            return False
        else:
            return True


def create_spend_chart(categories):
    title = "Percentage spent by category\n"
    total = 0
    percentages = []

    # Calculating total spending for all categories and all items
    for category in categories:
        for item in category.ledger:
            if float(item['amount']) < 0:
                total += (-1 * float(item['amount']))

    # Calculating the percentages
    for category in categories:
        # Resetting spent for each category
        spent = 0
        for item in category.ledger:
            # Calculating spent for each category
            if float(item['amount']) < 0:
                spent += (-1 * float(item['amount']))
                # Retrieving the percentage based on spent within category and total
                if item == category.ledger[-1]:
                    percentage = round((spent/total)*100, 2)
                    percentages.append(percentage)

    # Setting up the y axis
    y_axis = ""
    for y_label in range(100, -1, -10):
        y_label = str(y_label)
        y_axis += y_label.rjust(3) + "|"
        y_label = int(y_label)
        # Add "o" based on percentage
        for percentage in percentages:
            if percentage >= y_label:
                if percentage == percentages[-1]:
                    y_axis += " o  "
                else:
                    y_axis += " o "
            # Add empty spaces above "o"
            else:
                if percentage == percentages[-1]:
                    y_axis += "    "
                else:
                    y_axis += "   "
        # Add new lines until y axis is 0
        if y_label != 0:
            y_axis += "\n"

    # Setting up x axis
    x_axis = "    " + "-" * 3 * len(categories) + "-"
    categories_list = []
    x_label_list = []
    x = ""

    # Create a list of categories and get longest string value
    for category in categories:
        categories_list.append(category.name)
    longest = max(categories_list, key=len)

    # Add height of x labels
    for height in range(len(longest)):
        x_label = "    "
        # Add width of x labels
        for width in range(len(categories_list)):
            # Write all characters in a column form
            if len(categories_list[width]) > height:
                x_label += " " + categories_list[width][height] + " "
            else:
                x_label += "   "
        # Adds additional space in last column
        x_label += " "

        # Inserts additional space next to last character of longest label
        if height+1 == len(longest):
            x_label += " "

        # List of x labels
        x_label_list.append(x_label + "\n")

    # Remove empty row on the bottom
    x_label_list[-1] = x_label_list[-1][:-2]

    # Creating rows
    for row in x_label_list:
        x += row

    return title + y_axis + "\n" + x_axis + "\n" + x
