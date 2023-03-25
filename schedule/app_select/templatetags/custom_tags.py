from django import template
from app_schedule.models import Subjects_info


register = template.Library()


@register.filter
def get_list(dict, day):
    return dict[day]

@register.filter
def count(user,sub_id): 
    return user.filter(sub_id_id = sub_id).count()