from django.db import models


class MenuItem(models.Model):
    menu_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)
