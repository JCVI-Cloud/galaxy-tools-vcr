from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1297798364.924629
_template_filename='templates/tracks/new_browser.mako'
_template_uri='tracks/new_browser.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding=None
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        default_dbkey = context.get('default_dbkey', UNDEFINED)
        dbkeys = context.get('dbkeys', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<form id="new-browser-form" action="javascript:void(0);" method="post" onsubmit="return false;">\n    <div class="form-row">\n        <label for="new-title">Browser name:</label>\n        <div class="form-row-input">\n            <input type="text" name="title" id="new-title" value="Unnamed"></input>\n        </div>\n        <div style="clear: both;"></div>\n    </div>\n    <div class="form-row">\n        <label for="new-dbkey">Reference genome build (dbkey): </label>\n        <div class="form-row-input">\n            <select name="dbkey" id="new-dbkey">\n')
        # SOURCE LINE 13
        for dbkey in dbkeys:
            # SOURCE LINE 14
            __M_writer(u'                    <option value="')
            __M_writer(unicode(dbkey[1]))
            __M_writer(u'">')
            __M_writer(unicode(dbkey[0]))
            __M_writer(u'</option>\n')
        # SOURCE LINE 16
        __M_writer(u'            </select>\n        </div>\n        <div style="clear: both;"></div>\n    </div>\n    <div class="form-row">\n        Is the build not listed here? \n        <a href="')
        # SOURCE LINE 22
        __M_writer(unicode(h.url_for( controller='user', action='dbkeys', panels=True )))
        __M_writer(u'">Add a Custom Build</a>\n    </div>\n')
        # SOURCE LINE 24
        if default_dbkey is not None:
            # SOURCE LINE 25
            __M_writer(u'        <script type="text/javascript">\n            $("#new-dbkey option[value=\'')
            # SOURCE LINE 26
            __M_writer(unicode(default_dbkey))
            __M_writer(u'\']").attr("selected", true);\n        </script>\n')
        # SOURCE LINE 29
        __M_writer(u'</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


