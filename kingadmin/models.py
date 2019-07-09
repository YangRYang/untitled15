from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=20)
    id = models.IntegerField(primary_key=True)

    ChioceFiled = (
        (0,'高中'),
        (1,'大学'),
        (2,'硕士'),
        (3,'毕业'),
    )
    education = models.IntegerField(choices=ChioceFiled)
    role = models.ForeignKey('Role',on_delete=models.SET_NULL,null=True)
class Role(models.Model):
    RoleChioce = (
        (0,'领导'),
        (1,'实习生'),
        (2,'生力军'),
    )
    Role = models.IntegerField(choices=RoleChioce)
    Power = models.CharField(max_length=20)


class

