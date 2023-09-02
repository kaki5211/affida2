# Create your models here.
from django.db import models

class Performer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    birth = models.DateField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    name_eng = models.CharField(max_length=255, unique=True, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)
    name_eng = models.CharField(max_length=255, unique=True, blank=True, null=True)
    def __str__(self):
        return self.name

class Maker(models.Model):
    name = models.CharField(max_length=255, unique=True)
    name_eng = models.CharField(max_length=255, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Label(models.Model):
    name = models.CharField(max_length=255, unique=True)
    name_eng = models.CharField(max_length=255, unique=True, blank=True, null=True)
    def __str__(self):
        return self.name

class Series(models.Model):
    name = models.CharField(max_length=255, unique=True)
    name_eng = models.CharField(max_length=255, unique=True, blank=True, null=True)
    def __str__(self):
        return self.name
    
class Thumbnail(models.Model):
    url = models.URLField()
    width = models.IntegerField()
    height = models.IntegerField()

class Kyounuki(models.Model):
    post_day = models.DateField()
    productnumbers = models.ManyToManyField('Video')
    article = models.TextField()
    def __str__(self):
        return str(self.post_day)


class Video(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    performers = models.ManyToManyField(Performer, blank=True, null=True)
    productnumber = models.CharField(max_length=255, blank=True, null=True, unique=True)
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE, blank=True, null=True)
    label = models.ForeignKey(Label, on_delete=models.CASCADE, blank=True, null=True)
    series = models.ForeignKey(Series, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    duration = models.CharField(max_length=255, blank=True, null=True)
    views = models.IntegerField(blank=True, null=True)
    thumbnails = models.ManyToManyField(Thumbnail, blank=True, null=True)
    kyounuki_post_day = models.DateField(blank=True, null=True)
    producturl = models.URLField(blank=True, null=True)
    productimage = models.URLField(blank=True, null=True)
    productsumple = models.URLField(blank=True, null=True)
    productthumbnail = models.URLField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    active = models.BooleanField(default=True)
    images = models.CharField(max_length=1023, blank=True, null=True)
    issue = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.productnumber



class ContentsTag(models.Model):
    name = models.CharField(max_length=255, unique=True)
    name_eng = models.CharField(max_length=255, unique=True, blank=True, null=True)
    def __str__(self):
        return self.name

class Contents(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    contents = models.TextField(blank=True, null=True)
    views = models.IntegerField(blank=True, null=True)
    tags = models.ManyToManyField(ContentsTag, blank=True, null=True)

    def __str__(self):
        return self.title
    
    # contents = 
    #     <title>あいうえお
    #     <subtitle>かきくけこ
    #     <text>text
    #     <blockquote>blockquote<bookpage>2
    #     <title>2



class Test(models.Model):
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE, blank=True, null=True)
    teststr = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.maker
    


    