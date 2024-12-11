from django.db import models
from django.core.validators import RegexValidator
import uuid  # For generating UUIDs


# Organization Model
class Organization(models.Model):
    o_name = models.CharField(max_length=100)
    o_email = models.EmailField(unique=True)
    o_password = models.CharField(max_length=250)
    o_contact = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Enter a valid phone number.")],
        null=True,
        blank=True,
        unique=True
    )
    o_website = models.CharField(max_length=100)
    o_address = models.CharField(max_length=150)
    o_country = models.CharField(max_length=100, null=True, blank=True)
    o_state = models.CharField(max_length=100, null=True, blank=True)
    o_city = models.CharField(max_length=100, null=True, blank=True)
    o_pin_no = models.CharField(max_length=20, null=True, blank=True)

    # Logging date and time
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically adds creation time
    updated_at = models.DateTimeField(auto_now=True)  # Updates when the record is modified

    def __str__(self):
        return f'{self.o_name} ({self.o_email})'

    class Meta:
        db_table = "organization"


# Employee Model
class Employee(models.Model):
    o_id = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='employees')
    e_name = models.CharField(max_length=100)
    e_email = models.EmailField()
    e_password = models.CharField(max_length=255)
    e_gender = models.CharField(max_length=25)
    e_contact = models.CharField(max_length=100)
    e_address = models.CharField(max_length=150)
    e_role = models.CharField(max_length=150, default='Employee')
    monitored = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.e_name} ({self.e_email})'

    class Meta:
        db_table = "employee"


# Computer Model
class Computer(models.Model):
    c_log_ts = models.DateTimeField(auto_now_add=True)  # Automatically logs the current timestamp
    c_ip_address = models.GenericIPAddressField()
    c_system_status = models.CharField(max_length=50, default='no')
    c_operating_system = models.CharField(max_length=255)
    c_username = models.CharField(max_length=255)
    c_host_name = models.CharField(max_length=100)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    o_id = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='computers')
    e_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='computers')

    def __str__(self):
        return f'{self.c_host_name} ({self.c_ip_address})'

    class Meta:
        db_table = "computer"
