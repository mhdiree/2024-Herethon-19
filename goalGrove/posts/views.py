from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Category 
from django.contrib.auth.decorators import login_required

def post_list(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category')

    if category_id:
        category = get_object_or_404(Category, id = category_id)
        posts = category.posts.all().order_by('-id')
    else:
        posts = Post.objects.all().order_by('-id')
    return render(request, 'blog/list.html', {'posts' : posts, 'categories' : categories})

@login_required
def create_post(request):
    categories = Category.objects.all()

    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        video = request.FILES.get('video')
        image = request.FILES.get('image')

        category_ids = request.POST.getlist('category')
        category_list = [get_object_or_404(Category, id = category_id) for category_id in category_ids]

        post = Post.objects.create(
            title = title,
            content = content,
            author = request.user,
            image = image,
            video = video
        )

        for category in category_list:
            post.category.add(category)

        return redirect('users:main')
    return render(request, 'posts/create_post.html', {'categories' : categories})
