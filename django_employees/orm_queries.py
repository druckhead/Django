import os
import django
from datetime import datetime

os.environ["DJANGO_SETTINGS_MODULE"] = "employees.settings"
django.setup()

from employees_app.models import Employee, Company, Person


def get_person_name_by_id(person_id: int) -> str:
    """
    Given person id, return string that represents person full name
    :param person_id:
    :return:
    """
    p = Person.objects.get(id=person_id)

    return f"{p.first_name} {p.last_name}"


def get_people_by_age(age: int) -> list[Person]:
    """
    Given age in years, return list of persons of this age
    :param age:
    :return:
    """
    p = Person.objects.filter(birth_date__year=datetime.now().date().year - age)

    return p


def get_people_cnt_by_gender(gender: str) -> list[Person]:
    """
    Given the gender, return list of people of this gender
    :param gender:
    :return:
    """
    p = Person.objects.filter(gender__iexact=gender)

    return p


def get_companies_by_country(country: str) -> list[Company]:
    """
    Given country name, return list of companies' names in this country
    :param country:
    :return:
    """
    c = Company.objects.filter(country__iexact=country)
    return c


def get_company_employees(company_id: int, current_only: bool) -> list[Person]:
    """
    Given company id, return list of persons whi work(ed) for this company
    :param company_id:
    :param current_only: if True, return only people who are currently work in the company
    :return:
    """
    e = Employee.objects.filter(company_id=company_id)
    if current_only:
        e = e.filter(is_current_job=True)
    return e


def get_person_jobs(person_id: int) -> list[dict[str, str]]:
    """
    Given person_id, return list of dictionaries that map from company name to job title
    :param person_id:
    :return:
    """
    jobs = Employee.objects.prefetch_related("company").filter(person=person_id)
    return [{job.company.company_name: job.job_title} for job in jobs]


if __name__ == "__main__":
    print(get_person_jobs(11))
