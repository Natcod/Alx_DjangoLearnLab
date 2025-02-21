from django import models

class Company(models.Mode):
    name = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)

    def _str_(self):
        return self.name
    
class Department(models.Model):
    name = models.CharField(max_length = 255)
    company = models.ForeignKey(Company, on_delete = models.CASCADE, related_name = 'departments')

    def _str_(self):
        return f"{self.name} at {self.company}"
    
class Employee(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    department = models.ForeignKey(Department, on_delete = models.CASCADE, related_name = 'employees')

    def __str__(self):
        return f"{self.first_name} {self.last_name} in {self.department}"
    



class Product(models.Model):
    name = models.CharField(max_lenght = 255)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)

    def __str__(self):
        return self.name

class ProductDetail(models.Model):
    product = models.OneToOneField(Product, on_delete = models.CASCADE, related_name = 'detail')
    description = models.TextField()
    specifications = models.JSONField()

    def __str__(self):
        return f"Details for {self.prodocut.name}"

class Course(models.Model):
    title = models.CharField(max_lenght = 255)
    credist = models.IntegerField()   

    def __str__(self):
        return self.title
    
class Student(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_lenght = 255)
    courses = models.ManyToManyField(Course, related_name = 'students')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


