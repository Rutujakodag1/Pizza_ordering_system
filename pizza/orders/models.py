# # from django.db import models

# # Create your models here.
# # orders/models.py
# from django.db import models

# class Pizza(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=5, decimal_places=2)
#     image_url = models.URLField(max_length=200)

#     def __str__(self):
#         return self.name


from django.db import models

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    # image_url = models.URLField(max_length=200)
    image = models.ImageField(upload_to='images/')  # Specify the upload directory as per your MEDIA_ROOT setting

    def __str__(self):
        return self.name
