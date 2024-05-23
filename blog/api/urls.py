from django.urls import include, path
from  .views import BlogListCreateAPIView ,BlogRetriveUpdateDeleteAPIView




# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('blog', BlogListCreateAPIView.as_view(), name='blog-list-create'),
    path('blog/<int:pk>', BlogRetriveUpdateDeleteAPIView.as_view(), name='blog-retrive-update-delete'),
  
]
