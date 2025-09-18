from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class PublishStatus(models.TextChoices):
    PUBLISHED = "pub", "Published"
    COMING_SOON = "soon", "Coming Soon"
    DRAFT = "draft","Draft"



class AccessRequirement(models.TextChoices):
    FREE = "free", "Free"
    PAID = "paid", "Paid"
    SUBSCRIPTION = "sub", "Subscription"


def handle_image_upload(instance, filename):
    return f"{filename}"


class Course( models.Model ):
    title = models.CharField( max_length= 200 )
    description = models.TextField( blank=True,null = True )
    created_at = models.DateTimeField( auto_now_add=True )
    #image = models.ImageField(upload_to=handle_image_upload, blank=True, null=True)
    image = CloudinaryField('image', blank=True, null=True)
    access = models.CharField( max_length= 10, choices= AccessRequirement.choices, default= AccessRequirement.FREE )
    status = models.CharField( max_length= 10, choices= PublishStatus.choices, default= PublishStatus.DRAFT )


    @property

    def is_published(self):

        return self.status == PublishStatus.PUBLISHED
