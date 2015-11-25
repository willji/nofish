# -*- coding: utf-8 -*-
from django import forms

class GridForm(forms.Form):
    total_money = forms.CharField(max_length=20, label='总金额')
    start_price = forms.CharField(max_length=20, label='起始价格')
    stop_price = forms.CharField(max_length=20, label='结束价格')
    interval = forms.CharField(max_length=20, label='价格间隔')
    increment = forms.CharField(max_length=20, label='金额递增')


