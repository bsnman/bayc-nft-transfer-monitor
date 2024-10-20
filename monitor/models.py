from django.db import models

# Create your models here.


class TransferModel(models.Model):

    token_id = models.CharField(max_length=50)
    from_address = models.CharField(max_length=50)
    to_address = models.CharField(max_length=50)
    transaction_hash = models.TextField()
    block_number = models.IntegerField()
