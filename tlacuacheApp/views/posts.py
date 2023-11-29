from django.shortcuts import render, get_object_or_404
from tlacuacheApp.models import Post

#from twitter.account import Account

#muestra post
def posts(request):
    #llamamos los posts de la bd
    posts = Post.objects.all()
    return render(
        request,
        "posts/posts.html",
        {"posts": posts},
    )

#detalle de post
def detail_posts(request, posts_id):
    #llamamos los posts de la bd
    posts = Post.objects.exclude(pk=posts_id)
    post = get_object_or_404(Post, pk=posts_id)
    return render(
        request, "posts/detail.html", {"post": post, "posts": posts}
    )
