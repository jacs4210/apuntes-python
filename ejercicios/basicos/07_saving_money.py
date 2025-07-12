saving = 0
goal = 1000

money_to_save = int(input(f"Cuanto deseas ingresar en tu ahorro? Actualmente tienes ${saving} y la meta es de ${goal}: "))

saving += money_to_save

print(f"Ahora tienes ${saving} en tu ahorro.")

is_goal_reached = saving >= goal

print(f"Has alcanzado tu meta de ahorro? {'Si' if is_goal_reached else 'No'}")