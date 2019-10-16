'''自定义内容管理site'''
from django.contrib.admin import AdminSite

class CustomSite(AdminSite):
    '''定义内容管理'''
    site_header = 'Typeidea'
    site_title = 'Typeidea管理后台'
    index_title = '首页'

custom_site = CustomSite(name='cus_admin')
