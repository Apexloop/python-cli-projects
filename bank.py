accounts = {
    "account_1": {
        "name": "ali",
        "pin": "1234",
        "balance": 5000,
        "history": []
    },

    "account_2": {
        "name": "has",
        "pin": "2345",
        "balance": 4000,
        "history": []
    }

}

attempts = 0
current_account = None

while attempts < 3:
    user_acc = input("Enter user id: ")
    user_pin = input("Please enter your pin: ")
    if user_acc in accounts and accounts[user_acc]["pin"] == user_pin:
        current_account = user_acc
        print("Welcome")
        break
    else:
        attempts += 1
if current_account is None:
    print("Account locked due to  too many failed attempts")
