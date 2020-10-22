from django.db import models
class planet(models.Model):
    #行星名
    name=models.CharField(max_length=256)
    #行星描述
    planet_state=models.TextField()
    #行星图片
    planet_pic=models.ImageField(upload_to='shy_img/planet_img')


