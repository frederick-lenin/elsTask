from django.db import models
class Admin(models.Model):
    name = models.CharField(max_length=100)
    roleid=models.CharField(max_length=3,null= True)
    
    def __str__(self):
        return f"{self.name}{self.role}"
        
class Role(models.Model):
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return self.role

class Student(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=20,default='default_password')
    Role=models.ForeignKey(Role, on_delete=models.CASCADE,null=True)
    

    def __str__(self):
        return self.name
    
# class Role(models.Model):
#     id = models.AutoField(primary_key=True) 
#     role = models.CharField(max_length=3, unique=True)
    
#     def __str__(self):
        # return self.role
 
    # name = models.CharField(max_length=100)
    # email = models.EmailField(unique=True)
    # phone = models.CharField(max_length=15)
    # password = models.CharField(max_length=255)
    # roleid = models.IntegerField(choices=ROLE_CHOICES)

    # def __str__(self):
    #     return self.name
