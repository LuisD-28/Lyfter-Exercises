employees = [
    {
        "name": "Carlos", 
        "email": "carlos@empresa.com",
        "department": "Ventas"
    },
    {
        "name": "Ana",
        "email": "ana@empresa.com",
        "department": "TI"
    },
    {
        "name": "Luis",
        "email": "luis@empresa.com",
        "department": "Ventas"
    },
    {
        "name": "Sofía",
        "email": "sofia@empresa.com",
        "department": "RRHH"
    },
    {
        "name": "Raul",
        "email": "Raul@empresa.com",
        "department": "TI"
    },
    {
        "name": "Renata",
        "email": "Renata@empresa.com",
        "department": "RRHH"
    },
]

ventas_list = [i for i in employees if i["department"] == "Ventas"] 
ti_list = [i for i in employees if i["department"] == "TI"] 
rrhh_list = [i for i in employees if i["department"] == "RRHH"]

print(ventas_list)
print(ti_list)
print(rrhh_list)

