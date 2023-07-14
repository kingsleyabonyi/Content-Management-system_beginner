from django.shortcuts import render, redirect
from . models import Post, Category
from . forms import PostForm
from django.contrib import messages

# Create your views here.

def index(request):
    post = Post.objects.all()
    context = {'post': post}
    return render(request, 'cmsapp/index.html', context)



def detail_list(request):
    context  = {}
    return render(request, 'cmsapp/detail_list.html', context)


def createpost(request):
    form = PostForm()
    context = {'form': form}
    if request.method == 'POST':
        form  = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Article created successfully')
            return redirect ('create')
        else:
            messages.error(request, 'Article not created')

        
    return render (request, 'cmsapp/create.html', context)


def updatepost(request, pk):
    form = PostForm()
    form = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=pk)
        if form.is_valid():
            form.save()
            messages.info(request, 'Article Updated successfully')

            return redirect('detail')
        else:
            messages.error(request, 'Article not updated')


    context = {'form': form}
        
    
    return render(request, 'cmsapp/create.html', context)



def deletepost(request, pk):
    form = PostForm(instance=pk)
    form = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form.delete()
        messages.info(request, 'Article Updated successfully')

        return redirect('index')
    
    context = {'form': form}
    return render(request, 'cmsapp/delete.html', context)


