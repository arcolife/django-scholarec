from django import template
register = template.Library()

@register.filter
def div( value, arg ):
    '''
    Divides the value; argument is the divisor.
    Returns empty string on any error.
    '''
    try:
        value = int( value )
        arg = int( arg )
        if arg: return value / arg
    except: pass
    return ''

@register.filter
def sub( value, arg ):
    '''
    Subtracts the argument from the value.
    Returns empty string on any error.
    '''
    try:
        value = int( value )
        arg = int( arg )
        if arg:
            print value - arg
            return value - arg
    except: pass
    return ''

@register.simple_tag
def get_count(total, arg):
    try:
        total = int(total)
        arg = int( arg )
        if total % arg:
            return (total/arg + 1)
        else:
            return total/arg
    except:
        pass
    return ''

@register.filter
def get_range( value ):
    """
    Filter - returns a list containing range made from given value
    Usage (in template):

    <ul>{% for i in 3|get_range %}
      <li>{{ i }}. Do something</li>
    {% endfor %}</ul>

    Results with the HTML:
    <ul>
      <li>0. Do something</li>
      <li>1. Do something</li>
      <li>2. Do something</li>
    </ul>

    Instead of 3 one may use the variable set in the views
    """
    x = range( 1, value+1 )
    if len(x) > 5:
        return x[:5]
    return x
