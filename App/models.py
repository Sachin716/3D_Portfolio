from django.db import models

class category(models.Model):
    Name =  models.CharField(max_length=100)
    Thumbnail = models.ImageField(upload_to="staticfiles/Images/Category_Thumbnails")
    Description = models.CharField(max_length=1000)

    def __str__(self):
        return self.Name


class Product(models.Model):
    Belongs_To = models.ForeignKey(category , on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=1000)
    time_taken = models.CharField(max_length=1000)
    model = models.FileField(upload_to="App/3D_Models")
    thumbnail = models.ImageField(upload_to="App/Maps/Thumbnails")
    Custom_Three_File = models.FileField(upload_to="staticfiles/ThreeJSFiles" , blank = True , null=True)
    Metal_Maps = models.ImageField(upload_to="App/Maps/Metal_Maps" , null=True , blank=True)
    Ambeint_Occlusion_Maps = models.ImageField(upload_to="App/Maps/AmbientO_Maps" , null=True , blank=True)
    Emmission_Maps = models.ImageField(upload_to="App/Maps/Emmission_Maps" , null=True , blank=True)
    Height_Maps = models.ImageField(upload_to="App/Maps/Height_Maps" , null=True , blank=True)
    Colour_Maps = models.ImageField(upload_to="App/Maps/Colour_Maps" , null=True , blank=True)
    Roughness_Maps = models.ImageField(upload_to="App/Maps/Roughness_Maps" , null=True , blank=True)
    Normal_Map = models.ImageField(upload_to="App/Maps/Normal_Maps" , null=True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.Name
    


class Renders(models.Model):
    Name = models.CharField(max_length=100)
    render =  models.ImageField(upload_to="App/Renders")

    def __str__(self):
        return self.Name
# Create your models here.
