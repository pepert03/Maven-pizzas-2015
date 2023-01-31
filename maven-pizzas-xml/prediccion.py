import pandas as pd

def main():
    semanas = pd.read_csv('./data/semanas.csv', sep=';', encoding='latin-1')
    ingredientes = [column for column in semanas.columns]
    prediccion = pd.DataFrame(columns=[])
    for ingredient in ingredientes:
        prediccion[ingredient] = 0.0
    for i in range(53):
        prediccion.loc[i] = 0.0
    media = {}
    for ingrediente in ingredientes:
        suma = semanas[ingrediente].sum()
        media[ingrediente] = suma/53
    for n in range(0,53):
        row = semanas.iloc[n]
        for ingrediente in ingredientes:
            prediccion.iloc[n][ingrediente] = ((row[ingrediente]+media[ingrediente])/2).round(2)
    prediccion.to_csv('./data/prediccion.csv', sep=';', encoding='latin-1', index=False)
    return prediccion
