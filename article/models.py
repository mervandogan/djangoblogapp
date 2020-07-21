from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Article(models.Model):
    author = models.name = models.ForeignKey("auth.User",on_delete =models.CASCADE ,verbose_name="Yazar")      # BAŞKA Bir tabloyu referans aldık(auth.User).   Burdaki userimiz silinirse burdaki usere özgü bütün veriler silinmiş olucak. 
    title=models.name = models.CharField(max_length=50,verbose_name="Başlık")  #verbase_name= türkçe yazmak için yazıyoruz hepsinin sonuna
    content=RichTextField()      # content= models.TextField(verbose_name="İçerik")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    article_image=models.FileField(blank=True, null=True,verbose_name="Makaleye Fotğraf Ekleyin") #makalelerimize foto eklemek için bu makalemiz hem fotolu olabilir hemde fotosuz.

    def __str__(self):
        return self.title        #makale başlığını anasayfada (articlesde)gösterir.
    class Meta:
       ordering = ['-created_date']       #En son eklenen makalemiz ilk eklenecek
class Comment(models.Model):
    article= models.ForeignKey(Article,on_delete= models.CASCADE,verbose_name="Makale",related_name="comments")
    comment_author=models.CharField(max_length=50,verbose_name="isim")
    comment_content=models.CharField(max_length=200,verbose_name="yorum")
    comment_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date'] 
        
       
      