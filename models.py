# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Rspdtable(models.Model):
    year = models.IntegerField(blank=True, null=True)
    fname = models.TextField(blank=True, null=True)
    sex = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    rspd = models.TextField(blank=True, null=True)  # This field type is a guess.
    id = models.TextField(blank=True, primary_key=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'rspdTable'
