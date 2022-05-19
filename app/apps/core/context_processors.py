from django.contrib import admin


def global_context(request):
    """
    This is intended to be a global context processor.  Any templates rendered from views using the
    `django.template.RequestContext` context (the default context used by generic views) will have this context
    available to them.
    """

    context = {
        'index_title': admin.site.index_title,
        'site_header': admin.site.site_header,
        'site_title': admin.site.site_title
    }

    return context
