from django.urls import path, include
from django.contrib import admin

admin.autodiscover()

from . import views

app_name = 'names'

urlpatterns = [

    path('', views.index, name='index'),

    path('similar/<str:name_year_list_input>/<int:target_year_input>/<str:sex_input>/<int:number_of_names>', views.list_of_names_with_similar_distribution_NYSX, name="list_of_names_with_similar_distribution"),
    path('similar/<str:name_year_list_input>/<int:target_year_input>/<str:sex_input>', views.list_of_names_with_similar_distribution_NYS, name="list_of_names_with_similar_distribution"),
    path('similar/<str:name_year_list_input>/<int:target_year_input>/<int:number_of_names>', views.list_of_names_with_similar_distribution_NYX, name="list_of_names_with_similar_distribution"),
    path('similar/<str:name_year_list_input>/<int:target_year_input>', views.list_of_names_with_similar_distribution_NY, name="list_of_names_with_similar_distribution"),
    path('similar/<str:name_year_list_input>/<str:sex_input>/<int:number_of_names>', views.list_of_names_with_similar_distribution_NSX, name="list_of_names_with_similar_distribution"),
    path('similar/<str:name_year_list_input>/<str:sex_input>', views.list_of_names_with_similar_distribution_NS, name="list_of_names_with_similar_distribution"),
    path('similar/<str:name_year_list_input>/<int:number_of_names>', views.list_of_names_with_similar_distribution_NX, name="list_of_names_with_similar_distribution"),
    path('similar/<str:name_year_list_input>', views.list_of_names_with_similar_distribution_N, name="list_of_names_with_similar_distribution"),

    path('compmap/<str:state_input>/<int:year_input>/<int:number_of_names>', views.map_comparing_states_from_state_SYX, name="map-comparing-states-from-one-state"),
    path('compmap/<str:state_input>/<int:year_input>', views.map_comparing_states_from_state_SY, name="map-comparing-states-from-one-state"),
    # path('compmap/<str:state_input>/<int:number_of_names>', names.views.map_comparing_states_from_state_SX, name="map-comparing-states-from-one-state"),
    path('compmap/<str:state_input>', views.map_comparing_states_from_state_S, name="map-comparing-states-from-one-state"),

    path('complist/<int:year_input>/<int:number_of_names_to_use>', views.list_comparing_states_from_one_year_YX, name="list-comparing-states-from-one-year"),
    path('complist/<int:year_input>', views.list_comparing_states_from_one_year_Y, name="list-comparing-states-from-one-year"),

    path('state/<str:state_input>/<int:year_input>', views.list_from_one_state_and_year_SY, name="list-from-one-state-and-year"),
    path('state/<str:state_input>', views.list_from_one_state_and_year_S, name="list-from-one-state-and-year"),

    path('<int:year_input>/<str:sex_input>/<int:number_of_results>', views.map_most_popular_names_YSX, name="map_most_popular_names"),
    path('<int:year_input>/<int:number_of_results>', views.map_most_popular_names_YX, name="map_most_popular_names"),
    path('<int:year_input>/<str:sex_input>', views.map_most_popular_names_YS, name="map_most_popular_names"),
    path('<int:year_input>', views.map_most_popular_names_Y, name="map_most_popular_names"),

    path('<str:name_input>/<int:year_start_input>/<int:year_end_input>/<str:sex_input>', views.map_from_one_name_NYYS, name="map-from-one-name"),
    # path('<str:name_input>/<int:year_start_input>/<int:year_end_input>', names.views.map_from_one_name_NYY, name="map-from-one-name"),
    # path('<str:name_input>/<int:year_start_input>/<str:sex_input>', names.views.map_from_one_name_NYS, name="map-from-one-name"),
    # path('<str:name_input>/<int:year_start_input>', names.views.map_from_one_name_NY, name="map-from-one-name"),
    # path('<str:name_input>/<str:sex_input>', names.views.map_from_one_name_NS, name="map-from-one-name"),
    # path('<str:name_input>', names.views.map_from_one_name_N, name="map-from-one-name"),
    path('', views.map_from_one_name_NYYS, name="map-from-one-name"),

    path('test/', views.test, name='test'),
]
