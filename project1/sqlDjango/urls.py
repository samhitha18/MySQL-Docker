from django.urls import path
from . import views
urlpatterns=[path("sqlData/",views.sqlData,name="sqlData"),
path("student/display",views.display,name="display"),]