tasks = []  # lista de tareas

while True:
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Salir")
    choice = input("Elige una opción (1-3): ")
    
    if choice == '1':
        print("Tareas:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
    elif choice == '2':
        task = input("Ingresa la nueva tarea: ")
        tasks.append(task)
    elif choice == '3':
        break
    else:
        print("Opción inválida")
