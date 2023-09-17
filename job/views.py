from django.shortcuts import render,HttpResponse,redirect
from  django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from . models import Job,Recruiter,Contact,studentuser,Apply
from datetime import date



# Create your views here.

def index(request):
    return render(request,'index.html')

def admin_Login(request):
    msg = ""
    if request.method == 'POST':
        name = request.POST.get('name',"")
        pass1 = request.POST.get('password',"")
        user = authenticate(username  = name, password= pass1)
        try:
            if user.is_staff:
                login(request,user)
                messages.success(request, "logged in successfully.")  
                return redirect('/admin_home') 
            else:
                messages.error(request, " You are not  logged in ")      
        except:
            messages.warning(request, " You are not authenticated user something is wrong ")      
    else:
        messages.error(request, "user is not exits")      
                 
               
    return render(request,'admin_login.html',)



def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('/admin_login')
    recruiter = Recruiter.objects.all().count()
    student = studentuser.objects.all().count()
    #param = {"recruiter":recruiter,"student":student}
    return render(request,'admin_home.html',locals())


def user_Login(request):
    if request.method == 'POST':
        name = request.POST.get('name',"")
        pass1 = request.POST.get('password',"")
        user = authenticate(username  = name, password= pass1)
        if user is not None:
            try:
                user1 = studentuser.objects.get(user = user)
                if user1.type == "student":
                    login(request,user)
                    messages.success(request, "logged in successfully.")   
                    return redirect('/user_home')
                else:
                    messages.error(request, " You are not  logged in ")      
            except:
                messages.warning(request, " You are not authenticated user something is wrong ")      
        else:
            messages.error(request, "user is not exits")      
                 
    return render(request,'user_login.html')


