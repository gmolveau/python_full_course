with open("data.txt") as f:
    first_line = f.readline()
    user_number = int(first_line)
    user_number_squared = user_number ** 2
    print(f"{user_number}^2 = {user_number_squared}")
    for i in range(1, user_number):
        if i % 2 == 0:
            print(f"{i/3:.2f}")