from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from ..models import *
from django.db.models import Q

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


@receiver(pre_save, sender=PostThread)
def update_like_number(sender, instance,**kwargs):
    # send a message to WebSocket connection

    if(instance.pk):

        previous_likes = PostThread.objects.get(pk=instance.pk).likes
        thread_id=instance.id
        likes=instance.likes
        if previous_likes != instance.likes:

            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "my_group",
                {
                    "type": "New_Like_number",
                    "thread_id":  thread_id,
                    "likes": likes
                }
            )


@receiver(pre_save, sender=PostThread)
def update_tip(sender, instance,**kwargs):
    # send a message to WebSocket connection

    if(instance.pk):

        previous_tip = PostThread.objects.get(pk=instance.pk).tip_num
        if previous_tip != instance.tip_num:

            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "my_group",
                {
                    "type": "New_Tip",
                    "tip_num":  instance.tip_num,
                }

# @receiver(pre_save, sender=PostReward)
# def update_new_reward(sender, instance,**kwargs):
#     if(instance.pk is None):
#         previous_taken_user_id = PostReward.objects.get(pk=instance.pk).taken_user_id
#         reward_id=instance.id
#         taken_user_id=instance.taken_user_id
#         if previous_taken_user_id != taken_user_id:
#             channel_layer = get_channel_layer()
#             async_to_sync(channel_layer.group_send)(
#                 "my_group",
#                 {
#                     "type": "New_Accept_Reward",
#                     "reward_id":  reward_id,
#                 }
#             )

@receiver(post_save, sender=PostReward)
@receiver(post_save, sender=PostThread)
@receiver(post_save, sender=AnswerReward)
def auto_save_history(sender, instance, **kwargs):
    # send a message to WebSocket connection
    created = kwargs.get('created', True)
    if created:
        if isinstance(instance, PostReward):
            user = instance.user
            date = instance.date
            title = instance.title
            type1 = "post reward"

            # 在 history 模型中创建一条新记录
            History.objects.create(
                thread_id = instance.id,
                user=user,
                date=date,
                type=type1,
                title = title,
                coins_history = instance.coin_num
            )
        elif isinstance(instance, PostThread):
            user = instance.user
            date = instance.date
            title = instance.title
            type1 = "thread receive"
            # 在 history 模型中创建一条新记录
            History.objects.create(
                user=user,
                date=date,
                type=type1,
                title = title,
                thread_id=instance.id
                # coins_history = instance.coin_num
            )
            tmp = PostReward.objects.filter(Q(title=instance.title) & Q(user=instance.user)).first()
            ans_user = AnswerReward.objects.filter(reward=tmp).first()
            History.objects.create(
                user=ans_user.answer_user,
                date=date,
                type="Answer received",
                title=title,
                thread_id=instance.id
                # coins_history = instance.coin_num
            )
        elif isinstance(instance, AnswerReward):
            History.objects.create(
                user=instance.answer_user,
                date=instance.date,
                type="you answer",
                interact_id = instance.reward.user.id,
                thread_id=instance.reward.id
            )
            History.objects.create(
                user=instance.reward.user,
                date=instance.date,
                type="someone answered you",
                thread_id=instance.reward.id,
                interact_id=instance.answer_user.id,
            )