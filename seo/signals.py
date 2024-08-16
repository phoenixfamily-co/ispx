import os
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import Article


@receiver(pre_delete, sender=Article)
def delete_files_on_instance_delete(sender, instance, **kwargs):
    if instance.image and os.path.isfile(instance.image.path):
        os.remove(instance.image.path)
        print(f"deleted {instance.image.path}")

