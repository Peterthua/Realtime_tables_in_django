import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .forms import PostForm, ProfileForm

from django.core.exceptions import ValidationError


class LiveProfileTableConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.group_name = None
        # self.room_name = None

    def connect(self):
        self.group_name = "live_profile_table"
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        try:
            text_json_data = json.loads(text_data)
            # print("DATA: ", text_json_data)
            data = text_json_data['data']
            form = ProfileForm(data=data)

            if form.is_valid():
                profile_instance = form.save()
                # #print('CLEANED DATA: ', form.cleaned_data)
                async_to_sync(self.channel_layer.group_send)(
                    self.group_name,
                    {
                        'type': 'profile.created',
                        'data': {
                            'id': profile_instance.id,
                            'first_name': profile_instance.first_name,
                            'last_name': profile_instance.last_name,
                            'email': profile_instance.email,
                            'location': profile_instance.location,
                            'birth_date': profile_instance.birth_date.strftime('%d/%m/%Y'),
                            'language_preference': profile_instance.language_preference,
                        }
                    }
                )
        except json.JSONDecodeError as e:
            async_to_sync(self.channel_layer.group_send)(
                self.group_name,
                {
                    'type': 'profile.error',
                    'data': f"Error decoding JSON: {e}"
                }
            )
            # print(f"Error decoding JSON: {e}")
        except ValidationError as e:
            async_to_sync(self.channel_layer.group_send)(
                self.group_name,
                {
                    'type': 'profile.error',
                    'data': f"Validation error: {e}"
                }
            )
            # print(f"Validation error: {e}")
        except Exception as e:
            async_to_sync(self.channel_layer.group_send)(
                self.group_name,
                {
                    'type': 'profile.error',
                    'data': f"Unknown error occurred: {e}"
                }
            )
            # print(f"Error: {e}")

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    def profile_created(self, event):
        data = event['data']
        # print("XXX: ", data)
        self.send(text_data=json.dumps(data))

    def profile_error(self, event):
        data = event['data']
        # print("YYY: ", data)
        self.send(text_data=json.dumps(data))


# <editor-fold desc="Real-time Post Consumer">
class RealTimePostConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.group_name = None

    def connect(self):
        self.group_name = "post_updates"
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    def receive(self, text_data=None, bytes_data=None):
        try:
            text_json_data = json.loads(text_data)
            # #print("DATA: ", text_json_data)
            data = text_json_data['data']
            form = PostForm(data=data)

            if form.is_valid():
                post_instance = form.save()
                # #print('CLEANED DATA: ', form.cleaned_data)
                async_to_sync(self.channel_layer.group_send)(
                    self.group_name,
                    {
                        'type': 'post.created',
                        'data': {
                            'id': post_instance.id,
                            'title': post_instance.title,
                            'status': str(post_instance.status).capitalize(),
                            'author': str(post_instance.author.username).capitalize(),
                            # format the date as 20/01/2024 (date/month/year)
                            'created_at': post_instance.created_at.strftime('%d/%m/%Y'),
                        }
                    }
                )
        except json.JSONDecodeError as e:
            async_to_sync(self.channel_layer.group_send)(
                self.group_name,
                {
                    'type': 'post.error',
                    'data': f"Error decoding JSON: {e}"
                }
            )
            # print(f"Error decoding JSON: {e}")
        except ValidationError as e:
            async_to_sync(self.channel_layer.group_send)(
                self.group_name,
                {
                    'type': 'post.error',
                    'data': f"Validation error: {e}"
                }
            )
            # print(f"Validation error: {e}")
        except Exception as e:
            async_to_sync(self.channel_layer.group_send)(
                self.group_name,
                {
                    'type': 'post.error',
                    'data': f"Error: {e}"
                }
            )
            # print(f"Error: {e}")

    def post_created(self, event):
        data = event['data']
        # print("XXX: ", data)
        self.send(text_data=json.dumps(data))

    def post_error(self, event):
        data = event['data']
        # print("YYY: ", data)
        self.send(text_data=json.dumps(data))

# </editor-fold>
