from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [

# Shared URLs
path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('services/', views.services, name='services'),
path('contact/', views.contact, name='contact'),
path('lsign/', views.LearnerSignUpView.as_view(), name='lsign'),
path('login_form/', views.login_form, name='login_form'),
path('login/', views.loginView, name='login'),
path('logout/', views.logoutView, name='logout'),


# Admin URLs
path('dashboard/', views.dashboard, name='dashboard'),
path('course/', views.course, name='course'),
path('isign/', views.InstructorSignUpView.as_view(), name='isign'),
path('addlearner/', views.AdminLearner.as_view(), name='addlearner'),
path('apost/', views.AdminCreatePost.as_view(), name='apost'),
path('alpost/', views.AdminListTise.as_view(), name='alpost'),
path('alistalltise/', views.ListAllTise.as_view(), name='alistalltise'),
path('adpost/<int:pk>', views.ADeletePost.as_view(), name='adpost'),
path('aluser/', views.ListUserView.as_view(), name='aluser'),
path('aduser/<int:pk>', views.ADeleteuser.as_view(), name='aduser'),
path('create_user_form/', views.create_user_form, name='create_user_form'),
path('create_user/', views.create_user, name='create_user'),
path('acreate_profile/', views.acreate_profile, name='acreate_profile'),
path('auser_profile/', views.auser_profile, name='auser_profile'),



# Instructor URLs
path('instructor/', views.home_instructor, name='instructor'),
path('ipost/', views.CreatePost.as_view(), name='ipost'),
path('llchat/', views.TiseList.as_view(), name='llchat'),
path('user_profile/', views.user_profile, name='user_profile'),
path('create_profile/', views.create_profile, name='create_profile'),
path('tutorial/', views.tutorial, name='tutorial'),
path('post/',views.publish_tutorial,name='publish_tutorial'),
path('itutorial/',views.itutorial,name='itutorial'),
path('itutorials/<int:pk>/', views.ITutorialDetail.as_view(), name = "itutorial-detail"),
path('listnotes/', views.LNotesList.as_view(), name='lnotes'),
path('iadd_notes/', views.iadd_notes, name='iadd_notes'),
path('publish_notes/', views.publish_notes, name='publish_notes'),
path('update_file/<int:pk>', views.update_file, name='update_file'),




# Student URl's
path('learner/',views.home_learner,name='learner'),
path('ltutorial/',views.ltutorial,name='ltutorial'),
path('llistnotes/', views.LLNotesList.as_view(), name='llnotes'),
path('ilchat/', views.ITiseList.as_view(), name='ilchat'),
path('luser_profile/', views.luser_profile, name='luser_profile'),
path('lcreate_profile/', views.lcreate_profile, name='lcreate_profile'),
path('tutorials/<int:pk>/', views.LTutorialDetail.as_view(), name = "tutorial-detail"),
path('interests/', views.LearnerInterestsView.as_view(), name='interests'),







































 
]
