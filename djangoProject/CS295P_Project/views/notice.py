from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.db.models.signals import post_save
from django.dispatch import receiver
from ..models import PostReward

@receiver(post_save, sender=PostReward)
def handle_post_save_signal(sender, instance, **kwargs):
    # send a message to WebSocket connection
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "my_group",
        {
            "type": "NewData",
            "message": "New data has been inserted!"
        }
    )