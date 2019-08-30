from django.urls import path
from .views import (main, client_created_form, form_u,
    form_f, fop_create, legal_person_create)

urlpatterns = [
    path('', main),
    path('client_created_form/', client_created_form, name='client_created_form' ),
    path('form_u/', form_u, name='form_u' ),
    path('form_f/', form_f, name='form_f' ),
    path('fop_create/', fop_create, name='fop_create' ),
    path('legal_person_create/', legal_person_create, name='legal_person_create' ),


]