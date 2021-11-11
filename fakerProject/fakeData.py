import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','fakerProject.settings')
import django
django.setup()
print('fakedata')
#import random
from app1.models import Student
from faker import Faker
fake = Faker()

def phone_no():
    no1=fake.random_int(7,9)
    no2 = fake.random_number(9)
    return '+91'+str(no1)+str(no2)


def fakeDataGen(n):
    for i in range(n):
        fakeRn = fake.random_int(1,100)
        fakeName = fake.name()
        fakeEmail = fake.email()
        fakeMarks = fake.random_int(40,99)
        fakeAddress = fake.country()
        fakePhone = phone_no()
        student = Student.objects.get_or_create(rn=fakeRn,name=fakeName,email=fakeEmail,marks=fakeMarks,address=fakeAddress,phone=fakePhone)

if __name__== '__main__':
    print('data generating.....')

    fakeDataGen(10)
    print('data created')


