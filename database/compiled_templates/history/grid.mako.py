from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1297786001.852468
_template_filename='templates/history/grid.mako'
_template_uri='/history/grid.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding=None
_exports = ['grid_javascripts']


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
    return runtime._inherit_from(context, u'../grid_base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 17
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_grid_javascripts(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        refresh_frames = context.get('refresh_frames', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n    ')
        # SOURCE LINE 4
        __M_writer(unicode(parent.grid_javascripts()))
        __M_writer(u'\n    <script type="text/javascript">\n')
        # SOURCE LINE 6
        if refresh_frames:
            # SOURCE LINE 7
            if 'history' in refresh_frames:
                # SOURCE LINE 8
                __M_writer(u'                if ( parent.frames && parent.frames.galaxy_history ) {\n                    parent.frames.galaxy_history.location.href="')
                # SOURCE LINE 9
                __M_writer(unicode(h.url_for( controller='root', action='history')))
                __M_writer(u'";\n                    if ( parent.force_right_panel ) {\n                        parent.force_right_panel( \'show\' );\n                    }\n                }\n')
        # SOURCE LINE 16
        __M_writer(u'    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


