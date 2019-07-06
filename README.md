### django
---
https://www.djangoproject.com/

```py
class Band(models.Model):
  """ """
  name = models.CharField(max_length=200)
  can_rock = models.BooleanField(default=True)
  
class Member(models.Model):
  """ """
  name = models.CharField()
  instrument = models.CharField(choices=(
    ('g', "Guitar"),
    ('b', "Bass"),
    ('d', "Drums"),
  ),
  max_length=1
)
bnad = models.ForeignKey("Band")


from django.urls import path

form . import views

urlpatterns = [
  path('bands/', views.band_listing, name='band-list'),
  path('bands/<int:band_id>/', views.band_detail, name='band-detail'),
  path('bands/search/', views.band_search, name=''),
]

from django.shortcuts import render

def band_listing(request):
  """ """
  bands = models.Band.objects.all()
  return render(request, 'bands/band_listing.html', {'bands': bands})


```

```
```

```
```

