from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import CustomLostPostForm
from posts.models import lostItems
from django.contrib import messages
from signup.models import lostUser
from django.contrib.auth.decorators import login_required
from django.db.models import Q 

#For create form
@login_required(login_url='/login/')
def createPost(request):
    if request.method == 'POST':
        form = CustomLostPostForm(request.POST, request.FILES)
        
        if form.is_valid():
            # Get the currently logged-in user's username
            current_user_username = request.user.username
            # Query the lostUser model to find the corresponding user instance
            user_instance = lostUser.objects.get(username=current_user_username)
            new_post=lostItems(
                status='active',
                user=user_instance,
                postTitle=form.cleaned_data['postTitle'],
                lostItem=form.cleaned_data['lostItem'],
                location=form.cleaned_data['location'],
                description=form.cleaned_data['description'],
                fileUpload = form.cleaned_data['fileUpload']  # Get the uploaded file from the form

            )
            
            new_post.save()            
            return redirect('Lost Post Overall') 
        else:
            print('Not valid.')
    else:
        form = CustomLostPostForm()
    return render(request,'create_post.html', {'form': form})


#For posts overall and search
@login_required(login_url='/login/')
def postOverall(request):

    #get all lost items from DB first
    lost_items=lostItems.objects.all()

    #check is a search query named q in the request
    search_query=request.GET.get('q')

    #Filter lost items based on search query
    if search_query:
        lost_items=lostItems.objects.filter(
            Q(postTitle__icontains=search_query) |
            Q(lostItem__icontains=search_query) |
            Q(location__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    context={'lost_items': lost_items}

    return render(request,'lostpost_overall.html',context)

#for post Detail
@login_required(login_url='/login/')
def postDetail(request,post_id):

    current_post=get_object_or_404(lostItems, post_id=post_id)
    context={'current_post':current_post}
    return render(request,'lostpost_detail.html',context)

#For the current user's post
@login_required(login_url='/login/')
def userPosts(request):
    if request.user.is_authenticated:
        # Filter lostItems by the username of the current user
        current_user_posts = lostItems.objects.filter(user__username=request.user.username)
        context = {'current_user_posts': current_user_posts}
        return render(request, 'user_posts.html', context)
    return render(request,'user_posts.html')