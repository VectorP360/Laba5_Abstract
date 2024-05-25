from PR5 import Employee, Worker, Engineer
from DET import Detail, Knot, Machine, Product

#Первый файл

employee = Employee('print the document')
employee.complete_work()
print(f'Employee {employee.task} {employee.completed_task} times\n')

worker = Worker('work with machine-tool')
worker.complete_work()

engineer = Engineer('repare the machine-tool')
engineer.complete_work()

#Второй файл

knot = Knot('Steel')
knot.purpose()

machine = Machine('Table')
machine.purpose()

paper_plane = Product('50 копеек')
paper_plane.purpose()