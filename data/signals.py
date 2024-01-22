# from .models import Post
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from channels.layers import get_channel_layer
# from asgiref.sync import async_to_sync
#
#
# @receiver(post_save, sender=Post)
# def post_created(sender, instance, created, **kwargs):
#     if created:
#         channel_layer = get_channel_layer()
#         async_to_sync(channel_layer.group_send)(
#             'post_updates',
#             {
#                 'type': 'post.created',
#                 'data': {
#                     'id': instance.id,
#                     'title': instance.title,
#                     'status': str(instance.status).capitalize(),
#                     'author': str(instance.author.username).capitalize(),
#                     # format the date as 20/01/2024 (date/month/year)
#                     'created_at': instance.created_at.strftime('%d/%m/%Y'),
#                 }
#             }
#         )
