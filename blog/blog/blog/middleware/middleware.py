from django.utils.deprecation import MiddlewareMixin


class XxxMiddleware(MiddlewareMixin):
    """自定义中间件"""
    pass

    # def process_view(self, request, view_func, *args, **kwargs):
    #     try:
    #         abt = AboutMeModel.objects.order_by('-id').first()
    #     except:
    #         pass
    #     print("****************************************")



