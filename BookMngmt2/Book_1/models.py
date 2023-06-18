# Create your models here.
from django.db import models

class Book(models.Model):
    auth_first_name = models.CharField(max_length=30)
    auth_email = models.EmailField()
    Title = models.CharField(max_length=100)
    Publisher = models.CharField(max_length=100)
    Publication_year = models.IntegerField(default=0)
    Issue_status = models.BooleanField(default=False)
    Issued_roll_no = models.IntegerField(default=0, null=True)

    class Meta:
        verbose_name_plural = 'Book'

    def __str__(self):
        return '%s %s %s %s %s %s' % (
        self.auth_first_name,
        self.Title,
        self.Publisher,
        self.Publication_year,
        self.Issue_status,
        self.Issued_roll_no if self.Issued_roll_no is not None else 'N/A'
    )

