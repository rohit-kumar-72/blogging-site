from .models import Blog
from django.shortcuts import render
from .forms import BlogForm,UserRegistrationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404,redirect

# Create your views here.

def Home(request):
    return render(request,"index.html")

def get_All_Blogs(request):
    allBlog=Blog.objects.all().order_by("-created_at")
    return render(request,"Blog_list.html",{"allBlog":allBlog})

@login_required
def create_BLog(request):
    if(request.method=="POST"):
        form=BlogForm(request.POST,request.FILES)
        if(form.is_valid()):
            blog=form.save(commit=False)
            blog.user=request.user
            blog.save()
            return redirect('get_All_Blogs')
    else:
        form=BlogForm()
    return render(request,"create_Blog.html",{"form":form})

@login_required
def edit_Blog(request,blogId):
    blog=get_object_or_404(Blog,pk=blogId,user=request.user)
    if(request.method=="POST"):
        form=BlogForm(request.POST,request.FILES,instance=blog)
        if(form.is_valid()):
            blog=form.save(commit=False)
            blog.user=request.user
            blog.save()
            return redirect('get_All_Blogs')
    else:
        form=BlogForm(instance=blog)
    return render(request,"create_Blog.html",{"form":form})

@login_required
def delete_Blog(request,blogId):
    blog=get_object_or_404(Blog,user=request.user,pk=blogId)
    if(request.method=="POST"):
        blog.delete()
        return redirect("get_All_Blogs")
    return render(request,"blog_confirm_delete.html",{"blog":blog})

def register(request):
    if(request.method=='POST'):
        form=UserRegistrationForm(request.POST)
        if(form.is_valid()):
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('get_All_Blogs')
    else:
        form=UserRegistrationForm()
    return render(request,"registration/register.html",{'form':form})