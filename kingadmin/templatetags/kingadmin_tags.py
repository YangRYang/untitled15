from django.template import Library
from django.utils.safestring import mark_safe

register = Library()

@register.simple_tag
def create_table_row(obj,model_class):
    rowa = ''
    if model_class.list_display:
        for row in model_class.list_display:
            data = getattr(obj,row)
            show_data = '<td>{}</td>'.format(data)
            rowa+=show_data

    return mark_safe(rowa)



@register.simple_tag
def retu_add():
    a='<td>啦啦啦</td>'
    return a

@register.simple_tag
def get_select_filed(filter_filed,model_class):
    filed_obj = model_class.model._meta.get_field(filter_filed)
    option = ''
    for choice in filed_obj.get_choices():
        option += '<option value="{}">{}</option>'.format(choice,choice)

    return mark_safe(option)
