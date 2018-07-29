from django.db import models
from test1.users import models as user_models

# Create your models here.
class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True



class Image(TimeStampedModel):

    """ Image Model """

    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()
    creator = models.ForeignKey(user_models.User,on_delete = models.CASCADE, null=True  )


class Comment(TimeStampedModel):

    """ Commnet Model """

    message = models.TextField()
    creator = models.ForeignKey(user_models.User,on_delete = models.CASCADE , null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE , null=True)



class Like(TimeStampedModel):

    """ Like Model """

    creator = models.ForeignKey(user_models.User,on_delete = models.CASCADE , null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE , null=True)