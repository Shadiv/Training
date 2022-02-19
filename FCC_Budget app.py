class Category:

    def __init__(self, category_name):
        self.category_name = category_name
        self.ledger = []

    def __repr__(self):
        display_output = f'{self.category_name}'.center(30, '*')
        for i in self.ledger:
            if len(str([*i.values()][1])) > 23:
                a = str([*i.values()][1])[:23]
                number = round([*i.values()][0], 2)
                display_output += '\n' + a.ljust(23, ' ') + "{:.2f}".format(number).rjust(7, ' ')
            else:
                a = str([*i.values()][1])
                num = round([*i.values()][0], 2)
                display_output += '\n' + a.ljust(23, ' ') + "{:.2f}".format(num).rjust(7, ' ')
        balance = self.get_balance()
        display_output += f'\nTotal: {balance}'
        return display_output

    def deposit(self, amount, description=''):
        funds_in = {"amount": amount, "description": description}
        self.ledger.append(funds_in)

    def check_funds(self, amount):
        balance = self.get_balance()
        if amount > balance:
            return False
        else:
            return True

    def withdraw(self, amount, description=''):
        if not self.check_funds(amount):
            return False
        else:
            fund_out = {"amount": -amount, "description": description}
            self.ledger.append(fund_out)
            return True

    def get_balance(self):
        balance = 0
        for i in self.ledger:
            balance += [*i.values()][0]
        return balance

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False
        else:
            destination = category.category_name
            desc_out = f'Transfer to {destination}'
            self.withdraw(amount, desc_out)
            category.deposit(amount, f'Transfer from {self.category_name}')
            return True


def create_spend_chart(categories):
    names = [i.category_name for i in categories]

    def format_row_start(row_start):
        if len(row_start) < 4:
            row_start = ' ' + row_start
            if len(row_start) < 4:
                format_row_start(row_start)

    def get_spendings(category):
        spendings = 0
        for i in category.ledger:
            if i['amount'] < 0:
                spendings += i['amount']
        return spendings

    all_spendings = [get_spendings(category) for category in categories]
    shares = [round(i / sum(all_spendings), 2) for i in all_spendings]
    print(shares)
    rows_percentage = {1.0: '100|', 0.9: ' 90|', 0.8: ' 80|', 0.7: ' 70|', 0.6: ' 60|', 0.5: ' 50|', 0.4: ' 40|',
                       0.3: ' 30|', 0.2: ' 20|', 0.1: ' 10|', 0.0: '  0|'}
    categories_letters = [name for name in names]

    legend_deph = max([len(i) for i in categories_letters]) + 1
    rows = list(rows_percentage.values()) + ['    ' for i in range(legend_deph)]
    counter = 0
    bar_chart = ''
    for row in rows:
        if rows.index(row) == 11 and counter == 11:
            row += '---' * len(categories) + '-'
            counter += 1
        elif counter > 11:
            row_temp = ''
            for i in categories_letters:
                try:
                    row_temp += ' ' + i[counter - 12] + ' '
                except IndexError:
                    row_temp += '   '
            row += row_temp + ' '
            counter += 1
        else:
            row_temp2 = ''
            for s in shares:
                s2 = round(s, 1)
                if s < s2:
                    if rows_percentage[s2 - 0.1] == row:
                        row_temp2 += ' o '
                        continue
                if rows_percentage[s2] == row and s >= s2:
                    row_temp2 += ' o '
                else:
                    row_temp2 += '   '
            row += row_temp2 + ' '
            counter += 1
        bar_chart += row + '\n'
    row_lengh = 4 + len(names) * 3 + 3
    bcl = bar_chart.split('\n')
    bcl.pop(bcl.index(''))
    bcl = [i + '\n' for i in bcl if bcl.index(i) != len(bcl)]
    for row in bcl:
        ind_to_ch = [v for v in range(row_lengh - 7)]
        itc = ind_to_ch[::3]
        ind = [i + 5 for i in itc]
        if bcl.index(row) < 10:
            for i in ind:
                if row[i] == 'o':
                    temp_row_lst = [_ for _ in bcl[bcl.index(row) + 1]]
                    temp_row_lst[i] = 'o'
                    temp_row = ''.join(temp_row_lst)
                    bcl[bcl.index(row) + 1] = temp_row
    bar_chart = ''
    for row in bcl:
        if bcl.index(row) == len(bcl) - 1:
            row = row[:-1]
        bar_chart += row
    bar_chart = 'Percentage spent by category\n' + bar_chart
    return bar_chart


# food = Category("Food")
# food.deposit(1000, "initial deposit")
# food.withdraw(10.15, "groceries")
# food.withdraw(15.89, "restaurant and more food for dessert")
# print(food.get_balance())
# clothing = Category("Clothing")
# food.transfer(50, clothing)
# clothing.withdraw(25.55)
# clothing.withdraw(100)
# auto = Category("Auto")
# auto.deposit(1000, "initial deposit")
# auto.withdraw(15)
#
# print(food)
# print(clothing)

# print(create_spend_chart([food, clothing, auto]))

food = Category("Food")
entertainment = Category('Entertainment')
business = Category("Business")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
print(create_spend_chart([business, food, entertainment]))

expected = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
print(expected)
