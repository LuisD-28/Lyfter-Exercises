name = input("Ingrese su nombre: ")
last_name = input("Ingrese su apellido: ")
age = int(input("Ingrese su edad: "))

if age <= 2:
    print(f"{name} {last_name} es un bebe.")
elif age <= 9:
    print(f"{name} {last_name} es un niño.")
elif age <= 11:    
    print(f"{name} {last_name} es un preadolescente.")
elif age <= 19:
    print(f"{name} {last_name} es un adolescente.")
elif age <= 59:
    print(f"{name} {last_name} es un adulto.")
else:    
    print(f"{name} {last_name} es un adulto mayor.")
