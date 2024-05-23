from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import BlogSerializer, CreateBlogSerializer
from ..models import Blog


class BlogListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwrds):
        page = int(request.query_params.get('page', 1))
        _from = (page-1)*10
        _to = page*10
        blogs = Blog.objects.all()[_from:_to]
        data = BlogSerializer(blogs, many=True).data
        if len(data) == 0:
            return Response({
                "message": "no records found"
            })
        return Response(data)

    def post(self, request, *args, **kwrds):
        serializer = CreateBlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['auther'] = request.user
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class BlogRetriveUpdateDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, *args, **kwrds):
        blog = Blog.objects.filter(id=pk).first()
        if blog:
            data = BlogSerializer(blog).data
            return Response(data)
        return Response({
            "message": "records not found",
        }, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, *args, **kwrds):

        blog = Blog.objects.filter(id=pk).first()
        if blog:
            if blog.auther == request.user:
                serializer = BlogSerializer(blog, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors)
            return Response({
                "message": "You are not allowed to edit this blog",
            }, status=status.HTTP_404_NOT_FOUND)
        return Response({
            "message": "records not found",
        }, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, *args, **kwrds):
        blog = Blog.objects.filter(id=pk).first()
        if blog:
            if blog.auther == request.user:
                blog.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response({
                "message": "You are not allowed to delete this blog",
            }, status=status.HTTP_404_NOT_FOUND)
        return Response({
            "message": "records not found",
        }, status=status.HTTP_404_NOT_FOUND)
