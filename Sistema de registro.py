import random
import json


instrumentos_prioridad = ['guitarra', 'piano', 'bateria', 'bajo', 'guitarra electrica']
musicos_disponibles = []
instrumentos_asignados = []
musicos_en_min = r'C:\Users\comgo\Desktop\church stuff\Sistema Registro\sistema_registro\basededatos.json'
#procedure that opens the json file and converts it into a new variable called data
with open(musicos_en_min, 'r') as json_file:
    # Load the JSON data
    data = json.load(json_file)

def asignacion_instrumento(value):
    musico_instrumento = random.choice(data['Musicos'][str(musicos_disponibles[value])])
    print(musicos_disponibles[value], musico_instrumento)
    instrumentos_asignados.append(musico_instrumento)

def random_choice_with_skip(choices, skip_value):
    while True:
        selected_value = random.choice(choices)
        if selected_value != skip_value:
            return selected_value

def used_check(musico, instrumento):
    if instrumento not in instrumentos_prioridad:
        replacement = random_choice_with_skip(data['Musicos'][str(musico)], instrumento)
        instrumentos_asignados.remove(instrumento)
        instrumentos_asignados.append(replacement)
        instrumentos_prioridad.remove(replacement)
    else:
        instrumentos_prioridad.remove(instrumento)


#asks for how many people
cantidad_miembros = int(input("Cuantos musicos son? "))
for number in range(cantidad_miembros):
    nombre = input("Nombre del musico: ")
    musicos_disponibles.append(nombre)

# print(data['Musicos']['Alex'].index('bajo'))

for numero in range(0, cantidad_miembros):
    asignacion_instrumento(numero)
    used_check(musicos_disponibles[numero], instrumentos_asignados[numero])
print(instrumentos_prioridad)

for numero in range(0, cantidad_miembros):
    print(f"{musicos_disponibles[numero]} va a estar en {instrumentos_asignados[numero]}")
print

    

    

if 'Wendy' in data['Lideres']:
    print("Success")
else:
    print('Failure')
# print(random.choice(data['Musicos']['Alex']))

# prueba = str(input("Nombre de prueba: "))

# if prueba in data['Musicos']:
#     print("Musicos")
# elif prueba in data['Cantantes']:
#     print("Cantantes")
# elif prueba in data['Lideres']:
#     print("Lideres")
# elif prueba in data['A/V']:
#     print("A/V")
# else:
#     print("Not in list")




