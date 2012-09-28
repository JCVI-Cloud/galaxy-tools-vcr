from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1308683752.5269711
_template_filename='templates/dataset/display_application/display.mako'
_template_uri='dataset/display_application/display.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding=None
_exports = ['metas', 'title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.Namespace('__anon_0x7f425c704910', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, '__anon_0x7f425c704910')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f425c704910')._populate(_import_ns, [u'render_msg'])
        msg = _import_ns.get('msg', context.get('msg', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        refresh = _import_ns.get('refresh', context.get('refresh', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        for message, status in msg:
            # SOURCE LINE 5
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
        # SOURCE LINE 7
        if refresh:
            # SOURCE LINE 8
            __M_writer(u'\n<p>\nThis page will <a href="')
            # SOURCE LINE 10
            __M_writer(unicode(trans.request.url))
            __M_writer(u'">refresh</a> after 10 seconds.\n</p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_metas(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f425c704910')._populate(_import_ns, [u'render_msg'])
        __M_writer = context.writer()
        # SOURCE LINE 8
        __M_writer(u'<meta http-equiv="refresh" content="10" />')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f425c704910')._populate(_import_ns, [u'render_msg'])
        display_link = _import_ns.get('display_link', context.get('display_link', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'Display Application: ')
        __M_writer(unicode(display_link.link.display_application.name))
        __M_writer(u'  ')
        __M_writer(unicode(display_link.link.name))
        return ''
    finally:
        context.caller_stack._pop_frame()


