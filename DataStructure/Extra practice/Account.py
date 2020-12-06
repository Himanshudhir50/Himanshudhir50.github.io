"""
Practice dunder Methods First Link in Week 1
"""


class Account:
    """ A simple account class """

    def __init__(self, owner, amount=0):
        """ Need owner name for an account"""
        self.owner = owner
        self.amount = amount
        """ We have empty list to store a transaction in the account and we make 
        transaction a dunder value because transaction is immutable """
        self._transaction = []

    def __str__(self):
        return 'Account of {} with starting amount{}'.format(self.owner, self.amount)

    def __repr__(self):
        return 'Account of{} with starting{}'.format(self.owner, self.amount)

    def add_transaction(self, amount):
        """
        isinstance is use to check is the amount is int or not. if it is not then raise error
        """
        if not isinstance(amount, int):
            raise ValueError('please use int for amount')
        self._transaction.append(amount)

    @property
    def balance(self):
        """
        Sum is use to add all the transactions but if wee have float points then
        we need to use math.fsum instead of sum
        """
        return self.amount + sum(self._transaction)

    def __len__(self):
        return len(self._transaction)

    """ getitem is used to get a index value """

    def __getitem__(self, position):
        return self._transaction[position]

    def __reversed__(self):
        return self[::-1]

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __add__(self, other):
        change_owner = '{}&{}'.format(self.owner, other.owner)
        start_amount = self.amount + other.amount
        return Account(change_owner, start_amount)

    def _call_(self):
        print(f'Start amount: {self.amount}')
        print('Transactions: ')
        for transaction in self:
            print('/balance:{}'.format(self.balance))


if __name__ == '__main__':
    x = Account('Himanshu', 10)
    print(x)
