from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.core.mail import send_mail
from blogapp.Forms import EmailSendForm,CommentsForm
from blogapp.models import Post
from django.http import HttpResponseRedirect
from taggit.models import Tag

def post_list_view(request,tag_slug=None):
    post_list=Post.objects.all()
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        post_list=post_list.filter(tags__in=[tag])
    paginator=Paginator(post_list,2)
    page_number=request.GET.get('page')
    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)

    return render(request,'blogapp/post_list.html',{'post_list':post_list,'tag':tag})
def post_detail_view(request,year,month,day,post):
    post=get_object_or_404(Post,slug=post,
                                status='published',
                                publish__year=year,
                                publish__month=month,
                                publish__day=day)
    comments=post.comments.filter(active=True)
    csubmit=False
    if request.method=='POST':
        form=CommentsForm(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)#as of now form object contails only data submitted by end user like name email,comment
            new_comment.post=post#in db we shd also save ti which post these comments are submitted
            new_comment.save()#saving comments along with post
            csubmit=True
    else:
        form=CommentsForm()
    return render(request,'blogapp/post_detail.html',{'post':post,'form':form,'csubmit':csubmit,'comments':comments})

def mail_send_view(request,id):
    post=get_object_or_404(Post,id=id,status='published')
    sent=False
    if request.method=='POST':
        form=EmailSendForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            send_mail('Subject','message','pythonpthn@gmail.com',[cd['to']])
            sent=True
    else:
        form=EmailSendForm()
        return render(request,'blogapp/sharebymail.html',{'form':form,'post':post,'sent':sent})


def add_comment_view(request,id):
    post=get_object_or_404(Post,id=id,status='published')
    comments=post.comments.filter(active=True)
    csubmit=False
    if request.method=='POST':
        form=CommentsForm(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)#as of now form object contails only data submitted by end user like name email,comment
            new_comment.post=post#in db we shd also save ti which post these comments are submitted
            new_comment.save()#saving comments along with post
            csubmit=True
            return HttpResponseRedirect('/post')

    else:
        form=CommentsForm()
    return render(request,'blogapp/comments.html',{'post':post,'form':form,'csubmit':csubmit,'comments':comments})







# Create your views here.
