from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1308683819.3344669
_template_filename='templates/user/register.mako'
_template_uri='/user/register.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding=None
_exports = ['javascripts', 'render_registration_form']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.Namespace('__anon_0x6877ad0', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, '__anon_0x6877ad0')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x6877ad0')._populate(_import_ns, [u'render_msg'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        redirect_url = _import_ns.get('redirect_url', context.get('redirect_url', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        def render_registration_form(form_action=None):
            return render_render_registration_form(context.locals_(__M_locals),form_action)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 4
        if redirect_url:
            # SOURCE LINE 5
            __M_writer(u'    <script type="text/javascript">  \n        top.location.href = \'')
            # SOURCE LINE 6
            __M_writer(unicode(redirect_url))
            __M_writer(u"';\n    </script>\n")
        # SOURCE LINE 9
        __M_writer(u'\n')
        # SOURCE LINE 12
        __M_writer(u'\n\n')
        # SOURCE LINE 14
        if not redirect_url and message:
            # SOURCE LINE 15
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
        # SOURCE LINE 17
        __M_writer(u'\n')
        # SOURCE LINE 20
        if trans.user_is_admin() or not trans.user:
            # SOURCE LINE 21
            __M_writer(u'    ')
            __M_writer(unicode(render_registration_form()))
            __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n')
        # SOURCE LINE 95
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x6877ad0')._populate(_import_ns, [u'render_msg'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 10
        __M_writer(u'\n    ')
        # SOURCE LINE 11
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_registration_form(context,form_action=None):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x6877ad0')._populate(_import_ns, [u'render_msg'])
        username = _import_ns.get('username', context.get('username', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        user_type_form_definition = _import_ns.get('user_type_form_definition', context.get('user_type_form_definition', UNDEFINED))
        confirm = _import_ns.get('confirm', context.get('confirm', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        user_type_fd_id_select_field = _import_ns.get('user_type_fd_id_select_field', context.get('user_type_fd_id_select_field', UNDEFINED))
        widgets = _import_ns.get('widgets', context.get('widgets', UNDEFINED))
        subscribe_checked = _import_ns.get('subscribe_checked', context.get('subscribe_checked', UNDEFINED))
        referer = _import_ns.get('referer', context.get('referer', UNDEFINED))
        cntrller = _import_ns.get('cntrller', context.get('cntrller', UNDEFINED))
        webapp = _import_ns.get('webapp', context.get('webapp', UNDEFINED))
        password = _import_ns.get('password', context.get('password', UNDEFINED))
        email = _import_ns.get('email', context.get('email', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 24
        __M_writer(u'\n\n    ')
        # SOURCE LINE 26

        if form_action is None:
            form_action = h.url_for( controller='user', action='create', cntrller=cntrller )
        from galaxy.web.form_builder import CheckboxField
        subscribe_check_box = CheckboxField( 'subscribe' )
            
        
        # SOURCE LINE 31
        __M_writer(u'\n\n    <div class="toolForm">\n        <form name="registration" id="registration" action="')
        # SOURCE LINE 34
        __M_writer(unicode(form_action))
        __M_writer(u'" method="post" >\n            <div class="toolFormTitle">Create account</div>\n            <div class="form-row">\n                <label>Email address:</label>\n                <input type="text" name="email" value="')
        # SOURCE LINE 38
        __M_writer(unicode(email))
        __M_writer(u'" size="40"/>\n                <input type="hidden" name="webapp" value="')
        # SOURCE LINE 39
        __M_writer(unicode(webapp))
        __M_writer(u'" size="40"/>\n                <input type="hidden" name="referer" value="')
        # SOURCE LINE 40
        __M_writer(unicode(referer))
        __M_writer(u'" size="40"/>\n            </div>\n            <div class="form-row">\n                <label>Password:</label>\n                <input type="password" name="password" value="')
        # SOURCE LINE 44
        __M_writer(unicode(password))
        __M_writer(u'" size="40"/>\n            </div>\n            <div class="form-row">\n                <label>Confirm password:</label>\n                <input type="password" name="confirm" value="')
        # SOURCE LINE 48
        __M_writer(unicode(confirm))
        __M_writer(u'" size="40"/>\n            </div>\n            <div class="form-row">\n                <label>Public name:</label>\n                <input type="text" name="username" size="40" value="')
        # SOURCE LINE 52
        __M_writer(unicode(username))
        __M_writer(u'"/>\n                <div class="toolParamHelp" style="clear: both;">\n                    Your public name is an identifier that will be used to generate addresses for information\n                    you share publicly. Public names must be at least four characters in length and contain only lower-case\n                    letters, numbers, and the \'-\' character.\n                </div>\n            </div>\n')
        # SOURCE LINE 59
        if trans.app.config.smtp_server:
            # SOURCE LINE 60
            __M_writer(u'                <div class="form-row">\n                    <label>Subscribe to mailing list:</label>\n')
            # SOURCE LINE 62
            if subscribe_checked:
                # SOURCE LINE 63
                __M_writer(u'                        ')
                subscribe_check_box.checked = True 
                
                __M_writer(u'\n')
            # SOURCE LINE 65
            __M_writer(u'                    ')
            __M_writer(unicode(subscribe_check_box.get_html()))
            __M_writer(u'\n                </div>\n')
        # SOURCE LINE 68
        if user_type_fd_id_select_field:
            # SOURCE LINE 69
            __M_writer(u'                <div class="form-row">\n                    <label>User type</label>\n                    ')
            # SOURCE LINE 71
            __M_writer(unicode(user_type_fd_id_select_field.get_html()))
            __M_writer(u'\n                </div>\n')
        # SOURCE LINE 74
        if user_type_form_definition:
            # SOURCE LINE 75
            for field in widgets:
                # SOURCE LINE 76
                __M_writer(u'                    <div class="form-row">\n                        <label>')
                # SOURCE LINE 77
                __M_writer(unicode(field['label']))
                __M_writer(u'</label>\n                        ')
                # SOURCE LINE 78
                __M_writer(unicode(field['widget'].get_html()))
                __M_writer(u'\n                        <div class="toolParamHelp" style="clear: both;">\n                            ')
                # SOURCE LINE 80
                __M_writer(unicode(field['helptext']))
                __M_writer(u'\n                        </div>\n                        <div style="clear: both"></div>\n                    </div>\n')
            # SOURCE LINE 85
            if not user_type_fd_id_select_field:
                # SOURCE LINE 86
                __M_writer(u'                    <input type="hidden" name="user_type_fd_id" value="')
                __M_writer(unicode(trans.security.encode_id( user_type_form_definition.id )))
                __M_writer(u'"/>\n')
        # SOURCE LINE 89
        __M_writer(u'            <div class="form-row">\n                <input type="submit" name="create_user_button" value="Submit"/>\n            </div>\n        </form>\n    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


