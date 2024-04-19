from django.contrib.auth.models import AbstractUser
from django.db import models
#from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',
        blank=True,
    )

     #Edit 

    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)
    last_edit = models.DateTimeField(auto_now=True)

    
    #class Meta:
        #app_label = 'accounts'

    #groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name='custom_user_groups')
    #user_permissions = models.ManyToManyField(Permission, verbose_name=_('user permissions'), blank=True, related_name='custom_user_permissions')
