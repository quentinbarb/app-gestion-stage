from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gestionStage.views.home', name='home'),
    # url(r'^gestionStage/', include('gestionStage.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
   
    url(r'^/?$',"entreprise.views.show_entreprise"),

    url(r'^add/$',"entreprise.views.addEnt"),
    
    url(r'^(\d+)$',"entreprise.views.show_detail_entreprise"),

    url(r'^delete/(\d+)$',"entreprise.views.delEnt"),

    url(r'^modif/(\d+)$',"entreprise.views.modifEnt"),

)
