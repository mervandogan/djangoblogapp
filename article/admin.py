from django.contrib import admin

from .models import Article,Comment


# Register your models here.

#admin.site.register(Article)   #Admin panelimize article 'i kaydetmiş olduk.
admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=["title","author","created_date"]            #yazarı ve tarihi bizim articlede baita gösteriyor title ile birlikte   

    list_display_links = ["title","author","created_date"]             #Başlık Dışında Yazar ve Tarihe Bastığımız zaman da linke basmış gibi içeriğini  görebiliriz

    #ARAMA ÖZELLİĞİ KOYUYORUZ
    search_fields =["title"]              #arama özelliğini  title (başlık ile) yapmış olduk.
    #SOL TARAFTA TARİH FİLTRESİ KOYDUK
    list_filter=["created_date"]

    class Meta:                                             #djangonun komutları .İsmi hep Meta olucak
        model=Article                            #articleAdmin clası ile article birleşmiş oldu
