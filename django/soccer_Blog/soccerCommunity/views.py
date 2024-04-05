from django.shortcuts import render, get_object_or_404, redirect
from .models import community
from django.utils import timezone

# Create your views here.
def articleNum(articles) :

    count = 0
    for article in articles:
        count += 1
    return count
    

def home(request):

    articles = community.objects.all()
    NumOfArticle = articleNum(articles)
    return render(request, "home.html", {'articles':articles, 'NumOfArticle':NumOfArticle})



def detail(request, id):
    article = get_object_or_404(community, pk=id)
                                
    return render(request, "detail.html", {'article':article})

def new(request):
    return render(request, 'new.html')


def create(request):

    new_article = community()
    new_article.title = request.POST['title']
    new_article.writer = request.POST['writer']
    new_article.body = request.POST['body']
    new_article.pub_date = timezone.now()
    new_article.save()

    return redirect('detail', new_article.id)


    
