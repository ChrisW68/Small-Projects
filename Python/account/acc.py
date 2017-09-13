class Account:

    def __init__(self, filepath):
        self.filepath=filepath
        with open(filepath, 'r') as file:
            self.balance=int(file.read())

    def withdraw(self, amount):
        self.balance=self.balance - amount

    def deposit(self, amount):
        self.balance=self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class Checking(Account):
    #Constructor of a class
    def _init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee=fee

    #Class method
    def transfer(self,amount):
        self.balance=self.balance - amount - self.fee

#Instantiation of the Class
checking=Checking("balance.txt", 1)
checking.transfer(105)
print(checking.balance)
checking.commit()