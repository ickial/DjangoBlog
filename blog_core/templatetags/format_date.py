from django import template

register = template.Library()


@register.filter(name="format_date")
def format_date(value, format_type):
    if format_type == 'year':
        return value.year
    elif format_type == 'month':
        return value.month
    elif format_type == 'all_date':
        date_time_str = value.strftime("%d %B %Y at %H:%M")
        return date_time_str
    return ''
