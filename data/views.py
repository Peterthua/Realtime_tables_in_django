from django.shortcuts import render
from channels.layers import get_channel_layer
from .models import Profile
from asgiref.sync import async_to_sync
from django.http import JsonResponse
from .forms import ProfileForm, PostForm
from rest_framework import viewsets
from .serialisers import PostSerialiser
from .models import Post


# a view to show all the posts and also logic to create a new post
def posts_list(request):
    posts = Post.objects.order_by('-created_at')
    form = PostForm()
    context = {
        'posts': posts,
        'form': form
    }
    return render(request, 'post.html', context)


def create_post(request):
    # if request.POST.get('status', False) == 'on':
    #     status = True
    channel_layer = get_channel_layer()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()

            post_data = {
                'id': post.id,
                'title': post.title,
                'status': post.status,
                'author': post.author.username,
                'created_at': post.created_at.strftime('%B %d, %Y'),
            }

            # send the post data to the websocket
            async_to_sync(channel_layer.group_send)(
                'post_updates',
                {
                    'type': 'post.created',
                    'data': post_data
                }
            )
            # return JsonResponse({
            #     'data': post_data,
            # }, safe=False)
        else:
            async_to_sync(channel_layer.group_send)(
                'post_updates',
                {
                    'type': 'post.error',
                    'data': form.errors
                }
            )

    else:
        form = PostForm()
    return render(request, 'post.html', {
        'form': form,
        'posts': Post.objects.all(),
    })


def index(request):
    profiles = Profile.objects.all()
    form = ProfileForm()
    context = {
        'profiles': profiles,
        'form': form
    }
    return render(request, 'index.html', context)


def create_profile(request):
    pass


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerialiser
    queryset = Post.objects.all()
