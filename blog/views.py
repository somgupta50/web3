from django.shortcuts import render
from .models import Article, Tag, Subscriber
from .forms import SubscribeForm

def blog_list(request):
    # load all blog articles from database
    articles = Article.objects.all().order_by('-created_on')
    # subscribe form
    form = SubscribeForm()
    # handle form submission
    if request.method == 'POST':
        email = request.POST.get('email')
        if len(email) > 0:
            sub = Subscriber(email=email)   # create a new subscriber object
            sub.save()                      # save the subscriber to the database
            print('Subscriber saved')
    # add the form to the context
    ctx = {
        'articles': articles, 
        'form': form
    }
    # render the template
    return render(request, 'blog/list.html', ctx)