from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .serializers import PostSerializers
from blog.models import Post
from django.shortcuts import get_object_or_404

@api_view(['GET','POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def PostApi(request):
    if request.method == 'GET':
        post = Post.objects.all()
        serializer = PostSerializers(post,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def PostDetailApi(request,id):
    post = get_object_or_404(Post,pk=id)
    if request.method == 'GET':
        serializer = PostSerializers(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PostSerializers(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        post.delete()
        return Response({'details':'object successfully removed'})