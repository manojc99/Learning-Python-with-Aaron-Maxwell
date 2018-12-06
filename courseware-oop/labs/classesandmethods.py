'''

Let's create a class to manage invoices. Its constructor will take
an invoice number, the customer name, and the amount of money owed.

>>> invoice = Invoice(12, 'Mark Smith', 42.50)

The built-in type() function gives you the class of an object:
>>> type(invoice)
<class '__main__.Invoice'>

This object has some member variables:
>>> invoice.number
12
>>> invoice.customer
'Mark Smith'
>>> invoice.amount
42.5

We want to keep track too of the total payments made. At first, this
will be zero.

>>> invoice.total_payments
0

Now, the customer may make payments in stages (rather than paying all
at once).  So let's create methods to add payments, check whether the
invoice is fully paid off, etc.

>>> invoice.add_payment(20)
>>> invoice.is_fully_paid()
False
>>> invoice.total_payments
20
>>> invoice.amount_due()
22.5

>>> invoice.add_payment(22.50)
>>> invoice.is_fully_paid()
True
>>> invoice.amount_due()
0.0

'''

# Write your code here:


class Invoice(object):
    """docstring fo Invoice."""
    total_payments = 0

    def __init__(self, number, customer, amount):

        super(Invoice, self).__init__()
        self.number = number
        self.customer = customer
        self.amount = amount
        self.total_payments = 0

    def add_payment(self, paymment):
        self.total_payments += paymment

    def is_fully_paid(self):
        is_paid = False
        if self.total_payments >= self.amount:
            is_paid = True
        return is_paid

    def amount_due(self):
        return self.amount - self.total_payments
# Do not edit any code below this line!


if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Copyright 2015-2018 Aaron Maxwell. All rights reserved.