from django.shortcuts import render, reverse, redirect
from django.views import View
from apps.fun_time_app.models import *
from django.core.paginator import Paginator  # 分页
from django.conf import settings
from utils.check_page_number import check_page_number
import markdown


class DzView(View):
    """段子"""
    def get(self, request):
        # 1、查询全部
        dz = DzModel.objects.order_by('-id')
        if dz:
            for i in dz:
                i.content = markdown.markdown(i.content)  # 转换为HTML

        # 2、产生分页器
        paginator = Paginator(dz, settings.NUM_PAGES)  # 每页显示条数
        p = request.GET.get('page', 1)   # 获取页码
        page = check_page_number(page=p, paginator=paginator)  # 校验页码
        pager = paginator.get_page(page)  # 请求的页

        # 3、返回
        return render(request, 'fun_time_app/dz.html', locals())

    # 搜索框提交post请求
    def post(self, request):
        pass








