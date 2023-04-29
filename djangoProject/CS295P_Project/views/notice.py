from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from ..models import *

@receiver(pre_save, sender=PostReward)
def update_watch_number(sender, instance,**kwargs):
    # send a message to WebSocket connection
    if(instance.pk):
        previous_watches = PostReward.objects.get(pk=instance.pk).watches
        reward_id=instance.id
        watches=instance.watches
        if previous_watches != instance.watches:
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "my_group",
                {
                    "type": "New_Watch_number",
                    "reward_id":  reward_id,
                    "watches": watches
                }
            )

@receiver(post_save, sender=AnswerReward)
def update_answer_reward(sender, instance,**kwargs):
    # send a message to WebSocket connection
    answer_user_name=instance.answer_user.username
    reward_id=instance.reward.id
    content=instance.content
    date=instance.date.strftime('%Y-%m-%d %H:%M:%S')
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "my_group",
        {
            "type": "New_Answer",
            "reward_id":  reward_id
        }
    )

@receiver(pre_save, sender=PostReward)
def update_accept_reward(sender, instance,**kwargs):
    if(instance.pk):
        previous_taken_user_id = PostReward.objects.get(pk=instance.pk).taken_user_id
        reward_id=instance.id
        taken_user_id=instance.taken_user_id
        if previous_taken_user_id != taken_user_id:
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "my_group",
                {
                    "type": "New_Accept_Reward",
                    "reward_id":  reward_id,
                }
            )

@receiver(pre_save, sender=PostReward)
def update_new_reward(sender, instance,**kwargs):
    if(instance.pk is None):
        previous_taken_user_id = PostReward.objects.get(pk=instance.pk).taken_user_id
        reward_id=instance.id
        taken_user_id=instance.taken_user_id
        if previous_taken_user_id != taken_user_id:
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "my_group",
                {
                    "type": "New_Accept_Reward",
                    "reward_id":  reward_id,
                }
            )