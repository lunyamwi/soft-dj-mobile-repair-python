from django.shortcuts import render

# Create your views here.
def article_view(request):
    return render(request,'blog.html')

def article_detail(request):
    return render(request,'blog_detail.html')