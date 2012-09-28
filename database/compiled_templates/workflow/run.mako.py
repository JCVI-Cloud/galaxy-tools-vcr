from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1292435079.640506
_template_filename='templates/workflow/run.mako'
_template_uri='workflow/run.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding=None
_exports = ['stylesheets', 'javascripts', 'do_inputs', 'row_for_param']


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
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        basestring = context.get('basestring', UNDEFINED)
        errors = context.get('errors', UNDEFINED)
        tuple = context.get('tuple', UNDEFINED)
        int = context.get('int', UNDEFINED)
        h = context.get('h', UNDEFINED)
        app = context.get('app', UNDEFINED)
        workflow = context.get('workflow', UNDEFINED)
        def do_inputs(inputs,values,errors,prefix,step,other_values=None):
            return render_do_inputs(context.locals_(__M_locals),inputs,values,errors,prefix,step,other_values)
        len = context.get('len', UNDEFINED)
        dict = context.get('dict', UNDEFINED)
        t = context.get('t', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        has_upgrade_messages = context.get('has_upgrade_messages', UNDEFINED)
        steps = context.get('steps', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 13
        __M_writer(u'\n\n')
        # SOURCE LINE 32
        __M_writer(u'\n\n')
        # SOURCE LINE 34

        from galaxy.tools.parameters import DataToolParameter, RuntimeValue
        from galaxy.jobs.actions.post import ActionBox
        import re
        import colorsys
        import random
        
        wf_parms = {}
        for step in steps:
            for v in step.state.inputs.itervalues():
                if isinstance(v, basestring):
                    for rematch in re.findall('\$\{.+?\}', v):
                        if rematch[2:-1] not in wf_parms:
                            wf_parms[rematch[2:-1]] = ""
        if wf_parms:
            hue_offset = 1.0 / len(wf_parms)
            hue = 0.0
            for k in wf_parms.iterkeys():
                wf_parms[k] = "#%X%X%X" % tuple([int(x * 255) for x in colorsys.hsv_to_rgb(hue, .1, .9)])
                hue += hue_offset
        
        
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin()[__M_key]) for __M_key in ['hue','hue_offset','wf_parms','ActionBox','DataToolParameter','rematch','k','random','re','step','RuntimeValue','colorsys','v','x'] if __M_key in __M_locals_builtin()]))
        # SOURCE LINE 54
        __M_writer(u'\n\n')
        # SOURCE LINE 91
        __M_writer(u'\n\n')
        # SOURCE LINE 163
        __M_writer(u'\n\n<h2>Running workflow "')
        # SOURCE LINE 165
        __M_writer(unicode(h.to_unicode( workflow.name )))
        __M_writer(u'"</h2>\n\n')
        # SOURCE LINE 167
        if has_upgrade_messages:
            # SOURCE LINE 168
            __M_writer(u'<div class="warningmessage">\n    Problems were encountered when loading this workflow, likely due to tool\n    version changes. Missing parameter values have been replaced with default.\n    Please review the parameter values below.\n</div>\n')
        # SOURCE LINE 174
        __M_writer(u'\n')
        # SOURCE LINE 175
        if workflow.annotation:
            # SOURCE LINE 176
            __M_writer(u'    <div class="workflow-annotation">Annotation: ')
            __M_writer(unicode(workflow.annotation))
            __M_writer(u'</div>\n    <hr/>\n')
        # SOURCE LINE 179
        __M_writer(u'\n<form id="tool_form" name="tool_form" method="POST">\n')
        # SOURCE LINE 182
        __M_writer(u'\n\n')
        # SOURCE LINE 184
        if wf_parms:
            # SOURCE LINE 185
            __M_writer(u'<div class="metadataForm">\n    <div class="metadataFormTitle">Workflow Parameters</div>\n    <div class="metadataFormBody">\n')
            # SOURCE LINE 188
            for parm in wf_parms:
                # SOURCE LINE 189
                __M_writer(u"        <div class='form-row'><label style='width:100px;'>")
                __M_writer(unicode(parm))
                __M_writer(u'<input style="border:2px solid ')
                __M_writer(unicode(wf_parms[parm]))
                __M_writer(u';border-left-width:8px;" type="text" class=\'wf_parm_input ptag_')
                __M_writer(unicode(parm))
                __M_writer(u'\' name="wf_parm|')
                __M_writer(unicode(parm))
                __M_writer(u'" value=""/></label></div>\n')
            # SOURCE LINE 191
            __M_writer(u'    </div>\n</div>\n    <script type="text/javascript">\n    // Set the change hooks for workflow parameters.\n    $(document).ready(function () {\n        $(\'.wf_parm_input\').bind(\'change keypress keyup\', function(event){\n            // DBTODO This is probably not reliable.  Ensure we have the right class.\n            var new_text = $(this).val();\n            if (new_text === \'\'){\n                var tag_id = $(this).attr("class").split(\' \')[1].substring(5);\n                // Set text properly.\n                $(\'.wfpspan.wf_parm__\'+tag_id).text(tag_id);\n            }else{\n                var tag_id = $(this).attr("class").split(\' \')[1].substring(5);\n                // Set text properly.\n                $(\'.wfpspan.wf_parm__\'+tag_id).text(new_text);\n                // Now set the hidden input to the generated text.\n                $(\'.wfpspan.wf_parm__\'+tag_id).not(\'.pja_wfp\').each(function(){\n                    // var new_text = $(this).parent().text();\n                    $(this).parent().siblings().children().val(new_text);\n                });\n            }\n        });\n    });\n    </script>\n')
        # SOURCE LINE 217
        __M_writer(u'\n')
        # SOURCE LINE 218
        for i, step in enumerate( steps ):
            # SOURCE LINE 219
            if step.type == 'tool' or step.type is None:
                # SOURCE LINE 220
                __M_writer(u'      ')
                tool = app.toolbox.tools_by_id[step.tool_id] 
                
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin()[__M_key]) for __M_key in ['tool'] if __M_key in __M_locals_builtin()]))
                __M_writer(u'\n      <input type="hidden" name="')
                # SOURCE LINE 221
                __M_writer(unicode(step.id))
                __M_writer(u'|tool_state" value="')
                __M_writer(unicode(step.state.encode( tool, app )))
                __M_writer(u'">\n      <div class="toolForm">\n          <div class="toolFormTitle">\n              Step ')
                # SOURCE LINE 224
                __M_writer(unicode(int(step.order_index)+1))
                __M_writer(u': ')
                __M_writer(unicode(tool.name))
                __M_writer(u'\n')
                # SOURCE LINE 225
                if step.annotations:
                    # SOURCE LINE 226
                    __M_writer(u'                <div class="step-annotation">Annotation: ')
                    __M_writer(unicode(h.to_unicode( step.annotations[0].annotation )))
                    __M_writer(u'</div>\n')
                # SOURCE LINE 228
                __M_writer(u'          </div>\n          <div class="toolFormBody">\n            ')
                # SOURCE LINE 230
                __M_writer(unicode(do_inputs( tool.inputs, step.state.inputs, errors.get( step.id, dict() ), "", step )))
                __M_writer(u'\n')
                # SOURCE LINE 231
                if step.post_job_actions:
                    # SOURCE LINE 232
                    __M_writer(u"                <hr/>\n                <div class='form-row'>\n")
                    # SOURCE LINE 234
                    if len(step.post_job_actions) > 1:
                        # SOURCE LINE 235
                        __M_writer(u'                    <label>Actions:</label>\n')
                        # SOURCE LINE 236
                    else:
                        # SOURCE LINE 237
                        __M_writer(u'                    <label>Action:</label>\n')
                    # SOURCE LINE 239

                    pja_ss_all = []
                    for pja_ss in [ActionBox.get_short_str(pja) for pja in step.post_job_actions]:
                        for rematch in re.findall('\$\{.+?\}', pja_ss):
                            pja_ss = pja_ss.replace(rematch, '<span style="background-color:%s" class="wfpspan wf_parm__%s pja_wfp">%s</span>' % (wf_parms[rematch[2:-1]], rematch[2:-1], rematch[2:-1]))
                        pja_ss_all.append(pja_ss)
                    
                    
                    __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin()[__M_key]) for __M_key in ['rematch','pja_ss_all','pja','pja_ss'] if __M_key in __M_locals_builtin()]))
                    # SOURCE LINE 245
                    __M_writer(u'\n                ')
                    # SOURCE LINE 246
                    __M_writer(unicode('<br/>'.join(pja_ss_all)))
                    __M_writer(u'\n                </div>\n')
                # SOURCE LINE 249
                __M_writer(u'          </div>\n      </div>\n')
                # SOURCE LINE 251
            else:
                # SOURCE LINE 252
                __M_writer(u'    ')
                module = step.module 
                
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin()[__M_key]) for __M_key in ['module'] if __M_key in __M_locals_builtin()]))
                __M_writer(u'\n      <input type="hidden" name="')
                # SOURCE LINE 253
                __M_writer(unicode(step.id))
                __M_writer(u'|tool_state" value="')
                __M_writer(unicode(module.encode_runtime_state( t, step.state )))
                __M_writer(u'">\n      <div class="toolForm">\n          <div class="toolFormTitle">\n              Step ')
                # SOURCE LINE 256
                __M_writer(unicode(int(step.order_index)+1))
                __M_writer(u': ')
                __M_writer(unicode(module.name))
                __M_writer(u'\n')
                # SOURCE LINE 257
                if step.annotations:
                    # SOURCE LINE 258
                    __M_writer(u'                <div class="step-annotation">Annotation: ')
                    __M_writer(unicode(step.annotations[0].annotation))
                    __M_writer(u'</div>\n')
                # SOURCE LINE 260
                __M_writer(u'          </div>\n          <div class="toolFormBody">\n              ')
                # SOURCE LINE 262
                __M_writer(unicode(do_inputs( module.get_runtime_inputs(), step.state.inputs, errors.get( step.id, dict() ), "", step )))
                __M_writer(u'\n          </div>\n      </div>\n')
        # SOURCE LINE 267
        __M_writer(u'<input type="submit" name="run_workflow" value="Run workflow" />\n</form>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 15
        __M_writer(u'\n    ')
        # SOURCE LINE 16
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n    ')
        # SOURCE LINE 17
        __M_writer(unicode(h.css( "autocomplete_tagging" )))
        __M_writer(u'\n    <style type="text/css">\n    div.toolForm{\n        margin-top: 10px;\n        margin-bottom: 10px;\n    }\n    .step-annotation {\n        margin-top: 0.25em;\n        font-weight: normal;\n        font-size: 97%;\n    }\n    .workflow-annotation {\n        margin-bottom: 1em;\n    }\n    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n    ')
        # SOURCE LINE 4
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n    ')
        # SOURCE LINE 5
        __M_writer(unicode(h.js( "jquery.autocomplete" )))
        __M_writer(u'\n    <script type="text/javascript">        \n        $( function() {\n            $( "select[refresh_on_change=\'true\']").change( function() {\n                $( "#tool_form" ).submit();\n            });\n        });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_do_inputs(context,inputs,values,errors,prefix,step,other_values=None):
    context.caller_stack._push_frame()
    try:
        def row_for_param(param,value,other_values,error_dict,prefix,step):
            return render_row_for_param(context,param,value,other_values,error_dict,prefix,step)
        def do_inputs(inputs,values,errors,prefix,step,other_values=None):
            return render_do_inputs(context,inputs,values,errors,prefix,step,other_values)
        len = context.get('len', UNDEFINED)
        range = context.get('range', UNDEFINED)
        dict = context.get('dict', UNDEFINED)
        str = context.get('str', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 56
        __M_writer(u'\n')
        # SOURCE LINE 57
        if other_values is None:
            # SOURCE LINE 58
            __M_writer(u'      ')
            other_values = values 
            
            __M_writer(u'\n')
        # SOURCE LINE 60
        for input_index, input in enumerate( inputs.itervalues() ):
            # SOURCE LINE 61
            if input.type == "repeat":
                # SOURCE LINE 62
                __M_writer(u'      <div class="repeat-group">\n          <div class="form-title-row"><b>')
                # SOURCE LINE 63
                __M_writer(unicode(input.title_plural))
                __M_writer(u'</b></div>\n          ')
                # SOURCE LINE 64
                repeat_values = values[input.name] 
                
                __M_writer(u'\n')
                # SOURCE LINE 65
                for i in range( len( repeat_values ) ):
                    # SOURCE LINE 66
                    if input.name in errors:
                        # SOURCE LINE 67
                        __M_writer(u'                ')
                        rep_errors = errors[input.name][i] 
                        
                        __M_writer(u'\n')
                        # SOURCE LINE 68
                    else:
                        # SOURCE LINE 69
                        __M_writer(u'                ')
                        rep_errors = dict() 
                        
                        __M_writer(u'\n')
                    # SOURCE LINE 71
                    __M_writer(u'            <div class="repeat-group-item">\n            ')
                    # SOURCE LINE 72
                    index = repeat_values[i]['__index__'] 
                    
                    __M_writer(u'\n            <div class="form-title-row"><b>')
                    # SOURCE LINE 73
                    __M_writer(unicode(input.title))
                    __M_writer(u' ')
                    __M_writer(unicode(i + 1))
                    __M_writer(u'</b></div>\n            ')
                    # SOURCE LINE 74
                    __M_writer(unicode(do_inputs( input.inputs, repeat_values[ i ], rep_errors,  prefix + input.name + "_" + str(index) + "|", step, other_values )))
                    __M_writer(u'\n')
                    # SOURCE LINE 76
                    __M_writer(u'            </div> \n')
                # SOURCE LINE 79
                __M_writer(u'      </div>\n')
                # SOURCE LINE 80
            elif input.type == "conditional":
                # SOURCE LINE 81
                __M_writer(u'      ')
                group_values = values[input.name] 
                
                __M_writer(u'\n      ')
                # SOURCE LINE 82
                current_case = group_values['__current_case__'] 
                
                __M_writer(u'\n      ')
                # SOURCE LINE 83
                new_prefix = prefix + input.name + "|" 
                
                __M_writer(u'\n      ')
                # SOURCE LINE 84
                group_errors = errors.get( input.name, {} ) 
                
                __M_writer(u'\n      ')
                # SOURCE LINE 85
                __M_writer(unicode(row_for_param( input.test_param, group_values[ input.test_param.name ], other_values, group_errors, prefix, step )))
                __M_writer(u'\n      ')
                # SOURCE LINE 86
                __M_writer(unicode(do_inputs( input.cases[ current_case ].inputs, group_values, group_errors, new_prefix, step, other_values )))
                __M_writer(u'\n')
                # SOURCE LINE 87
            else:
                # SOURCE LINE 88
                __M_writer(u'      ')
                __M_writer(unicode(row_for_param( input, values[ input.name ], other_values, errors, prefix, step )))
                __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_row_for_param(context,param,value,other_values,error_dict,prefix,step):
    context.caller_stack._push_frame()
    try:
        basestring = context.get('basestring', UNDEFINED)
        wf_parms = context.get('wf_parms', UNDEFINED)
        incoming = context.get('incoming', UNDEFINED)
        DataToolParameter = context.get('DataToolParameter', UNDEFINED)
        int = context.get('int', UNDEFINED)
        h = context.get('h', UNDEFINED)
        app = context.get('app', UNDEFINED)
        re = context.get('re', UNDEFINED)
        RuntimeValue = context.get('RuntimeValue', UNDEFINED)
        t = context.get('t', UNDEFINED)
        str = context.get('str', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 93
        __M_writer(u'\n')
        # SOURCE LINE 95
        if error_dict.has_key( param.name ):
            # SOURCE LINE 96
            __M_writer(u'        ')
            cls = "form-row form-row-error" 
            
            __M_writer(u'\n')
            # SOURCE LINE 97
        else:
            # SOURCE LINE 98
            __M_writer(u'        ')
            cls = "form-row" 
            
            __M_writer(u'\n')
        # SOURCE LINE 100
        __M_writer(u'    <div class="')
        __M_writer(unicode(cls))
        __M_writer(u'">\n        <label>')
        # SOURCE LINE 101
        __M_writer(unicode(param.get_label()))
        __M_writer(u'</label>\n        <div>\n')
        # SOURCE LINE 103
        if isinstance( param, DataToolParameter ):
            # SOURCE LINE 104
            if ( prefix + param.name ) in step.input_connections_by_name:
                # SOURCE LINE 105
                __M_writer(u'                    ')

                conn = step.input_connections_by_name[ prefix + param.name ]
                                    
                
                # SOURCE LINE 107
                __M_writer(u"\n                    Output dataset '")
                # SOURCE LINE 108
                __M_writer(unicode(conn.output_name))
                __M_writer(u"' from step ")
                __M_writer(unicode(int(conn.output_step.order_index)+1))
                __M_writer(u'\n')
                # SOURCE LINE 109
            else:
                # SOURCE LINE 111
                __M_writer(u'                    ')

                if value is None:
                    value = other_values[ param.name ] = param.get_initial_value( t, other_values )
                
                
                # SOURCE LINE 114
                __M_writer(u'\n                    ')
                # SOURCE LINE 115
                __M_writer(unicode(param.get_html_field( t, value, other_values ).get_html( str(step.id) + "|" + prefix )))
                __M_writer(u'\n                    <input type="hidden" name="')
                # SOURCE LINE 116
                __M_writer(unicode(step.id))
                __M_writer(u'|__force_update__')
                __M_writer(unicode(prefix))
                __M_writer(unicode(param.name))
                __M_writer(u'" value="true" />\n')
            # SOURCE LINE 118
        elif isinstance( value, RuntimeValue ) or ( str(step.id) + '|__runtime__' + prefix + param.name ) in incoming:
            # SOURCE LINE 128
            __M_writer(u'                ')
            value = other_values[ param.name ] = param.get_initial_value( t, other_values ) 
            
            __M_writer(u'\n                ')
            # SOURCE LINE 129
            __M_writer(unicode(param.get_html_field( t, value, other_values ).get_html( str(step.id) + "|" + prefix )))
            __M_writer(u'\n                <input type="hidden" name="')
            # SOURCE LINE 130
            __M_writer(unicode(step.id))
            __M_writer(u'|__runtime__')
            __M_writer(unicode(prefix))
            __M_writer(unicode(param.name))
            __M_writer(u'" value="true" />\n')
            # SOURCE LINE 131
        else:
            # SOURCE LINE 133
            __M_writer(u'                ')

            p_text = param.value_to_display_text( value, app )
            replacements = []
            if isinstance(p_text, basestring):
                for rematch in re.findall('\$\{.+?\}', p_text):
                    replacements.append('wf_parm__%s' % rematch[2:-1])
                    p_text = p_text.replace(rematch, '<span style="background-color:%s" class="wfpspan wf_parm__%s">%s</span>' % (wf_parms[rematch[2:-1]], rematch[2:-1], rematch[2:-1]))
            
            
            # SOURCE LINE 140
            __M_writer(u'\n')
            # SOURCE LINE 141
            if replacements:
                # SOURCE LINE 143
                __M_writer(u'                    <span style="display:none" class="parm_wrap ')
                __M_writer(unicode(' '.join(replacements)))
                __M_writer(u'">\n                    ')
                # SOURCE LINE 144
                __M_writer(unicode(param.get_html_field( t, value, other_values ).get_html( str(step.id) + "|" + prefix )))
                __M_writer(u'\n                    </span>\n                    <span class="p_text_wrapper">')
                # SOURCE LINE 146
                __M_writer(unicode(p_text))
                __M_writer(u'</span>\n                    <input type="hidden" name="')
                # SOURCE LINE 147
                __M_writer(unicode(step.id))
                __M_writer(u'|__runtime__')
                __M_writer(unicode(prefix))
                __M_writer(unicode(param.name))
                __M_writer(u'" value="true" />\n')
                # SOURCE LINE 148
            else:
                # SOURCE LINE 149
                __M_writer(u'                    ')
                __M_writer(unicode(param.get_html_field( t, value, other_values ).get_html( str(step.id) + "|" + prefix )))
                __M_writer(u'\n')
        # SOURCE LINE 152
        __M_writer(u'        </div>\n')
        # SOURCE LINE 153
        if step.upgrade_messages and param.name in step.upgrade_messages:
            # SOURCE LINE 154
            __M_writer(u'        <div class="warningmark">')
            __M_writer(unicode(step.upgrade_messages[param.name]))
            __M_writer(u'</div>\n')
        # SOURCE LINE 156
        if error_dict.has_key( param.name ):
            # SOURCE LINE 157
            __M_writer(u'        <div style="color: red; font-weight: bold; padding-top: 1px; padding-bottom: 3px;">\n            <div style="width: 300px;"><img style="vertical-align: middle;" src="')
            # SOURCE LINE 158
            __M_writer(unicode(h.url_for('/static/style/error_small.png')))
            __M_writer(u'">&nbsp;<span style="vertical-align: middle;">')
            __M_writer(unicode(error_dict[param.name]))
            __M_writer(u'</span></div>\n        </div>\n')
        # SOURCE LINE 161
        __M_writer(u'        <div style="clear: both"></div>       \n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


