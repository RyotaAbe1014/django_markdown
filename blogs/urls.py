from django.urls import path
from .views import LessonList, CourseList, ArticleDetail

app_name = "blogs"

urlpatterns = [
    path('lesson/index', LessonList.as_view(), name="lesson_list"),
    path('courses/<int:pk>', CourseList.as_view(), name="course_list"),
    path('article/<int:pk>', ArticleDetail.as_view(), name="article_detail"),
]

