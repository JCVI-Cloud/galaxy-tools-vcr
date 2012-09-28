from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1308683838.9599171
_template_filename=u'templates/grid_base.mako'
_template_uri=u'/tracks/../grid_base.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding=None
_exports = ['body', 'grid_title', 'render_grid_header', 'title', 'center_panel', 'render_grid_table_body_contents', 'stylesheets', 'grid_javascripts', 'init', 'render_grid_table', 'grid_body', 'make_grid', 'render_grid_table_footer_contents', 'javascripts']


# SOURCE LINE 1

from galaxy.web.framework.helpers.grids import TextColumn
import galaxy.util
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
    # SOURCE LINE 15
    ns = runtime.Namespace('__anon_0x6557dd0', context._clean_inheritance_tokens(), templateuri=u'/display_common.mako', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, '__anon_0x6557dd0')] = ns

    # SOURCE LINE 708
    ns = runtime.Namespace('__anon_0x6acb750', context._clean_inheritance_tokens(), templateuri=u'./grid_common.mako', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, '__anon_0x6acb750')] = ns

    # SOURCE LINE 935
    ns = runtime.Namespace('__anon_0x6ad4390', context._clean_inheritance_tokens(), templateuri=u'/display_common.mako', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, '__anon_0x6ad4390')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, (inherit(context)), _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x6557dd0')._populate(_import_ns, [u'render_message'])
        _mako_get_namespace(context, '__anon_0x6acb750')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x6ad4390')._populate(_import_ns, [u'get_class_plural'])
        __M_writer = context.writer()
        # SOURCE LINE 13
        __M_writer(u'\n')
        # SOURCE LINE 14
        __M_writer(u'\n')
        # SOURCE LINE 15
        __M_writer(u'\n\n')
        # SOURCE LINE 25
        __M_writer(u'\n\n')
        # SOURCE LINE 30
        __M_writer(u'\n')
        # SOURCE LINE 33
        __M_writer(u'\n\n')
        # SOURCE LINE 38
        __M_writer(u'\n\n')
        # SOURCE LINE 45
        __M_writer(u'\n\n')
        # SOURCE LINE 47
        __M_writer(u'\n\n')
        # SOURCE LINE 52
        __M_writer(u'\n\n')
        # SOURCE LINE 610
        __M_writer(u'\n\n')
        # SOURCE LINE 702
        __M_writer(u'\n\n')
        # SOURCE LINE 707
        __M_writer(u'\n')
        # SOURCE LINE 708
        __M_writer(u'\n\n')
        # SOURCE LINE 725
        __M_writer(u'\n\n')
        # SOURCE LINE 729
        __M_writer(u'\n\n')
        # SOURCE LINE 757
        __M_writer(u'\n\n')
        # SOURCE LINE 827
        __M_writer(u'\n\n')
        # SOURCE LINE 930
        __M_writer(u'\n\n')
        # SOURCE LINE 1017
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x6557dd0')._populate(_import_ns, [u'render_message'])
        _mako_get_namespace(context, '__anon_0x6acb750')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x6ad4390')._populate(_import_ns, [u'get_class_plural'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        grid = _import_ns.get('grid', context.get('grid', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 36
        __M_writer(u'\n    ')
        # SOURCE LINE 37
        __M_writer(unicode(self.grid_body( grid )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_grid_title(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x6557dd0')._populate(_import_ns, [u'render_message'])
        _mako_get_namespace(context, '__anon_0x6acb750')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x6ad4390')._populate(_import_ns, [u'get_class_plural'])
        grid = _import_ns.get('grid', context.get('grid', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 727
        __M_writer(u'\n    <h2>')
        # SOURCE LINE 728
        __M_writer(unicode(grid.title))
        __M_writer(u'</h2>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_grid_header(context,grid,render_title=True):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x6557dd0')._populate(_import_ns, [u'render_message'])
        _mako_get_namespace(context, '__anon_0x6acb750')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x6ad4390')._populate(_import_ns, [u'get_class_plural'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        render_grid_filters = _import_ns.get('render_grid_filters', context.get('render_grid_filters', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 732
        __M_writer(u'\n    <div class="grid-header">\n')
        # SOURCE LINE 734
        if render_title:
            # SOURCE LINE 735
            __M_writer(u'            ')
            __M_writer(unicode(self.grid_title()))
            __M_writer(u'\n')
        # SOURCE LINE 737
        __M_writer(u'    \n')
        # SOURCE LINE 738
        if grid.global_actions:
            # SOURCE LINE 739
            __M_writer(u'            <ul class="manage-table-actions">\n')
            # SOURCE LINE 740
            if len( grid.global_actions ) < 4:
                # SOURCE LINE 741
                for action in grid.global_actions:
                    # SOURCE LINE 742
                    __M_writer(u'                        <li><a class="action-button" href="')
                    __M_writer(unicode(h.url_for( **action.url_args )))
                    __M_writer(u'">')
                    __M_writer(unicode(action.label))
                    __M_writer(u'</a></li>\n')
                # SOURCE LINE 744
            else:
                # SOURCE LINE 745
                __M_writer(u'                    <li><a class="action-button" id="action-8675309-popup" class="menubutton">Actions</a></li>\n                    <div popupmenu="action-8675309-popup">\n')
                # SOURCE LINE 747
                for action in grid.global_actions:
                    # SOURCE LINE 748
                    __M_writer(u'                            <a class="action-button" href="')
                    __M_writer(unicode(h.url_for( **action.url_args )))
                    __M_writer(u'">')
                    __M_writer(unicode(action.label))
                    __M_writer(u'</a>\n')
                # SOURCE LINE 750
                __M_writer(u'                    </div>\n')
            # SOURCE LINE 752
            __M_writer(u'            </ul>\n')
        # SOURCE LINE 754
        __M_writer(u'    \n        ')
        # SOURCE LINE 755
        __M_writer(unicode(render_grid_filters( grid )))
        __M_writer(u'\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x6557dd0')._populate(_import_ns, [u'render_message'])
        _mako_get_namespace(context, '__anon_0x6acb750')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x6ad4390')._populate(_import_ns, [u'get_class_plural'])
        grid = _import_ns.get('grid', context.get('grid', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 47
        __M_writer(unicode(grid.title))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x6557dd0')._populate(_import_ns, [u'render_message'])
        _mako_get_namespace(context, '__anon_0x6acb750')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x6ad4390')._populate(_import_ns, [u'get_class_plural'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        grid = _import_ns.get('grid', context.get('grid', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 31
        __M_writer(u'\n    ')
        # SOURCE LINE 32
        __M_writer(unicode(self.grid_body( grid )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_grid_table_body_contents(context,grid,show_item_checkboxes=False):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x6557dd0')._populate(_import_ns, [u'render_message'])
        _mako_get_namespace(context, '__anon_0x6acb750')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x6ad4390')._populate(_import_ns, [u'get_class_plural'])
        isinstance = _import_ns.get('isinstance', context.get('isinstance', UNDEFINED))
        str = _import_ns.get('str', context.get('str', UNDEFINED))
        url = _import_ns.get('url', context.get('url', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        current_item = _import_ns.get('current_item', context.get('current_item', UNDEFINED))
        unicode = _import_ns.get('unicode', context.get('unicode', UNDEFINED))
        enumerate = _import_ns.get('enumerate', context.get('enumerate', UNDEFINED))
        query = _import_ns.get('query', context.get('query', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 830
        __M_writer(u'\n        ')
        # SOURCE LINE 831
        num_rows_rendered = 0 
        
        __M_writer(u'\n')
        # SOURCE LINE 832
        if query.count() == 0:
            # SOURCE LINE 834
            __M_writer(u'            <tr><td colspan="100"><em>No Items</em></td></tr>\n            ')
            # SOURCE LINE 835
            num_rows_rendered = 1 
            
            __M_writer(u'\n')
        # SOURCE LINE 837
        for i, item in enumerate( query ):
            # SOURCE LINE 838
            __M_writer(u'            ')
            encoded_id = trans.security.encode_id( item.id ) 
            
            __M_writer(u'\n            <tr ')
            # SOURCE LINE 840
            if current_item == item:
                # SOURCE LINE 841
                __M_writer(u'                class="current" ')
            # SOURCE LINE 843
            __M_writer(u'            > \n')
            # SOURCE LINE 845
            if show_item_checkboxes:
                # SOURCE LINE 846
                __M_writer(u'                    <td style="width: 1.5em;">\n                        <input type="checkbox" name="id" value="')
                # SOURCE LINE 847
                __M_writer(unicode(encoded_id))
                __M_writer(u'" id="')
                __M_writer(unicode(encoded_id))
                __M_writer(u'" class="grid-row-select-checkbox" />\n                    </td>\n')
            # SOURCE LINE 851
            for column in grid.columns:
                # SOURCE LINE 852
                if column.visible:
                    # SOURCE LINE 853
                    __M_writer(u'                        ')

                            # Nowrap
                    nowrap = ""
                    if column.nowrap:
                      nowrap = 'style="white-space:nowrap;"'
                    # Link
                    link = column.get_link( trans, grid, item )
                    if link:
                        href = url( **link )
                    else:
                        href = None
                    # Value (coerced to list so we can loop)
                    value = column.get_value( trans, grid, item )
                    if column.ncells == 1:
                        value = [ value ]
                                            
                    
                    # SOURCE LINE 868
                    __M_writer(u'\n')
                    # SOURCE LINE 869
                    for cellnum, v in enumerate( value ):
                        # SOURCE LINE 870
                        __M_writer(u'                            ')

                        id = ""
                        # Handle non-ascii chars.
                        if isinstance(v, str):
                            v = unicode(v, 'utf-8')
                        # Attach popup menu?
                        if column.attach_popup and cellnum == 0:
                            id = 'grid-%d-popup' % i
                        # Determine appropriate class
                        cls = ""
                        if column.attach_popup or href:
                            cls = "menubutton"
                        if column.attach_popup and href:
                            cls = "menubutton split"
                        
                                                    
                        
                        # SOURCE LINE 885
                        __M_writer(u'\n                            <td ')
                        # SOURCE LINE 886
                        __M_writer(unicode(nowrap))
                        __M_writer(u'>\n')
                        # SOURCE LINE 887
                        if href:
                            # SOURCE LINE 888
                            if len(grid.operations) != 0:
                                # SOURCE LINE 889
                                __M_writer(u'                                <div id="')
                                __M_writer(unicode(id))
                                __M_writer(u'" class="')
                                __M_writer(unicode(cls))
                                __M_writer(u'" style="float: left;">\n')
                            # SOURCE LINE 891
                            __M_writer(u'                                    <a class="label" href="')
                            __M_writer(unicode(href))
                            __M_writer(u'">')
                            __M_writer(unicode(v))
                            __M_writer(u'</a>\n')
                            # SOURCE LINE 892
                            if len(grid.operations) != 0:
                                # SOURCE LINE 893
                                __M_writer(u'                                </div>\n')
                            # SOURCE LINE 895
                        else:
                            # SOURCE LINE 896
                            __M_writer(u'                                <div id="')
                            __M_writer(unicode(id))
                            __M_writer(u'" class="')
                            __M_writer(unicode(cls))
                            __M_writer(u'"><label id="')
                            __M_writer(unicode(column.label_id_prefix))
                            __M_writer(unicode(encoded_id))
                            __M_writer(u'" for="')
                            __M_writer(unicode(encoded_id))
                            __M_writer(u'">')
                            __M_writer(unicode(v))
                            __M_writer(u'</label></div>\n')
                        # SOURCE LINE 898
                        __M_writer(u'                            </td>\n')
            # SOURCE LINE 903
            __M_writer(u'                <td>\n                    <div popupmenu="grid-')
            # SOURCE LINE 904
            __M_writer(unicode(i))
            __M_writer(u'-popup">\n')
            # SOURCE LINE 905
            for operation in grid.operations:
                # SOURCE LINE 906
                if operation.allowed( item ) and operation.allow_popup:
                    # SOURCE LINE 907
                    __M_writer(u'                                ')

                    target = ""
                    if operation.target:
                        target = "target='" + operation.target + "'"
                    
                    
                    # SOURCE LINE 911
                    __M_writer(u'\n')
                    # SOURCE LINE 912
                    if operation.confirm:
                        # SOURCE LINE 913
                        __M_writer(u'                                    <a class="action-button" ')
                        __M_writer(unicode(target))
                        __M_writer(u' confirm="')
                        __M_writer(unicode(operation.confirm))
                        __M_writer(u'" href="')
                        __M_writer(unicode( url( **operation.get_url_args( item ) ) ))
                        __M_writer(u'">')
                        __M_writer(unicode(operation.label))
                        __M_writer(u'</a>\n')
                        # SOURCE LINE 914
                    else:
                        # SOURCE LINE 915
                        __M_writer(u'                                    <a class="action-button" ')
                        __M_writer(unicode(target))
                        __M_writer(u' href="')
                        __M_writer(unicode( url( **operation.get_url_args( item ) ) ))
                        __M_writer(u'">')
                        __M_writer(unicode(operation.label))
                        __M_writer(u'</a>\n')
            # SOURCE LINE 919
            __M_writer(u'                    </div>\n                </td>\n            </tr>\n            ')
            # SOURCE LINE 922
            num_rows_rendered += 1 
            
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x6557dd0')._populate(_import_ns, [u'render_message'])
        _mako_get_namespace(context, '__anon_0x6acb750')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x6ad4390')._populate(_import_ns, [u'get_class_plural'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 612
        __M_writer(u'\n    ')
        # SOURCE LINE 613
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n    ')
        # SOURCE LINE 614
        __M_writer(unicode(h.css( "autocomplete_tagging", "jquery.rating" )))
        __M_writer(u'\n    <style>\n        .count-box {\n            min-width: 1.1em;\n            padding: 5px;\n            border-width: 1px;\n            border-style: solid;\n            text-align: center;\n            display: inline-block;\n        }\n        .text-filter-val {\n            border: solid 1px #AAAAAA;\n            padding: 1px 2px 1px 3px;\n            margin-right: 5px;\n            -moz-border-radius: .5em;\n            -webkit-border-radius: .5em;\n            font-style: italic;\n        }\n        .page-link a, .inactive-link {\n            padding: 0px 7px 0px 7px;\n            color: #555;\n        }\n        .inactive-link, .current-filter {\n            font-weight: bold;\n            color: #000;\n        }\n        .submit-image {\n            background: url(')
        # SOURCE LINE 641
        __M_writer(unicode(h.url_for('/static/images/fugue/magnifier-left.png')))
        __M_writer(u') no-repeat right transparent;\n            background-color: #eee;\n            width: 20px;\n            height: 20px;\n            cursor: pointer;\n            border: 0;\n            border-left: 1px solid #ccc;\n            margin: 0;\n            padding: 0;\n            display: block;\n            float: right;\n        }\n        #advanced-search td {\n            padding: 3px;\n        }\n        #advanced-search table {\n            border-collapse: separate;\n        }\n        .delete-search-icon {\n            background: url(')
        # SOURCE LINE 660
        __M_writer(unicode(h.url_for("/static/images/delete_tag_icon_gray.png")))
        __M_writer(u') center no-repeat;\n            display: inline-block;\n            width: 10px;\n            cursor: pointer;\n            height: 18px;\n            vertical-align: middle;\n            margin-left: 2px;\n            \n        }\n        .search-box-input {\n            border: 0;\n            margin: 1px 0 0 2px;\n            float: left;\n            outline: medium none;\n            font-style: italic;\n            font-size: inherit;\n        }\n        .search-box {\n            vertical-align: bottom;\n            display: inline-block;\n            padding: 0;\n            border: 1px solid #aaa;\n        }\n        .gray-background {\n            background-color: #DDDDDD;\n        }\n        .loading-elt-overlay {\n            background-color : white;\n            opacity : 0.5;\n            width : 100%;\n            height : 100%;\n            z-index : 14000;\n            position : absolute;\n            display: none;\n        }\n')
        # SOURCE LINE 696
        if context.get('use_panels'):
            # SOURCE LINE 697
            __M_writer(u'        div#center {\n            padding: 10px;\n        }\n')
        # SOURCE LINE 701
        __M_writer(u'    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_grid_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x6557dd0')._populate(_import_ns, [u'render_message'])
        _mako_get_namespace(context, '__anon_0x6acb750')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x6ad4390')._populate(_import_ns, [u'get_class_plural'])
        isinstance = _import_ns.get('isinstance', context.get('isinstance', UNDEFINED))
        num_pages = _import_ns.get('num_pages', context.get('num_pages', UNDEFINED))
        cur_filter_dict = _import_ns.get('cur_filter_dict', context.get('cur_filter_dict', UNDEFINED))
        sort_key = _import_ns.get('sort_key', context.get('sort_key', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        app = _import_ns.get('app', context.get('app', UNDEFINED))
        filter = _import_ns.get('filter', context.get('filter', UNDEFINED))
        cur_page_num = _import_ns.get('cur_page_num', context.get('cur_page_num', UNDEFINED))
        int = _import_ns.get('int', context.get('int', UNDEFINED))
        refresh_frames = _import_ns.get('refresh_frames', context.get('refresh_frames', UNDEFINED))
        grid = _import_ns.get('grid', context.get('grid', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 54
        __M_writer(u'\n    ')
        # SOURCE LINE 55
        __M_writer(unicode(h.js("jquery.autocomplete", "autocomplete_tagging", "jquery.rating" )))
        __M_writer(u'\n    <script type="text/javascript">\n        // This is necessary so that, when nested arrays are used in ajax/post/get methods, square brackets (\'[]\') are\n        // not appended to the identifier of a nested array.\n        jQuery.ajaxSettings.traditional = true;\n        \n')
        # SOURCE LINE 62
        __M_writer(u'        $(document).ready(function() {\n            init_grid_elements();\n            init_grid_controls();\n            \n            // Initialize text filters to select text on click and use normal font when user is typing.\n            $(\'input[type=text]\').each(function() {\n                $(this).click(function() { $(this).select(); } )\n                       .keyup(function () { $(this).css("font-style", "normal"); })\n            });\n        });\n')
        # SOURCE LINE 73
        if refresh_frames:
            # SOURCE LINE 74
            if 'masthead' in refresh_frames:            
                # SOURCE LINE 76
                __M_writer(u'                if ( parent.user_changed ) {\n')
                # SOURCE LINE 77
                if trans.user:
                    # SOURCE LINE 78
                    __M_writer(u'                        parent.user_changed( "')
                    __M_writer(unicode(trans.user.email))
                    __M_writer(u'", ')
                    __M_writer(unicode(int( app.config.is_admin_user( trans.user ) )))
                    __M_writer(u' );\n')
                    # SOURCE LINE 79
                else:
                    # SOURCE LINE 80
                    __M_writer(u'                        parent.user_changed( null, false );\n')
                # SOURCE LINE 82
                __M_writer(u'                }\n')
            # SOURCE LINE 84
            if 'history' in refresh_frames:
                # SOURCE LINE 85
                __M_writer(u'                if ( parent.frames && parent.frames.galaxy_history ) {\n                    parent.frames.galaxy_history.location.href="')
                # SOURCE LINE 86
                __M_writer(unicode(h.url_for( controller='root', action='history')))
                __M_writer(u'";\n                    if ( parent.force_right_panel ) {\n                        parent.force_right_panel( \'show\' );\n                    }\n                }\n                else {\n                    // TODO: redirecting to root should be done on the server side so that page\n                    // doesn\'t have to load.\n                     \n                    // No history frame, so refresh to root to see history.\n                    window.top.location.href = "')
                # SOURCE LINE 96
                __M_writer(unicode(h.url_for( controller='root' )))
                __M_writer(u'";\n                }\n')
            # SOURCE LINE 99
            if 'tools' in refresh_frames:
                # SOURCE LINE 100
                __M_writer(u'                if ( parent.frames && parent.frames.galaxy_tools ) {\n                    parent.frames.galaxy_tools.location.href="')
                # SOURCE LINE 101
                __M_writer(unicode(h.url_for( controller='root', action='tool_menu')))
                __M_writer(u'";\n                    if ( parent.force_left_panel ) {\n                        parent.force_left_panel( \'show\' );\n                    }\n                }\n')
        # SOURCE LINE 108
        __M_writer(u'        \n        //\n        // Code to handle grid operations: filtering, sorting, paging, and operations.\n        //\n        \n        // Operations that are async (AJAX) compatible.\n        var async_ops = {};\n')
        # SOURCE LINE 115
        for operation in [op for op in grid.operations if op.async_compatible]:
            # SOURCE LINE 116
            __M_writer(u"            async_ops['")
            __M_writer(unicode(operation.label.lower()))
            __M_writer(u'\'] = "True";\n')
        # SOURCE LINE 118
        __M_writer(u'        \n        // Initialize grid controls\n        function init_grid_controls() {\n            // Initialize operation buttons.\n            $(\'input[name=operation]:submit\').each(function() {\n                $(this).click( function() {\n                   var webapp = $("input[name=webapp]").attr("value");\n                   var operation_name = $(this).val();\n                   // For some reason, $(\'input[name=id]:checked\').val() does not return all ids for checked boxes.\n                   // The code below performs this function.\n                   var item_ids = [];\n                   $(\'input[name=id]:checked\').each(function() {\n                       item_ids.push( $(this).val() );\n                   });\n                   do_operation(webapp, operation_name, item_ids); \n                });\n            });\n            \n            // Initialize submit image elements.\n            $(\'.submit-image\').each( function() {\n                // On mousedown, add class to simulate click.\n                $(this).mousedown( function() {\n                   $(this).addClass(\'gray-background\'); \n                });\n                \n                // On mouseup, add class to simulate click.\n                $(this).mouseup( function() {\n                   $(this).removeClass(\'gray-background\'); \n                });\n            });\n            \n            // Initialize sort links.\n            $(\'.sort-link\').each( function() {\n                $(this).click( function() {\n                   set_sort_condition( $(this).attr(\'sort_key\') );\n                   return false;\n                });\n            });\n            \n            // Initialize page links.\n            $(\'.page-link > a\').each( function() {\n                $(this).click( function() {\n                   set_page( $(this).attr(\'page_num\') );\n                   return false;\n                });\n            });\n\n            // Initialize categorical filters.\n            $(\'.categorical-filter > a\').each( function() {\n                $(this).click( function() {\n                    set_categorical_filter( $(this).attr(\'filter_key\'), $(this).attr(\'filter_val\') );\n                    return false;\n                });\n            });\n            \n            // Initialize text filters.\n            $(\'.text-filter-form\').each( function() {\n                $(this).submit( function() {\n                    var column_key = $(this).attr(\'column_key\');\n                    var text_input_obj = $(\'#input-\' + column_key + \'-filter\');\n                    var text_input = text_input_obj.val();\n                    text_input_obj.val(\'\');\n                    add_filter_condition(column_key, text_input, true);\n                    return false;\n                });\n            });\n            \n            // Initialize autocomplete for text inputs in search UI.\n            var t = $("#input-tags-filter");\n            if (t.length) {\n                t.autocomplete(  "')
        # SOURCE LINE 188
        __M_writer(unicode(h.url_for( controller='tag', action='tag_autocomplete_data', item_class='History' )))
        __M_writer(u'", \n                                 { selectFirst: false, autoFill: false, highlight: false, mustMatch: false });\n            }\n \n            var t2 = $("#input-name-filter");\n            if (t2.length) {\n                t2.autocomplete( "')
        # SOURCE LINE 194
        __M_writer(unicode(h.url_for( controller='history', action='name_autocomplete_data' )))
        __M_writer(u'",\n                                 { selectFirst: false, autoFill: false, highlight: false, mustMatch: false });\n            }\n            \n            // Initialize standard, advanced search toggles.\n            $(\'.advanced-search-toggle\').each( function() {\n                $(this).click( function() {\n                    $("#standard-search").slideToggle(\'fast\');\n                    $(\'#advanced-search\').slideToggle(\'fast\');\n                    return false;\n                });\n            });\n        }\n \n        // Initialize grid elements.\n        function init_grid_elements() {\n            // Initialize grid selection checkboxes.\n            $(".grid").each( function() {\n                var checkboxes = $(this).find("input.grid-row-select-checkbox");\n                var check_count = $(this).find("span.grid-selected-count");\n                var update_checked = function() {\n                    check_count.text( $(checkboxes).filter(":checked").length );\n                };\n                \n                $(checkboxes).each( function() {\n                    $(this).change(update_checked);\n                });\n                update_checked();\n            });\n            \n            // Initialize item labels.\n            $(".label").each( function() {\n                // If href has an operation in it, do operation when clicked. Otherwise do nothing.\n                var href = $(this).attr(\'href\');\n                if ( href !== undefined && href.indexOf(\'operation=\') != -1 ) {\n                    $(this).click( function() {\n                        do_operation_from_href( $(this).attr(\'href\') );\n                        return false;\n                    });   \n                }\n            });\n            \n            // Initialize ratings.\n            $(\'.community_rating_star\').rating({});\n            \n            // Initialize item menu operations.\n            make_popup_menus();\n        }\n        \n        // Filter values for categorical filters.\n        var categorical_filters = {};\n')
        # SOURCE LINE 245
        for column in grid.columns:
            # SOURCE LINE 246
            if column.filterable is not None and not isinstance( column, TextColumn ):
                # SOURCE LINE 247
                __M_writer(u'                var ')
                __M_writer(unicode(column.key))
                __M_writer(u'_filters = ')
                __M_writer(unicode( h.to_json_string( dict([ (filter.label, filter.args) for filter in column.get_accepted_filters() ]) ) ))
                __M_writer(u";\n                categorical_filters['")
                # SOURCE LINE 248
                __M_writer(unicode(column.key))
                __M_writer(u"'] = ")
                __M_writer(unicode(column.key))
                __M_writer(u'_filters;\n')
        # SOURCE LINE 251
        __M_writer(u'            \n        // Initialize URL args with filter arguments.\n        var url_args_init = ')
        # SOURCE LINE 253
        __M_writer(unicode(h.to_json_string( cur_filter_dict )))
        __M_writer(u',\n            url_args = {};\n        \n        // Place "f-" in front of all filter arguments.\n        \n        for (arg in url_args_init) {\n            url_args["f-" + arg] = url_args_init[arg];\n        }\n        \n        // Add sort argument to URL args.\n        url_args[\'sort\'] = "')
        # SOURCE LINE 263
        __M_writer(unicode(sort_key))
        __M_writer(u'";\n        \n        // Add show_item_checkboxes argument to URL args.\n        url_args[\'show_item_checkboxes\'] = ("')
        # SOURCE LINE 266
        __M_writer(unicode(context.get('show_item_checkboxes', False)))
        __M_writer(u'" === "True");\n        \n        // Add async keyword to URL args.\n        url_args[\'async\'] = true;\n        \n        // Add page to URL args.\n        url_args[\'page\'] = ')
        # SOURCE LINE 272
        __M_writer(unicode(cur_page_num))
        __M_writer(u';\n        \n        var num_pages = ')
        # SOURCE LINE 274
        __M_writer(unicode(num_pages))
        __M_writer(u';\n        \n        // Go back to page one; this is useful when a filter is applied.\n        function go_page_one() {\n            // Need to go back to page 1 if not showing all.\n            var cur_page = url_args[\'page\'];\n            if (cur_page !== null && cur_page !== undefined && cur_page != \'all\') {\n                url_args[\'page\'] = 1;\n            }               \n        }\n        \n        // Add a condition to the grid filter; this adds the condition and refreshes the grid.\n        function add_filter_condition(name, value, append) {\n            // Do nothing is value is empty.\n            if (value == "") {\n                return false;\n            }\n            \n            // Update URL arg with new condition.            \n            if (append) {\n                // Update or append value.\n                var cur_val = url_args["f-" + name];\n                var new_val;\n                if (cur_val === null || cur_val === undefined) {\n                    new_val = value;\n                } else if (typeof(cur_val) == "string") {\n                    if (cur_val == "All") {\n                        new_val = value;\n                    } else {\n                        // Replace string with array.\n                        var values = [];\n                        values[0] = cur_val;\n                        values[1] = value;\n                        new_val = values;   \n                    }\n                } else {\n                    // Current value is an array.\n                    new_val = cur_val;\n                    new_val[new_val.length] = value;\n                }\n                url_args["f-" + name] = new_val;\n            } else {\n                // Replace value.\n                url_args["f-" + name] = value;\n            }\n            \n            // Add button that displays filter and provides a button to delete it.\n            var t = $("<span>" + value + "<a href=\'javascript:void(0);\'><span class=\'delete-search-icon\' /></a></span>");\n            t.addClass(\'text-filter-val\');\n            t.click(function() {\n                // Remove filter condition.\n \n                // Remove visible element.\n                $(this).remove();\n                \n                // Remove condition from URL args.\n                var cur_val = url_args["f-" + name];\n                if (cur_val === null || cur_val === undefined) {\n                    // Unexpected. Throw error?\n                } else if (typeof(cur_val) == "string") {\n                    if (cur_val == "All") {\n                        // Unexpected. Throw error?\n                    } else {\n                        // Remove condition.\n                        delete url_args["f-" + name];\n                    }\n                } else {\n                    // Current value is an array.\n                    var conditions = cur_val;\n                    for (var index = 0; index < conditions.length; index++) {\n                        if (conditions[index] == value) {\n                            conditions.splice(index, 1);\n                            break;\n                        }\n                    }\n                }\n \n                go_page_one();\n                update_grid();\n            });\n            \n            var container = $(\'#\' + name + "-filtering-criteria");\n            container.append(t);\n            \n            go_page_one();\n            update_grid();\n        }\n        \n        // Add tag to grid filter.\n        function add_tag_to_grid_filter(tag_name, tag_value) {\n            // Put tag name and value together.\n            var tag = tag_name + (tag_value !== undefined && tag_value != "" ? ":" + tag_value : "");\n            $(\'#advanced-search\').show(\'fast\');\n            add_filter_condition("tags", tag, true); \n        }\n \n        // Set sort condition for grid.\n        function set_sort_condition(col_key) {\n            // Set new sort condition. New sort is col_key if sorting new column; if reversing sort on\n            // currently sorted column, sort is reversed.\n            var cur_sort = url_args[\'sort\'];\n            var new_sort = col_key;\n            if ( cur_sort.indexOf( col_key ) != -1) {                \n                // Reverse sort.\n                if ( cur_sort.substring(0,1) != \'-\' ) {\n                    new_sort = \'-\' + col_key;\n                } else { \n                    // Sort reversed by using just col_key.\n                }\n            }\n            \n            // Remove sort arrows elements.\n            $(\'.sort-arrow\').remove();\n            \n            // Add sort arrow element to new sort column.\n            var sort_arrow = (new_sort.substring(0,1) == \'-\') ? "&uarr;" : "&darr;";\n            var t = $("<span>" + sort_arrow + "</span>").addClass(\'sort-arrow\');\n            var th = $("#" + col_key + \'-header\');\n            th.append(t);\n            \n            // Need to go back to page 1 if not showing all.\n            var cur_page = url_args[\'page\'];\n            if (cur_page !== null && cur_page !== undefined && cur_page != \'all\') {\n                url_args[\'page\'] = 1;\n            }\n            // Update grid.\n            url_args[\'sort\'] = new_sort;\n            go_page_one();\n            update_grid();\n        }\n        \n        // Set new value for categorical filter.\n        function set_categorical_filter(name, new_value) {\n            // Update filter hyperlinks to reflect new filter value.\n            var category_filter = categorical_filters[name];\n            var cur_value = url_args["f-" + name];\n            $("." + name + "-filter").each( function() {\n                var text = $.trim( $(this).text() );\n                var filter = category_filter[text];\n                var filter_value = filter[name];\n                if (filter_value == new_value) {\n                    // Remove filter link since grid will be using this filter. It is assumed that\n                    // this element has a single child, a hyperlink/anchor with text.\n                    $(this).empty();\n                    $(this).addClass("current-filter");\n                    $(this).append(text);\n                } else if (filter_value == cur_value) {\n                    // Add hyperlink for this filter since grid will no longer be using this filter. It is assumed that\n                    // this element has a single child, a hyperlink/anchor.\n                    $(this).empty();\n                    var t = $("<a href=\'#\'>" + text + "</a>");\n                    t.click(function() {\n                        set_categorical_filter( name, filter_value ); \n                    });\n                    $(this).removeClass("current-filter");\n                    $(this).append(t);\n                }\n            });\n            \n            // Update grid.\n            url_args["f-" + name] = new_value;\n            go_page_one();\n            update_grid();\n        }\n        \n        // Set page to view.\n        function set_page(new_page) {\n            // Update page hyperlink to reflect new page.\n            $(".page-link").each( function() {\n               var id = $(this).attr(\'id\');\n               var page_num = parseInt( id.split("-")[2] ); // Id has form \'page-link-<page_num>\n               var cur_page = url_args[\'page\'];\n               if (page_num == new_page) {\n                   // Remove link to page since grid will be on this page. It is assumed that\n                   // this element has a single child, a hyperlink/anchor with text.\n                   var text = $(this).children().text();\n                   $(this).empty();\n                   $(this).addClass("inactive-link");\n                   $(this).text(text);\n               } else if (page_num == cur_page) {\n                   // Add hyperlink to this page since grid will no longer be on this page. It is assumed that\n                   // this element has a single child, a hyperlink/anchor.\n                   var text = $(this).text();\n                   $(this).empty();\n                   $(this).removeClass("inactive-link");\n                   var t = $("<a href=\'#\'>" + text + "</a>");\n                   t.click(function() {\n                      set_page(page_num); \n                   });\n                   $(this).append(t);\n               }\n            });\n \n            var maintain_page_links = true;\n            if (new_page == "all") {\n                url_args[\'page\'] = new_page;\n                maintain_page_links = false;\n            } else {\n                url_args[\'page\'] = parseInt(new_page);\n            }\n            update_grid(maintain_page_links);\n        }\n        \n        // Perform a grid operation.\n        function do_operation(webapp, operation, item_ids) {\n            operation = operation.toLowerCase();\n            \n            // Update URL args.\n            url_args["webapp"] = webapp;\n            url_args["operation"] = operation;\n            url_args["id"] = item_ids;\n            \n            // If operation cannot be performed asynchronously, redirect to location. Otherwise do operation.\n            var no_async = ( async_ops[operation] === undefined || async_ops[operation] === null);\n            if (no_async) {\n                go_to_URL();\n            } else {\n                update_grid(true);\n                delete url_args[\'webapp\'];\n                delete url_args[\'operation\'];\n                delete url_args[\'id\'];\n            }\n        }\n        \n        // Perform a hyperlink click that initiates an operation. If there is no operation, ignore click.\n        function do_operation_from_href(href) {\n            // Get operation, id in hyperlink\'s href.\n            var href_parts = href.split("?");\n            if (href_parts.length > 1) {\n                var href_parms_str = href_parts[1];\n                var href_parms = href_parms_str.split("&");\n                var operation = null;\n                var id = -1;\n                var webapp = \'galaxy\';\n                for (var index = 0; index < href_parms.length; index++) {\n                    if (href_parms[index].indexOf(\'operation\') != -1) {\n                        // Found operation parm; get operation value. \n                        operation = href_parms[index].split(\'=\')[1];\n                    } else if (href_parms[index].indexOf(\'id\') != -1) {\n                        // Found id parm; get id value.\n                        id = href_parms[index].split(\'=\')[1];\n                    } else if (href_parms[index].indexOf(\'webapp\') != -1) {\n                        // Found webapp parm; get webapp value.\n                        webapp = href_parms[index].split(\'=\')[1];\n                    }\n                }\n                // Do operation.\n                do_operation(webapp, operation, id);\n                return false;\n            }\n        }\n        \n        // Navigate window to the URL defined by url_args. This method should be used to short-circuit grid AJAXing.\n        function go_to_URL() {\n            // Not async request.\n            url_args[\'async\'] = false;\n            \n            // Build argument string.\n            var arg_str = "";\n            for (var arg in url_args) {\n                arg_str = arg_str + arg + "=" + url_args[arg] + "&";\n            }\n            \n            // Go.\n            window.location = encodeURI( "')
        # SOURCE LINE 538
        __M_writer(unicode(h.url_for()))
        __M_writer(u'?" + arg_str );\n        }\n        \n        // Update grid.\n        function update_grid(maintain_page_links) {\n')
        # SOURCE LINE 544
        if not grid.use_async:
            # SOURCE LINE 545
            __M_writer(u'                 go_to_URL();\n                 return;\n')
        # SOURCE LINE 548
        __M_writer(u'            \n            // If there\'s an operation in the args, do POST; otherwise, do GET.\n            var operation = url_args[\'operation\'];\n            var method = (operation !== null && operation !== undefined ? "POST" : "GET" );\n            $(\'.loading-elt-overlay\').show(); // Show overlay to indicate loading and prevent user actions.\n            $.ajax({\n                type: method,\n                url: "')
        # SOURCE LINE 555
        __M_writer(unicode(h.url_for()))
        __M_writer(u'",\n                data: url_args,\n                error: function() { alert( "Grid refresh failed" ); },\n                success: function(response_text) {\n                    // HACK: use a simple string to separate the elements in the\n                    // response: (1) table body; (2) number of pages in table; and (3) message.\n                    var parsed_response_text = response_text.split("*****");\n                    \n                    // Update grid body and footer.\n                    $(\'#grid-table-body\').html(parsed_response_text[0]);\n                    $(\'#grid-table-footer\').html(parsed_response_text[1]);\n                    \n                    // Trigger custom event to indicate grid body has changed.\n                    $(\'#grid-table-body\').trigger(\'update\');\n                    \n                    // Init grid.\n                    init_grid_elements();\n                    make_popup_menus();\n                    \n                    // Hide loading overlay.\n                    $(\'.loading-elt-overlay\').hide();\n                    \n                    // Show message if there is one.\n                    var message = $.trim( parsed_response_text[2] );\n                    if (message != "") {\n                        $(\'#grid-message\').html( message );\n                        setTimeout( function() { $(\'#grid-message\').hide(); }, 5000);\n                    }\n                }\n            });    \n        }\n        \n        function check_all_items() {\n            var chk_all = document.getElementById(\'check_all\');\n            var checks = document.getElementsByTagName(\'input\');\n            //var boxLength = checks.length;\n            var total = 0;\n            if ( chk_all.checked == true ) {\n                for ( i=0; i < checks.length; i++ ) {\n                    if ( checks[i].name.indexOf( \'id\' ) != -1) {\n                       checks[i].checked = true;\n                       total++;\n                    }\n                }\n            }\n            else {\n                for ( i=0; i < checks.length; i++ ) {\n                    if ( checks[i].name.indexOf( \'id\' ) != -1) {\n                       checks[i].checked = false\n                    }\n                }\n            }\n            init_grid_elements();\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x6557dd0')._populate(_import_ns, [u'render_message'])
        _mako_get_namespace(context, '__anon_0x6acb750')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x6ad4390')._populate(_import_ns, [u'get_class_plural'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 17
        __M_writer(u'\n')
        # SOURCE LINE 18

        self.has_left_panel=False
        self.has_right_panel=False
        self.message_box_visible=False
        self.active_view="user"
        self.overlay_visible=False
        
        
        # SOURCE LINE 24
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_grid_table(context,grid,show_item_checkboxes=False):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x6557dd0')._populate(_import_ns, [u'render_message'])
        _mako_get_namespace(context, '__anon_0x6acb750')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x6ad4390')._populate(_import_ns, [u'get_class_plural'])
        sort_key = _import_ns.get('sort_key', context.get('sort_key', UNDEFINED))
        url = _import_ns.get('url', context.get('url', UNDEFINED))
        def render_grid_table_footer_contents(grid,show_item_checkboxes=False):
            return render_render_grid_table_footer_contents(context,grid,show_item_checkboxes)
        def render_grid_table_body_contents(grid,show_item_checkboxes=False):
            return render_render_grid_table_body_contents(context,grid,show_item_checkboxes)
        query = _import_ns.get('query', context.get('query', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 760
        __M_writer(u'\n    ')
        # SOURCE LINE 761

        # Set flag to indicate whether grid has operations that operate on multiple items.
        multiple_item_ops_exist = False
        for operation in grid.operations:
            if operation.allow_multiple:
                multiple_item_ops_exist = True
                
        # Show checkboxes if flag is set or if multiple item ops exist.
        if show_item_checkboxes or multiple_item_ops_exist:
            show_item_checkboxes = True
            
        
        # SOURCE LINE 771
        __M_writer(u'\n\n    <form action="')
        # SOURCE LINE 773
        __M_writer(unicode(url()))
        __M_writer(u'" method="post" onsubmit="return false;">\n        <div class="loading-elt-overlay"></div>\n        <table id="grid-table" class="grid">\n            <thead id="grid-table-header">\n                <tr>\n')
        # SOURCE LINE 778
        if show_item_checkboxes:
            # SOURCE LINE 779
            __M_writer(u'                        <th>\n')
            # SOURCE LINE 780
            if query.count() > 0:
                # SOURCE LINE 781
                __M_writer(u'                                <input type="checkbox" id="check_all" name=select_all_checkbox value="true" onclick=\'check_all_items(1);\'><input type="hidden" name=select_all_checkbox value="true">\n')
            # SOURCE LINE 783
            __M_writer(u'                        </th>\n')
        # SOURCE LINE 785
        for column in grid.columns:
            # SOURCE LINE 786
            if column.visible:
                # SOURCE LINE 787
                __M_writer(u'                            ')

                href = ""
                extra = ""
                if column.sortable:
                    if sort_key.endswith(column.key):
                        if not sort_key.startswith("-"):
                            href = url( sort=( "-" + column.key ) )
                            extra = "&darr;"
                        else:
                            href = url( sort=( column.key ) )
                            extra = "&uarr;"
                    else:
                        href = url( sort=column.key )
                                            
                
                # SOURCE LINE 800
                __M_writer(u'\n                            <th')
                # SOURCE LINE 802
                __M_writer(u'                            id="')
                __M_writer(unicode(column.key))
                __M_writer(u'-header"\n')
                # SOURCE LINE 803
                if column.ncells > 1:
                    # SOURCE LINE 804
                    __M_writer(u'                                colspan="')
                    __M_writer(unicode(column.ncells))
                    __M_writer(u'"\n')
                # SOURCE LINE 806
                __M_writer(u'                            >\n')
                # SOURCE LINE 807
                if href:
                    # SOURCE LINE 808
                    __M_writer(u'                                    <a href="')
                    __M_writer(unicode(href))
                    __M_writer(u'" class="sort-link" sort_key="')
                    __M_writer(unicode(column.key))
                    __M_writer(u'">')
                    __M_writer(unicode(column.label))
                    __M_writer(u'</a>\n')
                    # SOURCE LINE 809
                else:
                    # SOURCE LINE 810
                    __M_writer(u'                                    ')
                    __M_writer(unicode(column.label))
                    __M_writer(u'\n')
                # SOURCE LINE 812
                __M_writer(u'                                <span class="sort-arrow">')
                __M_writer(unicode(extra))
                __M_writer(u'</span>\n                            </th>\n')
        # SOURCE LINE 816
        __M_writer(u'                    <th></th>\n                </tr>\n            </thead>\n            <tbody id="grid-table-body">\n                ')
        # SOURCE LINE 820
        __M_writer(unicode(render_grid_table_body_contents( grid, show_item_checkboxes )))
        __M_writer(u'\n            </tbody>\n            <tfoot id="grid-table-footer">\n                ')
        # SOURCE LINE 823
        __M_writer(unicode(render_grid_table_footer_contents( grid, show_item_checkboxes )))
        __M_writer(u'\n            </tfoot>\n        </table>\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_grid_body(context,grid):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x6557dd0')._populate(_import_ns, [u'render_message'])
        _mako_get_namespace(context, '__anon_0x6acb750')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x6ad4390')._populate(_import_ns, [u'get_class_plural'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 43
        __M_writer(u'\n    ')
        # SOURCE LINE 44
        __M_writer(unicode(self.make_grid( grid )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_make_grid(context,grid):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x6557dd0')._populate(_import_ns, [u'render_message'])
        _mako_get_namespace(context, '__anon_0x6acb750')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x6ad4390')._populate(_import_ns, [u'get_class_plural'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        show_item_checkboxes = _import_ns.get('show_item_checkboxes', context.get('show_item_checkboxes', UNDEFINED))
        render_message = _import_ns.get('render_message', context.get('render_message', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 710
        __M_writer(u'\n    <table>\n        <tr>\n            <td width="75%">')
        # SOURCE LINE 713
        __M_writer(unicode(self.render_grid_header( grid )))
        __M_writer(u'</td>\n            <td></td>\n            <td></td>\n        </tr>\n        <tr>\n            <td width="100%" id="grid-message" valign="top">')
        # SOURCE LINE 718
        __M_writer(unicode(render_message( message, status )))
        __M_writer(u'</td>\n            <td></td>\n            <td></td>\n        </tr>\n    </table>\n\n    ')
        # SOURCE LINE 724
        __M_writer(unicode(self.render_grid_table( grid, show_item_checkboxes )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_grid_table_footer_contents(context,grid,show_item_checkboxes=False):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x6557dd0')._populate(_import_ns, [u'render_message'])
        _mako_get_namespace(context, '__anon_0x6acb750')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x6ad4390')._populate(_import_ns, [u'get_class_plural'])
        num_pages = _import_ns.get('num_pages', context.get('num_pages', UNDEFINED))
        url = _import_ns.get('url', context.get('url', UNDEFINED))
        get_class_plural = _import_ns.get('get_class_plural', context.get('get_class_plural', UNDEFINED))
        cur_page_num = _import_ns.get('cur_page_num', context.get('cur_page_num', UNDEFINED))
        range = _import_ns.get('range', context.get('range', UNDEFINED))
        num_page_links = _import_ns.get('num_page_links', context.get('num_page_links', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 933
        __M_writer(u'\n')
        # SOURCE LINE 935
        __M_writer(u'    ')
        __M_writer(u'\n    ')
        # SOURCE LINE 936
        items_plural = get_class_plural( grid.model_class ).lower() 
        
        __M_writer(u'\n')
        # SOURCE LINE 937
        if grid.use_paging and num_pages > 1:
            # SOURCE LINE 938
            __M_writer(u'        <tr id="page-links-row">\n')
            # SOURCE LINE 939
            if show_item_checkboxes:
                # SOURCE LINE 940
                __M_writer(u'                <td></td>\n')
            # SOURCE LINE 942
            __M_writer(u'            <td colspan="100">\n                <span id=\'page-link-container\'>\n')
            # SOURCE LINE 945
            __M_writer(u'                    ')

                        #
                        # Set minimum & maximum page.
                        # 
            page_link_range = num_page_links/2
            
            # First pass on min page.
            min_page = cur_page_num - page_link_range
            if min_page >= 1:
                # Min page is fine.
                min_offset = 0
            else:
                # Min page is too low.
                min_page = 1
                min_offset = page_link_range - ( cur_page_num - min_page )
            
            # Set max page.
            max_range = page_link_range + min_offset
            max_page = cur_page_num + max_range
            if max_page <= num_pages:
                # Max page is fine.
                max_offset = 0
            else:
                # Max page is too high.
                max_page = num_pages
                # +1 to account for the +1 in the loop below.
                max_offset = max_range - ( max_page + 1 - cur_page_num )
            
            # Second and final pass on min page to add any unused 
            # offset from max to min.
            if max_offset != 0:
                min_page -= max_offset
                if min_page < 1:
                    min_page = 1
                                
            
            # SOURCE LINE 979
            __M_writer(u'\n                    Page:\n')
            # SOURCE LINE 981
            if min_page > 1:
                # SOURCE LINE 982
                __M_writer(u'                        <span class=\'page-link\'><a href="')
                __M_writer(unicode(url( page=1 )))
                __M_writer(u'" page_num="1">1</a></span> ...\n')
            # SOURCE LINE 984
            for page_index in range(min_page, max_page + 1):
                # SOURCE LINE 985
                if page_index == cur_page_num:
                    # SOURCE LINE 986
                    __M_writer(u'                            <span class=\'page-link inactive-link\' id="page-link-')
                    __M_writer(unicode(page_index))
                    __M_writer(u'">')
                    __M_writer(unicode(page_index))
                    __M_writer(u'</span>\n')
                    # SOURCE LINE 987
                else:
                    # SOURCE LINE 988
                    __M_writer(u'                            ')
                    args = { 'page' : page_index } 
                    
                    __M_writer(u'\n                            <span class=\'page-link\' id="page-link-')
                    # SOURCE LINE 989
                    __M_writer(unicode(page_index))
                    __M_writer(u'"><a href="')
                    __M_writer(unicode(url( args )))
                    __M_writer(u'" page_num=\'')
                    __M_writer(unicode(page_index))
                    __M_writer(u"'>")
                    __M_writer(unicode(page_index))
                    __M_writer(u'</a></span>\n')
            # SOURCE LINE 992
            if max_page < num_pages:
                # SOURCE LINE 993
                __M_writer(u'                        ...\n                        <span class=\'page-link\'><a href="')
                # SOURCE LINE 994
                __M_writer(unicode(url( page=num_pages )))
                __M_writer(u'" page_num="')
                __M_writer(unicode(num_pages))
                __M_writer(u'">')
                __M_writer(unicode(num_pages))
                __M_writer(u'</a></span>\n')
            # SOURCE LINE 996
            __M_writer(u'                </span>\n                \n')
            # SOURCE LINE 999
            __M_writer(u'                <span class=\'page-link\' id=\'show-all-link-span\'> | <a href="')
            __M_writer(unicode(url( page='all' )))
            __M_writer(u'" page_num="all">Show All</a></span>\n            </td>\n        </tr>    \n')
        # SOURCE LINE 1004
        if show_item_checkboxes:
            # SOURCE LINE 1005
            __M_writer(u'        <tr>\n            <td></td>\n            <td colspan="100">\n                For <span class="grid-selected-count"></span> selected ')
            # SOURCE LINE 1008
            __M_writer(unicode(items_plural))
            __M_writer(u':\n')
            # SOURCE LINE 1009
            for operation in grid.operations:
                # SOURCE LINE 1010
                if operation.allow_multiple:
                    # SOURCE LINE 1011
                    __M_writer(u'                        <input type="submit" name="operation" value="')
                    __M_writer(unicode(operation.label))
                    __M_writer(u'" class="action-button">\n')
            # SOURCE LINE 1014
            __M_writer(u'            </td>\n        </tr>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x6557dd0')._populate(_import_ns, [u'render_message'])
        _mako_get_namespace(context, '__anon_0x6acb750')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x6ad4390')._populate(_import_ns, [u'get_class_plural'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 49
        __M_writer(u'\n   ')
        # SOURCE LINE 50
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n   ')
        # SOURCE LINE 51
        __M_writer(unicode(self.grid_javascripts()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


