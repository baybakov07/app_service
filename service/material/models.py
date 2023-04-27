from django.db import models


class Faculty(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=250)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='faculty')

    def __str__(self):
        return self.name


class Semester(models.Model):
    number = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.number} семестр'


class Subject(models.Model):
    name = models.CharField(max_length=250)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='semester')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department')

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject')

    def __str__(self):
        return self.name


class Document(models.Model):
    name = models.CharField(max_length=100)
    document_file = models.FileField(upload_to='documents/')
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='section')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True)

    def __str__(self):
        return self.name
