from django.db import models

class Adminuser(models.Model):
    admin_name = models.CharField(max_length=200)
    admin_photo = models.ImageField(upload_to='Admin_Photo/', blank=True, null=True)
    admin_desc = models.TextField(blank=True)
    #phone = models.CharField(max_length=20)
    admin_email = models.EmailField(max_length=50, unique=True, blank=False)
    #is_mvp = models.BooleanField(default=False)
    #hire_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.admin_name
    

