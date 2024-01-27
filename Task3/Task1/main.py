def get_positive_integer_input(prompt):
    # This function prompts the user to input a positive integer and
    # keeps asking until a valid input is provided.
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a positive integer!")
        except ValueError:
            print("Please enter a number!")

def get_yes_no_input(prompt):
    # This function prompts the user to input 'Y' or 'N' and keeps
    # asking until a valid input is provided.
    while True:
        answer = input(prompt).strip().lower()
        if answer == 'y' or answer == 'n':
            return answer
        else:
            print('Please answer "Y" or "N".')

def calculate_total_price(num_pizzas, is_delivery, is_tuesday, used_app):
    # This function calculates the total price of pizzas based on various factors
    # such as the number of pizzas, delivery option, Tuesday discount, and app usage.

    # Constants for pizza price, delivery cost, and discount percentages.
    pizza_price = 12
    delivery_cost = 2.5
    discount_percentage = 0.25
    tuesday_discount_percentage = 0.5

    # Calculate the total price of pizzas without any discounts or delivery cost.
    total_pizza_price = num_pizzas * pizza_price

    # Apply Tuesday discount if it's Tuesday.
    if is_tuesday:
        total_pizza_price *= (1 - tuesday_discount_percentage)

    # Apply delivery cost if delivery is required, and adjust for free delivery if applicable.
    if is_delivery:
        if num_pizzas >= 5:
            delivery_cost = 0
        total_pizza_price += delivery_cost

    # Apply app discount if the customer used the app.
    if used_app:
        total_pizza_price *= (1 - discount_percentage)

    # Round the total price to two decimal places.
    return round(total_pizza_price, 2)

def main():
    # The main function where the program execution begins.

    # Display header.
    print("BPP Pizza Price Calculator")
    print("==========================")

    # Get user input for the number of pizzas.
    num_pizzas = get_positive_integer_input("How many pizzas ordered? ")

    # Get user input for delivery option.
    is_delivery = get_yes_no_input("Is delivery required? (Y/N) ")
    is_delivery = is_delivery == 'y'

    # Get user input for whether it's Tuesday.
    is_tuesday = get_yes_no_input("Is it Tuesday? (Y/N) ")
    is_tuesday = is_tuesday == 'y'

    # Get user input for app usage.
    used_app = get_yes_no_input("Did the customer use the app? (Y/N) ")
    used_app = used_app == 'y'

    # Calculate and display the total price.
    total_price = calculate_total_price(num_pizzas, is_delivery, is_tuesday, used_app)
    print(f"\nTotal Price: £{total_price:.2f}.")

# Execute the main function if this script is run as the main program.
if __name__ == "__main__":
    main()
