from PIL import Image
from django.db import models
import numpy as np
import cv2


# Create your models here.
class Cheque(models.Model):
    image_original = models.ImageField(upload_to="original", null=True)
    image_preprocessing = models.ImageField(upload_to="preprocessing", null=True)
    image_with_bounding_boxes = models.ImageField(upload_to="bounding_boxes", null=True)
    image_id = models.ImageField(upload_to="id", null=True)
    image_nom = models.ImageField(upload_to="nom", null=True)
    image_montant_chiffre = models.ImageField(upload_to="montant_chiffre", null=True)
    image_montant_lettre = models.ImageField(upload_to="montant_lettre", null=True)
    image_place = models.ImageField(upload_to="place", null=True)
    image_date = models.ImageField(upload_to="date", null=True)
    image_signature = models.ImageField(upload_to="signature", null=True)


    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     img = Image.open(self.image.path)
    #     img.show()
    #     # new_image = process_image(img)
    #
    #     return super().save(*args, **kwargs)

    class Meta:
        db_table = 'Cheque'

