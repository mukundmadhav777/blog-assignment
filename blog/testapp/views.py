from django.shortcuts import render
from testapp.forms import BlogForm
from testapp.models import Blog
# Create your views here.
def index_view(request):
    return render(request,'testapp/index.html')
def add_blog_view(request):
    form =BlogForm()
    if request.method=='POST':
        form=BlogForm(request.POST)
        if form.is_valid():
            form.save()
        return index_view(request)
    return render(request,'testapp/add.html',{'form':form})

def list_blog_view(request):
    blog_list=Blog.objects.all()
    return render(request,'testapp/list.html',{'blog_list':blog_list})
