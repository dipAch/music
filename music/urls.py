from django.urls import include, path
from rest_framework import routers
from mutecloud import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'songs', views.SongViewSet)
router.register(r'albums', views.AlbumViewSet)
router.register(r'genres', views.GenreViewSet)
router.register(r'playlists', views.PlaylistViewSet)
router.register(r'recommendations', views.RecommendationViewSet)
router.register(r'artists', views.ArtistViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
