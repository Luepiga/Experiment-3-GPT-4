
def get_email_input():
    print("\n===== CUSTOMER EMAIL INPUT =====")

    name = input("Enter Customer Name: ")
    subject = input("Enter Email Subject: ")
    email = input("Enter Customer Email: ")

    print("\n===== ENTERED DETAILS =====")
    print("Customer Name:", name)
    print("Subject:", subject)
    print("Customer Email:", email)

    return name, subject, email
