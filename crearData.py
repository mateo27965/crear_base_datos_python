import pandas as pd
from faker import Faker
import random

fake = Faker()

num_dispositivos = 50  

dispositivos = []

for i in range(num_dispositivos):
    tipo_dispositivo = random.choice(['smartphone', 'router'])

    if tipo_dispositivo == 'smartphone':
        sistema_operativo = random.choice(['iOS', 'Android'])
    else:
        sistema_operativo = 'firmware'

    if tipo_dispositivo == 'smartphone':
        if sistema_operativo == 'iOS':
            fabricante = 'Apple'
            modelo = random.choice(['iPhone 15 Pro Max','iPhone 15 Pro','iPhone 15 Plus','iPhone 15','iPhone 14 Pro Max','iPhone 14 Pro','iPhone 14 Plus','iPhone 14','iPhone 13 Pro Max','iPhone 13 Pro','iPhone 13 Plus','iPhone 13','iPhone 12 Pro Max','iPhone 12 Pro','iPhone 12 Plus','iPhone 12'])
        else: 
            fabricante = random.choice(['Huawei', 'Samsung', 'LG', 'Motorola'])
            if fabricante == 'Huawei':
                modelo = random.choice(['Mate 50 Pro','Mate 20','Mate 20 Pro','Mate 10','Mate 10 Pro','nova 2i','Mate 9 lite','Mate 9'])
            if fabricante == 'Samsung':
                modelo = random.choice(['Samsung Galaxy S23 Ultra','Samsung Galaxy S23+','Samsung Galaxy S23','Samsung Galaxy S22 Ultra','Samsung Galaxy S22+','Samsung Galaxy S22','Samsung Galaxy Z Fold5','Samsung Galaxy Z Fold4','Samsung Galaxy A03 Core','Samsung Galaxy M22'])
            if fabricante == 'LG':
                modelo = random.choice(['LG K62+ K525BMW','LG W41+','LG W41 Pro','LG W31+','LG W41','LG Phoenix 4','LG Wing Dual SIM','LG K42 Dual SIM'])
            if fabricante == 'Motorola':
                modelo = random.choice(['edge 40 neo','edge 40 pro','edge 40','edge 30','edge 30 fusion','edge 30 neo','edge 30 pro','motorola razr 40 ultra'])
    else:
        fabricante = random.choice(['Cisco', 'Huawei', 'Linksys', 'Netgear', 'Asus'])
        modelo = random.choice(['ARRIS TG2482 ','FAST3686V2 ','TECNICOLORCGA2121'])

    


    dispositivo = {
        'id': i + 1,
        'tipo': tipo_dispositivo,
        'modelo': modelo,
        'sistemaOperativo': sistema_operativo,
        'fabricante': fabricante,
        'precio': round(random.uniform(100, 1000), 2)
    }
    dispositivos.append(dispositivo)


df = pd.DataFrame(dispositivos)


nombre_archivo = 'datos_dispositivos.xlsx'
df.to_excel(nombre_archivo, index=False)

print(f"Se ha generado el archivo '{nombre_archivo}' con los datos de dispositivos.")
