from django.urls import path

from .views import index, create_profile, create_post, posts_list

# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
#
# router.register('post', PostViewSet, basename='post')

urlpatterns = [
    path('', index, name='index'),
    path('post/', posts_list, name='post'),
    path('create_profile/', create_profile, name='create_profile'),

]
# urlpatterns += router.urls
