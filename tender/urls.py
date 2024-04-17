from django.contrib import admin
from django.urls import path,include
from authentication.views import User
from .views import *

urlpatterns = [
    path('', ListOfTenders,name='home'),
    path('add-tenders',AddTenders,name='add_tender'),
    path('delete-tender/<int:tender_number>',delete_tender),
    path('update-tender/<int:tender_number>',update_tender),
    path('do-update-tender/<int:tender_number>',do_update_tender),
]
