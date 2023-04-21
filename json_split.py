import json
import random

def split_squad_data(input_file, train_ratio=0.8, dev_ratio=0.1):
    # Leer el archivo JSON de entrada
    with open(input_file, 'r') as f:
        squad_data = json.load(f)['data']

    # Calcular el número de párrafos y las proporciones para cada conjunto
    num_paragraphs = len(squad_data)
    num_train = int(num_paragraphs * train_ratio)
    num_dev = int(num_paragraphs * dev_ratio)

    # Crear diccionarios para almacenar los conjuntos divididos
    train_data, dev_data, val_data = {}, {}, {}

    # Asignar proporciones de datos a cada conjunto
    train_data['data'] = squad_data[:num_train]
    dev_data['data'] = squad_data[num_train:num_train + num_dev]
    val_data['data'] = squad_data[num_train + num_dev:]

    return train_data, dev_data, val_data

# Dividir el archivo SQuAD en conjuntos de entrenamiento, desarrollo y validación
input_file = './data/data.json'
train_data, dev_data, val_data = split_squad_data(input_file)

# Guardar los conjuntos divididos como archivos JSON
with open('data/train.json', 'w') as f:
    json.dump(train_data, f)

with open('data/dev.json', 'w') as f:
    json.dump(dev_data, f)

with open('data/val.json', 'w') as f:
    json.dump(val_data, f)
