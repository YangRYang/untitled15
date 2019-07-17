from django.template import Library
from django.utils.safestring import mark_safe

register = Library()

@register.simple_tag
def create_table_row(obj,model_class):
    rowa = '<tr>'
    if model_class.list_display:
        for row in model_class.list_display:
            data = getattr(obj,row)
            show_data = '<td>{}</td>'.format(data)
            rowa+=show_data
    rowa+='</tr>'
    print(rowa)
    return mark_safe(rowa)


@register.simple_tag
def retu_add():
    a='<td>啦啦啦</td>'
    return a