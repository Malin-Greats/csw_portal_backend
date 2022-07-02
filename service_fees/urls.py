from django.urls import path
from . import views
from .views import ApplicationSizeUpdate, InteriorColorUpdate, PaperTypeUpdate, BindingOptionUpdate, CoverFinishUpdate, PageUpdate, ApplicationSizeUpdate

urlpatterns = [


    path('interior_colors_list', views.interior_colors_list,
         name='interior_colors_list'),
    path('paper_type_list', views.paper_type_list,
         name='paper_type_list'),
    path('binding_options_list', views.binding_options_list,
         name='binding_options_list'),
    path('cover_finish_list', views.cover_finish_list,
         name='cover_finish_list'),
    path('pages_list', views.pages_list,
         name='pages_list'),
    path('application_size_list', views.application_size_list,
         name='application_size_list'),


    path('interior_color_update/<str:pk>',
         InteriorColorUpdate.as_view(), name='interior_color_update'),
    path('paper_type_update/<str:pk>',
         PaperTypeUpdate.as_view(), name='paper_type_update'),
    path('binding_options_update/<str:pk>',
         BindingOptionUpdate.as_view(), name='binding_options_update'),
    path('cover_finish_update/<str:pk>',
         CoverFinishUpdate.as_view(), name='cover_finish_update'),
    path('page_update/<str:pk>',
         PageUpdate.as_view(), name='page_update'),
    path('application_size_update/<str:pk>',
         ApplicationSizeUpdate.as_view(), name='application_size_update')


]
