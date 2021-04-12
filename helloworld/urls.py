# helloworld/urls.py

#code to start virtual environment in windows 
#C:\Users\susri\Documents\django\env\Scripts\activate

from django.urls import path

# from our views.py import the class definition 
# that will connect our url to our html
from .views import HomePageView 

urlpatterns = [
    # map the URL empty string, 
    # to the class HomePageView, 
    # with name to be used within code

    path('', HomePageView.as_view(), name = 'home'), 
    #DONT FORGET THE TRAILING COMMA 

]