from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length =30)

    def save_location(self):
        self.save()
    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length =30)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def search_by_category(cls,search_term):
        category = cls.objects.filter(name__icontains=search_term)
        return category

    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length =30)
    description = models.TextField()
    image = models.ImageField(upload_to = 'images/')
    upload_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank =True)
    location = models.ForeignKey(Location,on_delete=models.CASCADE,blank =True,null=True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_image_by_id(cls,number):
        return cls.objects.get(pk = number)

    def __str__(self):
        return self.name