def user_signup(request):
    if request.method == 'POST':
        username = request.POST.get('name',"")
        email = request.POST.get('email',"")
        fname = request.POST.get('fname',"")
        lname = request.POST.get('lname',"")
        pass1 = request.POST.get('password1',"")
        pass2 = request.POST.get('password2',"")
        image = request.FILES['img']
        gender = request.POST['gender']
        phone = request.POST['phone']
        #basic checks
        if pass1 != pass2:
            messages.error(request, "Please enter correct password")    
        if len(username)>70:
            messages.error(request, "Please enter name  under the  70 character")

        #create the user
        try:
            myuser =  User.objects.create_user(username,email,pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            studentuser.objects.create(user = myuser , phone = phone , image = image , gender = gender , type = "student")

            myuser.save()
            messages.success(request, "Your singup has been done.")      

           # return redirect('/') # redirect('/') same
        except:
            messages.error(request, "Please fill the correct form ")      
    return render(request,'user_signup.html')

def user_logout(request):
    logout(request)
    messages.success(request, "successfully logged out....")
    return redirect('/') 


def user_home(request):
    if not request.user.is_authenticated:
        return redirect('/user_login')
    user = request.user
    myuser = studentuser.objects.get(user=user)
    if request.method == 'POST':
        fname = request.POST.get('fname',"")
        lname = request.POST.get('lname',"")  
        gender = request.POST.get('gender',"")
        phone = request.POST['phone']
        img = request.FILES['img'] 

       
        myuser.user.first_name = fname
        myuser.user.last_name = lname
        myuser.gender = gender
        myuser.phone = phone 
        myuser.image = img

        try:
            myuser.save() 
            myuser.user.save()   
            messages.success(request, "profile updated has been successfully")  
            return redirect('/user_home')
        except :
            messages.error(request, "profile updated has not been successfully")   
    param ={'myuser':myuser}
    return render(request,'user_home.html',param)



def recruiter_Login(request):
    if request.method == 'POST':
        name = request.POST.get('name',"")
        pass1 = request.POST.get('password',"")
        user = authenticate(username  = name, password= pass1)
        if user is not None:
            try:
                user1 = Recruiter.objects.get(user = user)
                if user1.type == "recruiter" and user1.status !="pending":
                    login(request,user)
                    messages.success(request, "successfully logged in") 
                    return redirect('/recruiter_home')  
                else:
                    messages.error(request, "status is pending. ")      
            except:
                return redirect('authrnticated user')
        else:
            messages.error(request, "user is not exits")      
    return render(request,'recruiter.html')

def recruiter_signup(request):
    if request.method == 'POST':
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        fname = request.POST.get('fname',"")
        lname = request.POST.get('lname',"")
        pass1 = request.POST.get('password1',"")
        pass2 = request.POST.get('password2',"")
        image = request.FILES['img']
        gender = request.POST['gender']
        phone = request.POST['phone']
        com = request.POST['com']
        #basic checks
        if pass1 != pass2:
            messages.error(request, "Please enter correct password")      
        #create the user
        try:
            myuser =  User.objects.create_user(name,email,pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            Recruiter.objects.create(user = myuser , phone = phone , image = image , gender = gender ,company = com, type = "recruiter",status = "pending")

            myuser.save()
            messages.success(request, "Your singup has been done.")      

           # return redirect('/') # redirect('/') same
        except :
            messages.error(request, "Please fill the correct form ")      

    return render(request,'recruiter_signup.html')


def recruiter_home(request):
    if not request.user.is_authenticated:
        return redirect('/recruiter_login')
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    if request.method == 'POST':
        fname = request.POST.get('fname',"")
        lname = request.POST.get('lname',"")  
        gender = request.POST.get('gender',"")
        phone = request.POST['phone']
        com = request.POST['com']
        img = request.FILES['logo'] 

       
        recruiter.user.first_name = fname
        recruiter.user.last_name = lname
        recruiter.gender = gender
        recruiter.phone = phone 
        recruiter.company= com
        recruiter.image = img

        try:
            recruiter.save() 
            recruiter.user.save()   
            messages.success(request, "profile updated has been successfully")  
            return redirect('/recruiter_home')
        except :
            messages.error(request, "profile updated has not been successfully")   
    param ={'recruiter':recruiter}
    return render(request,'recruiter_home.html',param)


def recuriter_logout(request):
    logout(request)
    messages.success(request, "successfully logged out....")
    return redirect('/') 

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        phone = request.POST.get('phone',"")  
        desc = request.POST.get('desc',"")
        contact = Contact(name = name,email = email , phone = phone , desc = desc)
        contact.save() 
        messages.success(request, "Your contact from  has been done.")      

    return render(request,'contact.html')



def user_view(request):
    if not request.user.is_authenticated:
        return redirect('/user_login')
    alluser = studentuser.objects.all()
    param = {'alluser':alluser}
    return render(request,'user_views.html',param)

def user_delete(request,myid):
    if not request.user.is_authenticated:
        return redirect('/user_login')
    student = User.objects.get(id=myid)
    student.delete()
    return redirect('/user_view')

def recruiter_pending(request):
    if not request.user.is_authenticated:
        return redirect('/user_login')
    allrec = Recruiter.objects.filter(status="pending")
    param = {'allrec':allrec}
    return render(request,'recruiter_pending.html',param)

def recruiter_accepted(request):
    if not request.user.is_authenticated:
        return redirect('/user_login')
    allrec = Recruiter.objects.filter(status="Accept")
    param = {'allrec':allrec}
    return render(request,'recruiter_pending.html',param)

def recruiter_rejected(request):
    if not request.user.is_authenticated:
        return redirect('/user_login')
    allrec = Recruiter.objects.filter(status="Reject")
    param = {'allrec':allrec}
    return render(request,'recruiter_pending.html',param)

def recruiter_allview(request):
    if not request.user.is_authenticated:
        return redirect('/user_login')
    allrec = Recruiter.objects.all()
    param = {'allrec':allrec}
    return render(request,'recruiter_view_all.html',param)


def recruiter_delete(request,myid):
    if not request.user.is_authenticated:
        return redirect('/user_login')
    recruiter = Recruiter.objects.get(id=myid)
    recruiter.delete()
    return redirect('/recruiter_pending')

def change_status(request,myid):
    if not request.user.is_authenticated:
        return redirect('/user_login')
    recruiter = Recruiter.objects.get(id= myid)

    if request.method == "POST":
        name = request.POST.get('name',"")
        mystatus = request.POST.get('status',"")
        recruiter.status = mystatus
        try:
            recruiter.save()
            messages.success(request, "Your  Status has been updated.")    
            return redirect('/recruiter_pending') 
        except: 
            messages.error(request, "Your status has been not updated ,Please! try again ")      

    param = {'recruiter':recruiter}
    return render(request,'change_status.html',param)

def change_pass_admin(request):
    if not request.user.is_authenticated:
        return redirect('/adminlogin')
    if request.method == "POST":
        pass1 = request.POST.get('pass1',"")
        pass2 = request.POST.get('pass2',"")
        pass3 = request.POST.get('pass3',"")
       # try:
        if User:
            old_user = User.objects.get(id= request.user.id)
            old_user.check_password(pass1)
            old_user.set_password(pass2)
            if pass2 == pass3:
                old_user.save()
                messages.success(request, "password change successfully ....")
            else:
                messages.error(request, "Please fill the correct password") 
        else:   
            messages.error(request, "Please fill the correct form ") 
 
       
    return render(request,'change_pass_admin.html')
  


def change_pass_user(request):
    if not request.user.is_authenticated:
        return redirect('/user_login')
    if request.method == "POST":
        pass1 = request.POST.get('pass1',"")
        pass2 = request.POST.get('pass2',"")
        pass3 = request.POST.get('pass3',"")
       # try:
        if User:
            old_user = User.objects.get(id= request.user.id)
            old_user.check_password(pass1)
            old_user.set_password(pass2)
            if pass2 == pass3:
                old_user.save()
                messages.success(request, "password change successfully ....")
            else:
                messages.error(request, "Please fill the correct password") 
        else:   
            messages.error(request, "Please fill the correct form ") 
 
       
    return render(request,'change_pass_user.html')
  

def change_pass_recruiter(request):
    if not request.user.is_authenticated:
        return redirect('/recruiter')
    if request.method == "POST":
        pass1 = request.POST.get('pass1',"")
        pass2 = request.POST.get('pass2',"")
        pass3 = request.POST.get('pass3',"")
       # try:
        if User:
            old_user = User.objects.get(id= request.user.id)
            old_user.check_password(pass1)
            old_user.set_password(pass2)
            if pass2 == pass3:
                old_user.save()
                messages.success(request, "password change successfully ....")
            else:
                messages.error(request, "Please fill the correct password") 
        else:   
            messages.error(request, "Please fill the correct form ")   
    return render(request,'change_pass_recruiter.html')
  

def add_job(request):
    if not request.user.is_authenticated:
        return redirect('/recruiter')
    if request.method == 'POST':
        start_time= request.POST.get('firsttime',"")
        last_time= request.POST.get('lasttime',"")
        title = request.POST.get('jobtitle',"")
        desc= request.POST.get('desc',"")
        experience = request.POST.get('experience',"")
        location= request.POST.get('location',"")
        image = request.FILES['img'] 
        skills= request.POST['skill']
        salary= request.POST['salary']
        user = request.user
        recruiter = Recruiter.objects.filter(user = user).first()
        try:
            Job.objects.create(recruiter = recruiter ,start_time=start_time,last_time = last_time,title = title,desc = desc , experience=experience,image = image,location = location,skills = skills,salary = salary,creationdate=date.today())     
            
            messages.success(request, "add job has been successfully ....")
            return redirect('/job_list')
        except  :
            messages.error(request, "Please fill the correct form ") 
    return render(request,'rec_add_job.html')


def job_list(request):
    if not request.user.is_authenticated:
        return redirect('/recruiter')
    user = request.user
    recruiter = Recruiter.objects.filter(user=user).first()   
    job  = Job.objects.filter(recruiter=recruiter) 
    param = {'job':job}
    return render(request,'job_list.html',param)


def edit_jobdetail(request,myid):
    if not request.user.is_authenticated:
        return redirect('/recruiter')
    job = Job.objects.get(id = myid)
    if request.method == 'POST':
        start_time= request.POST.get('firsttime',"")
        last_time= request.POST.get('lasttime',"")
        title = request.POST.get('jobtitle',"")
        desc= request.POST.get('desc',"")
        experience = request.POST.get('experience',"")
        location= request.POST.get('location',"")
        skill= request.POST.get('skill',"")
        salary= request.POST.get('salary',"")
    
        job.title =title
        job.desc = desc
        job.experience = experience
        job.location = location
        job.skills = skill
        job.salary = salary
        try:
            job.save()
            messages.success(request, " job updated has been successfully ....")
            return redirect('/job_list')
        except :
            messages.error(request, "Please fill the correct form  ") 
        if start_time:
            job.start_time = start_time
            job.save()
        if last_time:
            job.last_time = last_time
            job.save()
    param = {'job':job}
    return render(request,'edit_jobdetail.html', param)


def change_logo(request,myid):
    if not request.user.is_authenticated:
        return redirect('/recruiter')
    job = Job.objects.get(id = myid)
    if request.method == 'POST':
        img = request.FILES['img'] 
        job.image = img
        try:
            job.save()
            messages.success(request, " company logo has been successfully ....")
            return redirect('/job_list')
        except Exception as e :
           messages.error(request, "Please fill the correct form  ") 
    param = {'job':job}
    return render(request,'change_logo.html', param)



def latest_job(request):
    job = Job.objects.all().order_by('-start_time')
    param = {"job":job}
    return render(request ,'latest_job.html',param)


def user_latest_job(request):
    job = Job.objects.all().order_by('-start_time')
    user = request.user
    student= studentuser.objects.get(user=user) 
    data = Apply.objects.filter(student=student)
    list=[]
    for i in data:
        list.append(i)
    param = {"job":job}
    return render(request ,'user_latest_job.html',param)


def user_detail(request,myid):
    job = Job.objects.get(id=myid)
    param = {'job':job}
    return render(request ,'user_detail.html',param)




def applyforjob(request,myid):
    if not request.user.is_authenticated:
        return redirect('/user_login')
    user=request.user
    student = studentuser.objects.get(user=user)
    job = Job.objects.get(id=myid)
    date1 =date.today()
    if job.last_time < date1:
        messages.warning(request,"Application line are closed because last date is over")
        return redirect('/user_latest_jobs')
    elif job.start_time > date1:
        messages.warning(request,"time is not start please check correct date")
        return redirect('/user_latest_jobs')
    else:
        if request.method == 'POST':
            img = request.FILES['resume'] 
            apply = Apply(job=job,student=student, resume = img,applydate = date.today())
            apply.save()
            messages.success(request, " Application jobs submited successfully ....")

    return render(request,'apply_for_job.html', )



def applied_condidate_list(request):
    if not request.user.is_authenticated:
        return redirect('/recruiter')
    job = Apply.objects.all()
    param = {'data':job}
    return render(request,'applied_condidate_list.html',param)
   