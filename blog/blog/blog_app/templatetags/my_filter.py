from lxml import etree
from django.template import Library


register = Library()


@register.filter
def my_f(str_html):
    html = etree.HTML(str_html)
    text = html.xpath("//text()")[0]
    text = text.strip()
    return text[:300] + '...'
