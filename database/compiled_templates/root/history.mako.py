# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1336505820.3548191
_template_filename='templates/root/history.mako'
_template_uri='root/history.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 1
    ns = runtime.TemplateNamespace('__anon_0x7fae1c59db90', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fae1c59db90')] = ns

    # SOURCE LINE 520
    ns = runtime.TemplateNamespace('__anon_0x7fae1c587e50', context._clean_inheritance_tokens(), templateuri=u'history_common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fae1c587e50')] = ns

    # SOURCE LINE 519
    ns = runtime.TemplateNamespace('__anon_0x7fae1c587f90', context._clean_inheritance_tokens(), templateuri=u'../tagging_common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fae1c587f90')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fae1c59db90')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7fae1c587e50')._populate(_import_ns, [u'render_dataset'])
        _mako_get_namespace(context, '__anon_0x7fae1c587f90')._populate(_import_ns, [u'render_individual_tagging_element'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        datasets = _import_ns.get('datasets', context.get('datasets', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        show_deleted = _import_ns.get('show_deleted', context.get('show_deleted', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        reversed = _import_ns.get('reversed', context.get('reversed', UNDEFINED))
        n_ = _import_ns.get('n_', context.get('n_', UNDEFINED))
        over_quota = _import_ns.get('over_quota', context.get('over_quota', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        bool = _import_ns.get('bool', context.get('bool', UNDEFINED))
        show_hidden = _import_ns.get('show_hidden', context.get('show_hidden', UNDEFINED))
        render_individual_tagging_element = _import_ns.get('render_individual_tagging_element', context.get('render_individual_tagging_element', UNDEFINED))
        render_dataset = _import_ns.get('render_dataset', context.get('render_dataset', UNDEFINED))
        hda_id = _import_ns.get('hda_id', context.get('hda_id', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        annotation = _import_ns.get('annotation', context.get('annotation', UNDEFINED))
        history = _import_ns.get('history', context.get('history', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 3
        _=n_ 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['_'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n<!DOCTYPE HTML>\n\n<html>\n\n<head>\n<title>')
        # SOURCE LINE 9
        __M_writer(unicode(_('Galaxy History')))
        __M_writer(u'</title>\n\n')
        # SOURCE LINE 12
        if bool( [ data for data in history.active_datasets if data.state in ['running', 'queued', '', None ] ] ):
            # SOURCE LINE 13
            __M_writer(u'<!-- running: do not change this comment, used by TwillTestCase.wait -->\n')
            pass
        # SOURCE LINE 15
        __M_writer(u'\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n<meta http-equiv="Pragma" content="no-cache">\n\n')
        # SOURCE LINE 19
        __M_writer(unicode(h.css( "base", "history", "autocomplete_tagging" )))
        __M_writer(u'\n')
        # SOURCE LINE 20
        __M_writer(unicode(h.js( "jquery", "jquery.tipsy", "galaxy.base", "json2", "jstorage", "jquery.autocomplete", "autocomplete_tagging" )))
        __M_writer(u'\n\n<script type="text/javascript">\n\n')
        # SOURCE LINE 24
        TERMINAL_STATES = ["ok", "error", "empty", "deleted", "discarded", "failed_metadata"] 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['TERMINAL_STATES'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\nTERMINAL_STATES = ')
        # SOURCE LINE 25
        __M_writer(unicode( h.to_json_string(TERMINAL_STATES) ))
        __M_writer(u';\n\n// Tag handling.\nfunction tag_handling(parent_elt) {\n    $(parent_elt).find("a.icon-button.tags").each( function() {\n        // Use links parameters but custom URL as ajax URL.\n        $(this).click( function() {\n            // Get tag area, tag element.\n            var history_item = $(this).parents(".historyItem");\n            var tag_area = history_item.find(".tag-area");\n            var tag_elt = history_item.find(".tag-elt");\n\n            // Show or hide tag area; if showing tag area and it\'s empty, fill it.\n            if ( tag_area.is( ":hidden" ) ) {\n                if (!tag_elt.html()) {\n                    // Need to fill tag element.\n                    var href_parms = $(this).attr("href").split("?")[1];\n                    var ajax_url = "')
        # SOURCE LINE 42
        __M_writer(unicode(h.url_for( controller='tag', action='get_tagging_elt_async' )))
        __M_writer(u'?" + href_parms;\n                    $.ajax({\n                        url: ajax_url,\n                        error: function() { alert( "Tagging failed" ) },\n                        success: function(tag_elt_html) {\n                            tag_elt.html(tag_elt_html);\n                            tag_elt.find(".tooltip").tipsy( { gravity: \'s\' } );\n                            tag_area.slideDown("fast");\n                        }\n                    });\n                } else {\n                    // Tag element is filled; show.\n                    tag_area.slideDown("fast");\n                }\n            } else {\n                // Hide.\n                tag_area.slideUp("fast");\n            }\n            return false;        \n        });\n    });\n};\n\n// Annotation handling.\nfunction annotation_handling(parent_elt) {\n    $(parent_elt).find("a.icon-button.annotate").each( function() {\n        // Use links parameters but custom URL as ajax URL.\n        $(this).click( function() {\n            // Get tag area, tag element.\n            var history_item = $(this).parents(".historyItem");\n            var annotation_area = history_item.find(".annotation-area");\n            var annotation_elt = history_item.find(".annotation-elt");\n\n            // Show or hide annotation area; if showing annotation area and it\'s empty, fill it.\n            if ( annotation_area.is( ":hidden" ) ) {\n                if (!annotation_elt.html()) {\n                    // Need to fill annotation element.\n                    var href_parms = $(this).attr("href").split("?")[1];\n                    var ajax_url = "')
        # SOURCE LINE 80
        __M_writer(unicode(h.url_for( controller='dataset', action='get_annotation_async' )))
        __M_writer(u'?" + href_parms;\n                    $.ajax({\n                        url: ajax_url,\n                        error: function() { alert( "Annotations failed" ) },\n                        success: function(annotation) {\n                            if (annotation == "") {\n                                annotation = "<em>Describe or add notes to dataset</em>";\n                            }\n                            annotation_elt.html(annotation);\n                            annotation_area.find(".tooltip").tipsy( { gravity: \'s\' } );\n                            async_save_text(\n                                annotation_elt.attr("id"), annotation_elt.attr("id"),\n                                "')
        # SOURCE LINE 92
        __M_writer(unicode(h.url_for( controller='/dataset', action='annotate_async')))
        __M_writer(u'?" + href_parms,\n                                "new_annotation", 18, true, 4);\n                            annotation_area.slideDown("fast");\n                        }\n                    });\n                } else {\n                    // Annotation element is filled; show.\n                    annotation_area.slideDown("fast");\n                }\n            } else {\n                // Hide.\n                annotation_area.slideUp("fast");\n            }\n            return false;        \n        });\n    });\n};\n\n// Update the message for async operations\nfunction render_message(message, status) {\n    $("div#message-container").html( "<div class=\\"" + status + "message\\">" + message + "</div><br/>" );\n}\n\n$(function() {\n    var historywrapper = $("div.historyItemWrapper");\n    init_history_items(historywrapper);\n    historywrapper.each( function() {\n        // Delete link\n        $(this).find("div.historyItemButtons > .delete" ).each( function() {\n            var data_id = this.id.split( "-" )[1];\n            $(this).click( function() {\n                $( \'#historyItem-\' + data_id + "> div.historyItemTitleBar" ).addClass( "spinner" );\n                $.ajax({\n                    url: "')
        # SOURCE LINE 125
        __M_writer(unicode(h.url_for( controller='dataset', action='delete_async', dataset_id='XXX' )))
        __M_writer(u'".replace( \'XXX\', data_id ),\n                    error: function() { render_message( "Dataset deletion failed", "error" ); },\n                    success: function(msg) {\n                        if (msg === "OK") {\n')
        # SOURCE LINE 129
        if show_deleted:
            # SOURCE LINE 130
            __M_writer(u'                            var to_update = {};\n                            to_update[data_id] = "none";\n                            updater( to_update );\n')
            # SOURCE LINE 133
        else:
            # SOURCE LINE 134
            __M_writer(u'                            $( "#historyItem-" + data_id ).fadeOut( "fast", function() {\n                                $( "#historyItemContainer-" + data_id ).remove();\n                                if ( $( "div.historyItemContainer" ).length < 1 ) {\n                                    $( "#emptyHistoryMessage" ).show();\n                                }\n                            });\n')
            pass
        # SOURCE LINE 141
        __M_writer(u'                            $(".tipsy").remove();\n                        } else {\n                            render_message( "Dataset deletion failed", "error" );\n                        }\n                    }\n                });\n                return false;\n            });\n        });\n        \n        // Check to see if the dataset data is cached or needs to be pulled in\n        // via objectstore\n        $(this).find("a.display").each( function() {\n            var history_item = $(this).parents(".historyItem")[0];\n            var history_id = history_item.id.split( "-" )[1];\n            $(this).click(function() {\n                check_transfer_status($(this), history_id);\n            });\n        });\n        \n        // If dataset data is not cached, keep making ajax calls to check on the\n        // data status and update the dataset UI element accordingly\n        function check_transfer_status(link, history_id) {\n            $.getJSON("')
        # SOURCE LINE 164
        __M_writer(unicode(h.url_for( controller='dataset', action='transfer_status', dataset_id='XXX' )))
        __M_writer(u'".replace( \'XXX\', link.attr("dataset_id") ), \n                function(ready) {\n                    if (ready === false) {\n                        // $("<div/>").text("Data is loading from S3... please be patient").appendTo(link.parent());\n                        $( \'#historyItem-\' + history_id).removeClass( "historyItem-ok" );\n                        $( \'#historyItem-\' + history_id).addClass( "historyItem-running" );\n                        setTimeout(function(){check_transfer_status(link, history_id)}, 1000);\n                    } else {\n                        $( \'#historyItem-\' + history_id).removeClass( "historyItem-running" );\n                        $( \'#historyItem-\' + history_id).addClass( "historyItem-ok" );\n                    }\n                }\n            );\n        }\n\n        // Undelete link\n        $(this).find("a.historyItemUndelete").each( function() {\n            var data_id = this.id.split( "-" )[1];\n            $(this).click( function() {\n                $( \'#historyItem-\' + data_id + " > div.historyItemTitleBar" ).addClass( "spinner" );\n                $.ajax({\n                    url: "')
        # SOURCE LINE 185
        __M_writer(unicode(h.url_for( controller='dataset', action='undelete_async', dataset_id='XXX' )))
        __M_writer(u'".replace( \'XXX\', data_id ),\n                    error: function() { render_message( "Dataset undeletion failed", "error" ); },\n                    success: function() {\n                        var to_update = {};\n                        to_update[data_id] = "none";\n                        updater( to_update );\n                    }\n                });\n                return false;\n            });\n        });\n        \n        // Purge link\n        $(this).find("a.historyItemPurge").each( function() {\n            var data_id = this.id.split( "-" )[1];\n            $(this).click( function() {\n                $( \'#historyItem-\' + data_id + " > div.historyItemTitleBar" ).addClass( "spinner" );\n                $.ajax({\n                    url: "')
        # SOURCE LINE 203
        __M_writer(unicode(h.url_for( controller='dataset', action='purge_async', dataset_id='XXX' )))
        __M_writer(u'".replace( \'XXX\', data_id ),\n                    error: function() { render_message( "Dataset removal from disk failed", "error" ) },\n                    success: function() {\n                        var to_update = {};\n                        to_update[data_id] = "none";\n                        updater( to_update );\n                    }\n                });\n                return false;\n            });\n        });\n        \n        // Show details icon -- Disabled since it often gets stuck, etc\n        /* $(this).find("a.show-details").bind("mouseenter.load-detail", function(e) {\n            var anchor = $(this);\n            $.get($(this).attr("href"), function(data) {\n                anchor.attr("title", data);\n                anchor.tipsy( { html: true, gravity: \'s\', opacity: 1.0, delayOut: 300 } );\n                anchor.unbind("mouseenter.load-detail");\n                anchor.trigger("mouseenter");\n            });\n            return false;\n        });\n        \n        // Disable clickthrough\n        $(this).find("a.show-details").bind("click", function() { return false; });\n        */\n        \n        tag_handling(this);\n        annotation_handling(this);\n    });\n    \n    // Trackster links\n    function init_trackster_links() {\n        // Add to trackster browser functionality\n        $(".trackster-add").live("click", function() {\n            var dataset = this,\n                dataset_jquery = $(this);\n            $.ajax({\n                url: dataset_jquery.attr("data-url"),\n                dataType: "html",\n                error: function() { alert( "Could not add this dataset to browser." ); },\n                success: function(table_html) {\n                    var parent = window.parent;\n                    \n                    parent.show_modal("View Data in a New or Saved Visualization", "", {\n                        "Cancel": function() {\n                            parent.hide_modal();\n                        },\n                        "View in saved visualization": function() {\n                            // Show new modal with saved visualizations.\n                            parent.hide_modal();\n                            parent.show_modal("Add Data to Saved Visualization", table_html, {\n                                "Cancel": function() {\n                                    parent.hide_modal();\n                                },\n                                "Add to visualization": function() {\n                                    $(parent.document).find(\'input[name=id]:checked\').each(function() {\n                                        var vis_id = $(this).val();\n                                        parent.location = dataset_jquery.attr("action-url") + "&id=" + vis_id;\n                                    });\n                                }, \n                            });\n                        },\n                        "View in new visualization": function() {\n                            parent.location = dataset_jquery.attr("new-url");\n                        }\n                    });\n                }\n            });\n        });\n    }\n    \n    init_trackster_links();\n    \n    // History rename functionality.\n    async_save_text("history-name-container", "history-name", "')
        # SOURCE LINE 279
        __M_writer(unicode(h.url_for( controller="/history", action="rename_async", id=trans.security.encode_id(history.id) )))
        __M_writer(u'", "new_name", 18);\n    \n    // History tagging functionality.\n    var historyTagArea = $(\'#history-tag-area\');\n    $(\'#history-tag\').click( function() {\n        if ( historyTagArea.is( ":hidden" ) ) {\n            historyTagArea.slideDown("fast");\n        } else {\n            historyTagArea.slideUp("fast");\n        }\n        return false;\n    });\n    \n    // History annotation functionality.\n    var historyAnnotationArea = $(\'#history-annotation-area\');\n    $(\'#history-annotate\').click( function() {\n        if ( historyAnnotationArea.is( ":hidden" ) ) {\n            historyAnnotationArea.slideDown("fast");\n        } else {\n            historyAnnotationArea.slideUp("fast");\n        }\n        return false;\n    });\n    async_save_text("history-annotation-container", "history-annotation", "')
        # SOURCE LINE 302
        __M_writer(unicode(h.url_for( controller="/history", action="annotate_async", id=trans.security.encode_id(history.id) )))
        __M_writer(u'", "new_annotation", 18, true, 4);\n    \n    // Updater\n    updater(\n        ')
        # SOURCE LINE 306
        __M_writer(unicode( h.to_json_string( dict([(trans.app.security.encode_id(data.id), data.state) for data in reversed( datasets ) if data.visible and data.state not in TERMINAL_STATES]) ) ))
        __M_writer(u'\n    );\n    \n    // Navigate to a dataset.\n')
        # SOURCE LINE 310
        if hda_id:
            # SOURCE LINE 311
            __M_writer(u'        self.location = "#')
            __M_writer(unicode(hda_id))
            __M_writer(u'";\n')
            pass
        # SOURCE LINE 313
        __M_writer(u'\n    // Update the Quota Meter\n    $.ajax( {\n        type: "POST",\n        url: "')
        # SOURCE LINE 317
        __M_writer(unicode(h.url_for( controller='root', action='user_get_usage' )))
        __M_writer(u'",\n        dataType: "json",\n        success : function ( data ) {\n            $.each( data, function( type, val ) {\n                quota_meter_updater( type, val );\n            });\n        }\n    });\n});\n\n// Updates the Quota Meter\nvar quota_meter_updater = function ( type, val ) {\n    if ( type == "usage" ) {\n        $("#quota-meter-bar", window.top.document).css( "width", "0" );\n        $("#quota-meter-text", window.top.document).text( "Using " + val );\n    } else if ( type == "percent" ) {\n        $("#quota-meter-bar", window.top.document).removeClass("quota-meter-bar-warn quota-meter-bar-error");\n        if ( val >= 100 ) {\n            $("#quota-meter-bar", window.top.document).addClass("quota-meter-bar-error");\n            $("#quota-message-container").slideDown();\n        } else if ( val >= 85 ) {\n            $("#quota-meter-bar", window.top.document).addClass("quota-meter-bar-warn");\n            $("#quota-message-container").slideUp();\n        } else {\n            $("#quota-message-container").slideUp();\n        }\n        $("#quota-meter-bar", window.top.document).css( "width", val + "px" );\n        $("#quota-meter-text", window.top.document).text( "Using " + val + "%" );\n    }\n}\n\n// Looks for changes in dataset state using an async request. Keeps\n// calling itself (via setTimeout) until all datasets are in a terminal\n// state.\nvar updater = function ( tracked_datasets ) {\n    // Check if there are any items left to track\n    var empty = true;\n    for ( i in tracked_datasets ) {\n        empty = false;\n        break;\n    }\n    if ( !empty ) {\n        setTimeout( function() { updater_callback( tracked_datasets ) }, 4000 );\n    }\n};\nvar updater_callback = function ( tracked_datasets ) {\n    // Build request data\n    var ids = [],\n        states = [],\n        force_history_refresh = false,\n        check_history_size = false;\n        \n    $.each( tracked_datasets, function ( id, state ) {\n        ids.push( id );\n        states.push( state );\n    });\n    // Make ajax call\n    $.ajax( {\n        type: "POST",\n        url: "')
        # SOURCE LINE 376
        __M_writer(unicode(h.url_for( controller='root', action='history_item_updates' )))
        __M_writer(u'",\n        dataType: "json",\n        data: { ids: ids.join( "," ), states: states.join( "," ) },\n        success : function ( data ) {\n            $.each( data, function( id, val ) {\n                // Replace HTML\n                var container = $("#historyItemContainer-" + id);\n                container.html( val.html );\n                init_history_items( $("div.historyItemWrapper"), "noinit" );\n                tag_handling(container);\n                annotation_handling(container);\n                // If new state is terminal, stop tracking\n                if (TERMINAL_STATES.indexOf(val.state) !== -1) {\n                    if ( val.force_history_refresh ){\n                        force_history_refresh = true;\n                    }\n                    delete tracked_datasets[id];\n                    // When a dataset becomes terminal, check for changes in history disk size\n                    check_history_size = true;\n                } else {\n                    tracked_datasets[id] = val.state;\n                }\n            });\n            if ( force_history_refresh ) {\n                parent.frames.galaxy_history.location.reload();\n            } else {\n                if ( check_history_size ) {\n                    $.ajax( {\n                        type: "POST",\n                        url: "')
        # SOURCE LINE 405
        __M_writer(unicode(h.url_for( controller='root', action='history_get_disk_size' )))
        __M_writer(u'",\n                        dataType: "json",\n                        success: function( data ) {\n                            $.each( data, function( type, val ) {\n                                if ( type == "history" ) {\n                                    $("#history-size").text( val );\n                                } else if ( type == "global_usage" ) {\n                                    quota_meter_updater( "usage", val );\n                                } else if ( type == "global_percent" ) {\n                                    quota_meter_updater( "percent", val );\n                                }\n                            });\n                        }\n                    });\n                    check_history_size = false;\n                }\n                // Keep going (if there are still any items to track)\n                updater( tracked_datasets ); \n            }\n            make_popup_menus();\n        },\n        error: function() {\n            // Just retry, like the old method, should try to be smarter\n            updater( tracked_datasets );\n        }\n    });\n};\n\n</script>\n\n<style>\n.historyItemBody {\n    display: none;\n}\ndiv.form-row {\n    padding: 5px 5px 5px 0px;\n}\n#top-links {\n    margin-bottom: 15px;\n}\n#history-name-container {\n    color: gray;\n    font-weight: bold;\n}\n#history-name {\n    word-wrap: break-word;\n}\n.editable-text {\n    border: solid transparent 1px;\n    padding: 3px;\n    margin: -4px;\n}\n</style>\n\n<noscript>\n<style>\n.historyItemBody {\n    display: block;\n}\n</style>\n</noscript>\n\n</head>\n\n<body class="historyPage">\n\n<div id="top-links" class="historyLinks">\n    \n    <a title="')
        # SOURCE LINE 473
        __M_writer(unicode(_('refresh')))
        __M_writer(u'" class="icon-button arrow-circle tooltip" href="')
        __M_writer(unicode(h.url_for('history', show_deleted=show_deleted)))
        __M_writer(u'"></a>\n    <a title=\'')
        # SOURCE LINE 474
        __M_writer(unicode(_('collapse all')))
        __M_writer(u'\' class=\'icon-button toggle tooltip\' href=\'#\' style="display: none"></a>\n    \n')
        # SOURCE LINE 476
        if trans.get_user():
            # SOURCE LINE 477
            __M_writer(u'    <div style="width: 40px; float: right; white-space: nowrap;">\n        <a id="history-tag" title="Edit history tags" class="icon-button tags tooltip" target="galaxy_main" href="')
            # SOURCE LINE 478
            __M_writer(unicode(h.url_for( controller='history', action='tag' )))
            __M_writer(u'"></a>\n        <a id="history-annotate" title="Edit history annotation" class="icon-button annotate tooltip" target="galaxy_main" href="')
            # SOURCE LINE 479
            __M_writer(unicode(h.url_for( controller='history', action='annotate' )))
            __M_writer(u'"></a>\n    </div>\n')
            pass
        # SOURCE LINE 482
        __M_writer(u'</div>\n\n<div class="clear"></div>\n\n')
        # SOURCE LINE 486
        if show_deleted:
            # SOURCE LINE 487
            __M_writer(u'<div class="historyLinks">\n    <a href="')
            # SOURCE LINE 488
            __M_writer(unicode(h.url_for('history', show_deleted=False)))
            __M_writer(u'">')
            __M_writer(unicode(_('hide deleted')))
            __M_writer(u'</a>\n</div>\n')
            pass
        # SOURCE LINE 491
        __M_writer(u'\n')
        # SOURCE LINE 492
        if show_hidden:
            # SOURCE LINE 493
            __M_writer(u'<div class="historyLinks">\n    <a href="')
            # SOURCE LINE 494
            __M_writer(unicode(h.url_for('history', show_hidden=False)))
            __M_writer(u'">')
            __M_writer(unicode(_('hide hidden')))
            __M_writer(u'</a>\n</div>\n')
            pass
        # SOURCE LINE 497
        __M_writer(u'\n<div id="history-name-area" class="historyLinks">\n    \n    <div id="history-name-container" style="position: relative;">\n')
        # SOURCE LINE 501
        if trans.get_user():
            # SOURCE LINE 502
            __M_writer(u'            <div id="history-size" style="position: absolute; top: 3px; right: 0px;">')
            __M_writer(unicode(history.get_disk_size(nice_size=True)))
            __M_writer(u'</div>\n            <div id="history-name" style="margin-right: 50px;" class="tooltip editable-text" title="Click to rename history">')
            # SOURCE LINE 503
            __M_writer(filters.html_escape(unicode(history.get_display_name() )))
            __M_writer(u'</div>\n            \n')
            # SOURCE LINE 505
        else:
            # SOURCE LINE 506
            __M_writer(u'            <div id="history-size">')
            __M_writer(unicode(history.get_disk_size(nice_size=True)))
            __M_writer(u'</div>\n')
            pass
        # SOURCE LINE 508
        __M_writer(u'    </div>                     \n</div>\n<div style="clear: both;"></div>\n\n')
        # SOURCE LINE 512
        if history.deleted:
            # SOURCE LINE 513
            __M_writer(u'    <div class="warningmessagesmall">\n        ')
            # SOURCE LINE 514
            __M_writer(unicode(_('You are currently viewing a deleted history!')))
            __M_writer(u'\n    </div>\n    <p></p>\n')
            pass
        # SOURCE LINE 518
        __M_writer(u'\n')
        # SOURCE LINE 519
        __M_writer(u'\n')
        # SOURCE LINE 520
        __M_writer(u'\n\n')
        # SOURCE LINE 522
        if trans.get_user() is not None:
            # SOURCE LINE 523
            __M_writer(u'    <div style="margin: 0px 5px 10px 5px">\n')
            # SOURCE LINE 525
            __M_writer(u'        <div id="history-tag-area" style="display: none">\n            <b>Tags:</b>\n            ')
            # SOURCE LINE 527
            __M_writer(unicode(render_individual_tagging_element(user=trans.get_user(), tagged_item=history, elt_context="history.mako", use_toggle_link=False, input_size="20")))
            __M_writer(u'\n        </div>\n    \n')
            # SOURCE LINE 531
            __M_writer(u'        <div id="history-annotation-area" style="display: none">\n            <strong>Annotation / Notes:</strong>\n            <div id="history-annotation-container">\n            <div id="history-annotation" class="tooltip editable-text" title="Click to edit annotation">\n')
            # SOURCE LINE 535
            if annotation:
                # SOURCE LINE 536
                __M_writer(u'                    ')
                __M_writer(filters.html_escape(unicode(h.to_unicode( annotation ) )))
                __M_writer(u'\n')
                # SOURCE LINE 537
            else:
                # SOURCE LINE 538
                __M_writer(u'                    <em>Describe or add notes to history</em>\n')
                pass
            # SOURCE LINE 540
            __M_writer(u'            </div>\n            </div>\n        </div>\n        \n    </div>\n')
            pass
        # SOURCE LINE 546
        __M_writer(u'\n<div id="message-container">\n')
        # SOURCE LINE 548
        if message:
            # SOURCE LINE 549
            __M_writer(u'        ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 551
        __M_writer(u'</div>\n\n')
        # SOURCE LINE 553
        if over_quota:
            # SOURCE LINE 554
            __M_writer(u'<div id="quota-message-container">\n')
            # SOURCE LINE 555
        else:
            # SOURCE LINE 556
            __M_writer(u'<div id="quota-message-container" style="display: none;">\n')
            pass
        # SOURCE LINE 558
        __M_writer(u'    <div id="quota-message" class="errormessage">\n        You are over your disk quota.  Tool execution is on hold until your disk usage drops below your allocated quota.\n    </div>\n    <br/>\n</div>\n\n')
        # SOURCE LINE 564
        if not datasets:
            # SOURCE LINE 565
            __M_writer(u'\n    <div class="infomessagesmall" id="emptyHistoryMessage">\n\n')
            # SOURCE LINE 568
        else:    
            # SOURCE LINE 569
            __M_writer(u'\n')
            # SOURCE LINE 571
            __M_writer(u'    <div>\n')
            # SOURCE LINE 572
            for data in reversed( datasets ):
                # SOURCE LINE 573
                if data.visible or show_hidden:
                    # SOURCE LINE 574
                    __M_writer(u'            <div class="historyItemContainer" id="historyItemContainer-')
                    __M_writer(unicode(trans.app.security.encode_id(data.id)))
                    __M_writer(u'">\n                ')
                    # SOURCE LINE 575
                    __M_writer(unicode(render_dataset( data, data.hid, show_deleted_on_refresh = show_deleted, for_editing = True )))
                    __M_writer(u'\n            </div>\n')
                    pass
                pass
            # SOURCE LINE 579
            __M_writer(u'    </div>\n\n    <div class="infomessagesmall" id="emptyHistoryMessage" style="display:none;">\n')
            pass
        # SOURCE LINE 583
        __M_writer(u'        ')
        __M_writer(unicode(_("Your history is empty. Click 'Get Data' on the left pane to start")))
        __M_writer(u'\n    </div>\n\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


