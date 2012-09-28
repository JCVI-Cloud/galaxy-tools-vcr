from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1297785170.1161439
_template_filename='templates/show_params.mako'
_template_uri='show_params.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding=None
_exports = ['inputs_recursive']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def inputs_recursive(input_params,param_values,depth=1):
            return render_inputs_recursive(context.locals_(__M_locals),input_params,param_values,depth)
        tool = context.get('tool', UNDEFINED)
        params_objects = context.get('params_objects', UNDEFINED)
        hda = context.get('hda', UNDEFINED)
        history = context.get('history', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        from galaxy.util import nice_size 
        
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin()[__M_key]) for __M_key in ['nice_size'] if __M_key in __M_locals_builtin()]))
        __M_writer(u'\n\n')
        # SOURCE LINE 23
        __M_writer(u'\n\n<table class="tabletip">\n  <thead>\n    <tr><th colspan="2" style="font-size: 120%;">')
        # SOURCE LINE 27
        __M_writer(unicode(tool.name))
        __M_writer(u'</th></tr>\n  </thead>\n  <tbody>\n    <tr><th>Created:</th><td>')
        # SOURCE LINE 30
        __M_writer(unicode(history.create_time.strftime("%b %d, %Y")))
        __M_writer(u'</td></tr>\n    <tr><th>Modified:</th><td>')
        # SOURCE LINE 31
        __M_writer(unicode(history.update_time.strftime("%b %d, %Y")))
        __M_writer(u'</td></tr>\n')
        # SOURCE LINE 33
        __M_writer(u'    <tr><th>Filesize:</th><td>')
        __M_writer(unicode(nice_size(hda.dataset.file_size)))
        __M_writer(u'</td></tr>\n    <tr><th>Dbkey:</th><td>')
        # SOURCE LINE 34
        __M_writer(unicode(hda.dbkey))
        __M_writer(u'</td></tr>\n    <tr><th>Format:</th><td>')
        # SOURCE LINE 35
        __M_writer(unicode(hda.ext))
        __M_writer(u'</td></tr>\n    \n</table><br />\n<table class="tabletip">\n  <thead>\n    <tr>\n      <th>Input Parameter</th>\n      <th>Value</th>\n    </tr>\n  </thead>\n  <tbody>\n      ')
        # SOURCE LINE 46
        __M_writer(unicode( inputs_recursive(tool.inputs, params_objects, depth=1) ))
        __M_writer(u'\n  </tbody>\n</table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_inputs_recursive(context,input_params,param_values,depth=1):
    context.caller_stack._push_frame()
    try:
        range = context.get('range', UNDEFINED)
        len = context.get('len', UNDEFINED)
        getattr = context.get('getattr', UNDEFINED)
        def inputs_recursive(input_params,param_values,depth=1):
            return render_inputs_recursive(context,input_params,param_values,depth)
        enumerate = context.get('enumerate', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        for input_index, input in enumerate( input_params.itervalues() ):
            # SOURCE LINE 5
            if input.type == "repeat":
                # SOURCE LINE 6
                for i in range( len(param_values[input.name]) ):
                    # SOURCE LINE 7
                    __M_writer(u'        ')
                    __M_writer(unicode( inputs_recursive(input.inputs, param_values[input.name][i], depth=depth+1) ))
                    __M_writer(u'\n')
                # SOURCE LINE 9
            elif input.type == "conditional":
                # SOURCE LINE 10
                __M_writer(u'      ')
                current_case = param_values[input.name]['__current_case__'] 
                
                __M_writer(u'\n        <tr>\n          <td>')
                # SOURCE LINE 12
                __M_writer(unicode(input.label))
                __M_writer(u'</td>\n          <td>')
                # SOURCE LINE 13
                __M_writer(unicode(current_case))
                __M_writer(u'</td>\n        </tr>\n        ')
                # SOURCE LINE 15
                __M_writer(unicode( inputs_recursive(input.cases[current_case].inputs, param_values[input.name], depth=depth+1) ))
                __M_writer(u'\n')
                # SOURCE LINE 16
            elif getattr(input, "label", None):
                # SOURCE LINE 17
                __M_writer(u'      <tr>\n        <td>')
                # SOURCE LINE 18
                __M_writer(unicode(input.label))
                __M_writer(u'</td>\n        <td>')
                # SOURCE LINE 19
                __M_writer(unicode(input.value_to_display_text(param_values[input.name], trans.app)))
                __M_writer(u'</td>\n      </tr>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


