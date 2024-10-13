from django.urls import path
from .views import *


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('', MovieListViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_list'),
    path('<int:pk>/', MovieDetailViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                              'delete': 'destroy'}), name='product_detail'),



    path('profile/', ProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='user_list'),
    path('profile/<int:pk>/', ProfileViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                        'delete': 'destroy'}), name='user_detail'),



    path('country/', CountryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category_list'),
    path('country/<int:pk>/', CountryViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                    'delete': 'destroy'}), name='category detail'),



    path('director/', DirectorListViewSet.as_view({'get': 'list', 'post': 'create'}), name='rating_list'),
    path('director/<int:pk>/', DirectorDetailViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                   'delete': 'destroy'}), name='rating_detail'),


    path('actor/', ActorListViewSet.as_view({'get': 'list', 'post': 'create'}), name='review_list'),
    path('actor/<int:pk>/', ActorDetailViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                    'delete': 'destroy'}), name='review_detail'),

    path('janre/', JanreListViewSet.as_view({'get': 'list', 'post': 'create'}), name='review_list'),
    path('janre/<int:pk>/', JanreDetailViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                   'delete': 'destroy'}), name='review_detail'),

    path('movie_photos/', MoviePhotosViewSet.as_view({'get': 'list', 'post': 'create'}), name='review_list'),
    path('movie_photos/<int:pk>/', MoviePhotosViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                        'delete': 'destroy'}), name='review_detail'),

    path('languages/', MovieLanguagesViewSet.as_view({'get': 'list', 'post': 'create'}), name='review_list'),
    path('languages/<int:pk>/', MovieLanguagesViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                   'delete': 'destroy'}), name='review_detail'),

    path('moments/', MomentsViewSet.as_view({'get': 'list', 'post': 'create'}), name='review_list'),
    path('moments/<int:pk>/', MomentsViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                            'delete': 'destroy'}), name='review_detail'),

    path('rating/', RatingViewSet.as_view({'get': 'list', 'post': 'create'}), name='review_list'),
    path('rating/<int:pk>/', RatingViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                     'delete': 'destroy'}), name='review_detail'),

    path('favorite/', FavoriteViewSet.as_view({'get': 'list', 'post': 'create'}), name='review_list'),
    path('favorite/<int:pk>/', FavoriteViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                     'delete': 'destroy'}), name='review_detail'),

    path('favorite_movie/', FavoriteMovieViewSet.as_view({'get': 'list', 'post': 'create'}), name='review_list'),
    path('favorite_movie/<int:pk>/', FavoriteMovieViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                      'delete': 'destroy'}), name='review_detail'),

    path('history/', HistoryListViewSet.as_view({'get': 'list', 'post': 'create'}), name='review_list'),
    path('history/<int:pk>/', HistoryDetailViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                      'delete': 'destroy'}), name='review_detail'),
    ]
