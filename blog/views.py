from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

me = User.objects.get(username='eren')

def post_list(request):
    posts = Post.objects\
                .all() \
                .order_by('created_date')
                # .filter(created_date__lte=timezone.now())\
                # .order_by('published_date')
    post_form = PostForm()
    # return render(request, 'blog/post_list.html', {'posts':posts})
    return render(request, 'blog/post_list.html', locals())

    # locals() == {'posts': posts, 'post_form': post_form}

@csrf_exempt
def add_record(request):
    if request.POST:
        title = request.POST['title'].encode('utf-8')
        text = request.POST['text'].encode('utf-8')
        newpost = Post.objects.create(author=me, title=title, text=text)
    return redirect('/blog')

def post_record(request, id):
    posts = Post.objects.filter(id__lte=id)[::-1][:2]
    post = posts[0]
    next_post = posts[1] if len(posts) > 1 else None
    # post = Post.objects.get(id = id)
    return render(request, 'blog/post_record.html', locals())
