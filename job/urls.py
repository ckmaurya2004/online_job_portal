from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index, name="home"),
    path('admin_login/',views.admin_Login,name="AdminLogin"),
    path('admin_home/',views.admin_home,name="AdminHome"),
    path('user_login/',views.user_Login,name="UserLogin"),
    path('user_home/',views.user_home,name="UserHome"), 
    path('change_pass_admin/',views.change_pass_admin,name = "change_pass_admin"), 
    path('change_pass_user/',views.change_pass_user,name = "change_pass_user"), 
    path('change_pass_recruiter/',views.change_pass_recruiter,name = "change_pass_recruiter"), 
    path('user_view/',views.user_view,name="UserViews"),
    path('user_delete/<int:myid>',views.user_delete,name="UserDelete"),
    path('user_signup/',views.user_signup,name="UserSignup"),
    path('recruiter_login/',views.recruiter_Login,name="RecruiterLogin"),
    path('recruiter_home/',views.recruiter_home,name="RecruiterHomes"),
    path('recruiter_delete/<int:myid>',views.recruiter_delete,name="RecruiterDelete"),
    path('recruiter_pending/',views.recruiter_pending,name="RecruiterPending"),
    path('recruiter_accepted/',views.recruiter_accepted,name="RecruiterAccepted"),
    path('recruiter_rejected/',views.recruiter_rejected,name="RecruiterRejected"),
    path('recruiter_allview/',views.recruiter_allview,name="RecruiterAllView"),
    path('change_status/<int:myid>',views.change_status,name="ChangeStatus"),
    path('recruiter_signup/',views.recruiter_signup,name="RecruiterSignups"),
    path('edit_jobdetail/<int:myid>',views.edit_jobdetail,name="EditJobdetail"),
    path('change_logo/<int:myid>',views.change_logo,name="ChangeLogo"),
    path('logout/',views.user_logout,name="UserLogout"),
    path('logout/',views.recuriter_logout,name="RecuriterLogout"),
    path('add_job/',views.add_job,name="add_job"),
    path('job_list/',views.job_list,name="job_list"),
    path('contact/',views.contact,name="Contact"),
    path('latest_jobs/',views.latest_job,name="LatestJobs"),
    path('user_latest_jobs/',views.user_latest_job,name="UserLatestJobs"),
    path('user_detail/<int:myid>',views.user_detail,name="UserDeatil"),
    path('apply_for_job/<int:myid>',views.applyforjob,name="ApplyForJob"),
    path('applied_condidate_list/',views.applied_condidate_list,name="ApplyCondidateList"),





]