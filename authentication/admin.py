from django.contrib import admin
from tender.models import Tender
# Register your models here.

class TenderAdmin(admin.ModelAdmin):
    list_display=('Hospital','Tender_number','Product','Location','Tender_Won_By','Winning_Price','Date','Active')
    search_fields=('Hospital','Tender_number','Product','Location','Tender_Won_By','Winning_Price','Date','Active')
    list_filter=('Active',)

admin.site.register(Tender, TenderAdmin)