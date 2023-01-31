import pandas as pd


# order_id,date,time
orders = pd.read_csv('./data/orders.csv', sep=',', encoding='latin-1')

# order_details_id,order_id,pizza_id,quantity
order_details = pd.read_csv('./data/order_details.csv', sep=',', encoding='latin-1')

# pizza_type_id,name,category,ingredients
pizza_types = pd.read_csv('./data/pizza_types.csv', sep=',', encoding='latin-1')

# pizza_id,pizza_type_id,size,price
pizza_price = pd.read_csv('./data/pizzas.csv', sep=',', encoding='latin-1')


def pizzas_dia():
    dias = pd.DataFrame(columns=['day_id', 'pizzas'])
    anterior = 0
    dia = 0
    j = 0
    for i in range(len(orders)):
        if orders['date'][i] != anterior:
            if anterior:
                dias.loc[dia] = [dia, pizzas]
                dia += 1
            pizzas = []
            anterior = orders['date'][i]
        same_order = True
        while same_order and j < len(order_details):
            if orders['order_id'][i] == order_details['order_id'][j]:
                for k in range(order_details['quantity'][j]):
                    pizzas.append(order_details['pizza_id'][j])
                j += 1
            else:
                same_order = False

    dias.loc[dia] = [dia, pizzas]
    print(dias)
    dias.to_csv('./data/dias_pizzas.csv', sep=';', encoding='latin-1')

def pizzas_por_dia(ingredientes, pizza_info):
    dias = pd.DataFrame(columns=[])
    for ingredient in ingredientes:
        dias[ingredient] = 0.0
    for i in range(366):
        dias.loc[i] = 0.0
    for i in range(len(orders)):
        x = orders['date'][i]
        a = pd.to_datetime(x, format='%d/%m/%Y')
        dia = a.timetuple().tm_yday
        for _,row in order_details[order_details['order_id'] == orders['order_id'][i]].iterrows():
            quantities = [[1,'One','one',-1,'1','-1',],[2,'Two','two',-2,'2','-2']]
            try:
                n = int(row['quantity'])
            except:
                for q in quantities:
                    if row['quantity'] in q:
                        n = q[0]
            for _ in range(n):
                pizza_t = row['pizza_id']
                for _,row in pizza_price.iterrows():
                    if pizza_t == row['pizza_id']:
                        pizza_t = row['pizza_type_id']
                        size = row['size']
                        if size == 'S':
                            size = 0.75
                        elif size == 'M':
                            size = 1
                        elif size == 'L':
                            size = 1.25
                        elif size == 'XL':
                            size = 1.5
                        elif size == 'XXL':
                            size = 2
                        break
                ingredientes_p = pizza_info[pizza_t].split(',')
                for ingrediente in ingredientes_p:
                    dias.iloc[dia][ingrediente] += size
    return dias

def pizzas_por_semana(dias,ingredientes):
    semanas = pd.DataFrame(columns=[])
    for ingredient in ingredientes:
        semanas[ingredient] = 0.0
    for i in range(53):
        semanas.loc[i] = 0.0
    for i in range(len(dias)):
        n = i//7
        semanas.iloc[n] += dias.iloc[i]
    return semanas

def main():
    pizzas_dia()

    print(orders.isna().sum())
    print(order_details.isna().sum())

    pizza_info = {}
    for i in range(len(pizza_types)):
        pizza_info[pizza_types['pizza_type_id'][i]] = pizza_types['ingredients'][i]
    
    ingredientes = []
    for i in pizza_types['ingredients']:
        ingred = i.split(',')
        for j in ingred:
            if j not in ingredientes:
                ingredientes.append(j)

    dias = pizzas_por_dia(ingredientes, pizza_info)
    dias.to_csv('./data/dias.csv', sep=';', encoding='latin-1', index=False)
    print(dias)
    semanas = pizzas_por_semana(dias,ingredientes)
    semanas.to_csv('./data/semanas.csv', sep=';', encoding='latin-1', index=False)
    print(semanas)

if __name__ == '__main__':
    main()
    # semanas = pd.read_csv('./data/semanas.csv', sep=';', encoding='latin-1')
    # dias = pd.read_csv('./data/dias.csv', sep=';', encoding='latin-1')