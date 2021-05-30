from django.db.models.signals import post_save
from django.dispatch import receiver
from api.models import Face


@receiver(post_save, sender=Face)
def face_post_save(sender, instance, **kwargs):
    instance.delete()
