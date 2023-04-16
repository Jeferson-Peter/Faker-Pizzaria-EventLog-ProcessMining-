# Fake Pizzaria Event Log Generator
This Python code generates a fake event log for a pizza restaurant. The event log consists of 1000 orders that contain information about when the order was received, processed, the pizza preparation and delivery times, the users who attended and delivered the orders, the type and size of the pizzas ordered, the quantity of pizzas, the unit price and the total amount paid for each order.

## The code uses the following libraries:
* pandas
* numpy
* faker
* openpyxl

## Installation
To run the code, you need to have Python (recommended 3.11) installed on your computer, as well as the following libraries:

* pandas
* numpy
* faker
* openpyxl

You can install these libraries using pip by running the following command:

```shell
pip install pandas numpy faker

# OR

pip install -r requirements.txt

```
## How to Run
To generate the fake event log, simply run the Python code `fake_pizzaria_event_log.py`. The code will generate an Excel file called `fake_pizzaria_eventlog.xlsx` in the same directory where the code is located.

## Customization
You can customize some parameters in the code to generate a different event log:

* **attendant_users**: A list of attendant users to be used in the orders. By default, the code generates a list of 10 random names using the `faker` library.
* **delivery_users**: A list of delivery users to be used in the orders. By default, the code generates a list of 10 random names using the `faker` library, excluding the names in the `attendant_users` list.
* **PIZZA_TYPES**: A tuple of pizza types to be used in the orders. By default, the code uses 15 different types of pizza.
* **PIZZA_SIZE**: A tuple of pizza sizes to be used in the orders. By default, the code uses 4 different sizes of pizza.
* **start_timestamp**: The starting timestamp to be used in the orders. By default, the code uses `April 10th, 2023 at 00:00:00`.
* **end_timestamp**: The ending timestamp to be used in the orders. By default, the code uses `April 16th, 2023 at 00:00:00`.
* **num_orders**: The number of orders to be generated. By default, the code generates 1000 orders.
* **pizza_prices**: A dictionary that maps each pizza type to its unit price. By default, the code generates a random price between 20 and 70 for each pizza type.
* **pizza_size_prices**: A dictionary that maps each pizza size to its price. By default, the code uses a fixed price for each size of pizza.
* **time_to_delivery_dispatch**: A function that calculates the time between pizza preparation and delivery dispatch based on pizza size and quantity. By default, the code uses a function that returns a random time based on the pizza size and quantity.
* **random_timestamp**: A function that generates a random timestamp within a given range. By default, the code uses the `np.random.randint()` and `pd.to_datetime()` functions to generate a random timestamp.
* **random_pizza_type**: A function that generates a random pizza type. By default, the code uses the `np.random.choice()` function to select a random pizza type from the `PIZZA_TYPES` tuple.
* **random_pizza_size**: A function that generates a random pizza size. By default, the code uses the `np.random.choice()` function to select a random pizza size from the `PIZZA_SIZE` tuple.
* **random_delivery_user**: A function that generates a random delivery user. By default, the code uses the `np.random.choice()` function to select a random name from the