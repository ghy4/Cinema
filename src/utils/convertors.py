from src.models.user import Customer, Employee, Manager

def user_to_person(user):
    name_parts = user.name.split(' ', 1)
    first_name = name_parts[0]
    last_name = name_parts[1] if len(name_parts) > 1 else ''
    age = getattr(user, 'age', 0)

    if user.role == "Manager":
        return Manager(first_name, last_name, age, getattr(user, 'employee_id', 0), getattr(user, 'department', ''))
    elif user.role == "Employee":
        return Employee(first_name, last_name, age, getattr(user, 'employee_id', 0))
    else:
        return Customer(first_name, last_name, age, user.email)