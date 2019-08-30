from django.db import models

# Create your models here.
class ContracOfNumber(models.Model):
    contrac_of_number = models.IntegerField(blank=True, null=True, default=1)

    class Meta:
        verbose_name = 'Останній номер договору'

    def __str__(self):
        return "%s" % (self.contrac_of_number)

class Customers(models.Model):
    client_code = models.IntegerField(blank=True, null=True, default=None)
    entity_name = models.CharField(max_length=200, blank=True, null=True, default=None)
    first_name = models.CharField(max_length=100, blank=True, null=True, default=None)
    second_name = models.CharField(max_length=100, blank=True, null=True, default=None)
    patronymic = models.CharField(max_length=100, blank=True, null=True, default=None)
    value_added_tax = models.IntegerField(blank=True, null=True, default=None)
    single_tax = models.BooleanField(default=False, null=True, blank=True)
    general_tax = models.BooleanField(default=False, null=True, blank=True)
    extract = models.BooleanField(default=False, null=True, blank=True)
    passport = models.BooleanField(default=False, null=True, blank=True)
    contract_number = models.IntegerField(blank=True, null=True, default=None)
    notes = models.TextField(blank=True, null=True, default=None)

    class Meta:
        verbose_name = 'Клієнт'
        verbose_name_plural = 'Клієнти'

    def __str__(self):
        return "%s" % (self.client_code)

class Address(models.Model):
    client_id = models.ForeignKey(Customers, blank=True, null=True, on_delete=models.SET_NULL)
    address = models.CharField(max_length=200, blank=True, null=True, default=None)
    license = models.BooleanField(default=False, null=True, blank=True)
    models.DateField(default=None, auto_now=False)
    notes = models.TextField(blank=True, null=True, default=None)

    class Meta:
        verbose_name = 'Адреса'
        verbose_name_plural = 'Адреси'

    def __str__(self):
        return "%s" % (self.address)











