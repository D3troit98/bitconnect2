from django.db import models
from django.utils import timezone

# Create your models here.

class PollingUnit(models.Model):
    uniqueid = models.IntegerField(primary_key=True)
    polling_unit_id = models.IntegerField()
    ward_id = models.IntegerField()
    lga_id = models.IntegerField()
    uniquewardid = models.IntegerField()
    polling_unit_number = models.CharField(max_length=255)
    polling_unit_name = models.CharField(max_length=255)
    polling_unit_description = models.TextField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    entered_by_user = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    user_ip_address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'polling_unit' # set the table name explicitly


class AnnouncedPuResult(models.Model):
    result_id=  models.IntegerField(primary_key=True)
    polling_unit_uniqueid = models.IntegerField()
    party_abbreviation = models.CharField(max_length=255)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=255, blank=True, null=True)
    date_entered =  models.DateTimeField(blank=True, null=True)
    user_ip_address = models.CharField(max_length=255,blank=True, null=True)

    class Meta:
        db_table = 'announced_pu_results' # set the table name explicitly    


class AgentName(models.Model):
    name_id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    pollingunit_uniqueid = models.IntegerField()

    class Meta:
        db_table = 'agentname'


class Ward(models.Model):
    uniqueid = models.IntegerField(primary_key=True)
    ward_id = models.IntegerField()
    ward_name = models.CharField(max_length=255)
    lga_id = models.IntegerField()
    ward_description = models.TextField(blank=True, null=True)
    entered_by_user = models.CharField(max_length=255)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=255)

    class Meta:
        db_table = 'ward'


class States(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'states'


class Lga(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    lga_id = models.IntegerField()
    lga_name = models.CharField(max_length=100)
    state_id = models.IntegerField()
    lga_description = models.TextField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(default=timezone.now)
    user_ip_address = models.GenericIPAddressField()

    class Meta:
        db_table = 'lga'