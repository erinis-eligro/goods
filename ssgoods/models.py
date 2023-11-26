from django.db import models
from django.urls import reverse

# Create your models here.
class CheckedUser(models.Model):
    username = models.CharField(max_length=20, verbose_name='fullname')
    email = models.EmailField(max_length=100, verbose_name='companyemail')
    
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.username
    
    class Meta:
        db_table = 'checkedUsers'
        # verbose_nmae = 'checkuserforgoods'
        # verbose_nmae_plural = 'checkuserforgoods'