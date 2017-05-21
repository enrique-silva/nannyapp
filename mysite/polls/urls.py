from django.conf.urls import url

from . import views

app_name = 'users'

urlpatterns = [
    # ex: localhost:8000
    url(r'^$', views.home_page, name='index'),

    # # ex: /polls/5/
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    # /localhost:8000/login to login the user
    url(r'^login/$', views.login_view, name='login'),

    # /localhost:8000/logout to logout the user
    url(r'^logout/$', views.logout_view, name='logout'),

    # /localhost:8000/logout to logout the user
    url(r'^register/$', views.register_view, name='register'),
    #
    # # /localhost:8000/signup to sign the user in
    # url(r'^signup/$', views.signup, name='signup'),

    # /localhost:8000/signup to sign the user in
    url(r'^employer_add/$', views.employer_add_view, name='employer_add'),

    # /localhost:8000/signup to sign the user in
    url(r'^expense_add/$', views.expense_add, name='expense_add'),

    # /localhost:8000/home_page_user where a user can manager their profile
    url(r'^home_page/$', views.home_page, name='homepage_page'),

    # /localhost:8000/home_page_user where a user can manager their profile
    url(r'^home_page_user/$', views.home_page_user, name='homepage_page_user'),

    # /users/showdata:url to display the list of users stored on the database
    url(r'^showdata/$', views.showdata, name='showdata'),

]
