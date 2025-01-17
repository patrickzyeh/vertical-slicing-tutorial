import argparse

def main():
    # configure first cli arg to be the price of the item 
    parser = argparse.ArgumentParser()

    parser.add_argument("quantity", type=int, help="The quantity of the item") 
    parser.add_argument("price", type=float, help="The price of the item")
    parser.add_argument("province", default="ON", choices=["ON", "QC"], help="The pronvince in which the item was purchased")

    args = parser.parse_args()
    price = args.quantity * args.price

    # conditionals to apply tax according to the province code supplied

    if args.province== "ON":
        total = price * 1.13
    elif args.province == "QC":
        total = price * 1.14975


    print(f"The total price is {total: .2f}")

if __name__ == '__main__':
    main()