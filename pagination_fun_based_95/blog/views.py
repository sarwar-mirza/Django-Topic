from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator
# Create your views here.

def post_list(request):
    all_post = Post.objects.all().order_by('id')
    pagi = Paginator(all_post, 3, orphans=1)
    page_number = request.GET.get('page')
    page_obj = pagi.get_page(page_number)
    return render(request, 'blog/home.html', {'page_obj':page_obj})
