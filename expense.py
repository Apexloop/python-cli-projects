expenses = []


def myexpense_tracker():

    expense_name = (input("enter the expense :"))
    expense_type = (input("enter the expense type :")).lower()
    expense_amount = int(input("enter the amount : "))
    expense = {
        "name": expense_name,
        "type": expense_type,
        "amount": expense_amount}
    expenses.append(expense)


choice = input("do you want to add anoterr expense ?")
while choice == "yes":
    myexpense_tracker()

else:
    print("Thankyou for using")
