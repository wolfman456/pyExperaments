running = True


def get_amount():
    amount = float(input("Pleas input the check amount : \n"))
    return amount


def get_tip_percent():
    return float(input("Pleas input the tip percentage : \n"))


def calculate_new_amount(amount, tip_percent):
    return round(amount + amount * (tip_percent / 100), 2)


def another_amount():
    global running
    answer = input("Would you like to calculate another amount? (yes or no) : \n")
    if answer == "yes" or answer == "y":
        main()
    else:
        running = False


def main():
    while running:
        amount = get_amount()
        tip = get_tip_percent()
        split = int(input("Pleas input the number of people splitting the check : \n"))
        new_amount = calculate_new_amount(amount, tip)
        if split == 1 or 0:
            print(f"Your total including tip is ${new_amount}")
        else:
            amount_split = round(float(new_amount / split, ), 2)
            print(f"The total amount with tip is {new_amount}, with \n"
                  f"the check being split {split}, ways \n"
                  f"each person ows {amount_split}")
        another_amount()


if __name__ == '__main__':
    main()
