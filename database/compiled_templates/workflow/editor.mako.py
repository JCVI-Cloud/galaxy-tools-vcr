from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1292434266.4580369
_template_filename='templates/workflow/editor.mako'
_template_uri='workflow/editor.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding=None
_exports = ['left_panel', 'overlay', 'render_label', 'center_panel', 'late_javascripts', 'right_panel', 'stylesheets', 'init', 'javascripts', 'render_tool']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 1070
    ns = runtime.Namespace('__anon_0x653ca50', context._clean_inheritance_tokens(), templateuri=u'/tagging_common.mako', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, '__anon_0x653ca50')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/webapps/galaxy/base_panels.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x653ca50')._populate(_import_ns, [u'render_individual_tagging_element'])
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 8
        __M_writer(u'\n\n')
        # SOURCE LINE 18
        __M_writer(u'\n\n')
        # SOURCE LINE 727
        __M_writer(u'\n\n')
        # SOURCE LINE 894
        __M_writer(u'\n\n')
        # SOURCE LINE 929
        __M_writer(u'\n\n')
        # SOURCE LINE 936
        __M_writer(u'\n\n')
        # SOURCE LINE 941
        __M_writer(u'\n\n')
        # SOURCE LINE 1018
        __M_writer(u'\n\n')
        # SOURCE LINE 1051
        __M_writer(u'\n\n')
        # SOURCE LINE 1114
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_panel(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x653ca50')._populate(_import_ns, [u'render_individual_tagging_element'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        app = _import_ns.get('app', context.get('app', UNDEFINED))
        def render_label(label):
            return render_render_label(context,label)
        _ = _import_ns.get('_', context.get('_', UNDEFINED))
        n_ = _import_ns.get('n_', context.get('n_', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        def render_tool(tool,section):
            return render_render_tool(context,tool,section)
        __M_writer = context.writer()
        # SOURCE LINE 943
        __M_writer(u'\n    <div class="unified-panel-header" unselectable="on">\n        <div class=\'unified-panel-header-inner\'>\n            <div style="float: right">\n                <a class=\'panel-header-button popup\' id="tools-options-button" href="#">')
        # SOURCE LINE 947
        __M_writer(unicode(_('Options')))
        __M_writer(u'</a>\n            </div>\n            ')
        # SOURCE LINE 949
        __M_writer(unicode(n_('Tools')))
        __M_writer(u'\n        </div>\n    </div>\n    \n    <div class="unified-panel-body" style="overflow: auto;">\n            <div class="toolMenu">\n')
        # SOURCE LINE 956
        __M_writer(u'            ')

        show_tool_search = False
        if trans.user:
            show_tool_search = trans.user.preferences.get( "workflow.show_tool_search", "True" )
                    
        if show_tool_search == "True":
            display = "block"
        else:
            display = "none"
                    
        
        # SOURCE LINE 965
        __M_writer(u'\n            <div id="tool-search" style="padding-bottom: 5px; position: relative; display: ')
        # SOURCE LINE 966
        __M_writer(unicode(display))
        __M_writer(u'; width: 100%">\n                <input type="text" name="query" value="search tools" id="tool-search-query" style="width: 100%; font-style:italic; font-size: inherit"/>\n                <img src="')
        # SOURCE LINE 968
        __M_writer(unicode(h.url_for('/static/images/loading_small_white_bg.gif')))
        __M_writer(u'" id="search-spinner" style="display: none; position: absolute; right: 0; top: 5px;"/>\n            </div>\n        \n            <div class="toolSectionList">\n')
        # SOURCE LINE 972
        for key, val in app.toolbox.tool_panel.items():
            # SOURCE LINE 973
            __M_writer(u'                    <div class="toolSectionWrapper">\n')
            # SOURCE LINE 974
            if key.startswith( 'tool' ):
                # SOURCE LINE 975
                __M_writer(u'                        ')
                __M_writer(unicode(render_tool( val, False )))
                __M_writer(u'\n')
                # SOURCE LINE 976
            elif key.startswith( 'section' ):
                # SOURCE LINE 977
                __M_writer(u'                    ')
                section = val 
                
                __M_writer(u'\n                        <div class="toolSectionTitle" id="title_')
                # SOURCE LINE 978
                __M_writer(unicode(section.id))
                __M_writer(u'">\n                            <span>')
                # SOURCE LINE 979
                __M_writer(unicode(section.name))
                __M_writer(u'</span>\n                        </div>\n                        <div id="')
                # SOURCE LINE 981
                __M_writer(unicode(section.id))
                __M_writer(u'" class="toolSectionBody">\n                            <div class="toolSectionBg">\n')
                # SOURCE LINE 983
                for section_key, section_val in section.elems.items():
                    # SOURCE LINE 984
                    if section_key.startswith( 'tool' ):
                        # SOURCE LINE 985
                        __M_writer(u'                                        ')
                        __M_writer(unicode(render_tool( section_val, True )))
                        __M_writer(u'\n')
                        # SOURCE LINE 986
                    elif section_key.startswith( 'label' ):
                        # SOURCE LINE 987
                        __M_writer(u'                                        ')
                        __M_writer(unicode(render_label( section_val )))
                        __M_writer(u'\n')
                # SOURCE LINE 990
                __M_writer(u'                            </div>\n                        </div>\n')
                # SOURCE LINE 992
            elif key.startswith( 'label' ):
                # SOURCE LINE 993
                __M_writer(u'                        ')
                __M_writer(unicode(render_label( val )))
                __M_writer(u'\n')
            # SOURCE LINE 995
            __M_writer(u'                    <div class="toolSectionPad"></div>\n                    </div>\n')
        # SOURCE LINE 998
        __M_writer(u'            </div>\n')
        # SOURCE LINE 1000
        __M_writer(u'            <div id="search-no-results" style="display: none; padding-top: 5px">\n                <em><strong>Search did not match any tools.</strong></em>\n            </div>\n            <div>&nbsp;</div>\n            <div class="toolMenuGroupHeader">Workflow control</div>\n            <div class="toolSectionTitle" id="title___workflow__input__">\n                <span>Inputs</span>\n            </div>\n            <div id="__workflow__input__" class="toolSectionBody">\n                <div class="toolSectionBg">\n                    <div class="toolTitle">\n                        <a href="#" onclick="add_node_for_module( \'data_input\', \'Input Dataset\' )">Input dataset</a>\n                    </div>\n                </div>\n            </div>                    \n        </div>\n    </div>\n    \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_overlay(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x653ca50')._populate(_import_ns, [u'render_individual_tagging_element'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 938
        __M_writer(u'\n    ')
        # SOURCE LINE 939
        __M_writer(unicode(parent.overlay( "Loading workflow editor...",
                      "<img src='" + h.url_for('/static/images/yui/rel_interstitial_loading.gif') + "'/>" )))
        # SOURCE LINE 940
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_label(context,label):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x653ca50')._populate(_import_ns, [u'render_individual_tagging_element'])
        __M_writer = context.writer()
        # SOURCE LINE 932
        __M_writer(u'\n    <div class="toolPanelLabel" id="title_')
        # SOURCE LINE 933
        __M_writer(unicode(label.id))
        __M_writer(u'">\n        <span>')
        # SOURCE LINE 934
        __M_writer(unicode(label.text))
        __M_writer(u'</span>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x653ca50')._populate(_import_ns, [u'render_individual_tagging_element'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        stored = _import_ns.get('stored', context.get('stored', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1020
        __M_writer(u'\n\n    <div class="unified-panel-header" unselectable="on">\n        <div class="unified-panel-header-inner" style="float: right">\n            <a id="workflow-options-button" class="panel-header-button popup" href="#">Options</a>\n        </div>\n        <div class="unified-panel-header-inner">\n            Workflow Canvas | ')
        # SOURCE LINE 1027
        __M_writer(filters.html_escape(unicode(h.to_unicode( stored.name ) )))
        __M_writer(u'\n        </div>\n    </div>\n\n    <div class="unified-panel-body">\n        <div id="canvas-viewport" style="width: 100%; height: 100%; position: absolute; overflow: hidden; background: #EEEEEE; background: white url(')
        # SOURCE LINE 1032
        __M_writer(unicode(h.url_for('/static/images/light_gray_grid.gif')))
        __M_writer(u') repeat;">\n            <div id="canvas-container" style="position: absolute; width: 100%; height: 100%;"></div>\n        </div>\n        <div id="overview-border" style="position: absolute; width: 150px; height: 150px; right: 20000px; bottom: 0px; border-top: solid gray 1px; border-left: solid grey 1px; padding: 7px 0 0 7px; background: #EEEEEE no-repeat url(')
        # SOURCE LINE 1035
        __M_writer(unicode(h.url_for('/static/images/resizable.png')))
        __M_writer(u'); z-index: 20000; overflow: hidden; max-width: 300px; max-height: 300px; min-width: 50px; min-height: 50px">\n            <div style="position: relative; overflow: hidden; width: 100%; height: 100%; border-top: solid gray 1px; border-left: solid grey 1px;">\n                <div id="overview" style="position: absolute;">\n                    <canvas width="0" height="0" style="background: white; width: 100%; height: 100%;" id="overview-canvas"></canvas>\n                    <div id="overview-viewport" style="position: absolute; width: 0px; height: 0px; border: solid blue 1px; z-index: 10;"></div>\n                </div>\n            </div>\n        </div>\n        <div id=\'workflow-parameters-box\' style="display:none; position: absolute; /*width: 150px; height: 150px;*/ right: 0px; top: 0px; border-bottom: solid gray 1px; border-left: solid grey 1px; padding: 7px; background: #EEEEEE; z-index: 20000; overflow: hidden; max-width: 300px; max-height: 300px; /*min-width: 50px; min-height: 50px*/">\n            <div style="margin-bottom:5px;"><b>Workflow Parameters</b></div>\n            <div id="workflow-parameters-container">\n            </div>\n        </div>\n        <div id="close-viewport" style="border-left: 1px solid #999; border-top: 1px solid #999; background: #ddd url(')
        # SOURCE LINE 1048
        __M_writer(unicode(h.url_for('/static/images/overview_arrows.png')))
        __M_writer(u') 12px 0px; position: absolute; right: 0px; bottom: 0px; width: 12px; height: 12px; z-index: 25000;"></div>\n    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x653ca50')._populate(_import_ns, [u'render_individual_tagging_element'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 10
        __M_writer(u'\n    <script type=\'text/javascript\' src="')
        # SOURCE LINE 11
        __M_writer(unicode(h.url_for('/static/scripts/galaxy.panels.js')))
        __M_writer(u'"> </script>\n    <script type="text/javascript">\n        ensure_dd_helper();\n        make_left_panel( $("#left"), $("#center"), $("#left-border" ) );\n        make_right_panel( $("#right"), $("#center"), $("#right-border" ) );\n')
        # SOURCE LINE 17
        __M_writer(u'    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_panel(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x653ca50')._populate(_import_ns, [u'render_individual_tagging_element'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        stored = _import_ns.get('stored', context.get('stored', UNDEFINED))
        annotation = _import_ns.get('annotation', context.get('annotation', UNDEFINED))
        render_individual_tagging_element = _import_ns.get('render_individual_tagging_element', context.get('render_individual_tagging_element', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1053
        __M_writer(u'\n    <div class="unified-panel-header" unselectable="on">\n        <div class="unified-panel-header-inner">\n            Details\n        </div>\n    </div>\n    <div class="unified-panel-body" style="overflow: auto;">\n')
        # SOURCE LINE 1061
        __M_writer(u'        <div id="edit-attributes" class="metadataForm right-content">\n            <div class="metadataFormTitle">Edit Workflow Attributes</div>\n            <div class="metadataFormBody">\n')
        # SOURCE LINE 1065
        __M_writer(u'            <div id="workflow-name-area" class="form-row">\n                <label>Name:</label>\n                <span id="workflow-name" class="tooltip editable-text" original-title="Click to rename workflow">')
        # SOURCE LINE 1067
        __M_writer(filters.html_escape(unicode(h.to_unicode( stored.name ) )))
        __M_writer(u'</span>\n            </div>\n')
        # SOURCE LINE 1070
        __M_writer(u'            ')
        __M_writer(u'\n            <div class="form-row">\n                <label>\n                    Tags:\n                </label>\n                    <div style="float: left; width: 225px; margin-right: 10px; border-style: inset; border-width: 1px; margin-left: 2px">\n                        <style>\n                            .tag-area {\n                                border: none;\n                            }\n                        </style>\n                        ')
        # SOURCE LINE 1081
        __M_writer(unicode(render_individual_tagging_element(user=trans.get_user(), tagged_item=stored, elt_context="edit_attributes.mako", use_toggle_link=False, input_size="20")))
        __M_writer(u'\n                    </div>\n                    <div class="toolParamHelp">Apply tags to make it easy to search for and find items with the same tag.</div>\n                </div>\n')
        # SOURCE LINE 1087
        __M_writer(u'                <div id="workflow-annotation-area" class="form-row">\n                    <label>Annotation / Notes:</label>\n                    <div id="workflow-annotation" class="tooltip editable-text" original-title="Click to edit annotation">\n')
        # SOURCE LINE 1090
        if annotation:
            # SOURCE LINE 1091
            __M_writer(u'                        ')
            __M_writer(filters.html_escape(unicode(h.to_unicode( annotation ) )))
            __M_writer(u'\n')
            # SOURCE LINE 1092
        else:
            # SOURCE LINE 1093
            __M_writer(u'                        <em>Describe or add notes to workflow</em>\n')
        # SOURCE LINE 1095
        __M_writer(u'                    </div>\n                    <div class="toolParamHelp">Add an annotation or notes to a workflow; annotations are available when a workflow is viewed.</div>\n                </div>\n            </div>\n        </div>\n\n')
        # SOURCE LINE 1102
        __M_writer(u'        <div id="right-content" class="right-content"></div>\n\n')
        # SOURCE LINE 1105
        __M_writer(u'        <div style="display:none;" id="workflow-output-area" class="metadataForm right-content">\n            <div class="metadataFormTitle">Edit Workflow Outputs</div>\n            <div class="metadataFormBody"><div class="form-row">\n                <div class="toolParamHelp">Tag step outputs to indicate the final dataset(s) to be generated by running this workflow.</div>\n                <div id="output-fill-area"></div>\n            </div></div>\n        </div>\n\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x653ca50')._populate(_import_ns, [u'render_individual_tagging_element'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 729
        __M_writer(u'\n\n')
        # SOURCE LINE 732
        __M_writer(u'    ')
        __M_writer(unicode(h.css( "base", "autocomplete_tagging", "tool_menu" )))
        __M_writer(u'\n\n')
        # SOURCE LINE 735
        __M_writer(u'    ')
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n\n    <style type="text/css">\n    body { margin: 0; padding: 0; overflow: hidden; }\n    \n    /* Wider right panel */\n    #center       { right: 309px; }\n    #right-border { right: 300px; }\n    #right        { width: 300px; }\n')
        # SOURCE LINE 751
        __M_writer(u'    \n    #left {\n        background: #C1C9E5 url(')
        # SOURCE LINE 753
        __M_writer(unicode(h.url_for('/static/style/menu_bg.png')))
        __M_writer(u') top repeat-x;\n    }\n    \n    div.toolMenu {\n        margin: 5px;\n        margin-left: 10px;\n        margin-right: 10px;\n    }\n    div.toolMenuGroupHeader {\n        font-weight: bold;\n        padding-top: 0.5em;\n        padding-bottom: 0.5em;\n        color: #333;\n        font-style: italic;\n        border-bottom: dotted #333 1px;\n        margin-bottom: 0.5em;\n    }\n    div.toolTitleDisabled {\n        padding-top: 5px;\n        padding-bottom: 5px;\n        margin-left: 16px;\n        margin-right: 10px;\n        display: list-item;\n        list-style: square outside;\n        font-style: italic;\n        color: gray;\n    }\n    div.toolTitleNoSectionDisabled {\n      padding-bottom: 0px;\n      font-style: italic;\n      color: gray;\n    }\n    div.toolFormRow {\n        position: relative;\n    }\n\n    .right-content {\n        margin: 5px;\n    }\n    \n    canvas { position: absolute; z-index: 10; } \n    canvas.dragging { position: absolute; z-index: 1000; }\n    .input-terminal { width: 12px; height: 12px; background: url(')
        # SOURCE LINE 795
        __M_writer(unicode(h.url_for('/static/style/workflow_circle_open.png')))
        __M_writer(u'); position: absolute; top: 50%; margin-top: -6px; left: -6px; z-index: 1500; }\n    .output-terminal { width: 12px; height: 12px; background: url(')
        # SOURCE LINE 796
        __M_writer(unicode(h.url_for('/static/style/workflow_circle_open.png')))
        __M_writer(u'); position: absolute; top: 50%; margin-top: -6px; right: -6px; z-index: 1500; }\n    .drag-terminal { width: 12px; height: 12px; background: url(')
        # SOURCE LINE 797
        __M_writer(unicode(h.url_for('/static/style/workflow_circle_drag.png')))
        __M_writer(u'); position: absolute; z-index: 1500; }\n    .input-terminal-active { background: url(')
        # SOURCE LINE 798
        __M_writer(unicode(h.url_for('/static/style/workflow_circle_green.png')))
        __M_writer(u'); }\n')
        # SOURCE LINE 800
        __M_writer(u'    .unselectable { -moz-user-select: none; -khtml-user-select: none; user-select: none; }\n    img { border: 0; }\n    \n    div.buttons img {\n    width: 16px; height: 16px;\n    cursor: pointer;\n    }\n    \n')
        # SOURCE LINE 810
        __M_writer(u'    div.toolFormInCanvas {\n        z-index: 100;\n        position: absolute;\n')
        # SOURCE LINE 814
        __M_writer(u'        margin: 6px;\n    }\n    \n    div.toolForm-active {\n        z-index: 1001;\n        border: solid #8080FF 4px;\n        margin: 3px;\n    }\n    \n    div.toolFormTitle {\n        cursor: move;\n        min-height: 16px;\n    }\n    \n    div.titleRow {\n        font-weight: bold;\n        border-bottom: dotted gray 1px;\n        margin-bottom: 0.5em;\n        padding-bottom: 0.25em;\n    }\n    div.form-row {\n      position: relative;\n    }\n    \n    div.tool-node-error div.toolFormTitle {\n        background: #FFCCCC;\n        border-color: #AA6666;\n    }\n    div.tool-node-error {\n        border-color: #AA6666;\n    }\n    \n    #canvas-area {\n        position: absolute;\n        top: 0; left: 305px; bottom: 0; right: 0;\n        border: solid red 1px;\n        overflow: none;\n    }\n    \n    .form-row {\n    }\n\n    div.toolFormInCanvas div.toolFormBody {\n        padding: 0;\n    }\n    .form-row-clear {\n        clear: both;\n    }\n    \n    div.rule {\n        height: 0;\n        border: none;\n        border-bottom: dotted black 1px;\n        margin: 0 5px;\n    }\n    \n    .callout {\n        position: absolute;\n        z-index: 10000;\n    }\n\n    .pjaForm {\n        margin-bottom:10px;\n    }\n    \n    .pjaForm .toolFormBody{\n        padding:10px;\n    }\n    \n    .pjaForm .toolParamHelp{\n        padding:5px;\n    }\n    \n    .panel-header-button-group {\n        margin-right: 5px;\n        padding-right: 5px;\n        border-right: solid gray 1px;\n    }\n        \n    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x653ca50')._populate(_import_ns, [u'render_individual_tagging_element'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4

        self.active_view="workflow"
        self.overlay_visible=True
        
        
        # SOURCE LINE 7
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x653ca50')._populate(_import_ns, [u'render_individual_tagging_element'])
        stored = _import_ns.get('stored', context.get('stored', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 20
        __M_writer(u'\n    \n    ')
        # SOURCE LINE 22
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n    \n    <!--[if lt IE 9]>\n      <script type=\'text/javascript\' src="')
        # SOURCE LINE 25
        __M_writer(unicode(h.url_for('/static/scripts/excanvas.js')))
        __M_writer(u'"></script>\n    <![endif]-->\n\n    ')
        # SOURCE LINE 28
        __M_writer(unicode(h.js( "jquery",
            "jquery.tipsy",
            "jquery.event.drag", 
            "jquery.event.drop", 
            "jquery.event.hover",
            "jquery.form",
            "class",
            "json2",
            "jquery.jstore",
            "galaxy.base",
            "galaxy.workflow_editor.canvas",
            "jquery.autocomplete",
            "autocomplete_tagging")))
        # SOURCE LINE 40
        __M_writer(u'\n\n    <!--[if lt IE 7]>\n    <script type=\'text/javascript\'>\n    window.lt_ie_7 = true;\n    </script>\n    <![endif]-->\n    \n    <script type=\'text/javascript\'>\n    // Globals\n    workflow = null;\n    canvas_manager = null;\n    active_ajax_call = false;\n    var galaxy_async = new GalaxyAsync();\n    galaxy_async.set_func_url(galaxy_async.set_user_pref, "')
        # SOURCE LINE 54
        __M_writer(unicode(h.url_for( controller='user', action='set_user_pref_async' )))
        __M_writer(u'");\n    \n    // jQuery onReady\n    $( function() {\n        \n        if ( window.lt_ie_7 ) {\n            show_modal(\n                "Browser not supported",\n                "Sorry, the workflow editor is not supported for IE6 and below."\n            );\n            return;\n        }\n        \n        // Init tool options.\n')
        # SOURCE LINE 68
        if trans.app.toolbox_search.enabled:
            # SOURCE LINE 69
            __M_writer(u'        make_popupmenu( $("#tools-options-button"), {\n')
            # SOURCE LINE 71
            __M_writer(u'            ')

            show_tool_search = False
            if trans.user:
                show_tool_search = trans.user.preferences.get( "workflow.show_tool_search", "True" )
                
            if show_tool_search == "True":
                initial_text = "Hide Search"
            else:
                initial_text = "Search Tools"
                        
            
            # SOURCE LINE 80
            __M_writer(u'\n            "')
            # SOURCE LINE 81
            __M_writer(unicode(initial_text))
            __M_writer(u'": function() {\n                // Show/hide menu and update vars, user preferences.\n                var menu = $(\'#tool-search\');\n                if (menu.is(":visible")) {\n                    // Hide menu.\n                    pref_value = "False";\n                    menu_option_text = "Search Tools";\n                    menu.toggle();\n                    \n                    // Reset search.\n                    reset_tool_search(true);\n                } else {\n                    // Show menu.\n                    pref_value = "True";\n                    menu_option_text = "Hide Search";\n                    menu.toggle();\n                }\n        \n                // Update menu option.\n                $("#tools-options-button-menu").find("li").eq(0).text(menu_option_text);\n        \n                galaxy_async.set_user_pref("workflow.show_tool_search", pref_value);\n            }\n        });\n        \n        // Init searching.\n        $("#tool-search-query").click( function (){\n            $(this).focus();\n            $(this).select();\n        })\n        .keyup( function () {\n            // Remove italics.\n            $(this).css("font-style", "normal");\n            \n            // Don\'t update if same value as last time\n            if ( this.value.length < 3 ) {\n                reset_tool_search(false);\n            } else if ( this.value != this.lastValue ) {\n                // Add class to denote that searching is active.\n                $(this).addClass("search_active");\n                // input.addClass(config.loadingClass);\n                // Add \'*\' to facilitate partial matching.\n                var q = this.value + \'*\';\n                // Stop previous ajax-request\n                if (this.timer) {\n                    clearTimeout(this.timer);\n                }\n                // Start a new ajax-request in X ms\n                $("#search-spinner").show();\n                this.timer = setTimeout(function () {\n                    \n                    $.get("')
            # SOURCE LINE 132
            __M_writer(unicode(h.url_for( controller='root', action='tool_search' )))
            __M_writer(u'", { query: q }, function (data) {\n                        // input.removeClass(config.loadingClass);\n                        // Show live-search if results and search-term aren\'t empty\n                        $("#search-no-results").hide();\n                        // Hide all tool sections.\n                        $(".toolSectionWrapper").hide();\n                        // This hides all tools but not workflows link (which is in a .toolTitle div).\n                        $(".toolSectionWrapper").find(".toolTitle").hide();\n                        if ( data.length != 0 ) {\n                            // Map tool ids to element ids and join them.\n                            var s = $.map( data, function( n, i ) { return "#link-" + n; } ).join( ", " );\n                            \n                            // First pass to show matching tools and their parents.\n                            $(s).each( function() {\n                                // Add class to denote match.\n                                $(this).parent().addClass("search_match");\n                                $(this).parent().show().parent().parent().show().parent().show();\n                            });\n                            \n                            // Hide labels that have no visible children.\n                            $(".toolPanelLabel").each( function() {\n                               var this_label = $(this);                                   \n                               var next = this_label.next();\n                               var no_visible_tools = true;\n                               // Look through tools following label and, if none are visible, hide label.\n                               while (next.length !== 0 && next.hasClass("toolTitle")) {\n                                   if (next.is(":visible")) {\n                                       no_visible_tools = false;\n                                       break;\n                                   } else {\n                                       next = next.next();\n                                   }\n                                }\n                                if (no_visible_tools) {\n                                    this_label.hide();\n                                }\n                            });\n                        } else {\n                            $("#search-no-results").show();\n                        }\n                        $("#search-spinner").hide();\n                    }, "json" );\n                }, 200 );\n            }\n            this.lastValue = this.value;\n        });\n')
        # SOURCE LINE 179
        __M_writer(u'        \n        // Load jStore for local storage\n        $.jStore.init("galaxy"); // Auto-select best storage\n        \n        // Canvas overview management\n        canvas_manager = new CanvasManager( $("#canvas-viewport"), $("#overview") );\n        \n        // Initialize workflow state\n        reset();\n        // Load the datatype info\n        $.ajax( {\n            url: "')
        # SOURCE LINE 190
        __M_writer(unicode(h.url_for( action='get_datatypes' )))
        __M_writer(u'",\n            dataType: "json",\n            cache: false,\n            success: function( data ) {\n                populate_datatype_info( data );\n                // Load workflow definition\n                $.ajax( {\n                    url: "')
        # SOURCE LINE 197
        __M_writer(unicode(h.url_for( action='load_workflow' )))
        __M_writer(u'",\n                    data: { id: "')
        # SOURCE LINE 198
        __M_writer(unicode(trans.security.encode_id( stored.id )))
        __M_writer(u'", "_": "true" },\n                    dataType: \'json\',\n                    cache: false,\n                    success: function( data ) {\n                         reset();\n                         workflow.from_simple( data );\n                         workflow.has_changes = false;\n                         workflow.fit_canvas_to_nodes();\n                         scroll_to_nodes();\n                         canvas_manager.draw_overview();\n                         // Determine if any parameters were \'upgraded\' and provide message\n                         upgrade_message = "";\n                         $.each( data.upgrade_messages, function( k, v ) {\n                            upgrade_message += ( "<li>Step " + ( parseInt(k, 10) + 1 ) + ": " + workflow.nodes[k].name + "<ul>");\n                            $.each( v, function( i, vv ) {\n                                upgrade_message += "<li>" + vv +"</li>";\n                            });\n                            upgrade_message += "</ul></li>";\n                         });\n                         if ( upgrade_message ) {\n                            show_modal( "Workflow loaded with changes",\n                                        "Problems were encountered loading this workflow (possibly a result of tool upgrades). Please review the following parameters and then save.<ul>" + upgrade_message + "</ul>",\n                                        { "Continue" : hide_modal } );\n                         } else {\n                            hide_modal();\n                         }\n                         show_workflow_parameters();\n                     },\n                     beforeSubmit: function( data ) {\n                         show_modal( "Loading workflow", "progress" );\n                     }\n                });\n            }\n        });\n        \n        // For autosave purposes\n        $(document).ajaxStart( function() {\n            active_ajax_call = true;\n            $(document).bind( "ajaxStop.global", function() {\n                active_ajax_call = false;\n            });\n        });\n        \n        $(document).ajaxError( function ( e, x ) {\n            // console.log( e, x );\n            var message = x.responseText || x.statusText || "Could not connect to server";\n            show_modal( "Server error", message, { "Ignore error" : hide_modal } );\n            return false;\n        });\n         \n        make_popupmenu( $("#workflow-options-button"), {\n')
        # SOURCE LINE 250
        __M_writer(u'             "Edit Attributes" : edit_workflow_attributes,\n')
        # SOURCE LINE 252
        __M_writer(u'             "Layout": layout_editor,\n             "Save" : save_current_workflow,\n')
        # SOURCE LINE 255
        __M_writer(u'             "Close": close_editor\n        });\n        \n        function edit_workflow_outputs(){\n            workflow.clear_active_node();\n            $(\'.right-content\').hide();\n            var new_content = "";\n            for (var node_key in workflow.nodes){\n                var node = workflow.nodes[node_key];\n                if(node.type == \'tool\'){\n                    new_content += "<div class=\'toolForm\' style=\'margin-bottom:5px;\'><div class=\'toolFormTitle\'>Step " + node.id + " - " + node.name + "</div>";\n                    for (var ot_key in node.output_terminals){\n                        var output = node.output_terminals[ot_key];\n                        // if (node.workflow_outputs[node.id + "|" + output.name]){\n                        if ($.inArray(output.name, node.workflow_outputs) != -1){\n                            new_content += "<p>"+output.name +"<input type=\'checkbox\' name=\'"+ node.id + "|" + output.name +"\' checked /></p>";\n                        }\n                        else{\n                            new_content += "<p>"+output.name +"<input type=\'checkbox\' name=\'"+ node.id + "|" + output.name +"\' /></p>";\n                        }\n                    }\n                    new_content += "</div>";\n                }\n            }\n            $("#output-fill-area").html(new_content);\n            $("#output-fill-area input").bind(\'click\', function(){\n                var node_id = this.name.split(\'|\')[0];\n                var output_name = this.name.split(\'|\')[1];\n                if (this.checked){\n                    if($.inArray(output_name, workflow.nodes[node_id].workflow_outputs) == -1){\n                        workflow.nodes[node_id].workflow_outputs.push(output_name);\n                    }//else it\'s already in the array.  Shouldn\'t happen, but forget it.\n                }else{\n                    while ($.inArray(output_name, workflow.nodes[node_id].workflow_outputs) != -1){\n                        var ia = $.inArray(output_name, workflow.nodes[node_id].workflow_outputs);\n                        workflow.nodes[node_id].workflow_outputs = workflow.nodes[node_id].workflow_outputs.slice(0,ia).concat( workflow.nodes[node_id].workflow_outputs.slice(ia+1) );\n                    }\n                }\n                workflow.has_changes = true;\n            });\n            $(\'#workflow-output-area\').show();\n        }\n\n        function layout_editor() {\n            workflow.layout();\n            workflow.fit_canvas_to_nodes();\n            scroll_to_nodes();\n            canvas_manager.draw_overview();\n        }\n        \n        function edit_workflow_attributes() {\n            workflow.clear_active_node();\n            $(\'.right-content\').hide();\n            $(\'#edit-attributes\').show();\n\n        }\n        \n        $.jStore.engineReady(function() {\n            // On load, set the size to the pref stored in local storage if it exists\n            overview_size = $.jStore.store("overview-size");\n            if (overview_size !== undefined) {\n                $("#overview-border").css( {\n                    width: overview_size,\n                    height: overview_size\n                });\n            }\n            \n            // Show viewport on load unless pref says it\'s off\n            if ($.jStore.store("overview-off")) {\n                hide_overview();\n            } else {\n                show_overview();\n            }\n        });\n        \n        // Stores the size of the overview into local storage when it\'s resized\n        $("#overview-border").bind( "dragend", function( e ) {\n            var op = $(this).offsetParent();\n            var opo = op.offset();\n            var new_size = Math.max( op.width() - ( e.offsetX - opo.left ),\n                                     op.height() - ( e.offsetY - opo.top ) );\n            $.jStore.store("overview-size", new_size + "px");\n        });\n        \n        function show_overview() {\n            $.jStore.remove("overview-off");\n            $("#overview-border").css("right", "0px");\n            $("#close-viewport").css("background-position", "0px 0px");\n        }\n        \n        function hide_overview() {\n            $.jStore.store("overview-off", true);\n            $("#overview-border").css("right", "20000px");\n            $("#close-viewport").css("background-position", "12px 0px");\n        }\n        \n        // Lets the overview be toggled visible and invisible, adjusting the arrows accordingly\n        $("#close-viewport").click( function() {\n            if ( $("#overview-border").css("right") === "0px" ) {\n                hide_overview();\n            } else {\n                show_overview();\n            }\n        });\n        \n        // Unload handler\n        window.onbeforeunload = function() {\n            if ( workflow && workflow.has_changes ) {\n                return "There are unsaved changes to your workflow which will be lost.";\n            }\n        };\n        \n        // Tool menu\n        $( "div.toolSectionBody" ).hide();\n        $( "div.toolSectionTitle > span" ).wrap( "<a href=\'#\'></a>" );\n        var last_expanded = null;\n        $( "div.toolSectionTitle" ).each( function() { \n           var body = $(this).next( "div.toolSectionBody" );\n           $(this).click( function() {\n               if ( body.is( ":hidden" ) ) {\n                   if ( last_expanded ) last_expanded.slideUp( "fast" );\n                   last_expanded = body;\n                   body.slideDown( "fast" );\n               }\n               else {\n                   body.slideUp( "fast" );\n                   last_expanded = null;\n               }\n           });\n        });\n\n        // Rename async.\n        async_save_text("workflow-name", "workflow-name", "')
        # SOURCE LINE 387
        __M_writer(unicode(h.url_for( action='rename_async', id=trans.security.encode_id(stored.id) )))
        __M_writer(u'", "new_name");\n        \n        // Tag async. Simply have the workflow edit element generate a click on the tag element to activate tagging.\n        $(\'#workflow-tag\').click( function() {\n            $(\'.tag-area\').click();\n            return false;\n        });\n        // Annotate async.\n        async_save_text("workflow-annotation", "workflow-annotation", "')
        # SOURCE LINE 395
        __M_writer(unicode(h.url_for( action='annotate_async', id=trans.security.encode_id(stored.id) )))
        __M_writer(u'", "new_annotation", 25, true, 4);\n    });\n\n    // Global state for the whole workflow\n    function reset() {\n        if ( workflow ) {\n            workflow.remove_all();\n        }\n        workflow = new Workflow( $("#canvas-container") );\n    }\n        \n    function scroll_to_nodes() {\n        var cv = $("#canvas-viewport");\n        var cc = $("#canvas-container");\n        var top, left;\n        if ( cc.width() < cv.width() ) {\n            left = ( cv.width() - cc.width() ) / 2;\n        } else {\n            left = 0;\n        }\n        if ( cc.height() < cv.height() ) {\n            top = ( cv.height() - cc.height() ) / 2;\n        } else {\n            top = 0;\n        }\n        cc.css( { left: left, top: top } );\n    }\n    \n    // Add a new step to the workflow by tool id\n    function add_node_for_tool( id, title ) {\n        var node = prebuild_node( \'tool\', title, id );\n        workflow.add_node( node );\n        workflow.fit_canvas_to_nodes();\n        canvas_manager.draw_overview();\n        workflow.activate_node( node );\n        $.ajax( {\n            url: "')
        # SOURCE LINE 431
        __M_writer(unicode(h.url_for( action='get_new_module_info' )))
        __M_writer(u'", \n            data: { type: "tool", tool_id: id, "_": "true" },\n            global: false,\n            dataType: "json",\n            success: function( data ) {\n                node.init_field_data( data );\n            },\n            error: function( x, e ) {\n                var m = "error loading field data";\n                if ( x.status === 0 ) {\n                    m += ", server unavailable";\n                }\n                node.error( m );\n            }\n        });\n    }\n    \n    function add_node_for_module( type, title ) {\n        node = prebuild_node( type, title );\n        workflow.add_node( node );\n        workflow.fit_canvas_to_nodes();\n        canvas_manager.draw_overview();\n        workflow.activate_node( node );\n        $.ajax( {\n            url: "')
        # SOURCE LINE 455
        __M_writer(unicode(h.url_for( action='get_new_module_info' )))
        __M_writer(u'", \n            data: { type: type, "_": "true" }, \n            dataType: "json",\n            success: function( data ) {\n                node.init_field_data( data );\n            },\n            error: function( x, e ) {\n                var m = "error loading field data"\n                if ( x.status == 0 ) {\n                    m += ", server unavailable"\n                }\n                node.error( m );\n            }\n        });\n    }\n\n')
        # SOURCE LINE 471

        from galaxy.jobs.actions.post import ActionBox
        
        
        # SOURCE LINE 473
        __M_writer(u"\n\n    // This function preloads how to display known pja's.\n    function display_pja(pja, node){\n        // DBTODO SANITIZE INPUTS.\n        p_str = '';\n        ")
        # SOURCE LINE 479
        __M_writer(unicode(ActionBox.get_forms(trans)))
        __M_writer(u'\n        $("#pja_container").append(p_str);\n        $("#pja_container>.toolForm:last>.toolFormTitle>.buttons").click(function (){\n            action_to_rem = $(this).closest(".toolForm", ".action_tag").children(".action_tag:first").text();\n            $(this).closest(".toolForm").remove();\n            delete workflow.active_node.post_job_actions[action_to_rem];\n            workflow.active_form_has_changes = true;\n        });\n    }\n    \n    function display_pja_list(){\n        return "')
        # SOURCE LINE 490
        __M_writer(unicode(ActionBox.get_add_list()))
        __M_writer(u'";\n    }\n    \n    function display_file_list(node){\n        addlist = "<select id=\'node_data_list\' name=\'node_data_list\'>";\n        for (var out_terminal in node.output_terminals){\n            addlist += "<option value=\'" + out_terminal + "\'>"+ out_terminal +"</option>";\n        }\n        addlist += "</select>";\n        return addlist;\n    }\n    \n    function new_pja(action_type, target, node){\n        if (node.post_job_actions === undefined){\n            //New tool node, set up dict.\n            node.post_job_actions = {};\n        }\n        if (node.post_job_actions[action_type+target] === undefined){\n            var new_pja = {};\n            new_pja.action_type = action_type;\n            new_pja.output_name = target;\n            node.post_job_actions[action_type+target] = null;\n            node.post_job_actions[action_type+target] =  new_pja;\n            display_pja(new_pja, node);\n            workflow.active_form_has_changes = true;\n            return true;\n        } else {\n            return false;\n        }\n    }\n    \n    function show_workflow_parameters(){\n        var parameter_re = /\\$\\{.+?\\}/g;\n        var workflow_parameters = [];\n        var wf_parm_container = $("#workflow-parameters-container");\n        var wf_parm_box = $("#workflow-parameters-box");\n        var new_parameter_content = "";\n        var matches = [];\n        $.each(workflow.nodes, function (k, node){\n            var form_matches = node.form_html.match(parameter_re);\n            if (form_matches){\n                matches = matches.concat(form_matches);\n            }\n            $.each(node.post_job_actions, function(k, pja){\n                    $.each(pja.action_arguments, function(k, action_argument){\n                        var arg_matches = action_argument.match(parameter_re);\n                        if (arg_matches){\n                            matches = matches.concat(arg_matches);\n                        }\n                    });\n            });\n            if (matches){\n                $.each(matches, function(k, element){\n                    if ($.inArray(element, workflow_parameters) === -1){\n                        workflow_parameters.push(element);\n                    }\n                });\n            }\n        });\n        if (workflow_parameters && workflow_parameters.length !== 0){\n            $.each(workflow_parameters, function(k, element){\n                new_parameter_content += "<div>" + element.substring(2, element.length -1) + "</div>";\n            });\n            wf_parm_container.html(new_parameter_content);\n            wf_parm_box.show();\n        }else{\n            wf_parm_container.html(new_parameter_content);\n            wf_parm_box.hide();\n        }\n    }\n    \n    \n    \n    function show_form_for_tool( text, node ) {\n        $(\'.right-content\').hide();\n        $("#right-content").show().html( text );\n        // Add metadata form to tool.\n        if (node) {\n            $("#right-content").find(".toolForm:first").after( "<p><div class=\'metadataForm\'> ')
        # SOURCE LINE 569
        __M_writer(u"                <div class='metadataFormTitle'>Edit Step Attributes</div> ")
        # SOURCE LINE 570
        __M_writer(u"                <div class='form-row'> ")
        # SOURCE LINE 571
        __M_writer(u'                <label>Annotation / Notes:</label> ')
        # SOURCE LINE 572
        __M_writer(u"                        <div style='margin-right: 10px;'> ")
        # SOURCE LINE 573
        __M_writer(u'                        <textarea name=\'annotation\' rows=\'3\' style=\'width: 100%\'>" + node.annotation + "</textarea> ')
        # SOURCE LINE 574
        __M_writer(u"                            <div class='toolParamHelp'>Add an annotation or notes to this step; annotations are available when a workflow is viewed.</div> ")
        # SOURCE LINE 575
        __M_writer(u'                        </div> ')
        # SOURCE LINE 576
        __M_writer(u'                </div> ')
        # SOURCE LINE 577
        __M_writer(u'                </div>" );\n        }\n        // Add step actions.\n        if (node && node.type==\'tool\'){\n            pjastr = "<p><div class=\'metadataForm\'><div class=\'metadataFormTitle\'>Edit Step Actions</div><div class=\'form-row\'> ')
        # SOURCE LINE 582
        __M_writer(u'                " + display_pja_list() + " <br/> "+ display_file_list(node) + " <div class=\'action-button\' style=\'border:1px solid black;display:inline;\' id=\'add_pja\'>Create</div>')
        # SOURCE LINE 583
        __M_writer(u"                </div><div class='form-row'>")
        # SOURCE LINE 584
        __M_writer(u'                <div style=\'margin-right: 10px;\'><span id=\'pja_container\'></span>";\n            pjastr += "<div class=\'toolParamHelp\'>Add actions to this step; actions are applied when this workflow step completes.</div></div></div></div>";\n            $("#right-content").find(".toolForm").after( pjastr );\n            for (var key in node.post_job_actions){\n                if (key != "undefined"){ //To make sure we haven\'t just deleted it.\n                    display_pja(node.post_job_actions[key], node);\n                }\n            }\n            $("#add_pja").click(function (){\n                new_pja($("#new_pja_list").val(),$("#node_data_list").val(), node);\n            });\n        }\n        $("#right-content").find( "form" ).ajaxForm( {\n            type: \'POST\',\n            dataType: \'json\',\n            success: function( data ) {\n                workflow.active_form_has_changes = false;\n                node.update_field_data( data );\n                show_workflow_parameters();\n            },\n            beforeSubmit: function( data ) {\n                data.push( { name: \'tool_state\', value: node.tool_state } );\n                data.push( { name: \'_\', value: "true" } );\n            }\n        }).each( function() {\n            var form = this;\n            $(this).find( "select[refresh_on_change=\'true\']").change( function() {\n                $(form).submit();\n            });\n            $(this).find( ".popupmenu" ).each( function() {\n                var id = $(this).parents( "div.form-row" ).attr( \'id\' );\n                var b = $(\'<a class="popup-arrow" id="popup-arrow-for-\' + id + \'">&#9660;</a>\');\n                var options = {};\n                $(this).find( "button" ).each( function() {\n                    var name = $(this).attr( \'name\' );\n                    var value = $(this).attr( \'value\' );\n                    options[ $(this).text() ] = function() {\n                        $(form).append( "<input type=\'hidden\' name=\'"+name+"\' value=\'"+value+"\' />" ).submit();\n                    };\n                });\n                b.insertAfter( this );\n                $(this).remove();\n                make_popupmenu( b, options );\n            });\n            // Implements auto-saving based on whether the inputs change. We consider\n            // "changed" to be when a field is accessed and not necessarily modified\n            // because of an issue where "onchange" is not triggered when activating\n            // another node, or saving the workflow.\n            $(this).find("input,textarea,select").each( function() {\n                $(this).bind("focus click", function() {\n                    workflow.active_form_has_changes = true;\n                });\n            });\n        });\n    }\n    \n    var close_editor = function() {\n        ')
        # SOURCE LINE 641
        next_url = h.url_for( controller='workflow', action='index' ) 
        
        __M_writer(u'\n        workflow.check_changes_in_active_form();\n        if ( workflow && workflow.has_changes ) {\n            do_close = function() {\n                window.onbeforeunload = undefined;\n                window.document.location = "')
        # SOURCE LINE 646
        __M_writer(unicode(next_url))
        __M_writer(u'"\n            };\n            show_modal( "Close workflow editor",\n                        "There are unsaved changes to your workflow which will be lost.",\n                        {\n                            "Cancel" : hide_modal,\n                            "Save Changes" : function() {\n                                save_current_workflow( null, do_close );\n                            }\n                        }, {\n                            "Don\'t Save": do_close\n                        } );\n        } else {\n            window.document.location = "')
        # SOURCE LINE 659
        __M_writer(unicode(next_url))
        __M_writer(u'";\n        }\n    };\n    \n    var save_current_workflow = function ( eventObj, success_callback ) {\n        show_modal( "Saving workflow", "progress" );\n        workflow.check_changes_in_active_form();\n        if (!workflow.has_changes) {\n            hide_modal();\n            if ( success_callback ) {\n                success_callback();\n            }\n            return;\n        }\n        workflow.rectify_workflow_outputs();\n        var savefn = function(callback) {\n            $.ajax( {\n                url: "')
        # SOURCE LINE 676
        __M_writer(unicode(h.url_for( action='save_workflow' )))
        __M_writer(u'",\n                type: "POST",\n                data: {\n                    id: "')
        # SOURCE LINE 679
        __M_writer(unicode(trans.security.encode_id( stored.id )))
        __M_writer(u'",\n                    workflow_data: function() { return JSON.stringify( workflow.to_simple() ); },\n                    "_": "true"\n                },\n                dataType: \'json\',\n                success: function( data ) { \n                    var body = $("<div></div>").text( data.message );\n                    if ( data.errors ) {\n                        body.addClass( "warningmark" );\n                        var errlist = $( "<ul/>" );\n                        $.each( data.errors, function( i, v ) {\n                            $("<li></li>").text( v ).appendTo( errlist );\n                        });\n                        body.append( errlist );\n                    } else {\n                        body.addClass( "donemark" );\n                    }\n                    workflow.name = data.name;\n                    workflow.has_changes = false;\n                    workflow.stored = true;\n                    show_workflow_parameters();\n                    if ( data.errors ) {\n                        show_modal( "Saving workflow", body, { "Ok" : hide_modal } );\n                    } else {\n                        if (callback) {\n                            callback();\n                        }\n                        hide_modal();\n                    }\n                }\n            });\n        };\n        \n        // We bind to ajaxStop because of auto-saving, since the form submission ajax\n        // call needs to be completed so that the new data is saved\n        if (active_ajax_call) {\n            $(document).bind(\'ajaxStop.save_workflow\', function() {\n                $(document).unbind(\'ajaxStop.save_workflow\');\n                savefn();\n                $(document).unbind(\'ajaxStop.save_workflow\'); // IE7 needs it here\n                active_ajax_call = false;\n            });\n        } else {\n            savefn(success_callback);\n        }\n    };\n    \n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_tool(context,tool,section):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x653ca50')._populate(_import_ns, [u'render_individual_tagging_element'])
        __M_writer = context.writer()
        # SOURCE LINE 897
        __M_writer(u'\n')
        # SOURCE LINE 898
        if not tool.hidden:
            # SOURCE LINE 899
            if tool.is_workflow_compatible:
                # SOURCE LINE 900
                if section:
                    # SOURCE LINE 901
                    __M_writer(u'                <div class="toolTitle">\n')
                    # SOURCE LINE 902
                else:
                    # SOURCE LINE 903
                    __M_writer(u'                <div class="toolTitleNoSection">\n')
                # SOURCE LINE 905
                if "[[" in tool.description and "]]" in tool.description:
                    # SOURCE LINE 906
                    __M_writer(u'                    ')
                    __M_writer(unicode(tool.description.replace( '[[', '<a id="link-${tool.id}" href="javascript:add_node_for_tool( ${tool.id} )">' % tool.id ).replace( "]]", "</a>" )))
                    __M_writer(u'\n')
                    # SOURCE LINE 907
                elif tool.name:
                    # SOURCE LINE 908
                    __M_writer(u'                    <a id="link-')
                    __M_writer(unicode(tool.id))
                    __M_writer(u'" href="#" onclick="add_node_for_tool( \'')
                    __M_writer(unicode(tool.id))
                    __M_writer(u"', '")
                    __M_writer(unicode(tool.name))
                    __M_writer(u'\' )">')
                    __M_writer(unicode(tool.name))
                    __M_writer(u'</a> ')
                    __M_writer(unicode(tool.description))
                    __M_writer(u'\n')
                    # SOURCE LINE 909
                else:
                    # SOURCE LINE 910
                    __M_writer(u'                    <a id="link-')
                    __M_writer(unicode(tool.id))
                    __M_writer(u'" href="#" onclick="add_node_for_tool( \'')
                    __M_writer(unicode(tool.id))
                    __M_writer(u"', '")
                    __M_writer(unicode(tool.name))
                    __M_writer(u'\' )">')
                    __M_writer(unicode(tool.description))
                    __M_writer(u'</a>\n')
                # SOURCE LINE 912
                __M_writer(u'            </div>\n')
                # SOURCE LINE 913
            else:
                # SOURCE LINE 914
                if section:
                    # SOURCE LINE 915
                    __M_writer(u'                <div class="toolTitleDisabled">\n')
                    # SOURCE LINE 916
                else:
                    # SOURCE LINE 917
                    __M_writer(u'                <div class="toolTitleNoSectionDisabled">\n')
                # SOURCE LINE 919
                if "[[" in tool.description and "]]" in tool.description:
                    # SOURCE LINE 920
                    __M_writer(u'                    ')
                    __M_writer(unicode(tool.description.replace( '[[', '' % tool.id ).replace( "]]", "" )))
                    __M_writer(u'\n')
                    # SOURCE LINE 921
                elif tool.name:
                    # SOURCE LINE 922
                    __M_writer(u'                    ')
                    __M_writer(unicode(tool.name))
                    __M_writer(u' ')
                    __M_writer(unicode(tool.description))
                    __M_writer(u'\n')
                    # SOURCE LINE 923
                else:
                    # SOURCE LINE 924
                    __M_writer(u'                    ')
                    __M_writer(unicode(tool.description))
                    __M_writer(u'\n')
                # SOURCE LINE 926
                __M_writer(u'            </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


