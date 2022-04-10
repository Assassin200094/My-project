from django import template

register = template.Library()

@register.filter(name='censor')  # регистрируем наш фильтр под именем multiply,
# чтоб django понимал, что это именно фильтр, а не простая функция
def censor(value,arg):
    # первый аргумент здесь — это то значение, к которому надо применить фильтр,
    # второй аргумент — это аргумент фильтра, т. е. примерно следующее будет в шаблоне value|multiply:arg
    pass