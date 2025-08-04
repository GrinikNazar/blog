from django.shortcuts import render

from .models import Post


def starting_page(request):
    all_posts_from_db = Post.objects.order_by('-publication_date')[:3]
    return render(request, "blog/index.html", {"posts": all_posts_from_db})


def posts(request):
    all_posts_from_db = Post.objects.order_by('-publication_date')
    return render(request, 'blog/all-posts.html', {"posts": all_posts_from_db})


def post_detail(request, slug):
    the_post = Post.objects.get(slug=slug)
    return render(request, 'blog/post-detail.html', {
        "post": the_post,
        'tags': the_post.tag.all()
    })

