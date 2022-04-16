from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Technologies, Article
# Create your views here.


class LessonList(ListView):
    model = Technologies
    template_name = 'lesson/index.html'


class CourseList(ListView):
    model = Article
    template_name = 'lesson/corse_list.html'
    context_object_name = 'articles'

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        queryset = queryset.filter(technology=self.kwargs['pk'])
        print(queryset)
        return queryset

class ArticleDetail(DetailView):
    model = Article
    template_name = 'lesson/article_detail.html'