def check_page_number(page, paginator):
    """校验页码
     :returns  返回合适的页码
    """
    try:
        p = int(page)
    except:
        p = 1
    if p < 1 or p > paginator.num_pages:
        p = 1
    return p