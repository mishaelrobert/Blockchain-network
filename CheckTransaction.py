from Client import Client
from Transaction import Transaction



Tom = Client()
Mishael = Client()

tx1 = Transaction(
    Tom,
    Mishael.identity,
    5.0
    )
signature = tx1.sign_transaction()
print(signature)
