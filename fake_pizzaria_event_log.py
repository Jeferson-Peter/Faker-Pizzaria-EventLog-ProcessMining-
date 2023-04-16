import pandas as pd
import numpy as np
from faker import Faker


faker = Faker()
attendant_users = [faker.name() for i in range(10)]
delivery_users = [faker.name() for i in range(10) if i not in attendant_users]
PIZZA_TYPES = (
'Margherita', 'Pepperoni', 'Hawaiian', 'Meat Lovers', 'Veggie', 'Cheese', 'BBQ Chicken', 'Buffalo Chicken',
'Pesto', 'Mushroom', 'Onion', 'Garlic Chicken', 'Spinach', 'Artichoke', 'Sausage')
PIZZA_SIZE = ('Small', 'Medium', 'Large', 'Extra Large')

pizza_prices = {pizza_type: round(np.random.uniform(20, 70.0), 2) for pizza_type in PIZZA_TYPES}
pizza_size_prices = {'Small': 5.0, 'Medium': 10.0,
                     'Large': 15.0, 'Extra Large': 20.0}

start_timestamp = pd.Timestamp('2023-04-10 00:00:00')
end_timestamp = pd.Timestamp('2023-04-16 00:00:00')

ev_order_received = []
ev_order_processed = []
ev_pizza_preparation = []
ev_delivery_dispatched = []
ev_pizza_delivered = []
ev_payment_received = []
pizza_type = []
pizza_size = []
qtd_pizza = []
attendant_user = []
delivery_user = []
total_pizza_amount = []
pizza_unit_price = []


# Define a function to calculate the time between pizza preparation and delivery dispatch based on pizza size and quantity
def time_to_delivery_dispatch(size, qtd):
    if size == 'Small':
        if qtd <= 2:
            return np.random.randint(20, 31)
        elif qtd <= 4:
            return np.random.randint(30, 41)
        else:
            return np.random.randint(40, 51)
    elif size == 'Medium':
        if qtd <= 2:
            return np.random.randint(30, 41)
        elif qtd <= 4:
            return np.random.randint(40, 51)
        else:
            return np.random.randint(50, 61)
    elif size == 'Large':
        if qtd <= 2:
            return np.random.randint(40, 51)
        elif qtd <= 4:
            return np.random.randint(50, 61)
        else:
            return np.random.randint(60, 71)
    elif size == 'Extra Large':
        if qtd <= 2:
            return np.random.randint(50, 61)
        elif qtd <= 4:
            return np.random.randint(60, 71)
        else:
            return np.random.randint(70, 81)


# Define a function to generate random timestamps within a given range
def random_timestamp(start, end):
    return pd.to_datetime(np.random.randint(start, end), unit='s')


# Define a function to generate random pizza types
def random_pizza_type():
    return np.random.choice(PIZZA_TYPES)


# Define a function to generate random pizza sizes
def random_pizza_size():
    return np.random.choice(PIZZA_SIZE)


# Define a function to generate random delivery user
def random_delivery_user():
    return np.random.choice(delivery_users)


# Define a function to generate random attendant user
def random_attendant_user():
    return np.random.choice(attendant_users)

if __name__ == '__main__':
    num_orders = 1000
    order_ids = np.random.choice(range(100000, 1000000), size=num_orders, replace=False)
    for order_id in order_ids:
        # Generate random timestamp for order received
        order_received = random_timestamp(start_timestamp.timestamp(), end_timestamp.timestamp())
        ev_order_received.append(order_received)

        # Calculate timestamp for order processed (1 minute after order received)
        order_processed = order_received + pd.Timedelta(minutes=1)
        ev_order_processed.append(order_processed)

        # Generate random user
        attendant_user.append(random_attendant_user())
        delivery_user.append(random_delivery_user())

        # Generate random pizza type, size, and quantity
        pizza_type_ = random_pizza_type()
        pizza_size_ = random_pizza_size()
        qtd_ = np.random.randint(1, 4)
        pizza_type.append(pizza_type_)
        pizza_size.append(pizza_size_)
        qtd_pizza.append(qtd_)
        pizza_unit_price.append(pizza_prices[pizza_type_])
        total_pizza_amount.append((qtd_ * pizza_prices[pizza_type_])
                                  + (qtd_ * pizza_size_prices[pizza_size_]))

        # Calculate timestamp for pizza preparation (5 to 8 minutes after order processed)
        pizza_preparation = order_processed + pd.Timedelta(minutes=np.random.randint(5, 8))
        ev_pizza_preparation.append(pizza_preparation)

        # Randomly select some orders that will not follow the expected sequence
        if np.random.rand() < 0.1:  # 10% of orders will have failures
            # Set delivery dispatch time as None
            ev_delivery_dispatched.append(pd.NaT)
            # Set pizza delivered and payment received times as None
            ev_pizza_delivered.append(pd.NaT)
            ev_payment_received.append(pd.NaT)
        else:
            # Calculate timestamp for delivery dispatched (time depends on pizza size and quantity)
            delivery_dispatched = pizza_preparation + pd.Timedelta(minutes=time_to_delivery_dispatch(pizza_size_, qtd_))
            ev_delivery_dispatched.append(delivery_dispatched)

            # Calculate timestamp for pizza delivered (20 to 30 minutes after delivery dispatched)
            pizza_delivered = delivery_dispatched + pd.Timedelta(minutes=np.random.randint(20, 31))
            ev_pizza_delivered.append(pizza_delivered)

            # Calculate timestamp for payment received (30 seconds to 1 minute after pizza delivered)
            payment_received = pizza_delivered + pd.Timedelta(seconds=np.random.randint(30, 61))
            ev_payment_received.append(payment_received)

    # Create a dictionary from the lists of values
    data = {
        'order_id': order_ids,
        'ev_order_received': ev_order_received,
        'ev_order_processed': ev_order_processed,
        'ev_pizza_preparation': ev_pizza_preparation,
        'ev_delivery_dispatched': ev_delivery_dispatched,
        'ev_pizza_delivered': ev_pizza_delivered,
        'ev_payment_received': ev_payment_received,
        'pizza_type': pizza_type,
        'pizza_size': pizza_size,
        'qtd_pizza': qtd_pizza,
        'delivery_user': delivery_user,
        'attendant_user': attendant_user,
        'unit_price': pizza_unit_price,
        'total_amount': total_pizza_amount,
    }

    df = pd.DataFrame(data)
    df.loc[df['ev_pizza_delivered'].isna(), 'delivery_user'] = pd.NA
    df.to_excel('fake_pizzaria_eventlog.xlsx', index=False)
