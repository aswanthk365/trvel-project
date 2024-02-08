from django.db import models

# Create your models here.
class servieces(models.Model):
    name=models.CharField(max_length=120)
    image=models.ImageField(upload_to='service_images')
    def __str__(self):
        return self.name

class customer_review(models.Model):
    name=models.CharField(max_length=122)
    comment=models.TextField()
    cus_image=models.ImageField(upload_to='customer_img')

    def __str__(self):
        return self.name
