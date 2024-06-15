def main():
    total_due = 50
    amount_inserted = 0

    # Valid coin denominations
    valid_coins = [25, 10, 5]

    while amount_inserted < total_due:
        print(f"Amount due: {total_due - amount_inserted} cents")
        coin = int(input("Insert coin: "))

        if coin in valid_coins:
            amount_inserted += coin
        else:
            print("Invalid coin. Please insert 25, 10, or 5 cents.")

    change_owed = amount_inserted - total_due
    print(f"Change owed: {change_owed} cents")

if __name__ == "__main__":
    main()
