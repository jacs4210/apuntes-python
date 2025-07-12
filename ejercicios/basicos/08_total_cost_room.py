measure_room = int(input("Ingrese el área de la habitación en m2: "))
print(f"El area de la habitación es {measure_room} m2")

square_meter_cost = int(input("Ingrese el coste por metro cuadrado de azulejos: "))
tile = float(input("Ingrese el número de azulejos por caja que puede cubrir metro cuadrado: "))

total_box_tile = measure_room * tile
print(f"La cantidad de cajas de azulejos necesarios es {total_box_tile}")

total_cost = total_box_tile * square_meter_cost
print(f"El coste total de la habitación es ${total_cost}")