from django.urls import path
from . import views

urlpatterns = [

    path('', views.index_general_docs, name='general_docs'),
    path('<int:pk>', views.GeneralDocsDetailView.as_view(), name='general_docs_detail'),
]
