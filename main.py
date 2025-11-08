from task_manager import TaskManager

def print_menu():
    print("\n--- Gestor de Tareas Inteligente ---")
    print("1. Añadir tarea")
    print("2. Añadir tarea compleja (con IA)")
    print("3. Listar tareas")
    print("4. Completar tarea")
    print("5. Eliminar tarea")
    print("6. Salir")    

def main():
    manager=TaskManager()

    while True:
        print_menu()

        choice =input("Elige una opción")

        match choice:
                case "1":
                    description=input("Dime descripcion")
                    manager.add_task(description)
                    
                case "2":
                    manager.list_task()
                case "3":
                    id=input("id de la tarea a completar")
                    manager.complete_task(id)
                case "4":
                    id=input("id de la tarea a eliminar")
                    manager.delete_task(id)
                case "5":
                    pass
                case "6":
                    print("Saliendo")
                    break
                case _:    
                    print("Opción no ovalidad")

if __name__ == "__main__":#nombre del fichero = a main
    main()