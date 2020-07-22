from django.db import models


class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField()
    update = models.DateTimeField()

    # abstract model
    class Meta:
        abstract = True
