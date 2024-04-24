from rest_framework import serializers
from blog.models import Post

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','author','title','content','status','category','created_date']