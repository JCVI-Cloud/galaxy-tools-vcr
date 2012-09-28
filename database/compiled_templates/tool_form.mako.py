# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1309387809.8504701
_template_filename='templates/tool_form.mako'
_template_uri='tool_form.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['do_inputs', 'row_for_param']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        add_frame = context.get('add_frame', UNDEFINED)
        errors = context.get('errors', UNDEFINED)
        h = context.get('h', UNDEFINED)
        tool = context.get('tool', UNDEFINED)
        def do_inputs(inputs,tool_state,errors,prefix,other_values=None):
            return render_do_inputs(context.locals_(__M_locals),inputs,tool_state,errors,prefix,other_values)
        len = context.get('len', UNDEFINED)
        util = context.get('util', UNDEFINED)
        unicode = context.get('unicode', UNDEFINED)
        type = context.get('type', UNDEFINED)
        tool_state = context.get('tool_state', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        AttributeError = context.get('AttributeError', UNDEFINED)
        app = context.get('app', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!-- -->\n<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\n\n')
        # SOURCE LINE 4

        from galaxy.util.expressions import ExpressionContext
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['ExpressionContext'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 6
        __M_writer(u'\n\n<html>\n\n<head>\n<title>Galaxy</title>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n')
        # SOURCE LINE 13
        __M_writer(unicode(h.css( "base", "autocomplete_tagging" )))
        __M_writer(u'\n')
        # SOURCE LINE 14
        __M_writer(unicode(h.js( "jquery", "galaxy.base", "jquery.autocomplete" )))
        __M_writer(u'\n<script type="text/javascript">\n$(function() {\n    $(window).bind("refresh_on_change", function() {\n        $(\':file\').each( function() {\n            var file = $(this);\n            var file_value = file.val();\n            if (file_value) {\n                // disable file input, since we don\'t want to upload the file on refresh\n                var file_name = $(this).attr("name");\n                file.attr( { name: \'replaced_file_input_\' + file_name, disabled: true } );\n                // create a new hidden field which stores the filename and has the original name of the file input\n                var new_file_input = $(document.createElement(\'input\'));\n                new_file_input.attr( { "type": "hidden", "value": file_value, "name": file_name } );\n                file.after(new_file_input);\n            }\n        });\n    });\n    \n    // For drilldown parameters: add expand/collapse buttons and collapse initially-collapsed elements\n    $( \'li ul.toolParameterExpandableCollapsable\' ).each( function() {\n        var el = $(this),\n            parent_li = el.parent(\'li\'),\n            sub_ul = el.remove();\n        \n        parent_li.find( \'span\' ).wrapInner( \'<a/>\' ).find( \'a\' ).click( function() {\n            sub_ul.toggle();\n            (this).html( sub_ul.is(":hidden") ? \'[+]\' : \'[-]\' );\n        });\n        parent_li.append( sub_ul );\n    });\n    \n    $( \'ul ul.toolParameterExpandableCollapsable\' ).each( function(i) {\n        var el = $(this);\n        if (el.attr("default_state") === "collapsed") {\n            el.hide();\n        }\n    });\n    \n    function checkUncheckAll( name, check ) {\n        $("input[name=\'" + name + "\'][type=\'checkbox\']").attr(\'checked\', !!check);\n    }\n    \n    // Inserts the Select All / Unselect All buttons for checkboxes\n    $("div.checkUncheckAllPlaceholder").each( function() {\n        var check_name = $(this).attr("checkbox_name");\n        select_link = $("<a class=\'action-button\'></a>").text("Select All").click(function() {\n           checkUncheckAll(check_name, true);\n        });\n        unselect_link = $("<a class=\'action-button\'></a>").text("Unselect All").click(function() {\n           checkUncheckAll(check_name, false);\n        });\n        $(this).append(select_link).append(" ").append(unselect_link);\n    });\n});\n\n')
        # SOURCE LINE 70
        if not add_frame.debug:
            # SOURCE LINE 71
            __M_writer(u'    if( window.name != "galaxy_main" ) {\n        location.replace( \'')
            # SOURCE LINE 72
            __M_writer(unicode(h.url_for( controller='root', action='index', tool_id=tool.id )))
            __M_writer(u"' );\n    }\n")
            pass
        # SOURCE LINE 75
        __M_writer(u'\n</script>\n</head>\n\n<body>\n    ')
        # SOURCE LINE 155
        __M_writer(u'\n    \n    ')
        # SOURCE LINE 197
        __M_writer(u'\n    \n')
        # SOURCE LINE 199
        if add_frame.from_noframe:
            # SOURCE LINE 200
            __M_writer(u'        <div class="warningmessage">\n        <strong>Welcome to Galaxy</strong>\n        <hr/>\n        It appears that you found this tool from a link outside of Galaxy.\n        If you\'re not familiar with Galaxy, please consider visiting the\n        <a href="')
            # SOURCE LINE 205
            __M_writer(unicode(h.url_for( controller='root' )))
            __M_writer(u'" target="_top">welcome page</a>.\n        To learn more about what Galaxy is and what it can do for you, please visit\n        the <a href="$add_frame.wiki_url" target="_top">Galaxy wiki</a>.\n        </div>\n        <br/>\n')
            pass
        # SOURCE LINE 211
        __M_writer(u'    \n')
        # SOURCE LINE 214
        __M_writer(u'    ')

        try:   
            tool_url = h.url_for(tool.action)
        except AttributeError:
            assert len(tool.action) == 2
            tool_url = tool.action[0] + h.url_for(tool.action[1])
            
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['tool_url'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 220
        __M_writer(u'<div class="toolForm" id="')
        __M_writer(unicode(tool.id))
        __M_writer(u'">\n')
        # SOURCE LINE 221
        if tool.has_multiple_pages:
            # SOURCE LINE 222
            __M_writer(u'            <div class="toolFormTitle">')
            __M_writer(unicode(tool.name))
            __M_writer(u' (step ')
            __M_writer(unicode(tool_state.page+1))
            __M_writer(u' of ')
            __M_writer(unicode(tool.npages))
            __M_writer(u')</div>\n')
            # SOURCE LINE 223
        else:
            # SOURCE LINE 224
            __M_writer(u'            <div class="toolFormTitle">')
            __M_writer(unicode(tool.name))
            __M_writer(u'</div>\n')
            pass
        # SOURCE LINE 226
        __M_writer(u'        <div class="toolFormBody">\n            <form id="tool_form" name="tool_form" action="')
        # SOURCE LINE 227
        __M_writer(unicode(tool_url))
        __M_writer(u'" enctype="')
        __M_writer(unicode(tool.enctype))
        __M_writer(u'" target="')
        __M_writer(unicode(tool.target))
        __M_writer(u'" method="')
        __M_writer(unicode(tool.method))
        __M_writer(u'">\n                <input type="hidden" name="tool_id" value="')
        # SOURCE LINE 228
        __M_writer(unicode(tool.id))
        __M_writer(u'">\n                <input type="hidden" name="tool_state" value="')
        # SOURCE LINE 229
        __M_writer(unicode(util.object_to_string( tool_state.encode( tool, app ) )))
        __M_writer(u'">\n')
        # SOURCE LINE 230
        if tool.display_by_page[tool_state.page]:
            # SOURCE LINE 231
            __M_writer(u'                    ')
            __M_writer(unicode(trans.fill_template_string( tool.display_by_page[tool_state.page], context=tool.get_param_html_map( trans, tool_state.page, tool_state.inputs ) )))
            __M_writer(u'\n                    <input type="submit" class="primary-button" name="runtool_btn" value="Execute">\n')
            # SOURCE LINE 233
        else:
            # SOURCE LINE 234
            __M_writer(u'                    ')
            __M_writer(unicode(do_inputs( tool.inputs_by_page[ tool_state.page ], tool_state.inputs, errors, "" )))
            __M_writer(u'\n                    <div class="form-row">\n')
            # SOURCE LINE 236
            if tool_state.page == tool.last_page:
                # SOURCE LINE 237
                __M_writer(u'                            <input type="submit" class="primary-button" name="runtool_btn" value="Execute">\n')
                # SOURCE LINE 238
            else:
                # SOURCE LINE 239
                __M_writer(u'                            <input type="submit" class="primary-button" name="runtool_btn" value="Next step">\n')
                pass
            # SOURCE LINE 241
            __M_writer(u'                    </div>\n')
            pass
        # SOURCE LINE 243
        __M_writer(u'            </form>\n        </div>\n    </div>\n')
        # SOURCE LINE 246
        if tool.help:
            # SOURCE LINE 247
            __M_writer(u'        <div class="toolHelp">\n            <div class="toolHelpBody">\n                ')
            # SOURCE LINE 249

            if tool.has_multiple_pages:
                tool_help = tool.help_by_page[tool_state.page]
            else:
                tool_help = tool.help
            
            # Convert to unicode to display non-ascii characters.
            if type( tool_help ) is not unicode:
                tool_help = unicode( tool_help, 'utf-8')
                            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['tool_help'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 258
            __M_writer(u'\n                ')
            # SOURCE LINE 259
            __M_writer(unicode(tool_help))
            __M_writer(u'\n            </div>        \n        </div>\n')
            pass
        # SOURCE LINE 263
        __M_writer(u'</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_do_inputs(context,inputs,tool_state,errors,prefix,other_values=None):
    context.caller_stack._push_frame()
    try:
        def row_for_param(prefix,param,parent_state,parent_errors,other_values):
            return render_row_for_param(context,prefix,param,parent_state,parent_errors,other_values)
        h = context.get('h', UNDEFINED)
        def do_inputs(inputs,tool_state,errors,prefix,other_values=None):
            return render_do_inputs(context,inputs,tool_state,errors,prefix,other_values)
        len = context.get('len', UNDEFINED)
        range = context.get('range', UNDEFINED)
        dict = context.get('dict', UNDEFINED)
        str = context.get('str', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        ExpressionContext = context.get('ExpressionContext', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 80
        __M_writer(u'\n      ')
        # SOURCE LINE 81
        other_values = ExpressionContext( tool_state, other_values ) 
        
        __M_writer(u'\n')
        # SOURCE LINE 82
        for input_index, input in enumerate( inputs.itervalues() ):
            # SOURCE LINE 83
            if not input.visible:
                # SOURCE LINE 84
                __M_writer(u'                ')
                pass 
                
                __M_writer(u'\n')
                # SOURCE LINE 85
            elif input.type == "repeat":
                # SOURCE LINE 86
                __M_writer(u'              <div class="repeat-group">\n                  <div class="form-title-row"><b>')
                # SOURCE LINE 87
                __M_writer(unicode(input.title_plural))
                __M_writer(u'</b></div>\n                  ')
                # SOURCE LINE 88
                repeat_state = tool_state[input.name] 
                
                __M_writer(u'\n')
                # SOURCE LINE 89
                for i in range( len( repeat_state ) ):
                    # SOURCE LINE 90
                    __M_writer(u'                    <div class="repeat-group-item">\n                        ')
                    # SOURCE LINE 91

                    if input.name in errors:
                        rep_errors = errors[input.name][i]
                    else:
                        rep_errors = dict()
                    index = repeat_state[i]['__index__']
                    
                    
                    # SOURCE LINE 97
                    __M_writer(u'\n                        <div class="form-title-row"><b>')
                    # SOURCE LINE 98
                    __M_writer(unicode(input.title))
                    __M_writer(u' ')
                    __M_writer(unicode(i + 1))
                    __M_writer(u'</b></div>\n                        ')
                    # SOURCE LINE 99
                    __M_writer(unicode(do_inputs( input.inputs, repeat_state[i], rep_errors, prefix + input.name + "_" + str(index) + "|", other_values )))
                    __M_writer(u'\n                        <div class="form-row"><input type="submit" name="')
                    # SOURCE LINE 100
                    __M_writer(unicode(prefix))
                    __M_writer(unicode(input.name))
                    __M_writer(u'_')
                    __M_writer(unicode(index))
                    __M_writer(u'_remove" value="Remove ')
                    __M_writer(unicode(input.title))
                    __M_writer(u' ')
                    __M_writer(unicode(i+1))
                    __M_writer(u'"></div>\n                    </div>\n')
                    # SOURCE LINE 102
                    if rep_errors.has_key( '__index__' ):
                        # SOURCE LINE 103
                        __M_writer(u'                        <div><img style="vertical-align: middle;" src="')
                        __M_writer(unicode(h.url_for('/static/style/error_small.png')))
                        __M_writer(u'">&nbsp;<span style="vertical-align: middle;">')
                        __M_writer(unicode(rep_errors['__index__']))
                        __M_writer(u'</span></div>\n')
                        pass
                    pass
                # SOURCE LINE 106
                __M_writer(u'                  <div class="form-row"><input type="submit" name="')
                __M_writer(unicode(prefix))
                __M_writer(unicode(input.name))
                __M_writer(u'_add" value="Add new ')
                __M_writer(unicode(input.title))
                __M_writer(u'"></div>\n              </div>\n')
                # SOURCE LINE 108
            elif input.type == "conditional":
                # SOURCE LINE 109
                __M_writer(u'                ')

                group_state = tool_state[input.name]
                group_errors = errors.get( input.name, {} )
                current_case = group_state['__current_case__']
                group_prefix = prefix + input.name + "|"
                
                
                # SOURCE LINE 114
                __M_writer(u'\n')
                # SOURCE LINE 115
                if input.value_ref_in_group:
                    # SOURCE LINE 116
                    __M_writer(u'                    ')
                    __M_writer(unicode(row_for_param( group_prefix, input.test_param, group_state, group_errors, other_values )))
                    __M_writer(u'\n')
                    pass
                # SOURCE LINE 118
                __M_writer(u'                ')
                __M_writer(unicode(do_inputs( input.cases[current_case].inputs, group_state, group_errors, group_prefix, other_values )))
                __M_writer(u'\n')
                # SOURCE LINE 119
            elif input.type == "upload_dataset":
                # SOURCE LINE 120
                if input.get_datatype( trans, other_values ).composite_type is None: #have non-composite upload appear as before
                    # SOURCE LINE 121
                    __M_writer(u'                    ')

                    if input.name in errors:
                        rep_errors = errors[input.name][0]
                    else:
                        rep_errors = dict()
                    
                    
                    # SOURCE LINE 126
                    __M_writer(u'\n                  ')
                    # SOURCE LINE 127
                    __M_writer(unicode(do_inputs( input.inputs, tool_state[input.name][0], rep_errors, prefix + input.name + "_" + str( 0 ) + "|", other_values )))
                    __M_writer(u'\n')
                    # SOURCE LINE 128
                else:
                    # SOURCE LINE 129
                    __M_writer(u'                    <div class="repeat-group">\n                        <div class="form-title-row"><b>')
                    # SOURCE LINE 130
                    __M_writer(unicode(input.group_title( other_values )))
                    __M_writer(u'</b></div>\n                        ')
                    # SOURCE LINE 131
 
                    repeat_state = tool_state[input.name] 
                    
                    
                    # SOURCE LINE 133
                    __M_writer(u'\n')
                    # SOURCE LINE 134
                    for i in range( len( repeat_state ) ):
                        # SOURCE LINE 135
                        __M_writer(u'                          <div class="repeat-group-item">\n                          ')
                        # SOURCE LINE 136

                        if input.name in errors:
                            rep_errors = errors[input.name][i]
                        else:
                            rep_errors = dict()
                        index = repeat_state[i]['__index__']
                        
                        
                        # SOURCE LINE 142
                        __M_writer(u'\n                          <div class="form-title-row"><b>File Contents for ')
                        # SOURCE LINE 143
                        __M_writer(unicode(input.title_by_index( trans, i, other_values )))
                        __M_writer(u'</b></div>\n                          ')
                        # SOURCE LINE 144
                        __M_writer(unicode(do_inputs( input.inputs, repeat_state[i], rep_errors, prefix + input.name + "_" + str(index) + "|", other_values )))
                        __M_writer(u'\n')
                        # SOURCE LINE 146
                        __M_writer(u'                          </div>\n')
                        pass
                    # SOURCE LINE 149
                    __M_writer(u'                    </div>\n')
                    pass
                # SOURCE LINE 151
            else:
                # SOURCE LINE 152
                __M_writer(u'                ')
                __M_writer(unicode(row_for_param( prefix, input, tool_state, errors, other_values )))
                __M_writer(u'\n')
                pass
            pass
        # SOURCE LINE 155
        __M_writer(u'    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_row_for_param(context,prefix,param,parent_state,parent_errors,other_values):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        type = context.get('type', UNDEFINED)
        unicode = context.get('unicode', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 157
        __M_writer(u'\n        ')
        # SOURCE LINE 158

        if parent_errors.has_key( param.name ):
            cls = "form-row form-row-error"
        else:
            cls = "form-row"
            
        label = param.get_label()
        
        field = param.get_html_field( trans, parent_state[ param.name ], other_values )
        field.refresh_on_change = param.refresh_on_change
        
        # Field may contain characters submitted by user and these characters may be unicode; handle non-ascii characters gracefully.
        field_html = field.get_html( prefix )
        if type( field_html ) is not unicode:
            field_html = unicode( field_html, 'utf-8' )
        
        if param.type == "hidden":
            return field_html
        
        
        # SOURCE LINE 176
        __M_writer(u'\n        <div class="')
        # SOURCE LINE 177
        __M_writer(unicode(cls))
        __M_writer(u'">\n')
        # SOURCE LINE 178
        if label:
            # SOURCE LINE 179
            __M_writer(u'                <label for="')
            __M_writer(unicode(param.name))
            __M_writer(u'">')
            __M_writer(unicode(label))
            __M_writer(u':</label>\n')
            pass
        # SOURCE LINE 181
        __M_writer(u'            <div class="form-row-input">')
        __M_writer(unicode(field_html))
        __M_writer(u'</div>\n')
        # SOURCE LINE 182
        if parent_errors.has_key( param.name ):
            # SOURCE LINE 183
            __M_writer(u'                <div class="form-row-error-message">\n                    <div><img style="vertical-align: middle;" src="')
            # SOURCE LINE 184
            __M_writer(unicode(h.url_for('/static/style/error_small.png')))
            __M_writer(u'">&nbsp;<span style="vertical-align: middle;">')
            __M_writer(unicode(parent_errors[param.name]))
            __M_writer(u'</span></div>\n                </div>\n')
            pass
        # SOURCE LINE 187
        __M_writer(u'            \n')
        # SOURCE LINE 188
        if param.help:
            # SOURCE LINE 189
            __M_writer(u'                <div class="toolParamHelp" style="clear: both;">\n                    ')
            # SOURCE LINE 190
            __M_writer(unicode(param.help))
            __M_writer(u'\n                </div>\n')
            pass
        # SOURCE LINE 193
        __M_writer(u'    \n            <div style="clear: both"></div>\n                    \n        </div>\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


