'''Create a python program to secure an existing password by replacing a set of characters with the corresponding 'password-secure' character (Provided as tuple).
Example:
    SECURE = (('s', '$'), ('and', '&'),
            ('a', '@'), ('o', '0'), ('i', '1'),
            ('I', '|'))

    Input:
    password = "Indians123"

    Output:
    Your secure password is |nd1@n$123

'''


SECURE = (('R', '$'), ('j', '&'),
            ('a', '@'), ('n', '0'), ('ee', '1'),
            ('t', '|'),('1','h'),('6','^^'),('4','!'),('0',')'))

def securePassword(password):
    for a,b in SECURE:
        password = password.replace(a, b)
    return password

if __name__ == "__main__":
    password = input("Enter your password\n")
    password = securePassword(password)
    print(f"Your secure password is {password}")