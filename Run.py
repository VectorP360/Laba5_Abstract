from PR5 import Employee, Worker, Engineer
from DET import Detail, Knot, Machine

employee = Employee('print the document')
employee.complete_work()
print(f'Employee {employee.task} {employee.completed_task} times')

worker = Worker('work with machine-tool')
worker.complete_work()

engineer = Engineer('repare the machine-tool')
engineer.complete_work()