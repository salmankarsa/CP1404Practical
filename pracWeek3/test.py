def main():
    password = input("Enter your password(your password must be at least 8 characters):")
    countPassword = len(password)

    while countPassword < 8:
        print("Invalid Password")
        password = input("Enter your password(your password must be at least 8 characters):")
        countPassword = len(password)


    else:
        for i in range(countPassword):
            print("*", end = '')


main()