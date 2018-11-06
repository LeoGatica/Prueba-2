from django.conf.urls import include, url
from . import views


urlpatterns = [
    
    url(r'^$', views.Principal, name='Principal'),
    url(r'^formulario/$', views.formulario, name='formulario'),
    url(r'^contactanos/$', views.contactanos, name='contactanos'),
    url(r'^servicios/$', views.servicios, name='servicios'),
    url(r'^somos/$', views.somos, name='somos'),
    url(r'^adopcion/$', views.adopcion, name='adopcion'),

    url(r'^adopcion/Principal$', views.Principal, ),
    url(r'^adopcion/adopcion$', views.adopcion, ),
    url(r'^adopcion/contactanos$', views.contactanos, ),
    url(r'^adopcion/servicios$', views.servicios, ),
    url(r'^adopcion/somos$', views.somos, ),
    url(r'^adopcion/Principal.html$', views.Principal, ),
    url(r'^adopcion/adopcion.html$', views.adopcion, ),
    url(r'^adopcion/contactanos.html$', views.contactanos, ),
    url(r'^adopcion/servicios.html$', views.servicios, ),
    url(r'^adopcion/somos.html$', views.somos, ),
    url(r'^adopcion/formulario.html$', views.formulario, ),
    url(r'^adopcion/formulario$', views.formulario, ),
    



    url(r'^somos/Principal$', views.Principal, ),
	url(r'^somos/adopcion$', views.Principal, ),
    url(r'^somos/somos$', views.somos, ),
    url(r'^somos/servicios$', views.servicios, ),
    url(r'^somos/contactanos$', views.contactanos, ),
    url(r'^somos/Principal.html$', views.Principal, ),
    url(r'^somos/contactanos.html$', views.contactanos, ),
    url(r'^somos/servicios.html$', views.servicios, ),
    url(r'^somos/somos.html$', views.somos, ),
	url(r'^somos/adopcion.html$', views.Principal, ),
	

    url(r'^servicios/Principal$', views.Principal, ),
	url(r'^servicios/adopcion$', views.Principal, ),
    url(r'^servicios/contactanos$', views.contactanos, ),
    url(r'^servicios/servicios$', views.servicios, ),
    url(r'^servicios/somos$', views.somos, ),
    url(r'^servicios/Principal.html$', views.Principal, ),
    url(r'^servicios/contactanos.html$', views.contactanos, ),
    url(r'^servicios/servicios.html$', views.servicios, ),
    url(r'^servicios/somos.html$', views.somos, ),
	url(r'^servicios/adopcion.html$', views.Principal, ),


    url(r'^contactanos/Principal$', views.Principal, ),
	url(r'^contactanos/adopcion$', views.Principal, ),
    url(r'^contactanos/contactanos$', views.contactanos, ),
    url(r'^contactanos/servicios$', views.servicios, ),
    url(r'^contactanos/somos$', views.somos, ),
    url(r'^contactanos/Principal.html$', views.Principal, ),
    url(r'^contactanos/contactanos.html$', views.contactanos, ),
    url(r'^contactanos/servicios.html$', views.servicios, ),
    url(r'^contactanos/somos.html$', views.somos, ),
	url(r'^contactanos/adopcion.html$', views.Principal, ),


    
    
    
]



