# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1336505820.1879871
_template_filename=u'templates/base.mako'
_template_uri=u'/base.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['stylesheets', 'javascripts', 'metas', 'title']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        next = context.get('next', UNDEFINED)
        n_ = context.get('n_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        _=n_ 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['_'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\n<html>\n    <head>\n        <title>')
        # SOURCE LINE 5
        __M_writer(unicode(self.title()))
        __M_writer(u'</title>\n        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n        ')
        # SOURCE LINE 7
        __M_writer(unicode(self.metas()))
        __M_writer(u'\n        ')
        # SOURCE LINE 8
        __M_writer(unicode(self.stylesheets()))
        __M_writer(u'\n        ')
        # SOURCE LINE 9
        __M_writer(unicode(self.javascripts()))
        __M_writer(u'\n    </head>\n    <body>\n        ')
        # SOURCE LINE 12
        __M_writer(unicode(next.body()))
        __M_writer(u'\n    </body>\n</html>\n\n')
        # SOURCE LINE 17
        __M_writer(u'\n\n')
        # SOURCE LINE 22
        __M_writer(u'\n\n')
        # SOURCE LINE 37
        __M_writer(u'\n\n')
        # SOURCE LINE 40
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 20
        __M_writer(u'\n    ')
        # SOURCE LINE 21
        __M_writer(unicode(h.css('base')))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 25
        __M_writer(u'\n')
        # SOURCE LINE 29
        __M_writer(u'  ')
        __M_writer(unicode(h.js( "jquery", "galaxy.base", "libs/underscore", "libs/backbone", "libs/backbone-relational", "libs/handlebars.runtime", "mvc/ui" )))
        __M_writer(u'\n  <script type="text/javascript">\n      // Set up needed paths.\n      var galaxy_paths = new GalaxyPaths({\n          root_path: \'')
        # SOURCE LINE 33
        __M_writer(unicode(h.url_for( "/" )))
        __M_writer(u"',\n          image_path: '")
        # SOURCE LINE 34
        __M_writer(unicode(h.url_for( "/static/images" )))
        __M_writer(u"'\n      });\n  </script>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_metas(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


