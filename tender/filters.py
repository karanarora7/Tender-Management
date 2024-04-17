import django_filters
from django_filters import DateFilter,CharFilter
from django import forms

from .models import *

class TenderFilters(django_filters.FilterSet):
    start_date=DateFilter(field_name="Date", lookup_expr='gte',
  widget=forms.TextInput(
    attrs={
      "class":"form-control text-black text-center",
      "max_length":"100"
    }
  ))
    end_date=DateFilter(field_name="Date", lookup_expr='lte',
  widget=forms.TextInput(
    attrs={
      "class":"form-control text-black text-center",
      "max_length":"100"
    }
  ))
    Remarks=CharFilter(field_name='Remarks',lookup_expr='icontains',
  widget=forms.TextInput(
    attrs={
      "class":"form-control text-black text-center",
      "max_length":"100"
    }
  ))
    Location=CharFilter(field_name='Location',lookup_expr='icontains',
  widget=forms.TextInput(
    attrs={
      "class":"form-control text-black text-center",
      "max_length":"100"
    }
  ))
    Hospital=CharFilter(field_name='Hospital',lookup_expr='icontains',
  widget=forms.TextInput(
    attrs={
      "class":"form-control text-black text-center",
      "max_length":"100"
    }
  ))
    Tender_number=CharFilter(field_name='Tender_number',lookup_expr='icontains',
  widget=forms.TextInput(
    attrs={
      "class":"form-control text-black text-center",
      "max_length":"100"
    }
  ))
    Product=CharFilter(field_name='Product',lookup_expr='icontains',
  widget=forms.TextInput(
    attrs={
      "class":"form-control text-black text-center",
      "max_length":"100"
    }
  ))
    Tender_Won_By=CharFilter(field_name='Tender_Won_By',lookup_expr='icontains',
  widget=forms.TextInput(
    attrs={
      "class":"form-control text-black text-center",
      "max_length":"100"
    }
  ))
    Winning_Price=CharFilter(field_name='Winning_Price',lookup_expr='icontains',
  widget=forms.TextInput(
    attrs={
      "class":"form-control text-black text-center",
      "max_length":"100"
    }
  ))
    class Meta:
        model = Tender
        fields='__all__'
        exclude=['Date','Location','Hospital','Tender_number','Product','Tender_Won_By','Winning_Price']