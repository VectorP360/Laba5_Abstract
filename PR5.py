from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def complete_work(self):
        pass

class Employee(Person):
    def __init__(self, task):
        self.task = task
        self.completed_task = 0
 
    def complete_work(self):
        print (f'Employee begin to complete {self.task}')
        self.completed_task += 1

class Worker(Person):
    def __init__(self, work):
        self.work = work

    def complete_work(self):
         print(f'Worker begin to complete {self.work}')

class Engineer(Worker):
    def __init__(self, engineer_work):
        self.engineer_work = engineer_work

    def complete_work(self):
        print(f'Engineer begin to complete {self.engineer_work}')