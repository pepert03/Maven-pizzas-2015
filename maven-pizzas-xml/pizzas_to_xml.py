import xml.etree.ElementTree as ET
import pandas as pd


def main():
    orders = pd.read_csv('./data/orders.csv', sep=';', encoding='latin-1')
    order_details = pd.read_csv('./data/order_details.csv', sep=';', encoding='latin-1')
    pizza_types = pd.read_csv('./data/pizza_types.csv', sep=',', encoding='latin-1')
    pizzas = pd.read_csv('./data/pizzas.csv', sep=',', encoding='latin-1')

    prediccion = pd.read_csv('./data/prediccion.csv', sep=';', encoding='latin-1')
    predict_j = eval(prediccion.to_json(orient='records'))
    
    data = ET.Element('root')
    topologia = ET.SubElement(data, 'topologia')
    ordersx = ET.SubElement(topologia, 'orders')
    order_detailsx = ET.SubElement(topologia, 'order_details')
    pizza_typesx = ET.SubElement(topologia, 'pizza_types')
    pizzasx = ET.SubElement(topologia, 'pizzas')
    for columnas in orders.columns:
        ET.SubElement(ordersx, 'Type', name=str(columnas)).text = str(orders[columnas].dtype)
        nans = orders[columnas].isna().sum()
        ET.SubElement(ordersx, 'Nans', name=str(columnas)).text = str(nans)
    for columnas in order_details.columns:
        ET.SubElement(order_detailsx, 'Type', name=str(columnas)).text = str(order_details[columnas].dtype)
        nans = order_details[columnas].isna().sum()
        ET.SubElement(order_detailsx, 'Nans', name=str(columnas)).text = str(nans)
    for columnas in pizza_types.columns:
        ET.SubElement(pizza_typesx, 'Type', name=str(columnas)).text = str(pizza_types[columnas].dtype)
        nans = pizza_types[columnas].isna().sum()
        ET.SubElement(pizza_typesx, 'Nans', name=str(columnas)).text = str(nans)
    for columnas in pizzas.columns:
        ET.SubElement(pizzasx, 'Type', name=str(columnas)).text = str(pizzas[columnas].dtype)
        nans = pizzas[columnas].isna().sum()
        ET.SubElement(pizzasx, 'Nans', name=str(columnas)).text = str(nans)
    
    
    
    prediccion = ET.SubElement(data, 'prediccion')
    for i in range(len(predict_j)):
        semana = ET.SubElement(prediccion, 'semana')
        semana.set('semana', str(i))
        for ingrediente in predict_j[i]:
            ET.SubElement(semana, 'ingrediente', name=ingrediente).text = str(predict_j[i][ingrediente])
    tree = ET.ElementTree(data)
    tree.write('pizzas.xml')


if __name__ == "__main__":
    main()