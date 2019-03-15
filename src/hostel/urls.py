from django.conf.urls import url


from .views import hostelLandingPage

app_name="hostel"

urlpatterns = [
    url(r'^$',hostelLandingPage,name="hostelHome"),

]