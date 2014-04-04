from django.template import loader, Context 
from django.template import RequestContext
from django.http import HttpResponse
from blog.models import BlogPost
from django.shortcuts import render_to_response

def archive(request):
    posts = BlogPost.objects.all()

    # template = loader.get_template("archive.html")
    context = RequestContext(request)
    context_dict = { 'posts': posts }
    return render_to_response('blog/archive.html', context_dict, context)
