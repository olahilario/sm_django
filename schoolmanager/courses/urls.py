from django.urls import path
from .views import CourseDetailView

urlpatterns = [
    path('', CourseDetailView.as_view(), name='course_list_create'),  # Handles GET (list) and POST (create)
    path('<int:course_id>', CourseDetailView.as_view(), name='course_detail_update'),  # Handles GET (detail) and PUT (update)
]
