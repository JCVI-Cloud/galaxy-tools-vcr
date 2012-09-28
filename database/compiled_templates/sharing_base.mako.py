from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1292428796.9511499
_template_filename='templates/sharing_base.mako'
_template_uri='/sharing_base.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding=None
_exports = ['body', 'title', 'center_panel', 'stylesheets', 'init', 'javascripts']


# SOURCE LINE 5

def inherit(context):
    if context.get('use_panels', False) == True:
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
    # SOURCE LINE 19
    ns = runtime.Namespace('__anon_0x6225310', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, '__anon_0x6225310')] = ns

    # SOURCE LINE 18
    ns = runtime.Namespace('__anon_0x64a5050', context._clean_inheritance_tokens(), templateuri=u'/display_common.mako', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, '__anon_0x64a5050')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, (inherit(context)), _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x6225310')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x64a5050')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        # SOURCE LINE 15
        __M_writer(u'\n')
        # SOURCE LINE 16
        __M_writer(u'\n\n')
        # SOURCE LINE 18
        __M_writer(u'\n')
        # SOURCE LINE 19
        __M_writer(u'\n\n')
        # SOURCE LINE 24
        __M_writer(u'\n')
        # SOURCE LINE 35
        __M_writer(u'\n\n')
        # SOURCE LINE 39
        __M_writer(u'\n\n')
        # SOURCE LINE 78
        __M_writer(u'\n\n')
        # SOURCE LINE 100
        __M_writer(u'\n\n')
        # SOURCE LINE 104
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x6225310')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x64a5050')._populate(_import_ns, [u'*'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        get_item_name = _import_ns.get('get_item_name', context.get('get_item_name', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        item = _import_ns.get('item', context.get('item', UNDEFINED))
        get_class_display_name = _import_ns.get('get_class_display_name', context.get('get_class_display_name', UNDEFINED))
        enumerate = _import_ns.get('enumerate', context.get('enumerate', UNDEFINED))
        get_class_plural_display_name = _import_ns.get('get_class_plural_display_name', context.get('get_class_plural_display_name', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 106
        __M_writer(u'\n')
        # SOURCE LINE 108
        __M_writer(u'    ')
        use_panels = context.get('use_panels', False)  
        
        __M_writer(u'\n\n')
        # SOURCE LINE 111
        if message:
            # SOURCE LINE 112
            __M_writer(u'        ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
        # SOURCE LINE 114
        __M_writer(u'\n    ')
        # SOURCE LINE 115

        #
        # Setup and variables needed for page.
        #
    
        # Get class name strings.
        item_class_name = get_class_display_name( item.__class__ ) 
        item_class_name_lc = item_class_name.lower()
        item_class_plural_name = get_class_plural_display_name( item.__class__ )
        item_class_plural_name_lc = item_class_plural_name.lower()
        
        # Get item name.
        item_name = get_item_name(item)
            
        
        # SOURCE LINE 128
        __M_writer(u'\n\n    <h2>Share or Publish ')
        # SOURCE LINE 130
        __M_writer(unicode(item_class_name))
        __M_writer(u" '")
        __M_writer(unicode(item_name))
        __M_writer(u"'</h2>\n\n")
        # SOURCE LINE 133
        if trans.get_user().username is None or trans.get_user().username is "":
            # SOURCE LINE 134
            __M_writer(u'        To make a ')
            __M_writer(unicode(item_class_name_lc))
            __M_writer(u' accessible via link or publish it, you must create a public username: \n        <p>\n        <form action="')
            # SOURCE LINE 136
            __M_writer(unicode(h.url_for( action='set_public_username', id=trans.security.encode_id( item.id ) )))
            __M_writer(u'"     \n                method="POST">\n            <div class="form-row">\n                <label>Public Username:</label>\n                <div class="form-row-input">\n                    <input type="text" name="username" size="40"/>\n                </div>\n            </div>\n            <div style="clear: both"></div>\n            <div class="form-row">\n                <input class="action-button" type="submit" name="Set Username" value="Set Username"/>\n            </div>\n        </form>\n')
            # SOURCE LINE 149
        else:
            # SOURCE LINE 151
            __M_writer(u'        <h3>Making ')
            __M_writer(unicode(item_class_name))
            __M_writer(u' Accessible via Link and Publishing It</h3>\n    \n            <div>\n')
            # SOURCE LINE 154
            if item.importable:
                # SOURCE LINE 155
                __M_writer(u'                    ')
 
                item_status = "accessible via link" 
                if item.published:
                    item_status = item_status + " and published"    
                                    
                
                # SOURCE LINE 159
                __M_writer(u'\n                    This ')
                # SOURCE LINE 160
                __M_writer(unicode(item_class_name_lc))
                __M_writer(u' is currently <strong>')
                __M_writer(unicode(item_status))
                __M_writer(u'</strong>. \n                    <div>\n                        <p>Anyone can view and import this ')
                # SOURCE LINE 162
                __M_writer(unicode(item_class_name_lc))
                __M_writer(u' by visiting the following URL:\n\n                        <blockquote>\n                            ')
                # SOURCE LINE 165
 
                url = h.url_for( action='display_by_username_and_slug', username=trans.get_user().username, slug=item.slug, qualified=True ) 
                url_parts = url.split("/")
                                            
                
                # SOURCE LINE 168
                __M_writer(u'\n                            <a id="item-url" href="')
                # SOURCE LINE 169
                __M_writer(unicode(url))
                __M_writer(u'" target="_top">')
                __M_writer(unicode(url))
                __M_writer(u'</a>\n                            <span id="item-url-text" style="display: none">\n                                ')
                # SOURCE LINE 171
                __M_writer(unicode("/".join( url_parts[:-1] )))
                __M_writer(u"/<span id='item-identifier'>")
                __M_writer(unicode(url_parts[-1]))
                __M_writer(u'</span>\n                            </span>\n                            \n                            <a href="#" id="edit-identifier"><img src="')
                # SOURCE LINE 174
                __M_writer(unicode(h.url_for('/static/images/fugue/pencil.png')))
                __M_writer(u'"/></a>\n                        </blockquote>\n        \n')
                # SOURCE LINE 177
                if item.published:
                    # SOURCE LINE 178
                    __M_writer(u'                            This ')
                    __M_writer(unicode(item_class_name_lc))
                    __M_writer(u" is publicly listed and searchable in Galaxy's <a href='")
                    __M_writer(unicode(h.url_for( action='list_published' )))
                    __M_writer(u'\' target="_top">Published ')
                    __M_writer(unicode(item_class_plural_name))
                    __M_writer(u'</a> section.\n')
                # SOURCE LINE 180
                __M_writer(u'                    </div>\n        \n                    <p>You can:\n                    <div>\n                    <form action="')
                # SOURCE LINE 184
                __M_writer(unicode(h.url_for( action='sharing', id=trans.security.encode_id( item.id ) )))
                __M_writer(u'" \n                            method="POST">\n')
                # SOURCE LINE 186
                if not item.published:
                    # SOURCE LINE 188
                    __M_writer(u'                                <input class="action-button" type="submit" name="disable_link_access" value="Disable Access to ')
                    __M_writer(unicode(item_class_name))
                    __M_writer(u' Link">\n                                <div class="toolParamHelp">Disables ')
                    # SOURCE LINE 189
                    __M_writer(unicode(item_class_name_lc))
                    __M_writer(u'\'s link so that it is not accessible.</div>\n                                <br>\n                                <input class="action-button" type="submit" name="publish" value="Publish ')
                    # SOURCE LINE 191
                    __M_writer(unicode(item_class_name))
                    __M_writer(u'" method="POST">\n                                <div class="toolParamHelp">Publishes the ')
                    # SOURCE LINE 192
                    __M_writer(unicode(item_class_name_lc))
                    __M_writer(u" to Galaxy's <a href='")
                    __M_writer(unicode(h.url_for( action='list_published' )))
                    __M_writer(u'\' target="_top">Published ')
                    __M_writer(unicode(item_class_plural_name))
                    __M_writer(u'</a> section, where it is publicly listed and searchable.</div>\n\n                            <br>\n')
                    # SOURCE LINE 195
                else: ## item.published == True
                    # SOURCE LINE 197
                    __M_writer(u'                                <input class="action-button" type="submit" name="unpublish" value="Unpublish ')
                    __M_writer(unicode(item_class_name))
                    __M_writer(u'">\n                                <div class="toolParamHelp">Removes this ')
                    # SOURCE LINE 198
                    __M_writer(unicode(item_class_name_lc))
                    __M_writer(u" from Galaxy's <a href='")
                    __M_writer(unicode(h.url_for( action='list_published' )))
                    __M_writer(u'\' target="_top">Published ')
                    __M_writer(unicode(item_class_plural_name))
                    __M_writer(u'</a> section so that it is not publicly listed or searchable.</div>\n                                <br>\n                                <input class="action-button" type="submit" name="disable_link_access_and_unpublish" value="Disable Access to ')
                    # SOURCE LINE 200
                    __M_writer(unicode(item_class_name))
                    __M_writer(u' via Link and Unpublish">\n                                <div class="toolParamHelp">Disables this ')
                    # SOURCE LINE 201
                    __M_writer(unicode(item_class_name_lc))
                    __M_writer(u"'s link so that it is not accessible and removes ")
                    __M_writer(unicode(item_class_name_lc))
                    __M_writer(u" from Galaxy's <a href='")
                    __M_writer(unicode(h.url_for( action='list_published' )))
                    __M_writer(u"' target='_top'>Published ")
                    __M_writer(unicode(item_class_plural_name))
                    __M_writer(u'</a> section so that it is not publicly listed or searchable.</div>\n')
                # SOURCE LINE 203
                __M_writer(u'                \n                    </form>\n                    </div>\n   \n')
                # SOURCE LINE 207
            else:
                # SOURCE LINE 208
                __M_writer(u'   \n                    This ')
                # SOURCE LINE 209
                __M_writer(unicode(item_class_name_lc))
                __M_writer(u' is currently restricted so that only you and the users listed below can access it. You can:\n                    <p>\n                    <form action="')
                # SOURCE LINE 211
                __M_writer(unicode(h.url_for( action='sharing', id=trans.security.encode_id(item.id) )))
                __M_writer(u'" method="POST">\n                        <input class="action-button" type="submit" name="make_accessible_via_link" value="Make ')
                # SOURCE LINE 212
                __M_writer(unicode(item_class_name))
                __M_writer(u' Accessible via Link">\n                        <div class="toolParamHelp">Generates a web link that you can share with other people so that they can view and import the ')
                # SOURCE LINE 213
                __M_writer(unicode(item_class_name_lc))
                __M_writer(u'.</div>\n        \n                        <br>\n                        <input class="action-button" type="submit" name="make_accessible_and_publish" value="Make ')
                # SOURCE LINE 216
                __M_writer(unicode(item_class_name))
                __M_writer(u' Accessible and Publish" method="POST">\n                        <div class="toolParamHelp">Makes the ')
                # SOURCE LINE 217
                __M_writer(unicode(item_class_name_lc))
                __M_writer(u' accessible via link (see above) and publishes the ')
                __M_writer(unicode(item_class_name_lc))
                __M_writer(u" to Galaxy's <a href='")
                __M_writer(unicode(h.url_for( action='list_published' )))
                __M_writer(u"' target='_top'>Published ")
                __M_writer(unicode(item_class_plural_name))
                __M_writer(u'</a> section, where it is publicly listed and searchable.</div>\n                    </form>\n       \n')
            # SOURCE LINE 221
            __M_writer(u'\n')
            # SOURCE LINE 225
            __M_writer(u'        <h3>Sharing ')
            __M_writer(unicode(item_class_name))
            __M_writer(u' with Specific Users</h3>\n\n            <div>\n')
            # SOURCE LINE 228
            if item.users_shared_with:
                # SOURCE LINE 229
                __M_writer(u'\n                    <p>\n                        The following users will see this ')
                # SOURCE LINE 231
                __M_writer(unicode(item_class_name_lc))
                __M_writer(u' in their ')
                __M_writer(unicode(item_class_name_lc))
                __M_writer(u' list and will be\n                        able to view, import, and run it.\n                    </p>\n            \n                    <table class="colored" border="0" cellspacing="0" cellpadding="0" width="100%">\n                        <tr class="header">\n                            <th>Email</th>\n                            <th></th>\n                        </tr>\n')
                # SOURCE LINE 240
                for i, association in enumerate( item.users_shared_with ):
                    # SOURCE LINE 241
                    __M_writer(u'                            ')
                    user = association.user 
                    
                    __M_writer(u'\n                            <tr>\n                                <td>\n                                    <div class="menubutton popup" id="user-')
                    # SOURCE LINE 244
                    __M_writer(unicode(i))
                    __M_writer(u'-popup">')
                    __M_writer(unicode(user.email))
                    __M_writer(u'</div>\n                                </td>\n                                <td>\n                                    <div popupmenu="user-')
                    # SOURCE LINE 247
                    __M_writer(unicode(i))
                    __M_writer(u'-popup">\n                                    <a class="action-button" href="')
                    # SOURCE LINE 248
                    __M_writer(unicode(h.url_for( action='sharing', id=trans.security.encode_id( item.id ), unshare_user=trans.security.encode_id( user.id ), use_panels=use_panels )))
                    __M_writer(u'">Unshare</a>\n                                    </div>\n                                </td>\n                            </tr>    \n')
                # SOURCE LINE 253
                __M_writer(u'                    </table>\n    \n                    <p>\n                    <a class="action-button" \n                       href="')
                # SOURCE LINE 257
                __M_writer(unicode(h.url_for( action='share', id=trans.security.encode_id(item.id), use_panels=use_panels )))
                __M_writer(u'">\n                        <span>Share with another user</span>\n                    </a>\n\n')
                # SOURCE LINE 261
            else:
                # SOURCE LINE 262
                __M_writer(u'\n                    <p>You have not shared this ')
                # SOURCE LINE 263
                __M_writer(unicode(item_class_name_lc))
                __M_writer(u' with any users.</p>\n    \n                    <a class="action-button" \n                       href="')
                # SOURCE LINE 266
                __M_writer(unicode(h.url_for( action='share', id=trans.security.encode_id(item.id), use_panels=use_panels )))
                __M_writer(u'">\n                        <span>Share with a user</span>\n                    </a>\n                    <br>\n    \n')
            # SOURCE LINE 272
            __M_writer(u'            </div>\n        </div>\n')
        # SOURCE LINE 275
        __M_writer(u'\n    <p><br><br>\n    <a href=')
        # SOURCE LINE 277
        __M_writer(unicode(h.url_for( action="list" )))
        __M_writer(u'>Back to ')
        __M_writer(unicode(item_class_plural_name))
        __M_writer(u' List</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x6225310')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x64a5050')._populate(_import_ns, [u'*'])
        item = _import_ns.get('item', context.get('item', UNDEFINED))
        get_class_display_name = _import_ns.get('get_class_display_name', context.get('get_class_display_name', UNDEFINED))
        get_item_name = _import_ns.get('get_item_name', context.get('get_item_name', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 37
        __M_writer(u'\n    Sharing and Publishing ')
        # SOURCE LINE 38
        __M_writer(unicode(get_class_display_name( item.__class__ )))
        __M_writer(u" '")
        __M_writer(unicode(get_item_name( item )))
        __M_writer(u"'\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x6225310')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x64a5050')._populate(_import_ns, [u'*'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 102
        __M_writer(u'\n    ')
        # SOURCE LINE 103
        __M_writer(unicode(self.body()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x6225310')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x64a5050')._populate(_import_ns, [u'*'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 80
        __M_writer(u'\n    ')
        # SOURCE LINE 81
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n    <style>\n')
        # SOURCE LINE 84
        __M_writer(u'        h3\n        {\n            margin-top: 2em;\n        }\n        input.action-button\n        {\n            margin-left: 0;\n        }\n')
        # SOURCE LINE 93
        if context.get('use_panels'):
            # SOURCE LINE 94
            __M_writer(u'        div#center\n        {\n            padding: 10px;\n        }\n')
        # SOURCE LINE 99
        __M_writer(u'    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x6225310')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x64a5050')._populate(_import_ns, [u'*'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 25
        __M_writer(u'\n')
        # SOURCE LINE 26

        self.has_left_panel=False
        self.has_right_panel=False
        self.message_box_visible=False
        self.overlay_visible=False
        self.message_box_class=""
        self.active_view=""
        self.body_class=""
        
        
        # SOURCE LINE 34
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x6225310')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x64a5050')._populate(_import_ns, [u'*'])
        item = _import_ns.get('item', context.get('item', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        get_controller_name = _import_ns.get('get_controller_name', context.get('get_controller_name', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 41
        __M_writer(u'\n    ')
        # SOURCE LINE 42
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n    <script type="text/javascript">\n    $(document).ready( function() \n    {\n        //\n        // Set up slug-editing functionality.\n        //\n        var on_start = function( text_elt ) \n        {\n            // Replace URL with URL text.\n            $(\'#item-url\').hide();\n            $(\'#item-url-text\').show();\n            \n            // Allow only lowercase alphanumeric and \'-\' characters in slug.\n            text_elt.keyup(function(){\n                text_elt.val( $(this).val().replace(/\\s+/g,\'-\').replace(/[^a-zA-Z0-9\\-]/g,\'\').toLowerCase() )\n            });\n        };\n        \n        var on_finish = function( text_elt ) \n        {\n            // Replace URL text with URL.\n            $(\'#item-url-text\').hide();\n            $(\'#item-url\').show();\n            \n            // Set URL to new value.\n            var new_url = $(\'#item-url-text\').text();\n            var item_url_obj = $(\'#item-url\');\n            item_url_obj.attr( "href", new_url );\n            item_url_obj.text( new_url );\n        };\n        \n        ')
        # SOURCE LINE 74
        controller_name = get_controller_name( item ) 
        
        __M_writer(u'\n        async_save_text("edit-identifier", "item-identifier", "')
        # SOURCE LINE 75
        __M_writer(unicode(h.url_for( controller=controller_name, action='set_slug_async', id=trans.security.encode_id( item.id ) )))
        __M_writer(u'", "new_slug", null, false, 0, on_start, on_finish); \n    });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


