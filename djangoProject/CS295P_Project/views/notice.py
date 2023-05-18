from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from ..models import *
from django.db.models import Q


@receiver(pre_save, sender=PostReward)
def update_watch_number(sender, instance, **kwargs):
    # send a message to WebSocket connection
    if (instance.pk):
        previous_watches = PostReward.objects.get(pk=instance.pk).watches
        reward_id = instance.id
        watches = instance.watches
        if previous_watches != instance.watches:
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "my_group",
                {
                    "type": "New_Watch_number",
                    "reward_id": reward_id,
                    "watches": watches
                }
            )


@receiver(post_save, sender=AnswerReward)
def update_answer_reward(sender, instance, **kwargs):
    # send a message to WebSocket connection
    answer_user_name = instance.answer_user.username
    reward_id = instance.reward.id
    content = instance.content
    date = instance.date.strftime('%Y-%m-%d %H:%M:%S')
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "my_group",
        {
            "type": "New_Answer",
            "reward_id": reward_id
        }
    )


@receiver(pre_save, sender=PostReward)
def update_accept_reward(sender, instance, **kwargs):
    if (instance.pk):
        previous_taken_user_id = PostReward.objects.get(pk=instance.pk).taken_user_id
        reward_id = instance.id
        taken_user_id = instance.taken_user_id
        if previous_taken_user_id != taken_user_id:
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "my_group",
                {
                    "type": "New_Accept_Reward",
                    "reward_id": reward_id,
                }
            )


@receiver(pre_save, sender=PostThread)
def update_like_number(sender, instance, **kwargs):
    # send a message to WebSocket connection

    if (instance.pk):

        previous_likes = PostThread.objects.get(pk=instance.pk).likes
        thread_id = instance.id
        likes = instance.likes
        if previous_likes != instance.likes:
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "my_group",
                {
                    "type": "New_Like_number",
                    "thread_id": thread_id,
                    "likes": likes
                }
            )


@receiver(pre_save, sender=PostThread)
def update_dislike_number(sender, instance, **kwargs):
    # send a message to WebSocket connection

    if (instance.pk):

        previous_dislikes = PostThread.objects.get(pk=instance.pk).dislikes
        thread_id = instance.id
        dislikes = instance.dislikes
        if previous_dislikes != instance.dislikes:
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "my_group",
                {
                    "type": "New_DisLike_number",
                    "thread_id": thread_id,
                    "dislikes": dislikes
                }
            )


@receiver(pre_save, sender=PostThread)
def update_tip(sender, instance, **kwargs):
    # send a message to WebSocket connection

    if (instance.pk):

        previous_tip = PostThread.objects.get(pk=instance.pk).tip_num
        if previous_tip != instance.tip_num:
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "my_group",
                {
                    "type": "New_Tip",
                    "tip_num": instance.tip_num,
                }
            )


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


@receiver(pre_save, sender=PostReward)
@receiver(post_save, sender=PostThread)
@receiver(post_save, sender=AnswerReward)
def auto_save_history(sender, instance, **kwargs):
    # send a message to WebSocket connection
    created = kwargs.get('created', True)
    if (created and (isinstance(instance, PostReward)) is False):
        # if isinstance(instance, PostReward):
        #     user = instance.user
        #     date = instance.date
        #     title = instance.title
        #     type1 = "post reward"
        #
        #     # 在 history 模型中创建一条新记录
        #     History.objects.create(
        #         thread_id = instance.id,
        #         user=user,
        #         date=date,
        #         type=type1,
        #         title = title,
        #         coins_history = instance.coin_num
        #     )
        if isinstance(instance, PostThread):
            user = instance.user
            title = instance.title
            type1 = "Reward Completed"
            # 在 history 模型中创建一条新记录
            History.objects.create(
                user=user,
                type=type1,
                title=title,
                thread_id=instance.reward_id
                # coins_history = instance.coin_num
            )  # give accept user a message
            # tmp = PostReward.objects.filter(Q(title=instance.title) & Q(user=instance.user)).first()
            # ans_user = AnswerReward.objects.filter(reward=tmp).first()
            ans_user = User.objects.get(id=instance.taken_user_id)
            History.objects.create(
                user=ans_user,
                type=type1,
                title=title,
                thread_id=instance.reward_id
                # coins_history = instance.coin_num
            )
        elif isinstance(instance, AnswerReward):
            ask_user = instance.reward.user
            if ask_user == instance.answer_user and instance.reward.taken_user_id != 0:
                user_tmp = User.objects.filter(id=instance.reward.taken_user_id).first()
                History.objects.create(
                    user=user_tmp,
                    type="Keep asking",
                    title=instance.reward.title,
                    thread_id=instance.reward.id,
                    interact_id=ask_user.username,
                )
            elif ask_user != instance.answer_user:
                History.objects.create(
                    user=instance.reward.user,
                    type="Someone answered you",
                    thread_id=instance.reward.id,
                    interact_id=instance.answer_user.username,
                    title=instance.reward.title,
                )
    else:
        if isinstance(instance, PostReward):
            if(instance.pk):
                previous_is_taken = PostReward.objects.get(pk=instance.pk).is_taken
                if instance.is_taken != previous_is_taken:
                    user_tmp = User.objects.get(id=instance.taken_user_id)
                    History.objects.create(
                        user=instance.user,
                        type="Reward Accepted",
                        thread_id=instance.id,
                        interact_id=user_tmp.username,
                        title=instance.title
                    )

# @receiver(pre_save, sender=History)
# def add_unread_message(sender, instance, **kwargs):
#     if not instance.pk:
#         print("dssaddasdasdas")
#         user=UserProfile.objects.filter(user=instance.user).first()
#         user.unread_messages+=1
#         user.save()

