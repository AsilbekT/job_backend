from django.db import models
from accounts.models import Account

class Company(models.Model):
    title = models.CharField(max_length=200, verbose_name="Company Name", help_text="The name of the company.")
    company_logo = models.ImageField(upload_to="static/company_logos/", help_text="The company's logo.")
    description = models.TextField(help_text="A brief description of the company.")
    website = models.URLField(help_text="The company's website.")

    def __str__(self):
        return self.title

class Catagory(models.Model):
    title = models.CharField(max_length=200, verbose_name="Job catagory", help_text="The catagory of the job.")

    def __str__(self):
        return self.title
    
    
class Job(models.Model):
    FULL_TIME = "FT"
    PART_TIME = "PT"
    FREELANCE = "FR"
    TEMPORARY = "TP"
    INTERNSHIP = "IN"
    JOB_TYPES = [
        (FULL_TIME, "Full Time"),
        (PART_TIME, "Part Time"),
        (FREELANCE, "Freelance"),
        (TEMPORARY, "Temporary"),
        (INTERNSHIP, "Internship"),
    ]

    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True, related_name="jobs")
    job_title = models.CharField(max_length=200, verbose_name="Job Title", help_text="The title of the job.")
    location = models.CharField(max_length=200, help_text="The location of the job.")
    salary = models.CharField(max_length=200, help_text="The salary for the job.")
    tag = models.CharField(max_length=200, help_text="A tag for the job.")
    category = models.ForeignKey(Catagory, on_delete=models.CASCADE, null=True, blank=True, related_name="jobs", help_text="The category of the job.")
    experience = models.CharField(max_length=200, help_text="The experience required for the job.")
    date_posted = models.DateTimeField(auto_now_add=True, help_text="The date and time when the job was posted.")
    job_type = models.CharField(max_length=2, choices=JOB_TYPES, default=FULL_TIME, help_text="The type of the job.")
    
    def get_destination(self):
        return {"min": 0, "max": 20}

    def get_total_salary(self):
        return {"min": 0, "max": 500}

    def __str__(self):
        return self.job_title



class Application(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="user")
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="job")
    cv = models.FileField(upload_to='static/applied/cvs/')
    status = models.BooleanField(default=False)
    date_applied = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.username