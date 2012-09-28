# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1336505820.0846679
_template_filename='templates/root/tool_menu.mako'
_template_uri='/root/tool_menu.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['stylesheets', 'title', 'javascripts', 'render_workflow']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 3
    ns = runtime.TemplateNamespace('__anon_0x603dc10', context._clean_inheritance_tokens(), templateuri=u'/tagging_common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x603dc10')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x603dc10')._populate(_import_ns, [u'render_tool_tagging_elements'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        t = _import_ns.get('t', context.get('t', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 3
        __M_writer(u'\n\n')
        # SOURCE LINE 15
        __M_writer(u'\n\n')
        # SOURCE LINE 77
        __M_writer(u'\n\n')
        # SOURCE LINE 82
        __M_writer(u'\n\n\n')
        # SOURCE LINE 87
        __M_writer(u'\n\n')
        # SOURCE LINE 90
        __M_writer(u'<body class="toolMenuContainer">\n    \n    <div class="toolMenu">\n')
        # SOURCE LINE 94
        __M_writer(u'        <div id="search-no-results" style="display: none; padding-top: 5px">\n            <em><strong>Search did not match any tools.</strong></em>\n        </div>\n        \n')
        # SOURCE LINE 101
        __M_writer(u'        \n')
        # SOURCE LINE 102
        if t.user:
            # SOURCE LINE 103
            __M_writer(u'            <div class="toolSectionPad"></div>\n            <div class="toolSectionPad"></div>\n            <div class="toolSectionTitle" id="title_XXinternalXXworkflow">\n              <span>Workflows</span>\n            </div>\n            <div id="XXinternalXXworkflow" class="toolSectionBody">\n                <div class="toolSectionBg">\n')
            # SOURCE LINE 110
            if t.user.stored_workflow_menu_entries:
                # SOURCE LINE 111
                for m in t.user.stored_workflow_menu_entries:
                    # SOURCE LINE 112
                    __M_writer(u'                            <div class="toolTitle">\n                                <a href="')
                    # SOURCE LINE 113
                    __M_writer(unicode(h.url_for( controller='workflow', action='run', id=trans.security.encode_id(m.stored_workflow_id) )))
                    __M_writer(u'" target="galaxy_main">')
                    __M_writer(unicode(m.stored_workflow.name))
                    __M_writer(u'</a>\n                            </div>\n')
                    pass
                pass
            # SOURCE LINE 117
            __M_writer(u'                    <div class="toolTitle">\n                        <a href="')
            # SOURCE LINE 118
            __M_writer(unicode(h.url_for( controller='workflow', action='list_for_run')))
            __M_writer(u'" target="galaxy_main">All workflows</a>\n                    </div>\n                </div>\n            </div>\n')
            pass
        # SOURCE LINE 123
        __M_writer(u'        \n    </div>\n</body>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x603dc10')._populate(_import_ns, [u'render_tool_tagging_elements'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 79
        __M_writer(u'\n    ')
        # SOURCE LINE 80
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n    ')
        # SOURCE LINE 81
        __M_writer(unicode(h.css("tool_menu")))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x603dc10')._populate(_import_ns, [u'render_tool_tagging_elements'])
        _ = _import_ns.get('_', context.get('_', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 85
        __M_writer(u'\n    ')
        # SOURCE LINE 86
        __M_writer(unicode(_('Galaxy Tools')))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x603dc10')._populate(_import_ns, [u'render_tool_tagging_elements'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 17
        __M_writer(u'\n    ')
        # SOURCE LINE 18
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n    ')
        # SOURCE LINE 19
        __M_writer(unicode(h.templates( "tool_link", "panel_section", "tool_search" )))
        __M_writer(u'\n    ')
        # SOURCE LINE 20
        __M_writer(unicode(h.js( "galaxy.base", "json2", "autocomplete_tagging", "mvc/tools" )))
        __M_writer(u'\n    \n    ')
        # SOURCE LINE 22

        # Set up for creating tool panel.
        tool_search_hidden = "false"
        if trans.user and trans.user.preferences.get( "show_tool_search", "False" ) == "False":
            tool_search_hidden = "true"
        
        dictified_panel = trans.app.toolbox.to_dict( trans )
            
        
        # SOURCE LINE 29
        __M_writer(u'\n    \n    <script type="text/javascript">\n        // Init. on document load.\n        var tool_panel, tool_panel_view, tool_search;\n        $(function() {\n            // Set up search.\n            tool_search = new ToolSearch( {spinner_url: "')
        # SOURCE LINE 36
        __M_writer(unicode(h.url_for('/static/images/loading_small_white_bg.gif')))
        __M_writer(u'",\n                                           search_url: "')
        # SOURCE LINE 37
        __M_writer(unicode(h.url_for( controller='root', action='tool_search' )))
        __M_writer(u'",\n                                           hidden: ')
        # SOURCE LINE 38
        __M_writer(unicode(tool_search_hidden))
        __M_writer(u' } );\n            \n            // Set up tool panel.\n            tool_panel = new ToolPanel( { tool_search: tool_search } );\n            tool_panel.reset( tool_panel.parse( ')
        # SOURCE LINE 42
        __M_writer(unicode(h.to_json_string( dictified_panel )))
        __M_writer(u' ) );\n            \n            // Set up tool panel view and initialize.\n            tool_panel_view = new ToolPanelView( {collection: tool_panel} );\n            tool_panel_view.render();\n            $(\'body\').prepend(tool_panel_view.$el);\n                        \n            // Minsize init hint.\n            $( "a[minsizehint]" ).click( function() {\n                if ( parent.handle_minwidth_hint ) {\n                    parent.handle_minwidth_hint( $(this).attr( "minsizehint" ) );\n                }\n            });\n            \n            // Log clicks on tools.\n            /*\n            $("div.toolTitle > a").click( function() {\n                var tool_title = $(this).attr(\'id\').split("-")[1];\n                var section_title = $.trim( $(this).parents("div.toolSectionWrapper").find("div.toolSectionTitle").text() );\n                var search_active = $(this).parents("div.toolTitle").hasClass("search_match");\n                \n                // Log action.\n                galaxy_async.log_user_action("tool_menu_click." + tool_title, section_title, \n                                                JSON.stringify({"search_active" : search_active}));\n            });\n            */\n            \n            // TODO: is this necessary?\n            $( "a[minsizehint]" ).click( function() {\n                if ( parent.handle_minwidth_hint ) {\n                    parent.handle_minwidth_hint( $(this).attr( "minsizehint" ) );\n                }\n            });\n        });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_workflow(context,key,workflow,section):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x603dc10')._populate(_import_ns, [u'render_tool_tagging_elements'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        _ = _import_ns.get('_', context.get('_', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 6
        __M_writer(u'\n')
        # SOURCE LINE 7
        if section:
            # SOURCE LINE 8
            __M_writer(u'        <div class="toolTitle">\n')
            # SOURCE LINE 9
        else:
            # SOURCE LINE 10
            __M_writer(u'        <div class="toolTitleNoSection">\n')
            pass
        # SOURCE LINE 12
        __M_writer(u'        ')
        encoded_id = key.lstrip( 'workflow_' ) 
        
        __M_writer(u'\n        <a id="link-')
        # SOURCE LINE 13
        __M_writer(unicode(workflow.id))
        __M_writer(u'" href="')
        __M_writer(unicode( h.url_for( controller='workflow', action='run', id=encoded_id )))
        __M_writer(u'" target="_parent">')
        __M_writer(unicode(_(workflow.name)))
        __M_writer(u'</a>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


