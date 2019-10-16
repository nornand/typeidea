'''自定义基类'''
from django.contrib import admin

class BaseOwnerAdmin(admin.ModelAdmin):
    """
    1.自动补充Model的owner字段
    2.针对query_set过滤当前用户
    """
    exclude = ('owner',)

    def get_queryset(self, request):
        qs = super(BaseOwnerAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(BaseOwnerAdmin, self).save_model(request, obj, form, change)
