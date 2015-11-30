# -*- coding: utf-8 -*-
from django.shortcuts import render
from .forms import GridForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .tasks import grid_calculate
import json

@csrf_exempt  
def grid(request):
    if request.method == 'POST':
        form = GridForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            total_money = float(cd.get('total_money'))
            start_price = float(cd.get('start_price'))
            stop_price = float(cd.get('stop_price'))
            interval = float(cd.get('interval'))
            increment = float(cd.get('increment'))
            return grid_calculate(total_money, start_price, stop_price, interval, increment)
    else:
        form = GridForm()
        return render(request, 'grid/grid.html', {'form': form}) 


