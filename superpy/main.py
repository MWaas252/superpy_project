#imports
import argparse
import csv
import os
from datetime import date, datetime

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.


# Load CSV function
def load_csv(filename):
    data = []
    with open(filename, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

# Get current day function
def get_current_day():
    try:
        with open('current_day.txt', 'r') as file:
            return int(file.read())
    except FileNotFoundError:
        return 1

# Set current day function
def set_current_day(day):
    with open('current_day.txt', 'w') as file:
        file.write(str(day))

# Action functions
def perform_products_action(args, bought_data):
    products = set(entry['product_name'] for entry in bought_data)
    print("Products offered by the supermarket:")
    if args.product_list:
        selected_products = set(args.product_list)
        products = products.intersection(selected_products)
    for product in products:
        print(product)

def perform_count_action(bought_data):
    product_counts = {}
    for entry in bought_data:
        product_name = entry['product_name']
        product_counts[product_name] = product_counts.get(product_name, 0) + 1

    print("Current product counts:")
    for product, count in product_counts.items():
        print(f"{product}: {count}")

def perform_details_action(bought_data):
    product_details = {}
    for entry in bought_data:
        product_name = entry['product_name']
        if product_name not in product_details:
            product_details[product_name] = {'purchase_price': entry['purchase_price'], 'expiry_date': entry['expiry_date']}
    
    print("Product details:")
    for product, details in product_details.items():
        print(f"Product: {product}")
        print(f"Purchase Price: {details['purchase_price']}")
        print(f"Expiry Date: {details['expiry_date']}")

def perform_sold_action(sold_data, current_date, product_to_check, date_to_check):
    sold_info = {}
    for entry in sold_data:
        product_name = entry['product_name']
        if product_name not in sold_info:
            sold_info[product_name] = {'sale_price': entry['sale_price'], 'expired': False}

        if entry['expiry_date']:
            expiry_date = datetime.strptime(entry['expiry_date'], '%Y-%m-%d').date() 
    
            if expiry_date < date_to_check:
                sold_info[product_name]['expired'] = True

    print("Product sale info:")
    for product, info in sold_info.items():
        print(f"Product: {product}")
        print(f"Sale Price: {info['sale_price']}")
        if info['expired']:
            print("Status: Expired")
        else:
            print("Status: Not Expired")

def main():
    parser = argparse.ArgumentParser(description="Superpy - Inventory Tracking Tool")
    subparsers = parser.add_subparsers(dest='subcommand', help='Subcommands')

    parser_action = subparsers.add_parser('action', help='Perform actions') 
    parser_action.add_argument('action', choices=['products', 'count', 'details', 'sold'], help='Action to perform')
    parser_action.add_argument('--product_list', nargs='+', help='List of product names to filter')
    parser_action.add_argument('--product', help='Product name to filter')
    parser_action.add_argument('--date', help='Date to check product status (YYYY-MM-DD)')

    parser_advance = subparsers.add_parser('advance-time', help='Advance time by specified number of days')
    parser_advance.add_argument('days', type=int, help='Number of days to advance')

    args = parser.parse_args()

    script_directory = os.path.dirname(os.path.abspath(__file__))
    bought_csv_path = os.path.join(script_directory, 'boughtcsv.csv')
    sold_csv_path = os.path.join(script_directory, 'soldcsv.csv')

    bought_data = load_csv(bought_csv_path)
    sold_data = load_csv(sold_csv_path)

    if args.subcommand == 'action':
        current_day = get_current_day()

        if args.action == 'products':
            perform_products_action(args, bought_data)
        elif args.action == 'count':
            perform_count_action(bought_data)
        elif args.action == 'details':
            perform_details_action(bought_data)
        elif args.action == 'sold':
            if args.product and args.date:
                product_to_check = args.product
                date_to_check = datetime.strptime(args.date, '%Y-%m-%d').date()
                perform_sold_action(sold_data, current_day, product_to_check, date_to_check)

    elif args.subcommand == 'advance-time':
        current_day = get_current_day()
        set_current_day(current_day + args.days)
        print(f"Advancing time by {args.days} day(s)...")

if __name__ == "__main__":
    main() 