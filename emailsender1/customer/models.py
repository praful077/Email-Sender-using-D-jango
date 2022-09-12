from django.db import models

# Create your models here.

# import email
# from unicodedata import name
# from django.db import models

# Create your models here.


class EmailInfo(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'email_info'
