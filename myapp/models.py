from django.db import models  
class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    econtact = models.CharField(max_length=15)  
    class Meta:  
        db_table = "employee"  



      
class UploadImage(models.Model):  
    caption = models.CharField(max_length=200)  
    image = models.ImageField(upload_to='images')  
      
    def __str__(self):  
        return self.caption  