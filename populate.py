import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','fbvcrudproject.settings')
import django
django.setup()

from testapp.models import Emp_model
from faker import Faker
from random import *
faker=Faker()
def populate(n):
    for i in range(n):
        feno=randint(1001,9999)
        fename=faker.name()
        fesal=randint(1000,10000)
        faddr=faker.city()
        emp_record=Emp_model.objects.get_or_create(eno=feno,ename=fename,esal=fesal,eaddr=faddr)
n=int(input('enter no of record'))
populate(n)
print(f'{n} record inserted successfully')
