from rest_framework import serializers
from .models import Job, Company, Catagory, Application
from api.models import Account
from django.urls import reverse
from django.utils import timezone
import datetime
from .models import Education, WorkExperience, Award, Skill


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class CatagorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Catagory
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    jobTitle = serializers.CharField(source='job_title')
    logo = serializers.SerializerMethodField()
    link = serializers.SerializerMethodField()
    destination = serializers.SerializerMethodField()
    totalSalary = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    time = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = [
            'id', 'logo', 'jobTitle', 'company', 'location', 'time', 'salary', 'tag', 
            'category', 'created_at', 'experience', 'job_type', 'link', 'destination', 'totalSalary'
        ]


    def get_destination(self, obj):
        return obj.get_destination()

    def get_totalSalary(self, obj):
        return obj.get_total_salary()

    def get_logo(self, obj):
        request = self.context.get('request')
        logo_url = obj.company.company_logo.url
        return request.build_absolute_uri(logo_url)

    def get_link(self, obj):
        # This assumes that you have a detail view for your Company model
        return reverse('company-detail', kwargs={'pk': obj.company.pk})

    def get_created_at(self, obj):
        # This assumes that you want to show the time since the job was posted in days
        return obj.date_posted

    def get_time(self, obj):
        now = datetime.datetime.now(timezone.utc)
        # now = datetime.time(timezone.utc)
        diff = now - obj.date_posted

        hours = diff.total_seconds() // 3600
        minutes = (diff.total_seconds() % 3600) // 60

        return  f"{int(hours)} hours, {int(minutes)} minutes ago"
    

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'user', 'job', 'cv', 'date_applied']


class AccountSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(required=False)
    cv = serializers.FileField(required=False)
    class Meta:
        model = Account
        fields = [
            'id', 
            'email', 
            'username', 
            'date_joined', 
            'avatar', 
            'last_login', 
            'cv', 
            'is_admin', 
            'is_active', 
            'is_staff', 
            'is_superuser',
            'is_employer'
            ]




class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = '__all__'

class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'
