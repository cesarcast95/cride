"""Circle model."""

#Django
from django.db import models

#Utilities
from cride.utils.models import CRideModel

class Circle(CRideModel):
    """Circle model.
    
    A circle is a private group where rides are offered and taken
    by its members. To join a circle a user must receive an unique
    invitation code from an existing circle member
    """

    name = models.CharField('circle name', max_length=128)
    slug_name = models.SlugField(unique=True, max_length=64)

    about = models.CharField('circle description', max_length=256)
    picture = models.ImageField(upload_to='circles/pictures', blank=True, null=True)

    #Stats
    rides_offered = models.PositiveIntegerField(default=0)
    rides_taken = models.PositiveIntegerField(default=0)

    verified = models.BooleanField(
        'verified circle',
        default=False,
        help_text='verified circles are also know as official communities.'
    )

    is_public = models.BooleanField(
        default=True,
        help_text='Public circles are listed in the main page so everyone know about their existence.'
    )

    is_limited = models.BooleanField(
        'limited',
        default=False,
        help_text='Limited circles can grow up to a fixed number of members.'
    )

    members_limit = models.PositiveIntegerField(
        default = 0,
        help_text = 'If circle is limited, this would be the limited on the numbers of members.'
    )

    def __str__(self):
        """Return circle name."""
        return self.name

    class Meta(CRideModel.Meta):
        """Meta class"""

        ordering = ['-rides_taken', '-rides_offered']
