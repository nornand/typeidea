'''blog model定义'''
from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除')
    )

    name = models.CharField(max_length=50, verbose_name='名称')
    status = models.PositiveIntegerField(default=STATUS_NORMAL,
                                         choices=STATUS_ITEMS, verbose_name='状态')
    is_nav = models.BooleanField(default=False, verbose_name='是否为导航')
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='作者')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '分类'

    def __str__(self):
        return self.name

class Tag(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除')
    )

    name = models.CharField(max_length=10, verbose_name='名称')
    status = models.PositiveIntegerField(default=STATUS_NORMAL,
                                         choices=STATUS_ITEMS, verbose_name='状态')
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='作者')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '标签'

    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_DRAFT = 2
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
        (STATUS_DRAFT, '草稿')
    )

    title = models.CharField(max_length=255, verbose_name='标题')
    desc = models.CharField(max_length=1024, blank=True, verbose_name='摘要')
    content = models.TextField(verbose_name='正文', help_text='正文必须为Markdown格式')
    status = models.PositiveIntegerField(default=STATUS_NORMAL,
                                         choices=STATUS_ITEMS, verbose_name='状态')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类')
    tag = models.ManyToManyField(Tag)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='作者')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    @staticmethod
    def get_by_tag(tag_id):
        '''根据标签获取文章'''
        post_list = []
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            tag = None
        else:
            post_list = tag.post_set.filter(status=Post.STATUS_NORMAL)\
                .select_related('owner', 'category')

        return post_list, tag

    @staticmethod
    def get_by_category(category_id):
        '''根据种类获取文章'''
        post_list = []
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            category = None
        else:
            post_list = category.post_set.filter(status=Post.STATUS_NORMAL)\
                .select_related('owner', 'category')

        return post_list, category

    class Meta:
        verbose_name = verbose_name_plural = '文章'
        ordering = ['-id']

    def __str__(self):
        return self.title
