from django.contrib.auth.decorators import login_required
from django.shortcuts import render 
from app_select.models import Subjects_Test_Date
from app_schedule.models import Subjects_info , User_subjects , AuthUser
from django.db.models import Q
from app_select.views import start_times,user_data


# Create your views here.
@login_required(login_url='login')
def schedule_view(request):

    # search btn
    if 'search_btn' in request.GET:
        search = request.GET['search_btn']
        multiple_search = Q(Q(name__icontains=search) | Q(code__icontains=search) | Q(prof__icontains=search))
        sub_name = Subjects_info.objects.filter(multiple_search)
    else:
        sub_name = Subjects_info.objects.none()


    sub_date = Subjects_Test_Date.objects.all()
    sub_objects = Subjects_info.objects.all()
    user_id = request.user.id
    user = User_subjects.objects.filter(user_id_id = user_id)
    user_all = User_subjects.objects.all()

    day_start_times_used = user_data[user_id]['day_start_times_used']


    
    days = {
    "M": "Monday",
    "T": "Tuesday",
    "W": "Wednesday",
    "H": "Thursday",
    "F": "Friday",
    "S": "Sunday",
}
    
    # The select button was clicked
    subject_id = request.POST.get('id')
    # insert name into user table using Django ORM
    if subject_id :
        User_subjects.objects.create(user_id_id=user_id, sub_id_id=subject_id)

    context = {'sub_date':sub_date, 
               'sub_objects':sub_objects,
               'users':user,
               'start_times':start_times,
               'user_all':user_all,
               'day_start_times_used':day_start_times_used,
               'sub_name':sub_name,
               'days':days}
    
    return render(request, 'schedule.html' , context)

def about(request):
    return render(request, 'about.html')

@login_required(login_url='login')
def subject_list(request):

    # search btn
    if 'search_btn' in request.GET:
        search = request.GET['search_btn']
        multiple_search = Q(Q(name__icontains=search) | Q(code__icontains=search) | Q(prof__icontains=search))
        sub_name = Subjects_info.objects.filter(multiple_search)
    else:
        sub_name = Subjects_info.objects.none()
        
    sub_objects = Subjects_info.objects.all()
    user_all = User_subjects.objects.all()


    context = {'sub_objects':sub_objects,
               'user_all':user_all,
               'sub_name':sub_name}
    
    return render(request, 'sub_std_list.html' , context)