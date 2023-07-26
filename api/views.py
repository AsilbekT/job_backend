from rest_framework import viewsets, status
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .utils import token_required
from rest_framework.permissions import IsAuthenticated
from api.models import Account
from rest_framework.decorators import action

from .serializers import (
    JobSerializer, CompanySerializer, CatagorySerializer, ApplicationSerializer, AccountSerializer,
    EducationSerializer, WorkExperienceSerializer, AwardSerializer, SkillSerializer
)
from .models import (
    Job, Company, Catagory, Application,
    Education, WorkExperience, Award, Skill
)

# @method_decorator(token_required, name='dispatch')
class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    # detail view
    def retrieve(self, request, pk=None):
        job = Job.objects.get(id=pk)
        serializer = JobSerializer(job, context={'request': request})
        return Response(serializer.data)


# @method_decorator(token_required, name='dispatch')
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    # detail view
    def retrieve(self, request, pk=None):
        company = Company.objects.get(id=pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data)


class CatagoryViewSet(viewsets.ModelViewSet):
    queryset = Catagory.objects.all()
    serializer_class = CatagorySerializer

    # detail view
    def retrieve(self, request, pk=None):
        company = Catagory.objects.get(id=pk)
        serializer = CatagorySerializer(company)
        return Response(serializer.data)

@method_decorator(token_required, name='dispatch')
class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    # permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Ensure the user applying is the one logged in
            # if request.user.id != serializer.validated_data['user'].id:
            #     return Response({"detail": "You can only apply for jobs for yourself."},
            #                     status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            # After a successful save, return a success message
            return Response({"detail": "Job application has been created."},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if not request.user.is_staff:
            return Response({"detail": "Only admins can update job applications."},
                            status=status.HTTP_403_FORBIDDEN)
        return super().update(request, pk)
    
    def partial_update(self, request, pk=None):
        if not request.user.is_staff:
            return Response({"detail": "Only admins can update job applications."},
                            status=status.HTTP_403_FORBIDDEN)
        return super().partial_update(request, pk)

from django.http import Http404

class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]  # Require user to be authenticated

    def get_queryset(self):
        # Only return the authenticated user's account
        return Account.objects.filter(id=self.request.user.id)

    @action(detail=True, methods=['patch'], permission_classes=[IsAuthenticated])
    def upload_files(self, request, pk=None):
        try:
            account = self.get_object()
            serializer = self.get_serializer(account, data=request.data, partial=True)  # Set partial=True to update a part of the Account
            if serializer.is_valid():
                serializer.save()
                return Response({"detail": "Account updated successfully."})
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Http404:
            return Response({"detail": f"Account with ID {pk} not found."}, status=status.HTTP_404_NOT_FOUND)

       


class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class WorkExperienceViewSet(viewsets.ModelViewSet):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer

class AwardViewSet(viewsets.ModelViewSet):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer