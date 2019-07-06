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

from django import froms

class BandContactForm(form.Form):
  subject = forms.CharField(max_length=100)
  message = froms.CharField()
  sender = forms.EmailField()
  cc_myself = froms.BooleanField(required=False)


from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def my_protected_view(request):
  """ """
  return render(request, 'protected.html', {'current_user': request.user})


from django.contrib import admin
from bands.models import Band, Member

class MemberAdmin(admin.ModelAdmin):
  """ """
  list_display = ('name', 'instrument')
  list_filter = ('band',)

admin.site.register(Band)
admin.site.register(Member, MemberAdmin)


from django.shortcuts import render
from django.utils.translation import ugettext

def homepage(request):
  """
  """
  message = ugettext('Welcom to our site!')
  return render(request, 'homepage.html', {'message': message})

```

```
{% load i18n %}
<html>
  <head>
    <title>Band Listing</title>
    <title>{% trans 'Homepage - Hall of Fame' %}</title>
  </head>
  <body>
    {# Translated in the view: #}
    <h1>{{ message }}</h1>
    <p>
      {% blocktrans count member_count=bands.count %}
      Here is the only band in the hall of fame:
      {% plural %}
      Here are all the {{ member_count }} bands in the hall of fame:
      {% endblocktrans %}
    </p>
    <ul>
      {% for band in bands %}
        <li>
          <h2><a href="{{ band.get_absolute_url }}">{{ band.name }}</a></h2>
          {% if band.can_rock %}<p>This band can rock!</p>{% endif %}
        </li>
      {% endfor %}
    </ul>
  </body>
</html>
```

```
```

