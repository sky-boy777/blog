from django.utils.deprecation import MiddlewareMixin
from blog_app.models import AboutMeModel


class MyMiddleware(MiddlewareMixin):
    """自定义中间件"""
    pass

    # def process_view(self, request, view_func, *args, **kwargs):
    #     try:
    #         abt = AboutMeModel.objects.order_by('-id').first()
    #     except:
    #         pass
    #     print("****************************************")



