from rest_framework import serializers
from .models import Post,Category
from accounts.models import Profile

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class BlogSerializer(serializers.ModelSerializer):
    snippet_text = serializers.ReadOnlyField(source='snippet')
    absolute_url = serializers.SerializerMethodField(method_name='get_abs_url')
    class Meta:
        model = Post
        fields = ['id','image','title','content','snippet_text','category','author','created_date','absolute_url']
        read_only_fields = ['author']
    
    def to_representation(self, instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('snippet_text', None)
            rep.pop('absolute_url', None)
        else:
            rep.pop('content', None)
        rep['category'] = CategorySerializer(instance.category).data # .get('name')
        return rep

    def create(self, validated_data):
        validated_data['author']=Profile.objects.get(user__id=self.context.get('request').user.id)
        print(validated_data['author'])
        return super().create(validated_data)
    
    def get_abs_url(self,obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)