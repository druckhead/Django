from django.db import models

# Create your models here.
class Person(models.Model):
    GenderType = models.TextChoices("GenderType", "Male Female Polygender Genderfluid Bigender Agender")
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)
    personal_email = models.CharField(max_length=50, null=False)
    gender = models.CharField(
        blank=True, choices=GenderType.choices, max_length=16, null=False
    )
    birth_date = models.DateField()
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = "persons"


class Company(models.Model):
    company_name = models.CharField(max_length=50, null=False)
    country = models.CharField(max_length=32, null=False)
    city = models.CharField(max_length=32, null=False)
    address = models.CharField(max_length=128, null=False)
    phone_num = models.CharField(max_length=20, null=False)
    persons = models.ManyToManyField(Person, through="Employee")
    
    def __str__(self) -> str:
        return self.company_name

    class Meta:
        db_table = "companies"


class Employee(models.Model):
    person = models.ForeignKey(to=Person, on_delete=models.CASCADE, null=False)
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE, null=False)
    job_title = models.CharField(max_length=128, null=False)
    is_current_job = models.BooleanField(null=False, blank=False)
    company_email = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f"p_id:{self.person_id} c_id:{self.company_id}"

    class Meta:
        db_table = "employees"
