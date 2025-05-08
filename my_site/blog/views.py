from datetime import date

from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "athor": "Naz",
        "date":  date(2023, 8, 15),
        "title": "Mountain Hiking",
        "excert": "Only Goverlyanka",
        "content": "I didnt hike to Goverla but I was in Goverlyanka",
    },     {
        "slug": "write-the-code",
        "image": "coding.jpg",
        "athor": "Naz",
        "date":  date(2023, 8, 17),
        "title": "Coding",
        "excert": "I coded some interesting",
        "content": "I have done new project where I use cool tecnologic",
    },     {
        "slug": "wood-walking",
        "image": "woods.jpg",
        "athor": "Naz",
        "date":  date(2023, 8, 16),
        "title": "Woods Walking",
        "excert": "Great forest",
        "content": "I breath fresh air and I got great vibe!",
    }
]


def starting_page(request):
    sorted_posts = sorted(all_posts, key=lambda post: post['date'])
    latest_post = sorted_posts[-3:]
    return render(request, "blog/index.html", {"posts": latest_post})


def posts(request):
    return render(request, 'blog/all-posts.html', {"posts": all_posts})


def post_detail(request, slug):
    # the_post = None
    # for post in all_posts:
    #     if slug == post['slug']:
    #         the_post = post
    the_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {
        "post": the_post
    })

