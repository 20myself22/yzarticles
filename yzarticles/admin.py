from django.contrib import admin
from yzarticles.models import Book,Entry

# 在这里注册你的模型
admin.site.register(Book)
admin.site.register(Entry)