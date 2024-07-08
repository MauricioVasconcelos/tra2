# calculadora.py

def calc_desc(price, discount):
    if price > 100:
        return price - price * discount / 100
    else:
        return price - price * discount / 100

def main():
    price = float(input("Enter the price: "))
    discount = float(input("Enter the discount percentage: "))
    final_price = calc_desc(price, discount)
    print(f"Final price after discount is: {final_price}")

if __name__ == "__main__":
    main()
