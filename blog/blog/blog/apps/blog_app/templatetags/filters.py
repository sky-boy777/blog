from lxml import etree
from django.template import Library


register = Library()


@register.filter
def str_cut(str_html, cut_len=100):
    html = etree.HTML(str_html)
    text = html.xpath("//text()")[0]
    text = text.strip()
    return text[:cut_len] + '...'
