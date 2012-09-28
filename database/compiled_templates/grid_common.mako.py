from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1297785256.070946
_template_filename=u'templates/grid_common.mako'
_template_uri=u'./grid_common.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding=None
_exports = ['render_grid_filters', 'render_grid_column_filter']


# SOURCE LINE 1
 
from galaxy.web.framework.helpers.grids import TextColumn, StateColumn, GridColumnFilter 
from galaxy.web.framework.helpers import iff


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n\n')
        # SOURCE LINE 102
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_grid_filters(context,grid):
    context.caller_stack._push_frame()
    try:
        cur_filter_dict = context.get('cur_filter_dict', UNDEFINED)
        url = context.get('url', UNDEFINED)
        kwargs = context.get('kwargs', UNDEFINED)
        def render_grid_column_filter(grid,column):
            return render_render_grid_column_filter(context,grid,column)
        default_filter_dict = context.get('default_filter_dict', UNDEFINED)
        endif = context.get('endif', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 105
        __M_writer(u'\n')
        # SOURCE LINE 107
        __M_writer(u'    <div id="standard-search">\n        <table>\n            <tr><td style="padding: 0;">\n                <table>\n')
        # SOURCE LINE 111
        for column in grid.columns:
            # SOURCE LINE 112
            if column.filterable == "standard":
                # SOURCE LINE 113
                __M_writer(u'                       ')
                __M_writer(unicode(render_grid_column_filter( grid, column )))
                __M_writer(u'\n')
        # SOURCE LINE 116
        __M_writer(u'                </table>\n            </td></tr>\n            <tr><td>\n')
        # SOURCE LINE 123
        __M_writer(u'                \n')
        # SOURCE LINE 125
        __M_writer(u'                ')

        show_advanced_search_link = False
        for column in grid.columns:
            if column.filterable == "advanced":
                show_advanced_search_link = True
                break
            endif
                        
        
        # SOURCE LINE 132
        __M_writer(u'\n')
        # SOURCE LINE 133
        if show_advanced_search_link:
            # SOURCE LINE 134
            __M_writer(u'                    ')
            args = { "advanced-search" : True } 
            
            __M_writer(u'\n                    <a href="')
            # SOURCE LINE 135
            __M_writer(unicode(url( args )))
            __M_writer(u'" class="advanced-search-toggle">Advanced Search</a>\n')
        # SOURCE LINE 137
        __M_writer(u'            </td></tr>\n        </table>\n    </div>\n    \n')
        # SOURCE LINE 142
        __M_writer(u'    ')

        # Show advanced search if flag set or if there are filters for advanced search fields.
        advanced_search_display = "none"
        if 'advanced-search' in kwargs and kwargs['advanced-search'] in ['True', 'true']:
            advanced_search_display = "block"
            
        for column in grid.columns:
            if column.filterable == "advanced":
                ## Show div if current filter has value that is different from the default filter.
                if column.key in cur_filter_dict and column.key in default_filter_dict and \
                    cur_filter_dict[column.key] != default_filter_dict[column.key]:
                        advanced_search_display = "block"
            
        
        # SOURCE LINE 154
        __M_writer(u'\n    <div id="advanced-search" style="display: ')
        # SOURCE LINE 155
        __M_writer(unicode(advanced_search_display))
        __M_writer(u'; margin-top: 5px; border: 1px solid #ccc;">\n        <table>\n            <tr><td style="text-align: left" colspan="100">\n                ')
        # SOURCE LINE 158
        args = { "advanced-search" : False } 
        
        __M_writer(u'\n                <a href="')
        # SOURCE LINE 159
        __M_writer(unicode(url( args )))
        __M_writer(u'" class="advanced-search-toggle">Close Advanced Search</a>\n')
        # SOURCE LINE 166
        __M_writer(u'            </td></tr>\n')
        # SOURCE LINE 167
        for column in grid.columns:            
            # SOURCE LINE 168
            if column.filterable == "advanced":
                # SOURCE LINE 170
                if column.key in cur_filter_dict and column.key in default_filter_dict and \
                        cur_filter_dict[column.key] != default_filter_dict[column.key]:
                    # SOURCE LINE 172
                    __M_writer(u'                        <script type="text/javascript">\n                            $(\'#advanced-search\').css("display", "block");\n                        </script>\n')
                # SOURCE LINE 176
                __M_writer(u'            \n                    ')
                # SOURCE LINE 177
                __M_writer(unicode(render_grid_column_filter( grid, column )))
                __M_writer(u'\n')
        # SOURCE LINE 180
        __M_writer(u'        </table>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_grid_column_filter(context,grid,column):
    context.caller_stack._push_frame()
    try:
        basestring = context.get('basestring', UNDEFINED)
        cur_filter_dict = context.get('cur_filter_dict', UNDEFINED)
        url = context.get('url', UNDEFINED)
        h = context.get('h', UNDEFINED)
        list = context.get('list', UNDEFINED)
        len = context.get('len', UNDEFINED)
        dict = context.get('dict', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 7
        __M_writer(u'\n    <tr>\n        ')
        # SOURCE LINE 9

        column_label = column.label
        if column.filterable == "advanced":
            column_label = column_label.lower()
                
        
        # SOURCE LINE 13
        __M_writer(u'\n')
        # SOURCE LINE 14
        if column.filterable == "advanced":
            # SOURCE LINE 15
            __M_writer(u'            <td align="left" style="padding-left: 10px">')
            __M_writer(unicode(column_label))
            __M_writer(u':</td>\n')
        # SOURCE LINE 17
        __M_writer(u'        <td style="padding: 0;">\n')
        # SOURCE LINE 18
        if isinstance(column, TextColumn):
            # SOURCE LINE 19
            __M_writer(u'                <form class="text-filter-form" column_key="')
            __M_writer(unicode(column.key))
            __M_writer(u'" action="')
            __M_writer(unicode(url( dict() )))
            __M_writer(u'" method="get" >\n')
            # SOURCE LINE 21
            for temp_column in grid.columns:
                # SOURCE LINE 22
                if temp_column.key in cur_filter_dict:
                    # SOURCE LINE 23
                    __M_writer(u'                            ')
                    value = cur_filter_dict[ temp_column.key ] 
                    
                    __M_writer(u'\n')
                    # SOURCE LINE 24
                    if value != "All":
                        # SOURCE LINE 25
                        __M_writer(u'                                ')

                        if isinstance( temp_column, TextColumn ):
                            value = h.to_json_string( value )
                                                        
                        
                        # SOURCE LINE 28
                        __M_writer(u'\n                                <input type="hidden" id="')
                        # SOURCE LINE 29
                        __M_writer(unicode(temp_column.key))
                        __M_writer(u'" name="f-')
                        __M_writer(unicode(temp_column.key))
                        __M_writer(u'" value=\'')
                        __M_writer(unicode(value))
                        __M_writer(u"'/>\n")
            # SOURCE LINE 33
            __M_writer(u'                    \n')
            # SOURCE LINE 35
            __M_writer(u'                    <span id="')
            __M_writer(unicode(column.key))
            __M_writer(u'-filtering-criteria">\n')
            # SOURCE LINE 36
            if column.key in cur_filter_dict:
                # SOURCE LINE 37
                __M_writer(u'                            ')
                column_filter = cur_filter_dict[column.key] 
                
                __M_writer(u'\n')
                # SOURCE LINE 38
                if isinstance( column_filter, basestring ):
                    # SOURCE LINE 39
                    if column_filter != "All":
                        # SOURCE LINE 40
                        __M_writer(u"                                    <span class='text-filter-val'>\n                                        ")
                        # SOURCE LINE 41
                        __M_writer(unicode(cur_filter_dict[column.key]))
                        __M_writer(u'\n                                        ')
                        # SOURCE LINE 42
                        filter_all = GridColumnFilter( "", { column.key : "All" } ) 
                        
                        __M_writer(u'\n                                        <a href="')
                        # SOURCE LINE 43
                        __M_writer(unicode(url( filter_all.get_url_args() )))
                        __M_writer(u'"><span class="delete-search-icon" /></a>                                \n                                    </span>\n')
                    # SOURCE LINE 46
                elif isinstance( column_filter, list ):
                    # SOURCE LINE 47
                    for i, filter in enumerate( column_filter ):
                        # SOURCE LINE 48
                        if i > 0:
                            # SOURCE LINE 49
                            __M_writer(u'                                        ,\n')
                        # SOURCE LINE 51
                        __M_writer(u"                                    <span class='text-filter-val'>")
                        __M_writer(unicode(filter))
                        __M_writer(u'\n                                        ')
                        # SOURCE LINE 52

                        new_filter = list( column_filter )
                        del new_filter[ i ]
                        new_column_filter = GridColumnFilter( "", { column.key : h.to_json_string( new_filter ) } )
                                                                
                        
                        # SOURCE LINE 56
                        __M_writer(u'\n                                        <a href="')
                        # SOURCE LINE 57
                        __M_writer(unicode(url( new_column_filter.get_url_args() )))
                        __M_writer(u'"><span class="delete-search-icon" /></a>\n                                    </span>\n')
            # SOURCE LINE 62
            __M_writer(u'                    </span>\n')
            # SOURCE LINE 64
            __M_writer(u'                    <span class="search-box">\n                        ')
            # SOURCE LINE 65
 
                            # Set value, size of search input field. Minimum size is 20 characters.
            value = iff( column.filterable == "standard", column.label.lower(), "") 
            size = len( value )
            if size < 20:
                size = 20
            # +4 to account for search icon/button.
            size = size + 4
                                    
            
            # SOURCE LINE 73
            __M_writer(u'\n                        <input class="search-box-input" id="input-')
            # SOURCE LINE 74
            __M_writer(unicode(column.key))
            __M_writer(u'-filter" name="f-')
            __M_writer(unicode(column.key))
            __M_writer(u'" type="text" value="')
            __M_writer(unicode(value))
            __M_writer(u'" size="')
            __M_writer(unicode(size))
            __M_writer(u'"/>\n                        <button class="submit-image" type="submit" title=\'Search\'><span style="display: none;"></button>\n                    </span>\n                </form>\n')
            # SOURCE LINE 78
        else:
            # SOURCE LINE 79
            __M_writer(u'                <span id="')
            __M_writer(unicode(column.key))
            __M_writer(u'-filtering-criteria">\n')
            # SOURCE LINE 80
            for i, filter in enumerate( column.get_accepted_filters() ):
                # SOURCE LINE 81
                __M_writer(u'                        ')
 
                            # HACK: we know that each filter will have only a single argument, so get that single argument.
                for key, arg in filter.args.items():
                    filter_key = key
                    filter_arg = arg
                                        
                
                # SOURCE LINE 86
                __M_writer(u'\n')
                # SOURCE LINE 87
                if i > 0:
                    # SOURCE LINE 88
                    __M_writer(u'                            |\n')
                # SOURCE LINE 90
                if column.key in cur_filter_dict and column.key in filter.args and cur_filter_dict[column.key] == filter.args[column.key]:
                    # SOURCE LINE 91
                    __M_writer(u'                            <span class="categorical-filter ')
                    __M_writer(unicode(column.key))
                    __M_writer(u'-filter current-filter">')
                    __M_writer(unicode(filter.label))
                    __M_writer(u'</span>\n')
                    # SOURCE LINE 92
                else:
                    # SOURCE LINE 93
                    __M_writer(u'                            <span class="categorical-filter ')
                    __M_writer(unicode(column.key))
                    __M_writer(u'-filter">\n                                <a href="')
                    # SOURCE LINE 94
                    __M_writer(unicode(url( filter.get_url_args() )))
                    __M_writer(u'" filter_key="')
                    __M_writer(unicode(filter_key))
                    __M_writer(u'" filter_val="')
                    __M_writer(unicode(filter_arg))
                    __M_writer(u'">')
                    __M_writer(unicode(filter.label))
                    __M_writer(u'</a>\n                            </span>\n')
            # SOURCE LINE 98
            __M_writer(u'                </span>\n')
        # SOURCE LINE 100
        __M_writer(u'        </td>\n    </tr>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


