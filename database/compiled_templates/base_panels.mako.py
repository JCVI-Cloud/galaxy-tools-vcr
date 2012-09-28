# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1336498137.96486
_template_filename=u'templates/base_panels.mako'
_template_uri=u'/base_panels.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['message_box_content', 'overlay', 'late_javascripts', 'stylesheets', 'init', 'masthead', 'javascripts']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE HTML>\n\n')
        # SOURCE LINE 3

        self.has_left_panel=True
        self.has_right_panel=True
        self.message_box_visible=False
        self.overlay_visible=False
        self.message_box_class=""
        self.active_view=None
        self.body_class=""
        
        
        # SOURCE LINE 11
        __M_writer(u'\n    \n')
        # SOURCE LINE 15
        __M_writer(u'\n\n')
        # SOURCE LINE 43
        __M_writer(u'\n\n')
        # SOURCE LINE 58
        __M_writer(u'\n\n')
        # SOURCE LINE 171
        __M_writer(u'\n\n')
        # SOURCE LINE 176
        __M_writer(u'\n\n')
        # SOURCE LINE 208
        __M_writer(u'\n\n')
        # SOURCE LINE 212
        __M_writer(u'\n\n')
        # SOURCE LINE 215
        __M_writer(u'<html>\n    ')
        # SOURCE LINE 216
        __M_writer(unicode(self.init()))
        __M_writer(u'    \n    <head>\n        <title>')
        # SOURCE LINE 218
        __M_writer(unicode(self.title()))
        __M_writer(u'</title>\n        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n')
        # SOURCE LINE 221
        __M_writer(u'        <meta name = "viewport" content = "maximum-scale=1.0">\n')
        # SOURCE LINE 223
        __M_writer(u'        <meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1">\n        ')
        # SOURCE LINE 224
        __M_writer(unicode(self.stylesheets()))
        __M_writer(u'\n        ')
        # SOURCE LINE 225
        __M_writer(unicode(self.javascripts()))
        __M_writer(u'\n    </head>\n    \n    <body scroll="no" class="')
        # SOURCE LINE 228
        __M_writer(unicode(self.body_class))
        __M_writer(u'">\n        <div id="everything" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; min-width: 600px;">\n')
        # SOURCE LINE 231
        __M_writer(u'            <div id="background"></div>\n')
        # SOURCE LINE 233
        __M_writer(u'            <div id="masthead" class="navbar navbar-fixed-top">\n                <div class="masthead-inner navbar-inner">\n                    <div class="container">')
        # SOURCE LINE 235
        __M_writer(unicode(self.masthead()))
        __M_writer(u'</div>\n                </div>\n            </div>\n            <div id="messagebox" class="panel-')
        # SOURCE LINE 238
        __M_writer(unicode(self.message_box_class))
        __M_writer(u'-message">\n')
        # SOURCE LINE 239
        if self.message_box_visible:
            # SOURCE LINE 240
            __M_writer(u'                    ')
            __M_writer(unicode(self.message_box_content()))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 242
        __M_writer(u'            </div>\n            ')
        # SOURCE LINE 243
        __M_writer(unicode(self.overlay(visible=self.overlay_visible)))
        __M_writer(u'\n')
        # SOURCE LINE 244
        if self.has_left_panel:
            # SOURCE LINE 245
            __M_writer(u'                <div id="left">\n                    ')
            # SOURCE LINE 246
            __M_writer(unicode(self.left_panel()))
            __M_writer(u'\n                    <div class="unified-panel-footer">\n                        <div class="panel-collapse"></span></div>\n                        <div class="drag"></div>\n                    </div>\n                </div>\n')
            pass
        # SOURCE LINE 253
        __M_writer(u'            <div id="center">\n                ')
        # SOURCE LINE 254
        __M_writer(unicode(self.center_panel()))
        __M_writer(u'\n            </div>\n')
        # SOURCE LINE 256
        if self.has_right_panel:
            # SOURCE LINE 257
            __M_writer(u'                <div id="right">\n                    ')
            # SOURCE LINE 258
            __M_writer(unicode(self.right_panel()))
            __M_writer(u'\n                    <div class="unified-panel-footer">\n                        <div class="panel-collapse right"></span></div>\n                        <div class="drag"></div>\n                    </div>\n                </div>\n')
            pass
        # SOURCE LINE 265
        __M_writer(u'        </div>\n')
        # SOURCE LINE 267
        __M_writer(u'    </body>\n')
        # SOURCE LINE 270
        __M_writer(u'    ')
        __M_writer(unicode(self.late_javascripts()))
        __M_writer(u'\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_message_box_content(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 211
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_overlay(context,title='',content='',visible=False):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 178
        __M_writer(u'\n    ')
        # SOURCE LINE 179
        __M_writer(u'\n    ')
        # SOURCE LINE 180
        __M_writer(u'\n\n    ')
        # SOURCE LINE 182

        if visible:
            display = "style='display: block;'"
            overlay_class = "in"
        else:
            display = "style='display: none;'"
            overlay_class = ""
        
        
        # SOURCE LINE 189
        __M_writer(u'\n\n    <div id="overlay" ')
        # SOURCE LINE 191
        __M_writer(unicode(display))
        __M_writer(u'>\n\n        <div id="overlay-background" class="modal-backdrop fade ')
        # SOURCE LINE 193
        __M_writer(unicode(overlay_class))
        __M_writer(u'"></div>\n\n        <div id="dialog-box" class="modal dialog-box" border="0" ')
        # SOURCE LINE 195
        __M_writer(unicode(display))
        __M_writer(u'>\n                <div class="modal-header">\n                    <span><h3 class=\'title\'>')
        # SOURCE LINE 197
        __M_writer(unicode(title))
        __M_writer(u'</h3></span>\n                </div>\n                <div class="modal-body">')
        # SOURCE LINE 199
        __M_writer(unicode(content))
        __M_writer(u'</div>\n                <div class="modal-footer">\n                    <div class="buttons" style="float: right;"></div>\n                    <div class="extra_buttons" style=""></div>\n                    <div style="clear: both;"></div>\n                </div>\n        </div>\n    \n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_javascripts(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 61
        __M_writer(u'\n')
        # SOURCE LINE 64
        __M_writer(u'    ')
        __M_writer(unicode(h.js( 'jquery.event.drag', 'jquery.event.hover', 'jquery.form', 'jquery.rating', 'galaxy.base', 'galaxy.panels' )))
        __M_writer(u'\n    <script type="text/javascript">\n        \n    ensure_dd_helper();\n        \n')
        # SOURCE LINE 69
        if self.has_left_panel:
            # SOURCE LINE 70
            __M_writer(u'            var lp = new Panel( { panel: $("#left"), center: $("#center"), drag: $("#left > .unified-panel-footer > .drag" ), toggle: $("#left > .unified-panel-footer > .panel-collapse" ) } );\n            force_left_panel = function( x ) { lp.force_panel( x ) };\n')
            pass
        # SOURCE LINE 73
        __M_writer(u'        \n')
        # SOURCE LINE 74
        if self.has_right_panel:
            # SOURCE LINE 75
            __M_writer(u'            var rp = new Panel( { panel: $("#right"), center: $("#center"), drag: $("#right > .unified-panel-footer > .drag" ), toggle: $("#right > .unified-panel-footer > .panel-collapse" ), right: true } );\n            window.handle_minwidth_hint = function( x ) { rp.handle_minwidth_hint( x ) };\n            force_right_panel = function( x ) { rp.force_panel( x ) };\n')
            pass
        # SOURCE LINE 79
        __M_writer(u'    \n    </script>\n')
        # SOURCE LINE 82
        __M_writer(u'    <![if !IE]>\n    <script type="text/javascript">\n        var upload_form_error = function( msg ) {\n            if ( ! $("iframe#galaxy_main").contents().find("body").find("div[class=\'errormessage\']").size() ) {\n                $("iframe#galaxy_main").contents().find("body").prepend( \'<div class="errormessage" name="upload_error">\' + msg + \'</div><p/>\' );\n            } else {\n                $("iframe#galaxy_main").contents().find("body").find("div[class=\'errormessage\']").text( msg );\n            }\n        }\n        var uploads_in_progress = 0;\n        jQuery( function() {\n            $("iframe#galaxy_main").load( function() {\n                $(this).contents().find("form").each( function() { \n                    if ( $(this).find("input[galaxy-ajax-upload]").length > 0 ){\n                        $(this).submit( function() {\n                            // Only bother using a hidden iframe if there\'s a file (e.g. big data) upload\n                            var file_upload = false;\n                            $(this).find("input[galaxy-ajax-upload]").each( function() {\n                                if ( $(this).val() != \'\' ) {\n                                    file_upload = true;\n                                }\n                            });\n                            if ( ! file_upload ) {\n                                return true;\n                            }\n                            // Make a synchronous request to create the datasets first\n                            var async_datasets;\n                            var upload_error = false;\n                            $.ajax( {\n                                async:      false,\n                                type:       "POST",\n                                url:        "')
        # SOURCE LINE 113
        __M_writer(unicode(h.url_for(controller='/tool_runner', action='upload_async_create')))
        __M_writer(u'",\n                                data:       $(this).formSerialize(),\n                                dataType:   "json",\n                                success:    function(array_obj, status) {\n                                                if (array_obj.length > 0) {\n                                                    if (array_obj[0] == \'error\') {\n                                                        upload_error = true;\n                                                        upload_form_error(array_obj[1]);\n                                                    } else {\n                                                        async_datasets = array_obj.join();\n                                                    }\n                                                } else {\n                                                    // ( gvk 1/22/10 ) FIXME: this block is never entered, so there may be a bug somewhere\n                                                    // I\'ve done some debugging like checking to see if array_obj is undefined, but have not\n                                                    // tracked down the behavior that will result in this block being entered.  I believe the\n                                                    // intent was to have this block entered if the upload button is clicked on the upload\n                                                    // form but no file was selected.\n                                                    upload_error = true;\n                                                    upload_form_error( \'No data was entered in the upload form.  You may choose to upload a file, paste some data directly in the data box, or enter URL(s) to fetch data.\' );\n                                                }\n                                            }\n                            } );\n                            if (upload_error == true) {\n                                return false;\n                            } else {\n                                $(this).find("input[name=async_datasets]").val( async_datasets );\n                                $(this).append("<input type=\'hidden\' name=\'ajax_upload\' value=\'true\'>");\n                            }\n                            // iframe submit is required for nginx (otherwise the encoding is wrong)\n                            $(this).ajaxSubmit( { iframe:   true,\n                                                  complete: function (xhr, stat) {\n                                                                uploads_in_progress--;\n                                                                if (uploads_in_progress == 0) {\n                                                                    window.onbeforeunload = null;\n                                                                }\n                                                            }\n                                                 } );\n                            uploads_in_progress++;\n                            window.onbeforeunload = function() { return "Navigating away from the Galaxy analysis interface will interrupt the file upload(s) currently in progress.  Do you really want to do this?"; }\n                            if ( $(this).find("input[name=\'folder_id\']").val() != undefined ) {\n                                var library_id = $(this).find("input[name=\'library_id\']").val();\n                                var show_deleted = $(this).find("input[name=\'show_deleted\']").val();\n                                if ( location.pathname.indexOf( \'admin\' ) != -1 ) {\n                                    $("iframe#galaxy_main").attr("src","')
        # SOURCE LINE 156
        __M_writer(unicode(h.url_for( controller='library_common', action='browse_library' )))
        __M_writer(u'?cntrller=library_admin&id=" + library_id + "&created_ldda_ids=" + async_datasets + "&show_deleted=" + show_deleted);\n                                } else {\n                                    $("iframe#galaxy_main").attr("src","')
        # SOURCE LINE 158
        __M_writer(unicode(h.url_for( controller='library_common', action='browse_library' )))
        __M_writer(u'?cntrller=library&id=" + library_id + "&created_ldda_ids=" + async_datasets + "&show_deleted=" + show_deleted);\n                                }\n                            } else {\n                                $("iframe#galaxy_main").attr("src","')
        # SOURCE LINE 161
        __M_writer(unicode(h.url_for(controller='tool_runner', action='upload_async_message')))
        __M_writer(u'");\n                            }\n                            return false;\n                        });\n                    }\n                });\n            });\n        });\n    </script>\n    <![endif]>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 18
        __M_writer(u'\n    ')
        # SOURCE LINE 19
        __M_writer(unicode(h.css('base','panel_layout','jquery.rating')))
        __M_writer(u'\n    <style type="text/css">\n    body, html {\n        overflow: hidden;\n        margin: 0;\n        padding: 0;\n        width: 100%;\n        height: 100%;\n    }\n    #center {\n')
        # SOURCE LINE 29
        if not self.has_left_panel:
            # SOURCE LINE 30
            __M_writer(u'            left: 0 !important;\n')
            pass
        # SOURCE LINE 32
        if not self.has_right_panel:
            # SOURCE LINE 33
            __M_writer(u'            right: 0 !important;\n')
            pass
        # SOURCE LINE 35
        __M_writer(u'    }\n')
        # SOURCE LINE 36
        if self.message_box_visible:
            # SOURCE LINE 37
            __M_writer(u'        #left, #left-border, #center, #right-border, #right\n        {\n            top: 64px;\n        }\n')
            pass
        # SOURCE LINE 42
        __M_writer(u'    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 13
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_masthead(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 174
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 46
        __M_writer(u'\n    <!--[if lt IE 7]>\n    ')
        # SOURCE LINE 48
        __M_writer(unicode(h.js( 'IE7', 'ie7-recalc' )))
        __M_writer(u'\n    <![endif]-->\n    ')
        # SOURCE LINE 50
        __M_writer(unicode(h.js( 'jquery', 'libs/underscore', 'libs/backbone', 'libs/backbone-relational', 'libs/handlebars.runtime', 'mvc/ui' )))
        __M_writer(u'\n    <script type="text/javascript">\n        // Set up needed paths.\n        var galaxy_paths = new GalaxyPaths({\n            root_path: \'')
        # SOURCE LINE 54
        __M_writer(unicode(h.url_for( "/" )))
        __M_writer(u"',\n            image_path: '")
        # SOURCE LINE 55
        __M_writer(unicode(h.url_for( "/static/images" )))
        __M_writer(u"'\n        });\n    </script>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


