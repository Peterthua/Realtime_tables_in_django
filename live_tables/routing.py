from django.urls import path

from data.consumer import LiveProfileTableConsumer, RealTimePostConsumer

websocket_urlpatterns = [
    path('ws/live_profile_table/', LiveProfileTableConsumer.as_asgi()),
    path('ws/post/', RealTimePostConsumer.as_asgi()),
]
