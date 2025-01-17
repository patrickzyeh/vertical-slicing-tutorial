import argparse

def main():
    #configure first cli arg to be the price of the item 
    parser = argparse.ArgumentParser()
    parser.add_argument("quantity", type=int, help="The quantity of the item")
    parser.add_argument("price", type=float, help="The price of the item")
    args = parser.parse_args()
    price = args.quantity * args.price

    # add tax to the price
    total = price * 1.13 # Since in Ontario

    print(f"The total price is {total: .2f}")


if __name__ == '__main__':
    main()