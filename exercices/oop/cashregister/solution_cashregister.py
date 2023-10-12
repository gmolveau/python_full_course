class CashRegister:
    def __init__(self):
        self.drawer = [500, 200, 100, 50, 20, 10, 5, 2, 1]

    def make_change(self, owed, tendered):
        difference = tendered - owed
        change = []
        i = 0
        denomination = self.drawer[i]
        while difference > 0:
            if difference < denomination:
                i += 1
                denomination = self.drawer[i]
                continue
            change.append(denomination)
            difference -= denomination
        return change


# le client donne 50€ pour régler 24€ de courses
cash = CashRegister()
change = cash.make_change(24, 50)
print(change)
