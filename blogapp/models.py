from django.db import models
from django.contrib.auth.models import User
# import PIL.Image

def images_path(instance, filename):
    return "{}/{}".format(instance.topic.title, filename)

def topic_images_path(self, filename):
    return "{}/{}".format(self.title, filename)

class Topic(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=600)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    header_image = models.ImageField(blank=True, upload_to=topic_images_path)
    header_image_description = models.CharField(max_length=200, blank=True)
    confirmed = models.BooleanField(default=False)

    @property
    def short_description(self):
        if len(self.description)> (lenght:=270):
            return self.description[:lenght]+'...'
        else:
            return self.description
    
    def __str__(self):
        return self.title.capitalize()

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     # if self.header_image:            
    #     #     img = PIL.Image.open(self.header_image)

    #     #     output_size = (1600, 768)
    #     #     new_img= img.resize(output_size)
    #     #     new_img.save(self.header_image.name+'.'+img.format)

    #         # fh = storage.open(self.header_image.name, "w")
    #         # format = img.format
    #         # new_img.save(fh, format)
    #         # fh.close()
    #         # new_img.save(self.header_image.path)

    #         # fh = storage.open(self.header_image.name, "w")
    #         # format = img.format
    #         # new_img.save(fh, format)
    #         # fh.close()

class Comment(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.CharField(max_length=600)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)

class Image(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=images_path)
    show_in_gallery = models.BooleanField(default=True)



