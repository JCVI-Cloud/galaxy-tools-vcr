from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1292336834.3176651
_template_filename=u'templates/dataset/security_common.mako'
_template_uri=u'/dataset/security_common.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding=None
_exports = ['render_permission_form', 'render_select']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 37
        __M_writer(u'\n\n')
        # SOURCE LINE 123
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_permission_form(context,obj,obj_name,form_url,all_roles,do_not_render=[]):
    context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        def render_select(current_actions,action_key,action,all_roles):
            return render_render_select(context,current_actions,action_key,action,all_roles)
        isinstance = context.get('isinstance', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 40
        __M_writer(u'\n    ')
        # SOURCE LINE 41

        if isinstance( obj, trans.app.model.User ):
            current_actions = obj.default_permissions
            permitted_actions = trans.app.model.Dataset.permitted_actions.items()
            obj_str = 'user %s' % obj_name
            obj_type = 'dataset'
        elif isinstance( obj, trans.app.model.History ):
            current_actions = obj.default_permissions
            permitted_actions = trans.app.model.Dataset.permitted_actions.items()
            obj_str = 'history %s' % obj_name
            obj_type = 'dataset'
        elif isinstance( obj, trans.app.model.Dataset ):
            current_actions = obj.actions
            permitted_actions = trans.app.model.Dataset.permitted_actions.items()
            obj_str = obj_name
            obj_type = 'dataset'
        elif isinstance( obj, trans.app.model.LibraryDatasetDatasetAssociation ):
            current_actions = obj.actions + obj.dataset.actions
            permitted_actions = trans.app.model.Dataset.permitted_actions.items() + trans.app.model.Library.permitted_actions.items()
            obj_str = obj_name
            obj_type = 'dataset'
        elif isinstance( obj, trans.app.model.Library ):
            current_actions = obj.actions
            permitted_actions = trans.app.model.Library.permitted_actions.items()
            obj_str = 'library %s' % obj_name
            obj_type = 'library'
        elif isinstance( obj, trans.app.model.LibraryDataset ):
            current_actions = obj.actions
            permitted_actions = trans.app.model.Library.permitted_actions.items()
            obj_str = 'library dataset %s' % obj_name
            obj_type = 'library'
        elif isinstance( obj, trans.app.model.LibraryFolder ):
            current_actions = obj.actions
            permitted_actions = trans.app.model.Library.permitted_actions.items()
            obj_str = 'library folder %s' % obj_name
            obj_type = 'library'
        else:
            current_actions = []
            permitted_actions = {}.items()
            obj_str = 'unknown object %s' %obj_name
            obj_type = ''
            
        
        # SOURCE LINE 82
        __M_writer(u'\n    <script type="text/javascript">\n        $( document ).ready( function () {\n            $( \'.role_add_button\' ).click( function() {\n                var action = this.id.substring( 0, this.id.lastIndexOf( \'_add_button\' ) )\n                var in_select = \'#\' + action + \'_in_select\';\n                var out_select = \'#\' + action + \'_out_select\';\n                return !$( out_select + \' option:selected\' ).remove().appendTo( in_select );\n            });\n            $( \'.role_remove_button\' ).click( function() {\n                var action = this.id.substring( 0, this.id.lastIndexOf( \'_remove_button\' ) )\n                var in_select = \'#\' + action + \'_in_select\';\n                var out_select = \'#\' + action + \'_out_select\';\n                return !$( in_select + \' option:selected\' ).remove().appendTo( out_select );\n            });\n            $( \'form#edit_role_associations\' ).submit( function() {\n                $( \'.in_select option\' ).each(function( i ) {\n                    $( this ).attr( "selected", "selected" );\n                });\n            });\n        });\n    </script>\n    <div class="toolForm">\n        <div class="toolFormTitle">Manage ')
        # SOURCE LINE 105
        __M_writer(unicode(obj_type))
        __M_writer(u' permissions on ')
        __M_writer(unicode(obj_str))
        __M_writer(u'</div>\n        <div class="toolFormBody">\n            <form name="edit_role_associations" id="edit_role_associations" action="')
        # SOURCE LINE 107
        __M_writer(unicode(form_url))
        __M_writer(u'" method="post">\n                <div class="form-row"></div>\n')
        # SOURCE LINE 109
        for k, v in permitted_actions:
            # SOURCE LINE 110
            if k not in do_not_render:
                # SOURCE LINE 111
                __M_writer(u'                        <div class="form-row">\n                            ')
                # SOURCE LINE 112
                __M_writer(unicode(render_select( current_actions, k, v, all_roles )))
                __M_writer(u'\n                        </div>\n')
        # SOURCE LINE 116
        __M_writer(u'                <div class="form-row">\n                    <input type="submit" name="update_roles_button" value="Save"/>\n                </div>\n            </form>\n        </div>\n    </div>\n    <p/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_select(context,current_actions,action_key,action,all_roles):
    context.caller_stack._push_frame()
    try:
        filter = context.get('filter', UNDEFINED)
        x = context.get('x', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n    ')
        # SOURCE LINE 2

        import sets
        in_roles = sets.Set()
        for a in current_actions:
            if a.action == action.action:
                in_roles.add( a.role )
        out_roles = filter( lambda x: x not in in_roles, all_roles )
            
        
        # SOURCE LINE 9
        __M_writer(u'\n    <p>\n        <b>')
        # SOURCE LINE 11
        __M_writer(unicode(action.action))
        __M_writer(u':</b> ')
        __M_writer(unicode(action.description))
        __M_writer(u'\n')
        # SOURCE LINE 12
        if action == trans.app.security_agent.permitted_actions.DATASET_ACCESS:
            # SOURCE LINE 13
            __M_writer(u'            <br/>\n            NOTE: Users must have every role associated with this dataset in order to access it\n')
        # SOURCE LINE 16
        __M_writer(u'    </p>\n    <div style="width: 100%; white-space: nowrap;">\n        <div style="float: left; width: 50%;">\n            Roles associated:<br/>\n            <select name="')
        # SOURCE LINE 20
        __M_writer(unicode(action_key))
        __M_writer(u'_in" id="')
        __M_writer(unicode(action_key))
        __M_writer(u'_in_select" class="in_select" style="max-width: 98%; width: 98%; height: 150px; font-size: 100%;" multiple>\n')
        # SOURCE LINE 21
        for role in in_roles:
            # SOURCE LINE 22
            __M_writer(u'                    <option value="')
            __M_writer(unicode(role.id))
            __M_writer(u'">')
            __M_writer(unicode(role.name))
            __M_writer(u'</option>\n')
        # SOURCE LINE 24
        __M_writer(u'            </select> <br/>\n            <div style="width: 98%; text-align: right"><input type="submit" id="')
        # SOURCE LINE 25
        __M_writer(unicode(action_key))
        __M_writer(u'_remove_button" class="role_remove_button" value=">>"/></div>\n        </div>\n        <div style="width: 50%;">\n            Roles not associated:<br/>\n            <select name="')
        # SOURCE LINE 29
        __M_writer(unicode(action_key))
        __M_writer(u'_out" id="')
        __M_writer(unicode(action_key))
        __M_writer(u'_out_select" style="max-width: 98%; width: 98%; height: 150px; font-size: 100%;" multiple>\n')
        # SOURCE LINE 30
        for role in out_roles:
            # SOURCE LINE 31
            __M_writer(u'                    <option value="')
            __M_writer(unicode(role.id))
            __M_writer(u'">')
            __M_writer(unicode(role.name))
            __M_writer(u'</option>\n')
        # SOURCE LINE 33
        __M_writer(u'            </select> <br/>\n            <input type="submit" id="')
        # SOURCE LINE 34
        __M_writer(unicode(action_key))
        __M_writer(u'_add_button" class="role_add_button" value="<<"/>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


