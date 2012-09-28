# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1336498137.777849
_template_filename='templates/root/index.mako'
_template_uri='root/index.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['init', 'left_panel', 'center_panel', 'late_javascripts', 'right_panel']


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
    return runtime._inherit_from(context, u'/webapps/galaxy/base_panels.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 184
        __M_writer(u'\n\n')
        # SOURCE LINE 199
        __M_writer(u'\n\n')
        # SOURCE LINE 213
        __M_writer(u'\n\n')
        # SOURCE LINE 233
        __M_writer(u'\n\n')
        # SOURCE LINE 247
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 186
        __M_writer(u'\n')
        # SOURCE LINE 187

        self.has_left_panel = True
        self.has_right_panel = True
        self.active_view = "analysis"
        
        
        # SOURCE LINE 191
        __M_writer(u'\n')
        # SOURCE LINE 192
        if trans.app.config.require_login and not trans.user:
            # SOURCE LINE 193
            __M_writer(u'    <script type="text/javascript">\n        if ( window != top ) {\n            top.location.href = location.href;\n        }\n    </script>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_panel(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        n_ = context.get('n_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 201
        __M_writer(u'\n    <div class="unified-panel-header" unselectable="on">\n        <div class=\'unified-panel-header-inner\'>\n            <div style="float: right">\n                <a class=\'panel-header-button\' id="tools-options-button" href="#"><span class="ficon large cog"></span></a>\n            </div>\n            ')
        # SOURCE LINE 207
        __M_writer(unicode(n_('Tools')))
        __M_writer(u'\n        </div>\n    </div>\n    <div class="unified-panel-body" style="overflow: hidden;">\n        <iframe name="galaxy_tools" id="galaxy_tools" src="')
        # SOURCE LINE 211
        __M_writer(unicode(h.url_for( controller='root', action='tool_menu' )))
        __M_writer(u'" frameborder="0" style="position: absolute; margin: 0; border: 0 none; height: 100%; width: 100%;"> </iframe>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    context.caller_stack._push_frame()
    try:
        tool_id = context.get('tool_id', UNDEFINED)
        m_c = context.get('m_c', UNDEFINED)
        h = context.get('h', UNDEFINED)
        m_a = context.get('m_a', UNDEFINED)
        workflow_id = context.get('workflow_id', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 215
        __M_writer(u'\n\n')
        # SOURCE LINE 218
        __M_writer(u'    ')

        if trans.app.config.require_login and not trans.user:
            center_url = h.url_for( controller='user', action='login' )
        elif tool_id is not None:
            center_url = h.url_for( 'tool_runner', tool_id=tool_id, from_noframe=True )
        elif workflow_id is not None:
            center_url = h.url_for( controller='workflow', action='run', id=workflow_id )
        elif m_c is not None:
            center_url = h.url_for( controller=m_c, action=m_a )
        else:
            center_url = h.url_for( '/static/welcome.html' )
        
        
        # SOURCE LINE 229
        __M_writer(u'\n    \n    <iframe name="galaxy_main" id="galaxy_main" frameborder="0" style="position: absolute; width: 100%; height: 100%;" src="')
        # SOURCE LINE 231
        __M_writer(unicode(center_url))
        __M_writer(u'"></iframe>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_javascripts(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n    ')
        # SOURCE LINE 4
        __M_writer(unicode(parent.late_javascripts()))
        __M_writer(u'\n    <script type="text/javascript">\n    // Set up GalaxyAsync object.\n    var galaxy_async = new GalaxyAsync();\n    galaxy_async.set_func_url(galaxy_async.set_user_pref, "')
        # SOURCE LINE 8
        __M_writer(unicode(h.url_for( controller='user', action='set_user_pref_async' )))
        __M_writer(u'");\n    \n    $(function(){\n        // Init history options.\n        $("#history-options-button").css( "position", "relative" );\n        make_popupmenu( $("#history-options-button"), {\n            "')
        # SOURCE LINE 14
        __M_writer(unicode(_("History Lists")))
        __M_writer(u'": null,\n            "')
        # SOURCE LINE 15
        __M_writer(unicode(_("Saved Histories")))
        __M_writer(u'": function() {\n                galaxy_main.location = "')
        # SOURCE LINE 16
        __M_writer(unicode(h.url_for( controller='history', action='list')))
        __M_writer(u'";\n            },\n            "')
        # SOURCE LINE 18
        __M_writer(unicode(_("Histories Shared with Me")))
        __M_writer(u'": function() {\n                galaxy_main.location = "')
        # SOURCE LINE 19
        __M_writer(unicode(h.url_for( controller='history', action='list_shared')))
        __M_writer(u'";\n            },\n            "')
        # SOURCE LINE 21
        __M_writer(unicode(_("Current History")))
        __M_writer(u'": null,\n            "')
        # SOURCE LINE 22
        __M_writer(unicode(_("Create New")))
        __M_writer(u'": function() {\n                galaxy_history.location = "')
        # SOURCE LINE 23
        __M_writer(unicode(h.url_for( controller='root', action='history_new' )))
        __M_writer(u'";\n            },\n            "')
        # SOURCE LINE 25
        __M_writer(unicode(_("Clone")))
        __M_writer(u'": function() {\n                galaxy_main.location = "')
        # SOURCE LINE 26
        __M_writer(unicode(h.url_for( controller='history', action='clone')))
        __M_writer(u'";\n            },\n            "')
        # SOURCE LINE 28
        __M_writer(unicode(_("Copy Datasets")))
        __M_writer(u'": function() {\n                galaxy_main.location = "')
        # SOURCE LINE 29
        __M_writer(unicode(h.url_for( controller='dataset', action='copy_datasets' )))
        __M_writer(u'";\n            },\n            "')
        # SOURCE LINE 31
        __M_writer(unicode(_("Share or Publish")))
        __M_writer(u'": function() {\n                galaxy_main.location = "')
        # SOURCE LINE 32
        __M_writer(unicode(h.url_for( controller='history', action='sharing' )))
        __M_writer(u'";\n            },\n            "')
        # SOURCE LINE 34
        __M_writer(unicode(_("Extract Workflow")))
        __M_writer(u'": function() {\n                galaxy_main.location = "')
        # SOURCE LINE 35
        __M_writer(unicode(h.url_for( controller='workflow', action='build_from_current_history' )))
        __M_writer(u'";\n            },\n            "')
        # SOURCE LINE 37
        __M_writer(unicode(_("Dataset Security")))
        __M_writer(u'": function() {\n                galaxy_main.location = "')
        # SOURCE LINE 38
        __M_writer(unicode(h.url_for( controller='root', action='history_set_default_permissions' )))
        __M_writer(u'";\n            },\n            "')
        # SOURCE LINE 40
        __M_writer(unicode(_("Show Deleted Datasets")))
        __M_writer(u'": function() {\n                galaxy_history.location = "')
        # SOURCE LINE 41
        __M_writer(unicode(h.url_for( controller='root', action='history', show_deleted=True)))
        __M_writer(u'";\n            },\n            "')
        # SOURCE LINE 43
        __M_writer(unicode(_("Show Hidden Datasets")))
        __M_writer(u'": function() {\n                galaxy_history.location = "')
        # SOURCE LINE 44
        __M_writer(unicode(h.url_for( controller='root', action='history', show_hidden=True)))
        __M_writer(u'";\n            },\n            "')
        # SOURCE LINE 46
        __M_writer(unicode(_("Purge Deleted Datasets")))
        __M_writer(u'": function() {\n                if ( confirm( "Really delete all deleted datasets permanently? This cannot be undone." ) ) {\n                    galaxy_main.location = "')
        # SOURCE LINE 48
        __M_writer(unicode(h.url_for( controller='history', action='purge_deleted_datasets' )))
        __M_writer(u'";\n                }\n            },\n            "')
        # SOURCE LINE 51
        __M_writer(unicode(_("Show Structure")))
        __M_writer(u'": function() {\n                galaxy_main.location = "')
        # SOURCE LINE 52
        __M_writer(unicode(h.url_for( controller='history', action='display_structured' )))
        __M_writer(u'";\n            },\n            "')
        # SOURCE LINE 54
        __M_writer(unicode(_("Export to File")))
        __M_writer(u'": function() {\n                galaxy_main.location = "')
        # SOURCE LINE 55
        __M_writer(unicode(h.url_for( controller='history', action='export_archive' )))
        __M_writer(u'";\n            },\n            "')
        # SOURCE LINE 57
        __M_writer(unicode(_("Delete")))
        __M_writer(u'": function() {\n                if ( confirm( "Really delete the current history?" ) ) {\n                    galaxy_main.location = "')
        # SOURCE LINE 59
        __M_writer(unicode(h.url_for( controller='history', action='delete_current' )))
        __M_writer(u'";\n                }\n            },\n            "')
        # SOURCE LINE 62
        __M_writer(unicode(_("Delete Permanently")))
        __M_writer(u'": function() {\n                if ( confirm( "Really delete the current history permanently? This cannot be undone." ) ) {\n                    galaxy_main.location = "')
        # SOURCE LINE 64
        __M_writer(unicode(h.url_for( controller='history', action='delete_current', purge=True )))
        __M_writer(u'";\n                }\n            },\n            "')
        # SOURCE LINE 67
        __M_writer(unicode(_("Other Actions")))
        __M_writer(u'": null,\n            "')
        # SOURCE LINE 68
        __M_writer(unicode(_("Import from File")))
        __M_writer(u'": function() {\n                galaxy_main.location = "')
        # SOURCE LINE 69
        __M_writer(unicode(h.url_for( controller='history', action='import_archive' )))
        __M_writer(u'";\n            }\n        });\n        \n        var menu_options = {}; // Holds dictionary of { label: toggle_fn }\n        \n        SHOW_TOOL = "')
        # SOURCE LINE 75
        __M_writer(unicode(_("Show Tool Search")))
        __M_writer(u'";\n        HIDE_TOOL = "')
        # SOURCE LINE 76
        __M_writer(unicode(_("Hide Tool Search")))
        __M_writer(u'";\n        SHOW_RECENT = "')
        # SOURCE LINE 77
        __M_writer(unicode(_("Show Recently Used")))
        __M_writer(u'";\n        HIDE_RECENT = "')
        # SOURCE LINE 78
        __M_writer(unicode(_("Hide Recently Used")))
        __M_writer(u'";\n        \n        var toggle_tool_search_fn = function() {\n            // Show/hide menu and update vars, user preferences.\n            var menu = $("#galaxy_tools").contents().find(\'#tool-search\'),\n                pref_value, menu_option_text, old_text;\n            if (menu.is(":visible")) {\n                // Hide menu.\n                pref_value = "False";\n                menu_option_text = SHOW_TOOL;\n                old_text = HIDE_TOOL;\n                \n                // Reset search.\n                reset_tool_search(true);\n            } else {\n                // Show menu.\n                pref_value = "True";\n                menu_option_text = HIDE_TOOL;\n                old_text = SHOW_TOOL;\n            }\n            menu.toggle();\n    \n            // Update menu option.\n            delete menu_options[old_text];\n            \n            var new_menu_options = {}; \n            // Because we always want tool menu to be the first link in the dropdown,\n            // we re-create the menu_options dictionary by creating a new\n            // dict and then appending the old dict to it\n            new_menu_options[menu_option_text] = toggle_tool_search_fn;\n            menu_options = $.extend( new_menu_options, menu_options );\n            make_popupmenu( $("#tools-options-button"), menu_options );\n            galaxy_async.set_user_pref("show_tool_search", pref_value);\n        };\n        \n        var toggle_recently_used_fn = function() {\n            // Show/hide menu.\n            var ru_menu = $(\'#galaxy_tools\').contents().find(\'#recently_used_wrapper\'),\n                ru_menu_body = ru_menu.find(".toolSectionBody"),\n                pref_value, old_text, menu_option_text;\n            if (ru_menu.hasClass("user_pref_visible")) {\n                // Hide menu.\n                ru_menu_body.slideUp();\n                ru_menu.slideUp();\n                \n                // Set vars used below and in tool menu frame.\n                pref_value = "False";\n                old_text = HIDE_RECENT;\n                menu_option_text = SHOW_RECENT;\n            } else {\n                // "Show" menu.\n                if (!$(\'#galaxy_tools\').contents().find(\'#tool-search-query\').hasClass("search_active")) {\n                    // Default.\n                    ru_menu.slideDown();\n                } else {\n                    // Search active: tf there are matching tools in RU menu, show menu.\n                    if ( ru_menu.find(".toolTitle.search_match").length !== 0 ) {\n                        ru_menu.slideDown();\n                        ru_menu_body.slideDown();\n                    }\n                }\n                // Set vars used below and in tool menu frame.\n                pref_value = "True";\n                old_text = SHOW_RECENT;\n                menu_option_text = HIDE_RECENT;\n            }\n            \n            // Update menu class and option.\n            ru_menu.toggleClass("user_pref_hidden user_pref_visible");\n            delete menu_options[old_text];\n            menu_options[menu_option_text] = toggle_recently_used_fn;\n            make_popupmenu( $("#tools-options-button"), menu_options );\n            galaxy_async.set_user_pref("show_recently_used_menu", pref_value);\n        };\n        \n        // Init tool options.\n')
        # SOURCE LINE 155
        if trans.app.toolbox_search.enabled:
            # SOURCE LINE 156
            __M_writer(u'            ')
 
            show_tool_search = True
            if trans.user:
                show_tool_search = trans.user.preferences.get( "show_tool_search", "False" ) == "True"
                
            if show_tool_search:
                action = "HIDE_TOOL"
            else:
                action = "SHOW_TOOL"
                        
            
            # SOURCE LINE 165
            __M_writer(u'\n            menu_options[ ')
            # SOURCE LINE 166
            __M_writer(unicode(action))
            __M_writer(u' ] = toggle_tool_search_fn;\n')
            pass
        # SOURCE LINE 169
        if trans.user:
            # SOURCE LINE 170
            __M_writer(u'            ')

            if trans.user.preferences.get( 'show_recently_used_menu', 'False' ) == 'True':
                action = "HIDE_RECENT"
            else:
                action = "SHOW_RECENT"
                        
            
            # SOURCE LINE 175
            __M_writer(u'\n            // TODO: make compatible with new tool menu.\n            //menu_options[ ')
            # SOURCE LINE 177
            __M_writer(unicode(action))
            __M_writer(u' ] = toggle_recently_used_fn;\n')
            pass
        # SOURCE LINE 179
        __M_writer(u'        \n        \n        make_popupmenu( $("#tools-options-button"), menu_options );\n    });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_panel(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 235
        __M_writer(u'\n    <div class="unified-panel-header" unselectable="on">\n        <div class="unified-panel-header-inner">\n            <div style="float: right">\n                <a id="history-options-button" class=\'panel-header-button\' href="')
        # SOURCE LINE 239
        __M_writer(unicode(h.url_for( controller='root', action='history_options' )))
        __M_writer(u'" target="galaxy_main"><span class="ficon large cog"></span></a>\n            </div>\n            <div class="panel-header-text">')
        # SOURCE LINE 241
        __M_writer(unicode(_('History')))
        __M_writer(u'</div>\n        </div>\n    </div>\n    <div class="unified-panel-body" style="overflow: hidden;">\n        <iframe name="galaxy_history" width="100%" height="100%" frameborder="0" style="position: absolute; margin: 0; border: 0 none; height: 100%;" src="')
        # SOURCE LINE 245
        __M_writer(unicode(h.url_for( controller='root', action='history' )))
        __M_writer(u'"></iframe>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


