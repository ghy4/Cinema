from sqlalchemy import Column, Integer, String, DateTime, Boolean
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from abc import ABC, abstractmethod
from typing import List
from src.extensions import db, Base

class Person(ABC):
    instance_count = 0
    def __init__(self, first_name: str, last_name: str, age:int):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self.first_name = first_name
        self.last_name = last_name
        Person.instance_count += 1

    @abstractmethod
    def get_role(self) -> str:
        pass

    def __str__(self):
        return f"{self.first_namename} {self.last_name}, {self.age} years old"
    
    @staticmethod
    def get_instance_count():
        return Person.instance_count
    

class Customer(Person):
    def __init__(self, first_name: str, last_name: str, age:int, email: str):
        super().__init__(first_name, last_name, age)
        self.email = email

    def get_role(self) -> str:
        return "Customer"
    
class Employee(Person):
    def __init__(self, first_name: str, last_name: str, age:int, employee_id: int):
        super().__init__(first_name, last_name, age)
        self.employee_id = employee_id

    def get_role(self) -> str:
        return "Employee"
    
class Manager(Employee):
    def __init__(self, first_name: str, last_name: str, age:int, employee_id: int, department: str):
        super().__init__(first_name, last_name, age)
        self.department = department

    def get_role(self) -> str:
        return "Manager"
    def __str__(self):
        return f"{self.first_name} {self.last_name}, Manager of {self.department}"
    

class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    def __repr__(self):
        return f'<User {self.name}>'