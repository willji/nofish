# -*- coding: utf-8 -*-
from django.shortcuts import render
from .forms import GridForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt  
def Grid(request):
    if request.method == 'POST':
        form = GridForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            total_money = float(cd.get('total_money'))
            start_price = float(cd.get('start_price'))
            stop_price = float(cd.get('stop_price'))
            interval = float(cd.get('interval'))
            increment = float(cd.get('increment'))
        #模板变量，买入金额、买入价格、买入资金、买入股数、买入手数
        content = []
        #买入次数
        times = int((start_price-stop_price) / interval + 1)
        #总的增量资金数
        total_increment = 0
        for i in range(times):
            total_increment = total_increment + increment * i
        #第一次投入资金数
        money = (total_money-total_increment) / times
        #价格
        price = start_price
        for i in range(times):
            #买入资金
            money = int(money+increment)
            #买入股数
            stock_num = int(money/price)
            #买入手数
            hand_num = stock_num / 100 
            content.append([price, money, stock_num, hand_num])
            #买入价格
            price = price - interval
        return HttpResponse(json.dumps(content))
    else:
        form = GridForm()
        return render(request, 'grid/grid.html', {'form': form}) 
