from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1297798364.3934381
_template_filename='templates/tracks/browser.mako'
_template_uri='tracks/browser.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding=None
_exports = ['stylesheets', 'init', 'javascripts', 'center_panel']


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
        # SOURCE LINE 10
        __M_writer(u'\n\n')
        # SOURCE LINE 36
        __M_writer(u'\n\n')
        # SOURCE LINE 49
        __M_writer(u'\n\n')
        # SOURCE LINE 269
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 12
        __M_writer(u'\n')
        # SOURCE LINE 13
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n\n')
        # SOURCE LINE 15
        __M_writer(unicode(h.css( "history", "autocomplete_tagging", "trackster", "overcast/jquery-ui-1.8.5.custom" )))
        __M_writer(u'\n\n<style type="text/css">\n    #browser-container {\n        overflow: none;\n    }\n    .nav-container {\n        width: 100%;\n')
        # SOURCE LINE 24
        __M_writer(u'        height: 0;\n        text-align: center;\n    }\n    .nav {\n')
        # SOURCE LINE 29
        __M_writer(u'        position: relative;\n        display: inline-block;\n        top: -2em;\n        background: transparent;\n        border: none;\n    }\n</style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4

        self.has_left_panel=False
        self.has_right_panel=False
        self.active_view="visualization"
        self.message_box_visible=False
        
        
        # SOURCE LINE 9
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        default_dbkey = context.get('default_dbkey', UNDEFINED)
        h = context.get('h', UNDEFINED)
        config = context.get('config', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        add_dataset = context.get('add_dataset', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 51
        __M_writer(u'\n')
        # SOURCE LINE 52
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n\n<!--[if lt IE 9]>\n  <script type=\'text/javascript\' src="')
        # SOURCE LINE 55
        __M_writer(unicode(h.url_for('/static/scripts/excanvas.js')))
        __M_writer(u'"></script>\n<![endif]-->\n\n')
        # SOURCE LINE 58
        __M_writer(unicode(h.js( "galaxy.base", "galaxy.panels", "json2", "jquery", "jquery.event.drag", "jquery.mousewheel", "jquery.autocomplete", "trackster", "jquery.ui.sortable.slider", "farbtastic" )))
        __M_writer(u'\n\n<script type="text/javascript">\n\n    //\n    // Place URLs here so that url_for can be used to generate them.\n    // \n    var default_data_url = "')
        # SOURCE LINE 65
        __M_writer(unicode(h.url_for( action='data' )))
        __M_writer(u'",\n        raw_data_url = "')
        # SOURCE LINE 66
        __M_writer(unicode(h.url_for( action='raw_data' )))
        __M_writer(u'",\n        run_tool_url = "')
        # SOURCE LINE 67
        __M_writer(unicode(h.url_for( action='run_tool' )))
        __M_writer(u'",\n        reference_url = "')
        # SOURCE LINE 68
        __M_writer(unicode(h.url_for( action='reference' )))
        __M_writer(u'",\n        chrom_url = "')
        # SOURCE LINE 69
        __M_writer(unicode(h.url_for( action='chroms' )))
        __M_writer(u'",\n        dataset_state_url = "')
        # SOURCE LINE 70
        __M_writer(unicode(h.url_for( action='dataset_state' )))
        __M_writer(u'",\n        converted_datasets_state_url = "')
        # SOURCE LINE 71
        __M_writer(unicode(h.url_for( action='converted_datasets_state' )))
        __M_writer(u'",\n        addable_track_types = { "LineTrack": LineTrack, "FeatureTrack": FeatureTrack, "ReadTrack": ReadTrack },\n        view;\n    \n    $(function() {\n        \n')
        # SOURCE LINE 77
        if config:
            # SOURCE LINE 78
            __M_writer(u'            var callback;\n')
            # SOURCE LINE 79
            if 'viewport' in config:
                # SOURCE LINE 80
                __M_writer(u"                var callback = function() { view.change_chrom( '")
                __M_writer(unicode(config['viewport']['chrom']))
                __M_writer(u"', ")
                __M_writer(unicode(config['viewport']['start']))
                __M_writer(u', ')
                __M_writer(unicode(config['viewport']['end']))
                __M_writer(u' ); }\n')
            # SOURCE LINE 82
            __M_writer(u'            view = new View( $("#browser-container"), "')
            __M_writer(filters.html_escape(unicode(config.get('title') )))
            __M_writer(u'", "')
            __M_writer(unicode(config.get('vis_id')))
            __M_writer(u'", "')
            __M_writer(unicode(config.get('dbkey')))
            __M_writer(u'", callback );\n            view.editor = true;\n')
            # SOURCE LINE 85
            __M_writer(u"            var tracks_config = JSON.parse('")
            __M_writer(unicode( h.to_json_string( config.get('tracks') ) ))
            __M_writer(u'\');\n            var track_config, track, parent_track, parent_obj;\n            for (var i = 0; i < tracks_config.length; i++) {\n                track_config = tracks_config[i];\n                track = new addable_track_types[track_config["track_type"]](\n                                track_config[\'name\'], \n                                view,\n                                track_config[\'hda_ldda\'],\n                                track_config[\'dataset_id\'],\n                                track_config[\'prefs\'], \n                                track_config[\'filters\'],\n                                track_config[\'tool\'], \n                                (track_config.is_child ? parent_track : undefined));\n                parent_obj = view;\n                if (track_config.is_child) {\n                    parent_obj = parent_track;\n                }\n                else {\n                    // New parent track is this track.\n                    parent_track = track;\n                }\n                parent_obj.add_track(track);\n            }\n            init();\n')
            # SOURCE LINE 109
        else:
            # SOURCE LINE 110
            __M_writer(u'            var continue_fn = function() {\n                view = new View( $("#browser-container"), $("#new-title").val(), undefined, $("#new-dbkey").val() );\n                view.editor = true;\n                init();\n                hide_modal();\n            };\n            $.ajax({\n                url: "')
            # SOURCE LINE 117
            __M_writer(unicode(h.url_for( action='new_browser', default_dbkey=default_dbkey )))
            __M_writer(u'",\n                data: {},\n                error: function() { alert( "Couldn\'t create new browser" ) },\n                success: function(form_html) {\n                    show_modal("New Track Browser", form_html, {\n                        "Cancel": function() { window.location = "')
            # SOURCE LINE 122
            __M_writer(unicode(h.url_for( controller='visualization', action='list' )))
            __M_writer(u'"; },\n                        "Continue": function() { $(document).trigger("convert_to_values"); continue_fn(); }\n                    });\n                    $("#new-title").focus();\n                    replace_big_select_inputs();\n                }\n            });\n')
        # SOURCE LINE 130
        __M_writer(u'        \n        // Execute initializer for EDITOR specific javascript\n        function init() {\n            if (view.num_tracks === 0) {\n                $("#no-tracks").show();\n            }\n            $("#title").text(view.title + " (" + view.dbkey + ")");\n           \n            window.onbeforeunload = function() {\n                if (view.has_changes) {\n                    return "There are unsaved changes to your visualization which will be lost.";\n                }\n            };\n            \n            var add_async_success = function(track_data) {\n                var td = track_data,\n                    new_track = new addable_track_types[track_data.track_type]( \n                                        track_data.name, view, track_data.hda_ldda, track_data.dataset_id,\n                                        track_data.prefs, track_data.filters, track_data.tool );\n                view.add_track(new_track);\n')
        # SOURCE LINE 151
        __M_writer(u'                sortable( new_track.container_div, ".draghandle" );\n                view.has_changes = true;\n                $("#no-tracks").hide();\n            };\n            \n')
        # SOURCE LINE 156
        if add_dataset is not None:
            # SOURCE LINE 157
            __M_writer(u'                $.ajax( {\n                    url: "')
            # SOURCE LINE 158
            __M_writer(unicode(h.url_for( action='add_track_async' )))
            __M_writer(u'",\n                    data: { hda_id: "')
            # SOURCE LINE 159
            __M_writer(unicode(add_dataset))
            __M_writer(u'" },\n                    dataType: "json",\n                    success: add_async_success\n                });\n                \n')
        # SOURCE LINE 165
        __M_writer(u'            \n            // Use a popup grid to add more tracks\n            $("#add-track").bind("click", function(e) {\n                $.ajax({\n                    url: "')
        # SOURCE LINE 169
        __M_writer(unicode(h.url_for( action='list_histories' )))
        __M_writer(u'",\n                    data: { "f-dbkey": view.dbkey },\n                    error: function() { alert( "Grid failed" ); },\n                    success: function(table_html) {\n                        show_modal(\n                            "Add Track &mdash; Select history/library, then datasets", \n                            table_html, \n                            {\n                                "Cancel": function() {\n                                    hide_modal();\n                                },\n                                "Insert": function() {\n                                    $(\'input[name=id]:checked,input[name=ldda_ids]:checked\').each(function() {\n                                        var data,\n                                            id = $(this).val();\n                                        if ($(this).attr("name") === "id") {\n                                            data = { hda_id: id };\n                                        } else {\n                                            data = { ldda_id: id};\n                                        }\n                                        $.ajax( {\n                                            url: "')
        # SOURCE LINE 190
        __M_writer(unicode(h.url_for( action='add_track_async' )))
        __M_writer(u'",\n                                            data: data,\n                                            dataType: "json",\n                                            success: add_async_success\n                                        });\n\n                                    });\n                                    hide_modal();\n                                }\n                            }\n                        );\n                    }\n                });\n            });\n            \n            $("#save-button").bind("click", function(e) {\n                // Show saving dialog box\n                show_modal("Saving...", "<img src=\'')
        # SOURCE LINE 207
        __M_writer(unicode(h.url_for('/static/images/yui/rel_interstitial_loading.gif')))
        __M_writer(u'\'/>");\n                \n                // Save all tracks.\n                var tracks = [];\n                $(".viewport-container .track").each(function () {\n                    // ID has form track_<main_track_id>_<child_track_id>\n                    var \n                        id_split = $(this).attr("id").split("_"),\n                        track_id = id_split[1],\n                        child_id = id_split[2];\n                    \n                    // Get track.    \n                    var track = view.tracks[track_id];\n                    if (child_id) {\n                        track = track.child_tracks[child_id];\n                    }\n                    \n                    // Add track.\n                    tracks.push( {\n                        "track_type": track.track_type,\n                        "name": track.name,\n                        "hda_ldda": track.hda_ldda,\n                        "dataset_id": track.dataset_id,\n                        "prefs": track.prefs,\n                        "is_child": (child_id ? true : false )\n                    });\n                });\n\n                var payload = { \'tracks\': tracks, \'viewport\': { \'chrom\': view.chrom, \'start\': view.low , \'end\': view.high } };\n                \n                $.ajax({\n                    url: "')
        # SOURCE LINE 238
        __M_writer(unicode(h.url_for( action='save' )))
        __M_writer(u'",\n                    type: "POST",\n                    data: {\n                        \'vis_id\': view.vis_id,\n                        \'vis_title\': view.title,\n                        \'dbkey\': view.dbkey,\n                        \'payload\': JSON.stringify(payload)\n                    },\n                    success: function(vis_id) {\n                        view.vis_id = vis_id;\n                        view.has_changes = false;\n                        hide_modal();\n                    },\n                    error: function() { alert("Could not save visualization"); }\n                });\n            });\n\n            $(document).keydown( function( e ) {\n                // 37 == left\n                if ( e.which == 39 ) {\n                   view.move_fraction( -0.25 ); \n                // 39 == right\n                } else if ( e.which == 37 ) {\n                   view.move_fraction( 0.25 ); \n                }\n            });\n        };\n        \n    });\n\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 38
        __M_writer(u'\n<div class="unified-panel-header" unselectable="on">\n    <div class="unified-panel-header-inner">\n        <div style="float:left;" id="title"></div>\n        <a class="panel-header-button right-float" href="')
        # SOURCE LINE 42
        __M_writer(unicode(h.url_for( controller='visualization', action='list' )))
        __M_writer(u'">Close</a>\n        <a id="save-button" class="panel-header-button right-float" href="javascript:void(0);">Save</a>\n        <a id="add-track" class="panel-header-button right-float" href="javascript:void(0);">Add Tracks</a>\n    </div>\n</div>\n<div id="browser-container" class="unified-panel-body"></div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


