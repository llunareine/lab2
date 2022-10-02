# class Money:
#
#     def __init__(self, number, currency, amount):
#         self.number = number
#         self.currency = currency
#         self.amount = amount
#         self.currencies = {
#             "USD": 476,
#             "RUB": 7.91,
#             "EUR": 464.81
#         }
#
#     def to_tenge(self):
#         return self.currencies[self.currency] * (self.number * self.amount)
#
#     def __str__(self):
#         return f"{self.number * self.amount} {self.currency}"
#
#
# class Wallet():
#     def __init__(self):
#         self.money = [
#             Money(10, "USD", 5),
#             Money(100, "RUB", 2),
#             Money(50, "EUR", 1),
#         ]
#
#     def get(self, index):
#         return self.money[index]
#
#     def add(self, money):
#         self.money.append(money)
#         return  self.money
#
#     def size(self):
#         return len(self.money)
#
#     def sort(self):
#         self.money.sort(key=lambda x: x.amount * x.number, reverse=True)
#         return ','.join(str(x) for x in self.money)
#
#     def total_balance_in_tenge(self):
#         sum = 0
#         for i in self.money:
#             sum = sum + i.to_tenge()
#         return sum
#
#     def __str__(self):
#         return ','.join(str(x) for x in self.money)
#
# balance = 0
#
# def deposit(amount):
#     global balance
#     balance += amount
#     return balance
#
# def withdraw(amount):
#     global balance
#     balance -= amount
#     return balance
# print("Balance before: ", balance)
# print("Deposit 1000: ", deposit(1000))
# print("After Withdraw 200: ", withdraw(200))
#
# wallet = Wallet()
# wallet.add(Money(10, "USD", 5))
# print(wallet.__str__())
# wallet.add(Money(100, "EUR", 1000))
# print(wallet.__str__())
# print("Get last money: ", wallet.get(-1))
# print("Sorted: ", wallet.sort())
# print("Total balance in tenge: ", wallet.total_balance_in_tenge())


class bankAccount:
    def __init__(amount):
        amount.b = 0
    def deposit(amount):
        a = int(input("Enter the sum you want to withdraw: "))
        amount.b = amount.b + a
    def withdraw(amount):
        a = int(input("How much money do you want to withdraw? "))
        if amount.b >= a:
            amount.b = amount.b - a
            print("Funds withdrawn successfully!" )
            print("Balance on balance", amount.b, "$")
        else:
            print("You don't have enough funds to withdraw")
            print("On account", amount.b, "$")
bank = bankAccount()
bank.deposit()
bank.withdraw()

