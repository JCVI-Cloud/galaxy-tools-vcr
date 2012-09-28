from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1297783230.3722379
_template_filename='templates/dataset/edit_attributes.mako'
_template_uri='/dataset/edit_attributes.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding=None
_exports = ['stylesheets', 'datatype', 'javascripts', 'title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 163
    ns = runtime.Namespace('__anon_0x12e9e950', context._clean_inheritance_tokens(), templateuri=u'/dataset/security_common.mako', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, '__anon_0x12e9e950')] = ns

    # SOURCE LINE 2
    ns = runtime.Namespace('__anon_0x12e21bd0', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, '__anon_0x12e21bd0')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x12e9e950')._populate(_import_ns, [u'render_permission_form'])
        _mako_get_namespace(context, '__anon_0x12e21bd0')._populate(_import_ns, [u'render_msg'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        render_permission_form = _import_ns.get('render_permission_form', context.get('render_permission_form', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        all_roles = _import_ns.get('all_roles', context.get('all_roles', UNDEFINED))
        data_annotation = _import_ns.get('data_annotation', context.get('data_annotation', UNDEFINED))
        def datatype(dataset,datatypes):
            return render_datatype(context.locals_(__M_locals),dataset,datatypes)
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        current_user_roles = _import_ns.get('current_user_roles', context.get('current_user_roles', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        data = _import_ns.get('data', context.get('data', UNDEFINED))
        datatypes = _import_ns.get('datatypes', context.get('datatypes', UNDEFINED))
        _ = _import_ns.get('_', context.get('_', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 4
        __M_writer(u'\n\n')
        # SOURCE LINE 8
        __M_writer(u'\n\n')
        # SOURCE LINE 13
        __M_writer(u'\n\n')
        # SOURCE LINE 25
        __M_writer(u'\n\n')
        # SOURCE LINE 27
        if message:
            # SOURCE LINE 28
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
        # SOURCE LINE 30
        __M_writer(u'\n<div class="toolForm">\n    <div class="toolFormTitle">')
        # SOURCE LINE 32
        __M_writer(unicode(_('Edit Attributes')))
        __M_writer(u'</div>\n    <div class="toolFormBody">\n        <form name="edit_attributes" action="')
        # SOURCE LINE 34
        __M_writer(unicode(h.url_for( controller='root', action='edit' )))
        __M_writer(u'" method="post">\n            <input type="hidden" name="id" value="')
        # SOURCE LINE 35
        __M_writer(unicode(data.id))
        __M_writer(u'"/>\n            <div class="form-row">\n                <label>\n                    Name:\n                </label>\n                <div style="float: left; width: 250px; margin-right: 10px;">\n                    <input type="text" name="name" value="')
        # SOURCE LINE 41
        __M_writer(unicode(data.get_display_name()))
        __M_writer(u'" size="40"/>\n                </div>\n                <div style="clear: both"></div>\n            </div>\n            <div class="form-row">\n                <label>\n                    Info:\n                </label>\n                <div style="float: left; width: 250px; margin-right: 10px;">\n                    <input type="text" name="info" value="')
        # SOURCE LINE 50
        __M_writer(unicode(data.info))
        __M_writer(u'" size="40"/>\n                </div>\n                <div style="clear: both"></div>\n            </div>\n')
        # SOURCE LINE 54
        if trans.get_user() is not None:
            # SOURCE LINE 55
            __M_writer(u'                <div class="form-row">                    \n                    <label>\n                        Annotation / Notes:\n                    </label>\n                    <div style="float: left; width: 250px; margin-right: 10px;">\n                        <textarea name="annotation" cols="40" rows="2">')
            # SOURCE LINE 60
            __M_writer(unicode(data_annotation))
            __M_writer(u'</textarea>\n                    </div>\n                    <div style="clear: both"></div>\n                    <div class="toolParamHelp">Add an annotation or notes to a dataset; annotations are available when a history is viewed.</div>\n                </div>\n')
        # SOURCE LINE 66
        for name, spec in data.metadata.spec.items():
            # SOURCE LINE 67
            if spec.visible:
                # SOURCE LINE 68
                __M_writer(u'                    <div class="form-row">\n                        <label>\n                            ')
                # SOURCE LINE 70
                __M_writer(unicode(spec.desc))
                __M_writer(u':\n                        </label>\n                        <div style="float: left; width: 250px; margin-right: 10px;">\n                            ')
                # SOURCE LINE 73
                __M_writer(unicode(data.metadata.get_html_by_name( name, trans=trans )))
                __M_writer(u'\n                        </div>\n                        <div style="clear: both"></div>\n                    </div>\n')
        # SOURCE LINE 79
        __M_writer(u'            <div class="form-row">\n                <input type="submit" name="save" value="')
        # SOURCE LINE 80
        __M_writer(unicode(_('Save')))
        __M_writer(u'"/>\n            </div>\n        </form>\n        <form name="auto_detect" action="')
        # SOURCE LINE 83
        __M_writer(unicode(h.url_for( controller='root', action='edit' )))
        __M_writer(u'" method="post">\n            <input type="hidden" name="id" value="')
        # SOURCE LINE 84
        __M_writer(unicode(data.id))
        __M_writer(u'"/>\n            <div class="form-row">\n                <div style="float: left; width: 250px; margin-right: 10px;">\n                    <input type="submit" name="detect" value="')
        # SOURCE LINE 87
        __M_writer(unicode(_('Auto-detect')))
        __M_writer(u'"/>\n                </div>\n                <div class="toolParamHelp" style="clear: both;">\n                    This will inspect the dataset and attempt to correct the above column values if they are not accurate.\n                </div>\n            </div>\n        </form>\n')
        # SOURCE LINE 94
        if data.missing_meta():
            # SOURCE LINE 95
            __M_writer(u'            <div class="form-row">\n                <div class="errormessagesmall">')
            # SOURCE LINE 96
            __M_writer(unicode(_('Required metadata values are missing. Some of these values may not be editable by the user. Selecting "Auto-detect" will attempt to fix these values.')))
            __M_writer(u'</div>\n            </div>\n')
        # SOURCE LINE 99
        __M_writer(u'    </div>\n</div>\n<p />\n')
        # SOURCE LINE 102
        converters = data.get_converter_types() 
        
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin()[__M_key]) for __M_key in ['converters'] if __M_key in __M_locals_builtin()]))
        __M_writer(u'\n')
        # SOURCE LINE 103
        if len( converters ) > 0:
            # SOURCE LINE 104
            __M_writer(u'    <div class="toolForm">\n        <div class="toolFormTitle">')
            # SOURCE LINE 105
            __M_writer(unicode(_('Convert to new format')))
            __M_writer(u'</div>\n        <div class="toolFormBody">\n            <form name="convert_data" action="')
            # SOURCE LINE 107
            __M_writer(unicode(h.url_for( controller='root', action='edit' )))
            __M_writer(u'" method="post">\n                <input type="hidden" name="id" value="')
            # SOURCE LINE 108
            __M_writer(unicode(data.id))
            __M_writer(u'"/>\n                <div class="form-row">\n                    <div style="float: left; width: 250px; margin-right: 10px;">\n                        <select name="target_type">\n')
            # SOURCE LINE 112
            for key, value in converters.items():
                # SOURCE LINE 113
                __M_writer(u'                                <option value="')
                __M_writer(unicode(key))
                __M_writer(u'">')
                __M_writer(unicode(value.name))
                __M_writer(u'</option>\n')
            # SOURCE LINE 115
            __M_writer(u'                        </select>\n                    </div>\n                    <div class="toolParamHelp" style="clear: both;">\n                        This will create a new dataset with the contents of this dataset converted to a new format. \n                    </div>\n                    <div style="clear: both"></div>\n                </div>\n                <div class="form-row">\n                    <input type="submit" name="convert_data" value="')
            # SOURCE LINE 123
            __M_writer(unicode(_('Convert')))
            __M_writer(u'"/>\n                </div>\n            </form>\n        </div>\n    </div>\n    <p />\n')
        # SOURCE LINE 130
        __M_writer(u'\n<div class="toolForm">\n    <div class="toolFormTitle">')
        # SOURCE LINE 132
        __M_writer(unicode(_('Change data type')))
        __M_writer(u'</div>\n    <div class="toolFormBody">\n')
        # SOURCE LINE 134
        if data.datatype.allow_datatype_change:
            # SOURCE LINE 135
            __M_writer(u'            <form name="change_datatype" action="')
            __M_writer(unicode(h.url_for( controller='root', action='edit' )))
            __M_writer(u'" method="post">\n                <input type="hidden" name="id" value="')
            # SOURCE LINE 136
            __M_writer(unicode(data.id))
            __M_writer(u'"/>\n                <div class="form-row">\n                    <label>\n                        ')
            # SOURCE LINE 139
            __M_writer(unicode(_('New Type')))
            __M_writer(u':\n                    </label>\n                    <div style="float: left; width: 250px; margin-right: 10px;">\n                        ')
            # SOURCE LINE 142
            __M_writer(unicode(datatype( data, datatypes )))
            __M_writer(u'\n                    </div>\n                    <div class="toolParamHelp" style="clear: both;">\n                        ')
            # SOURCE LINE 145
            __M_writer(unicode(_('This will change the datatype of the existing dataset but <i>not</i> modify its contents. Use this if Galaxy has incorrectly guessed the type of your dataset.')))
            __M_writer(u'\n                    </div>\n                    <div style="clear: both"></div>\n                </div>\n                <div class="form-row">\n                    <input type="submit" name="change" value="')
            # SOURCE LINE 150
            __M_writer(unicode(_('Save')))
            __M_writer(u'"/>\n                </div>\n            </form>\n')
            # SOURCE LINE 153
        else:
            # SOURCE LINE 154
            __M_writer(u'            <div class="form-row">\n                <div class="warningmessagesmall">')
            # SOURCE LINE 155
            __M_writer(unicode(_('Changing the datatype of this dataset is not allowed.')))
            __M_writer(u'</div>\n            </div>\n')
        # SOURCE LINE 158
        __M_writer(u'    </div>\n</div>\n<p />\n\n')
        # SOURCE LINE 162
        if trans.app.security_agent.can_manage_dataset( current_user_roles, data.dataset ):
            # SOURCE LINE 163
            __M_writer(u'    ')
            __M_writer(u'\n    ')
            # SOURCE LINE 164
            __M_writer(unicode(render_permission_form( data.dataset, data.get_display_name(), h.url_for( controller='root', action='edit', id=data.id ), all_roles )))
            __M_writer(u'\n')
            # SOURCE LINE 165
        elif trans.user:
            # SOURCE LINE 166
            __M_writer(u'    <div class="toolForm">\n        <div class="toolFormTitle">View Permissions</div>\n        <div class="toolFormBody">\n            <div class="form-row">\n')
            # SOURCE LINE 170
            if data.dataset.actions:
                # SOURCE LINE 171
                __M_writer(u'                    <ul>\n')
                # SOURCE LINE 172
                for action, roles in trans.app.security_agent.get_permissions( data.dataset ).items():
                    # SOURCE LINE 173
                    if roles:
                        # SOURCE LINE 174
                        __M_writer(u'                                <li>')
                        __M_writer(unicode(action.description))
                        __M_writer(u'</li>\n                                <ul>\n')
                        # SOURCE LINE 176
                        for role in roles:
                            # SOURCE LINE 177
                            __M_writer(u'                                        <li>')
                            __M_writer(unicode(role.name))
                            __M_writer(u'</li>\n')
                        # SOURCE LINE 179
                        __M_writer(u'                                </ul>\n')
                # SOURCE LINE 182
                __M_writer(u'                    </ul>\n')
                # SOURCE LINE 183
            else:
                # SOURCE LINE 184
                __M_writer(u'                    <p>This dataset is accessible by everyone (it is public).</p>\n')
            # SOURCE LINE 186
            __M_writer(u'            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x12e9e950')._populate(_import_ns, [u'render_permission_form'])
        _mako_get_namespace(context, '__anon_0x12e21bd0')._populate(_import_ns, [u'render_msg'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 6
        __M_writer(u'\n    ')
        # SOURCE LINE 7
        __M_writer(unicode(h.css( "base", "autocomplete_tagging" )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_datatype(context,dataset,datatypes):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x12e9e950')._populate(_import_ns, [u'render_permission_form'])
        _mako_get_namespace(context, '__anon_0x12e21bd0')._populate(_import_ns, [u'render_msg'])
        _ = _import_ns.get('_', context.get('_', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 15
        __M_writer(u'\n    <select name="datatype">\n')
        # SOURCE LINE 17
        for ext in datatypes:
            # SOURCE LINE 18
            if dataset.ext == ext:
                # SOURCE LINE 19
                __M_writer(u'                <option value="')
                __M_writer(unicode(ext))
                __M_writer(u'" selected="yes">')
                __M_writer(unicode(_(ext)))
                __M_writer(u'</option>\n')
                # SOURCE LINE 20
            else:
                # SOURCE LINE 21
                __M_writer(u'                <option value="')
                __M_writer(unicode(ext))
                __M_writer(u'">')
                __M_writer(unicode(_(ext)))
                __M_writer(u'</option>\n')
        # SOURCE LINE 24
        __M_writer(u'    </select>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x12e9e950')._populate(_import_ns, [u'render_permission_form'])
        _mako_get_namespace(context, '__anon_0x12e21bd0')._populate(_import_ns, [u'render_msg'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 10
        __M_writer(u'\n    ')
        # SOURCE LINE 11
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n    ')
        # SOURCE LINE 12
        __M_writer(unicode(h.js( "galaxy.base", "jquery.autocomplete", "autocomplete_tagging" )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x12e9e950')._populate(_import_ns, [u'render_permission_form'])
        _mako_get_namespace(context, '__anon_0x12e21bd0')._populate(_import_ns, [u'render_msg'])
        _ = _import_ns.get('_', context.get('_', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(unicode(_('Edit Dataset Attributes')))
        return ''
    finally:
        context.caller_stack._pop_frame()


