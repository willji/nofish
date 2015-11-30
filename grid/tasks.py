# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.shortcuts import render
from .forms import GridForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from celery import shared_task

@shared_task
def grid_calculate(total_money,start_price,stop_price,interval,increment):
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
