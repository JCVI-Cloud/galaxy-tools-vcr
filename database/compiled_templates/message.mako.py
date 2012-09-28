# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1336505820.4005389
_template_filename=u'templates/message.mako'
_template_uri=u'/message.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['body', 'render_msg', 'center_panel', 'init', 'render_large_message', 'javascripts']


# SOURCE LINE 1

def inherit(context):
    if context.get('use_panels'):
        if context.get('webapp'):
            webapp = context.get('webapp')
        else:
            webapp = 'galaxy'
        return '/webapps/%s/base_panels.mako' % webapp
    else:
        return '/base.mako'


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, (inherit(context)), _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        n_ = context.get('n_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 11
        __M_writer(u'\n')
        # SOURCE LINE 12
        __M_writer(u'\n')
        # SOURCE LINE 13
        _=n_ 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['_'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n')
        # SOURCE LINE 22
        __M_writer(u'\n\n')
        # SOURCE LINE 69
        __M_writer(u'\n\n')
        # SOURCE LINE 74
        __M_writer(u'\n')
        # SOURCE LINE 77
        __M_writer(u'\n\n')
        # SOURCE LINE 81
        __M_writer(u'\n\n')
        # SOURCE LINE 86
        __M_writer(u'\n\n')
        # SOURCE LINE 92
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    context.caller_stack._push_frame()
    try:
        status = context.get('status', UNDEFINED)
        message = context.get('message', UNDEFINED)
        def render_large_message(message,status):
            return render_render_large_message(context,message,status)
        __M_writer = context.writer()
        # SOURCE LINE 79
        __M_writer(u'\n    ')
        # SOURCE LINE 80
        __M_writer(unicode(render_large_message( message, status )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_msg(context,msg,status='done'):
    context.caller_stack._push_frame()
    try:
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 89
        __M_writer(u'\n    <div class="')
        # SOURCE LINE 90
        __M_writer(unicode(status))
        __M_writer(u'message">')
        __M_writer(unicode(_(msg)))
        __M_writer(u'</div>\n    <br/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    context.caller_stack._push_frame()
    try:
        status = context.get('status', UNDEFINED)
        message = context.get('message', UNDEFINED)
        def render_large_message(message,status):
            return render_render_large_message(context,message,status)
        __M_writer = context.writer()
        # SOURCE LINE 75
        __M_writer(u'\n    ')
        # SOURCE LINE 76
        __M_writer(unicode(render_large_message( message, status )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        active_view = context.get('active_view', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 15
        __M_writer(u'\n')
        # SOURCE LINE 16

        self.has_left_panel=False
        self.has_right_panel=False
        self.active_view=active_view
        self.message_box_visible=False
        
        
        # SOURCE LINE 21
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_large_message(context,message,status):
    context.caller_stack._push_frame()
    try:
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 84
        __M_writer(u'\n    <div class="')
        # SOURCE LINE 85
        __M_writer(unicode(status))
        __M_writer(u'messagelarge" style="margin: 1em">')
        __M_writer(unicode(_(message)))
        __M_writer(u'</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        parent = context.get('parent', UNDEFINED)
        int = context.get('int', UNDEFINED)
        h = context.get('h', UNDEFINED)
        app = context.get('app', UNDEFINED)
        refresh_frames = context.get('refresh_frames', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 24
        __M_writer(u'\n    ')
        # SOURCE LINE 25
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n    <script type="text/javascript">\n')
        # SOURCE LINE 27
        if 'everything' in refresh_frames:
            # SOURCE LINE 28
            __M_writer(u'            parent.location.href="')
            __M_writer(unicode(h.url_for( controller='root' )))
            __M_writer(u'";\n')
            pass
        # SOURCE LINE 30
        if 'masthead' in refresh_frames:
            # SOURCE LINE 37
            __M_writer(u'            \n')
            # SOURCE LINE 39
            __M_writer(u'            if ( parent.user_changed ) {\n')
            # SOURCE LINE 40
            if trans.user:
                # SOURCE LINE 41
                __M_writer(u'                    parent.user_changed( "')
                __M_writer(unicode(trans.user.email))
                __M_writer(u'", ')
                __M_writer(unicode(int( app.config.is_admin_user( trans.user ) )))
                __M_writer(u' );\n')
                # SOURCE LINE 42
            else:
                # SOURCE LINE 43
                __M_writer(u'                    parent.user_changed( null, false );\n')
                pass
            # SOURCE LINE 45
            __M_writer(u'            }\n')
            pass
        # SOURCE LINE 47
        if 'history' in refresh_frames:
            # SOURCE LINE 48
            __M_writer(u'            if ( parent.frames && parent.frames.galaxy_history ) {\n                parent.frames.galaxy_history.location.href="')
            # SOURCE LINE 49
            __M_writer(unicode(h.url_for( controller='root', action='history')))
            __M_writer(u'";\n                if ( parent.force_right_panel ) {\n                    parent.force_right_panel( \'show\' );\n                }\n            }\n')
            pass
        # SOURCE LINE 55
        if 'tools' in refresh_frames:
            # SOURCE LINE 56
            __M_writer(u'            if ( parent.frames && parent.frames.galaxy_tools ) {\n                parent.frames.galaxy_tools.location.href="')
            # SOURCE LINE 57
            __M_writer(unicode(h.url_for( controller='root', action='tool_menu')))
            __M_writer(u'";\n                if ( parent.force_left_panel ) {\n                    parent.force_left_panel( \'show\' );\n                }\n            }\n')
            pass
        # SOURCE LINE 63
        __M_writer(u'\n        if ( parent.handle_minwidth_hint )\n        {\n            parent.handle_minwidth_hint( -1 );\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


