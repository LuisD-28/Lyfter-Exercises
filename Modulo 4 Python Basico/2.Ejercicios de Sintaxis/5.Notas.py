grade_total = 0
gradecount = 1
actual_grade = 0
aprovedgrades = 0
failedgrades = 0
averagepassedgrades = 0
averagefailedgrades = 0
averagetotalgrades = 0

grade_total = int(input("Ingrese la cantidad de notas: "))

while gradecount <= grade_total:
    actual_grade = int(input(f"Ingrese la nota {gradecount}: "))
    gradecount += 1
    if actual_grade < 70:
        failedgrades += 1
        averagefailedgrades += actual_grade
    else:
        aprovedgrades += 1
        averagepassedgrades += actual_grade
    averagetotalgrades = averagetotalgrades + actual_grade  / grade_total

if averagefailedgrades == 0:
    averagefailedgrades = 'No hay notas reprobadas'
else:
    averagefailedgrades = averagefailedgrades / failedgrades

if averagepassedgrades == 0:
    averagepassedgrades = 'No hay notas aprobadas'
else:
    averagepassedgrades = averagepassedgrades / aprovedgrades


# averagefailedgrades = averagefailedgrades / failedgrades
# averagepassedgrades = averagepassedgrades / aprovedgrades

print(f"El promedio de las notas aprobadas es: {averagepassedgrades}")
print(f"El promedio de las notas reprobadas es: {averagefailedgrades}")
print(f"El promedio total de las notas es: {averagetotalgrades}")
