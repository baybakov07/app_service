from rest_framework import viewsets
from .models import Faculty, Department, Semester, Subject, Section, Document
from .serializers import (
    FacultySerializer,
    DepartmentSerializer,
    SemesterSerializer,
    SubjectSerializer,
    SectionSerializer,
    DocumentSerializer,
)

class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
