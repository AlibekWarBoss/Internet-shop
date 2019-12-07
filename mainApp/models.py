from django.db import models

class Smartphone(models.Model):
    processor_choice = {("snapdragon", "Snapdragon"),("mediatek", "Mediatek")}
    name = models.CharField(max_length = 120, blank = True)
    ram = models.IntegerField()
    rom = models.IntegerField()
    diagonal = models.FloatField()
    price = models.IntegerField()
    camera = models.IntegerField()
    processor = models.CharField(max_length = 100, choices = processor_choice)
    image = models.ImageField(upload_to = 'Smartphone', blank = True, null = True)

    def __str__(self):
        return self.name


class Laptop(models.Model):
    processor_choice = {("intel", "Intel"),("amd Raedon", "AMD Raedon")}
    generation = models.IntegerField()
    name = models.CharField(max_length = 120, blank = True)
    ram = models.IntegerField()
    rom = models.IntegerField()
    diagonal = models.FloatField()
    price = models.IntegerField()
    processor = models.CharField(max_length = 100, choices = processor_choice)
    image = models.ImageField(upload_to = 'laptop', blank = True, null = True)

    def __str__(self):
        return self.name


class Camera(models.Model):
    name =  models.CharField(max_length = 120)
    mpx = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to = 'camera', blank = True, null = True)
    memory = models.IntegerField()
    def __str__(self):
        return self.name


class Earphone(models.Model):
    name =  models.CharField(max_length = 120)
    mpx = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to = 'Earphone', blank = True, null = True)

    def __str__(self):
        return self.name
