import csv
from datetime import datetime

import os
import django

os.environ["DJANGO_SETTINGS_MODULE"] = "employees.settings"
django.setup()

from employees_app.models import Employee, Company, Person


def populate(path: str, table: str):
    with open(path, "r") as csv_file:
        reader = csv.DictReader(
            csv_file,
            delimiter=",",
        )

        for row in reader:
            if table.lower() == "employees":
                p = Person.objects.get(id=int(row.pop("person_id")))
                c = Company.objects.get(id=int(row.pop("company_id")))
                iscurrentjob = row.pop('is_current_job').capitalize()
                Employee.objects.create(person=p, company=c, is_current_job=iscurrentjob, **row)
            elif table.lower() == "companies":
                Company.objects.create(**row)
            elif table.lower() == "persons":
                dt = (
                    datetime.strptime(row.pop("birth_date"), "%m/%d/%Y")
                    .date()
                    .strftime("%Y-%m-%d")
                )
                Person.objects.create(birth_date=dt, **row)
            else:
                raise NotImplementedError()


if __name__ == "__main__":
    Person.objects.all().delete()
    Company.objects.all().delete()
    Employee.objects.all().delete()

    populate(
        "/Users/danielraz/repos/django_employees/csv_data/persons.csv", table="persons"
    )
    populate(
        "/Users/danielraz/repos/django_employees/csv_data/companies.csv",
        table="companies",
    )
    populate(
        "/Users/danielraz/repos/django_employees/csv_data/employees.csv",
        table="employees",
    )
