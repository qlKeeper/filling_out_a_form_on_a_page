from data.data import Person
from faker import Faker
from random import randint

faker_en = Faker('En')

def generated_person():
    return Person(
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        email=faker_en.email(),
        current_address=faker_en.address(),
        mobile=faker_en.msisdn(),
        subject='English'
    )

def generated_file():
    path = f'/home/keeper/QA_automation/automation_project_demoqa/test{randint(10, 100)}.txt'
    file = open(path, 'w')
    file.write(f"Hello world! {randint(11, 135)}")
    file.close()
    return path