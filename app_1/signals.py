'''
This file is used to send notifications to the users when a new notification is created.
'''


from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from notifs.models import BroadcastNotification as Notification



@receiver(post_save, sender=Notification)
def notification_created(_, instance, created, **__):
    '''
    Function to send notification to the users when a new notification is created
    '''
    if created:

        channel_layer = get_channel_layer()

        async_to_sync(channel_layer.group_send)(
            'public_room',

            {
                "type": "send_notification",
                "message": instance.message
            }

        )
