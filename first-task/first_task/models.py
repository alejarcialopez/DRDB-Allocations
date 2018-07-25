from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class DRBDAllocation(models.Model):
    name = models.CharField(max_length=30)
    device = models.PositiveIntegerField(validators=[MinValueValidator(3), MaxValueValidator(999)])
    port = models.PositiveIntegerField(validators=[MinValueValidator(7791)])


    def __str__(self):
        return str(self.name)

    def name_validator(self):

        number = self.name.split('-')[2]
        if 'mws-priv-' not in self.name or number < 1:
            raise ValidationError(
                _(f'{self.name} is not valid'),
                params={'value': self.name},
            )

