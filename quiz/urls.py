from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.index ,name='index'),
    path('C/',views.C, name='C'),
    path('Python/',views.Python, name='Python'),
    path('submit_answers/', views.submit_answers, name='submit_answers'),
    path('submit1_answers/', views.submit1_answers, name='submit1_answers'),
    path('submit2_answers/', views.submit2_answers, name='submit2_answers'),
    path('contact/',views.contact, name='contact'),
    path('about/',views.about, name='about'),
    path('prize/',views.prize, name='prize'),
    path('contact/',views.contact, name='contact'),
    path('info/',views.info, name='info'),
    path('Guides/',views.Guides, name='Guides'),
    path('Timings/',views.Timings, name='Timings'),
    path('Outreach/',views.Outreach, name='Outreach'),
    path('Login/',views.Login, name='Login'),
    path('ML/', views.ML, name='ML'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('Login/index.html',views.index ,name='index'),
]