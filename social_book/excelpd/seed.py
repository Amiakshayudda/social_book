from .models import Employee
from faker import Faker

fake = Faker()

def seed_db(n):
    for i in range(0, n):
        Employee.objects.create(
            name=fake.name(),
            address=fake.address(),
            phone=fake.phone_number()
        )