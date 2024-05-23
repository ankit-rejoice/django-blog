from rest_framework import serializers
from ..models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        exclude = ()


class CreateBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        exclude = ()
