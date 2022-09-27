from django.db import models
from django.contrib.auth.models import User


# class UserName(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(verbose_name='Name', max_length=30)
#     surname = models.CharField(verbose_name='Name', max_length=30)
#
#     def __str__(self):
#         return 'User: {} {}'.format(self.name, self.surname)


class UserFields(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, unique=True)
    url = models.URLField(verbose_name="URL")
    phone = models.CharField(max_length=30)
    image = models.ImageField(verbose_name="IMG")
    FullUserAddress = models.ForeignKey(FullUserAddress, verbose_name="FullUserAddress", on_delete=models.PROTECT)

    def __str__(self):
        return 'User: {}'.format(self.user)


class FullUserAddress(models.Model):
    country = models.CharField(verbose_name='Name', max_length=30)
    city = models.CharField(verbose_name='Name', max_length=30)
    street = models.CharField(verbose_name='Name', max_length=30)

    def __str__(self):
        return 'Address: {}, {}, {}'.format(self.country, self.city, self.street)


