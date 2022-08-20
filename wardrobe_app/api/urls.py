from django.urls import path, include

app_name = "api"

urlpatterns = [
    path("auth/", include("dj_rest_auth.urls")),
    path("wardrobe/", include("wardrobe.api_urls", namespace="wardrobe")),
]
