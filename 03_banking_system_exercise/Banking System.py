# Classes
class User:
    def __init__(self, first_name, last_name, gender, street_address, city,
                 email, cc_number, cc_type, balance, account_no):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.street_address = street_address
        self.city = city
        self.email = email
        self.cc_number = cc_number
        self.cc_type = cc_type
        self.balance = balance
        self.account_no = account_no
        user_list.append(self)

    def display_info(self):
        # TO COMPLETE
        print("--------------------------------------------------------------")
        print(f"Name: {self. first_name} {self.last_name}")
        print(f"Gender: {self.gender}")
        print(f"Address: {self.street_address}, {self.city}")
        print(f"Email: {self.email}")
        print(f"CC number: {self.cc_number}")
        print(f"CC type: {self.cc_type}")
        print(f"Balance: {self.balance}")
        print(f"Account number: {self.account_no}")


# Functions
def generate_users():
    import csv
    with open('bankUsers.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',', quotechar="'")
        for line in filereader:
            User(line[0], line[1], line[2], line[3], line[4], line[5], line[6],
                 line[7], float(line[8][1:]), line[9])


def find_user():
    # TO COMPLETE
    user_to_find = input("Enter user's first and lastname: ").title()
    for user in user_list:
        user_name = f"{user.first_name} {user.last_name}"
        if user_to_find == user_name:
            user.display_info()
            return
    print("Sorry, no user was found with that name")


def overdrafts():
    # TO COMPLETE
    overdraft_users = []
    total_amount = []

    for user in user_list:
        if user.balance < 0:
            overdraft_users.append(user)
            total_amount.append(user.balance)
            user.display_info()
    print(f"\nTotal number of users with overdraft accounts: "
          f"{len(overdraft_users)}")
    print(f"Total amount overdraft: {sum(total_amount)}")


def missing_emails():
    # TO COMPLETE
    users_missing_emails = []
    for user in user_list:
        if not user.email:
            users_missing_emails.append(user)
            user.display_info()
    print(f"\nTotal amount of users with no email: "
          f"{len(users_missing_emails)}")


def bank_details():
    # TO COMPLETE
    total_balance = []
    for user in user_list:
        total_balance.append(user.balance)
    user_list.sort(key=lambda user: user.balance)
    top_user = user_list[-1]
    last_user = user_list[0]
    print(f"Total users: {len(user_list)}")
    print(f"Bank worth total: {sum(total_balance)}")
    print("\nUser with highest balance:")
    print(top_user.display_info())
    print("\nUser with lowest balance:")
    print(last_user.display_info())


def transfer():
    user1 = ""
    user2 = ""
    action = True

    while True:
        account1 = input("Enter account number: ")
        for user in user_list:
            if account1 == user.account_no:
                print(f"{user.account_no} - {user.first_name} {user.last_name}"
                      f"\nBalance: ${user.balance}")
                user1 = user
                action = False
                break
        if not action:
            break
        else:
            print("There is no user with that account number")

    while True:
        try:
            transfer_amount = int(input("\nHow much money do you want to "
                                        "transfer: $"))
            break
        except ValueError:
            print("Please enter a valid amount")
    while True:
        account2 = input("\nEnter account number to transfer money into: ")
        for user in user_list:
            if account2 == user.account_no:
                print(f"{user.account_no} - {user.first_name} {user.last_name}"
                      f"\nBalance: ${user.balance}")
                user2 = user
                action = False
                break
        if not action:
            break
        else:
            print("There is no user with that account number")

    while True:
        confirm = input("\nConfirm transfer (Y or N): ").upper()
        if confirm == "Y":
            user1.balance -= transfer_amount
            user2.balance += transfer_amount
            print("Transaction complete")
            print(f"{user1.first_name} {user1.last_name} balance: "
                  f"${user1.balance}")
            print(f"{user2.first_name} {user2.last_name} balance: "
                  f"${user2.balance}")
            return
        elif confirm == "N":
            print("Transaction cancelled")
            return
        else:
            print("Please enter 'Y' or 'N'")


# Main routine
user_list = []
generate_users()

userChoice = ""
print("Welcome")

while userChoice != "Q":
    print("What function would you like to run?")
    print("Type 1 to find a user")
    print("Type 2 to print overdraft information")
    print("Type 3 to print users with missing emails")
    print("Type 4 to print bank details")
    print("Type 5 to transfer money")
    print("Type Q to quit")
    userChoice = input("Enter choice: ").upper()
    print()

    if userChoice == "1":
        find_user()
    elif userChoice == "2":
        overdrafts()
    elif userChoice == "3":
        missing_emails()
    elif userChoice == "4":
        bank_details()
    elif userChoice == "5":
        transfer()
    print()
