from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import ArticleForm
from .models import Article,Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.        #url den gelen çalışacak kodları (fonksiyonları buraya yazarız.)

#MAKALE SAYFASI TASARIMI
def articles(request):
    keyword=request.GET.get("keyword")

    if keyword:
        articles=Article.objects.filter(title__contains =keyword)
        return render(request,"articles.html",{"articles":articles})
        
    articles=Article.objects.all()   #tüm artikıllarımızı alır ve bir tane listeye atar

    return render(request,"articles.html",{"articles":articles})
#ANASAYFA
def index(request):
    #return HttpResponse("<h3>Anasayfa</h3>")

    return render(request,"index.html",)        #{"number":7})

#HAKKIMIZDA
def about(request):
    return render(request,"about.html")

@login_required(login_url="user:login")       #ismi login olan url ye git

#MAKALELERİM
def dashboard(request):
    articles= Article.objects.filter(author=request.user)  #şuanda sisteme kim giriş yapmışsa onun makalelerini almış oluyoruz
    context={
        "articles":articles
    }

    return render(request,"dashboard.html",context)
@login_required(login_url="user:login") 
#MAKALE OLUŞTURMA
def addArticle(request):
    form=ArticleForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        article=form.save(commit =False)
        article.author=request.user
        article.save()
        messages.success(request,"Makale Başarıyla Oluşturuldu.")
        return redirect("index")

    return render(request,"addarticle.html",{"form":form})


#def detail(request,id):
    
    # return HttpResponse("Detail:"+ str(id))



#MAKALE DETAY SAYFASI OLUŞTURMA
@login_required(login_url="user:login") 
def detail(request,id):
    #article=Article.objects.filter(id=id).first()      #gördğün ilk articleyi dön (.first())
    article=get_object_or_404(Article,id=id)

    comments = article.comments.all()
    return render(request,"detail.html",{"article":article,"comments":comments})
@login_required(login_url="user:login") 

#MAKALE GÜNCELLEME
def updateArticle(request,id):
    article= get_object_or_404(Article,id=id)
    form=ArticleForm(request.POST or None,request.FILES or None, instance=article)
    if form.is_valid():
        article=form.save(commit =False)
        article.author=request.user
        article.save()
        messages.success(request,"Makale Başarıyla Güncellendi")
        return redirect("article:dashboard")

    return render(request,"update.html",{"form":form})
@login_required(login_url="user:login") 
#MAKALE SİLME
def deleteArticle(request,id):
    artcle=get_object_or_404(Article,id=id)
    artcle.delete()
    messages.success(request,"Makale Başarıyla Silindi")

    return redirect("article:dashboard")
#Yorum KISMI
def addComment(request,id):
    article=get_object_or_404(Article,id=id)

    if request.method =="POST":
        comment_author=request.POST.get("comment_author")
        comment_content=request.POST.get("comment_content")

        newComment = Comment(comment_author=comment_author,comment_content=comment_content)

        newComment.article=article

        newComment.save()
    return redirect(reverse("article:detail",kwargs={"id":id}))      #/articles/detail/15 haline getirmiş oldu dinamik url yaparken reverse fonksiyonunu kullanmalıyız
