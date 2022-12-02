import pandas as pd

# order_id,date,time
orders = pd.read_csv('./data/orders.csv', sep=',', encoding='latin-1')

# order_details_id,order_id,pizza_id,quantity
order_details = pd.read_csv('./data/order_details.csv', sep=',', encoding='latin-1')

# pizza_type_id,name,category,ingredients
pizza_types = pd.read_csv('./data/pizza_types.csv', sep=',', encoding='latin-1')

# pizza_id,pizza_type_id,size,price
pizza_price = pd.read_csv('./data/pizzas.csv', sep=',', encoding='latin-1')

dict_pizzas = pd.read_csv('./data/data_dictionary.csv', sep=',', encoding='latin-1')
print('INFORME DE TOPOLOGÍA DE DATOS')
# tipo de dato de cada columna
print('orders')
for columna in orders.columns:
    print(columna, orders[columna].dtype)
print('order_details')
for columna in order_details.columns:
    print(columna, order_details[columna].dtype)
print('pizza_types')
for columna in pizza_types.columns:
    print(columna, pizza_types[columna].dtype)
print('pizza_price')
for columna in pizza_price.columns:
    print(columna, pizza_price[columna].dtype)
print('dict_pizzas')
for columna in dict_pizzas.columns:
    print(columna, dict_pizzas[columna].dtype)

# cantidad de nulls y nan
print('Numero de nulls en orders: ')
print(orders.isna().sum())
print('Numero de nulls en order_details: ')
print(order_details.isna().sum())
print('Numero de nulls en pizza_types: ')
print(pizza_types.isna().sum())
print('Numero de nulls en pizza_price: ')
print(pizza_price.isna().sum())
print('Numero de nulls en dict_pizzas: ')
print(dict_pizzas.isna().sum())