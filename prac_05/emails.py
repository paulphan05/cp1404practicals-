def main():
    """Create dictionary of emails-to-name."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ")
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Extract expected name from email address."""
    username_part = email.split('@')[0]
    name_parts = username_part.split('.')
    for i in range(len(name_parts)):
        name_parts[i] = name_parts[i].title()
    name = " ".join(name_parts)
    return name


main()
