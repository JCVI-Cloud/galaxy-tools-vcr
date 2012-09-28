# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1336505820.547673
_template_filename=u'templates/root/history_common.mako'
_template_uri=u'root/history_common.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['render_download_links', 'render_dataset']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        n_ = context.get('n_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        _=n_ 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['_'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n')
        # SOURCE LINE 27
        __M_writer(u'\n\n')
        # SOURCE LINE 315
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_download_links(context,data,dataset_id):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n    ')
        # SOURCE LINE 4

        from galaxy.datatypes.metadata import FileParameter
            
        
        # SOURCE LINE 6
        __M_writer(u'\n')
        # SOURCE LINE 7
        if not data.purged:
            # SOURCE LINE 9
            __M_writer(u'        ')
            meta_files = [ k for k in data.metadata.spec.keys() if isinstance( data.metadata.spec[k].param, FileParameter ) ] 
            
            __M_writer(u'\n')
            # SOURCE LINE 10
            if meta_files:
                # SOURCE LINE 11
                __M_writer(u'            <div popupmenu="dataset-')
                __M_writer(unicode(dataset_id))
                __M_writer(u'-popup">\n                <a class="action-button" href="')
                # SOURCE LINE 12
                __M_writer(unicode(h.url_for( controller='dataset', action='display', dataset_id=dataset_id, \
                    to_ext=data.ext )))
                # SOURCE LINE 13
                __M_writer(u'">Download Dataset</a>\n                <a>Additional Files</a>\n')
                # SOURCE LINE 15
                for file_type in meta_files:
                    # SOURCE LINE 16
                    __M_writer(u'                <a class="action-button" href="')
                    __M_writer(unicode(h.url_for( controller='/dataset', action='get_metadata_file', \
                    hda_id=dataset_id, metadata_name=file_type )))
                    # SOURCE LINE 17
                    __M_writer(u'">Download ')
                    __M_writer(unicode(file_type))
                    __M_writer(u'</a>\n')
                    pass
                # SOURCE LINE 19
                __M_writer(u'            </div>\n            <div style="float:left;" class="menubutton split popup" id="dataset-')
                # SOURCE LINE 20
                __M_writer(unicode(dataset_id))
                __M_writer(u'-popup">\n')
                pass
            # SOURCE LINE 22
            __M_writer(u'        <a href="')
            __M_writer(unicode(h.url_for( controller='dataset', action='display', dataset_id=dataset_id, to_ext=data.ext )))
            __M_writer(u'" title=\'')
            __M_writer(unicode(_("Download")))
            __M_writer(u'\' class="icon-button disk tooltip"></a>\n')
            # SOURCE LINE 23
            if meta_files:
                # SOURCE LINE 24
                __M_writer(u'            </div>\n')
                pass
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_dataset(context,data,hid,show_deleted_on_refresh=False,for_editing=True,display_structured=False):
    context.caller_stack._push_frame()
    try:
        def render_download_links(data,dataset_id):
            return render_render_download_links(context,data,dataset_id)
        h = context.get('h', UNDEFINED)
        app = context.get('app', UNDEFINED)
        def render_dataset(data,hid,show_deleted_on_refresh=False,for_editing=True,display_structured=False):
            return render_render_dataset(context,data,hid,show_deleted_on_refresh,for_editing,display_structured)
        request = context.get('request', UNDEFINED)
        len = context.get('len', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 30
        __M_writer(u'\n    ')
        # SOURCE LINE 31

        dataset_id = trans.security.encode_id( data.id )
        
        if data.state in ['no state','',None]:
            data_state = "queued"
        else:
            data_state = data.state
        current_user_roles = trans.get_current_user_roles()
        can_edit = not ( data.deleted or data.purged )
            
        
        # SOURCE LINE 40
        __M_writer(u'\n')
        # SOURCE LINE 41
        if not trans.user_is_admin() and not trans.app.security_agent.can_access_dataset( current_user_roles, data.dataset ):
            # SOURCE LINE 42
            __M_writer(u'        <div class="historyItemWrapper historyItem historyItem-')
            __M_writer(unicode(data_state))
            __M_writer(u' historyItem-noPermission" id="historyItem-')
            __M_writer(unicode(dataset_id))
            __M_writer(u'">\n')
            # SOURCE LINE 43
        else:
            # SOURCE LINE 44
            __M_writer(u'        <div class="historyItemWrapper historyItem historyItem-')
            __M_writer(unicode(data_state))
            __M_writer(u'" id="historyItem-')
            __M_writer(unicode(dataset_id))
            __M_writer(u'">\n')
            pass
        # SOURCE LINE 46
        __M_writer(u'        \n')
        # SOURCE LINE 47
        if data.deleted or data.purged or data.dataset.purged:
            # SOURCE LINE 48
            __M_writer(u'        <div class="warningmessagesmall"><strong>\n')
            # SOURCE LINE 49
            if data.dataset.purged or data.purged:
                # SOURCE LINE 50
                __M_writer(u'                This dataset has been deleted and removed from disk.\n')
                # SOURCE LINE 51
            else:
                # SOURCE LINE 52
                __M_writer(u'                This dataset has been deleted. \n')
                # SOURCE LINE 53
                if for_editing:
                    # SOURCE LINE 54
                    __M_writer(u'                    Click <a href="')
                    __M_writer(unicode(h.url_for( controller='dataset', action='undelete', dataset_id=dataset_id )))
                    __M_writer(u'" class="historyItemUndelete" id="historyItemUndeleter-')
                    __M_writer(unicode(dataset_id))
                    __M_writer(u'" target="galaxy_history">here</a> to undelete\n')
                    # SOURCE LINE 55
                    if trans.app.config.allow_user_dataset_purge:
                        # SOURCE LINE 56
                        __M_writer(u'                        or <a href="')
                        __M_writer(unicode(h.url_for( controller='dataset', action='purge', dataset_id=dataset_id )))
                        __M_writer(u'" class="historyItemPurge" id="historyItemPurger-')
                        __M_writer(unicode(dataset_id))
                        __M_writer(u'" target="galaxy_history">here</a> to immediately remove it from disk.\n')
                        # SOURCE LINE 57
                    else:
                        # SOURCE LINE 58
                        __M_writer(u'                        it.\n')
                        pass
                    pass
                pass
            # SOURCE LINE 62
            __M_writer(u'        </strong></div>\n')
            pass
        # SOURCE LINE 64
        __M_writer(u'\n')
        # SOURCE LINE 65
        if data.visible is False:
            # SOURCE LINE 66
            __M_writer(u'        <div class="warningmessagesmall">\n            <strong>This dataset has been hidden. Click <a href="')
            # SOURCE LINE 67
            __M_writer(unicode(h.url_for( controller='dataset', action='unhide', dataset_id=dataset_id )))
            __M_writer(u'" class="historyItemUnhide" id="historyItemUnhider-')
            __M_writer(unicode(dataset_id))
            __M_writer(u'" target="galaxy_history">here</a> to unhide.</strong>\n        </div>\n')
            pass
        # SOURCE LINE 70
        __M_writer(u'\n')
        # SOURCE LINE 72
        __M_writer(u'    <div style="overflow: hidden;" class="historyItemTitleBar">     \n        <div class="historyItemButtons">\n')
        # SOURCE LINE 74
        if data_state == "upload":
            # SOURCE LINE 78
            __M_writer(u"                <span title='")
            __M_writer(unicode(_("Display Data")))
            __M_writer(u"' class='icon-button display_disabled tooltip'></span>\n")
            # SOURCE LINE 79
            if for_editing:
                # SOURCE LINE 80
                __M_writer(u"                    <span title='Edit Attributes' class='icon-button edit_disabled tooltip'></span>\n")
                pass
            # SOURCE LINE 82
        else:
            # SOURCE LINE 83
            __M_writer(u'                ')
 
            if for_editing:
                display_url = h.url_for( controller='dataset', action='display', dataset_id=dataset_id, preview=True, filename='' )
            else:
                # Get URL for display only.
                if data.history.user and data.history.user.username:
                    display_url = h.url_for( controller='dataset', action='display_by_username_and_slug',
                                             username=data.history.user.username, slug=dataset_id, filename='' )
                else:
                    # HACK: revert to for_editing display URL when there is no user/username. This should only happen when
                    # there's no user/username because dataset is being displayed by history/view after error reported.
                    # There are no security concerns here because both dataset/display and dataset/display_by_username_and_slug
                    # check user permissions (to the same degree) before displaying.
                    display_url = h.url_for( controller='dataset', action='display', dataset_id=dataset_id, preview=True, filename='' )
                            
            
            # SOURCE LINE 97
            __M_writer(u'\n')
            # SOURCE LINE 98
            if data.purged:
                # SOURCE LINE 99
                __M_writer(u'                    <span class="icon-button display_disabled tooltip" title="Cannot display datasets removed from disk"></span>\n')
                # SOURCE LINE 100
            else:
                # SOURCE LINE 101
                __M_writer(u'                    <a class="icon-button display tooltip" dataset_id="')
                __M_writer(unicode(dataset_id))
                __M_writer(u'" title=\'')
                __M_writer(unicode(_("Display data in browser")))
                __M_writer(u'\' href="')
                __M_writer(unicode(display_url))
                __M_writer(u'"\n')
                # SOURCE LINE 102
                if for_editing:
                    # SOURCE LINE 103
                    __M_writer(u'                        target="galaxy_main"\n')
                    pass
                # SOURCE LINE 105
                __M_writer(u'                    ></a>\n')
                pass
            # SOURCE LINE 107
            if for_editing:
                # SOURCE LINE 108
                if data.deleted and not data.purged:
                    # SOURCE LINE 109
                    __M_writer(u'                        <span title="Undelete dataset to edit attributes" class="icon-button edit_disabled tooltip"></span>\n')
                    # SOURCE LINE 110
                elif data.purged:
                    # SOURCE LINE 111
                    __M_writer(u'                        <span title="Cannot edit attributes of datasets removed from disk" class="icon-button edit_disabled tooltip"></span>\n')
                    # SOURCE LINE 112
                else:
                    # SOURCE LINE 113
                    __M_writer(u'                        <a class="icon-button edit tooltip" title=\'')
                    __M_writer(unicode(_("Edit attributes")))
                    __M_writer(u'\' href="')
                    __M_writer(unicode(h.url_for( controller='dataset', action='edit', dataset_id=dataset_id )))
                    __M_writer(u'" target="galaxy_main"></a>\n')
                    pass
                pass
            pass
        # SOURCE LINE 117
        if for_editing:
            # SOURCE LINE 118
            if can_edit:
                # SOURCE LINE 119
                __M_writer(u'                    <a class="icon-button delete tooltip" title=\'')
                __M_writer(unicode(_("Delete")))
                __M_writer(u'\' href="')
                __M_writer(unicode(h.url_for( controller='dataset', action='delete', dataset_id=dataset_id, show_deleted_on_refresh=show_deleted_on_refresh )))
                __M_writer(u'" id="historyItemDeleter-')
                __M_writer(unicode(dataset_id))
                __M_writer(u'"></a>\n')
                # SOURCE LINE 120
            else:
                # SOURCE LINE 121
                __M_writer(u'                    <span title="Dataset is already deleted" class="icon-button delete_disabled tooltip"></span>\n')
                pass
            pass
        # SOURCE LINE 124
        __M_writer(u'        </div>\n        <span class="state-icon"></span>\n        <span class="historyItemTitle">')
        # SOURCE LINE 126
        __M_writer(unicode(hid))
        __M_writer(u': ')
        __M_writer(unicode(data.display_name()))
        __M_writer(u'</span>\n    </div>\n        \n')
        # SOURCE LINE 130
        __M_writer(u'    \n    <div id="info')
        # SOURCE LINE 131
        __M_writer(unicode(data.id))
        __M_writer(u'" class="historyItemBody">\n')
        # SOURCE LINE 132
        if not trans.user_is_admin() and not trans.app.security_agent.can_access_dataset( current_user_roles, data.dataset ):
            # SOURCE LINE 133
            __M_writer(u'            <div>You do not have permission to view this dataset.</div>\n')
            # SOURCE LINE 134
        elif data_state == "upload":
            # SOURCE LINE 135
            __M_writer(u'            <div>Dataset is uploading</div>\n')
            # SOURCE LINE 136
        elif data_state == "queued":
            # SOURCE LINE 137
            __M_writer(u'            <div>')
            __M_writer(unicode(_('Job is waiting to run')))
            __M_writer(u'</div>\n            <div>\n                <a href="')
            # SOURCE LINE 139
            __M_writer(unicode(h.url_for( controller='dataset', action='show_params', dataset_id=dataset_id )))
            __M_writer(u'" target="galaxy_main" title=\'')
            __M_writer(unicode(_("View Details")))
            __M_writer(u'\' class="icon-button information tooltip"></a>\n')
            # SOURCE LINE 140
            if for_editing:
                # SOURCE LINE 141
                __M_writer(u'                    <a href="')
                __M_writer(unicode(h.url_for( controller='tool_runner', action='rerun', id=data.id )))
                __M_writer(u'" target="galaxy_main" title=\'')
                __M_writer(unicode(_("Run this job again")))
                __M_writer(u'\' class="icon-button arrow-circle tooltip"></a>\n')
                pass
            # SOURCE LINE 143
            __M_writer(u'            </div>\n')
            # SOURCE LINE 144
        elif data_state == "running":
            # SOURCE LINE 145
            __M_writer(u'            <div>')
            __M_writer(unicode(_('Job is currently running')))
            __M_writer(u'</div>\n            <div>\n                <a href="')
            # SOURCE LINE 147
            __M_writer(unicode(h.url_for( controller='dataset', action='show_params', dataset_id=dataset_id )))
            __M_writer(u'" target="galaxy_main" title=\'')
            __M_writer(unicode(_("View Details")))
            __M_writer(u'\' class="icon-button information tooltip"></a>\n')
            # SOURCE LINE 148
            if for_editing:
                # SOURCE LINE 149
                __M_writer(u'                    <a href="')
                __M_writer(unicode(h.url_for( controller='tool_runner', action='rerun', id=data.id )))
                __M_writer(u'" target="galaxy_main" title=\'')
                __M_writer(unicode(_("Run this job again")))
                __M_writer(u'\' class="icon-button arrow-circle tooltip"></a>\n')
                pass
            # SOURCE LINE 151
            __M_writer(u'            </div>\n')
            # SOURCE LINE 152
        elif data_state == "error":
            # SOURCE LINE 153
            if not data.purged:
                # SOURCE LINE 154
                __M_writer(u'                <div>')
                __M_writer(unicode(data.get_size( nice_size=True )))
                __M_writer(u'</div>\n')
                pass
            # SOURCE LINE 156
            __M_writer(u'            <div>\n                An error occurred running this job: <i>')
            # SOURCE LINE 157
            __M_writer(unicode(data.display_info().strip()))
            __M_writer(u'</i>\n            </div>\n            <div>\n')
            # SOURCE LINE 160
            if for_editing:
                # SOURCE LINE 161
                __M_writer(u'                    <a href="')
                __M_writer(unicode(h.url_for( controller='dataset', action='errors', id=data.id )))
                __M_writer(u'" target="galaxy_main" title="View or report this error" class="icon-button bug tooltip"></a>\n')
                pass
            # SOURCE LINE 163
            if data.has_data():
                # SOURCE LINE 164
                __M_writer(u'                    ')
                __M_writer(unicode(render_download_links( data, dataset_id )))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 166
            __M_writer(u'                <a href="')
            __M_writer(unicode(h.url_for( controller='dataset', action='show_params', dataset_id=dataset_id )))
            __M_writer(u'" target="galaxy_main" title=\'')
            __M_writer(unicode(_("View Details")))
            __M_writer(u'\' class="icon-button information tooltip"></a>\n')
            # SOURCE LINE 167
            if for_editing:
                # SOURCE LINE 168
                __M_writer(u'                    <a href="')
                __M_writer(unicode(h.url_for( controller='tool_runner', action='rerun', id=data.id )))
                __M_writer(u'" target="galaxy_main" title=\'')
                __M_writer(unicode(_("Run this job again")))
                __M_writer(u'\' class="icon-button arrow-circle tooltip"></a>\n')
                pass
            # SOURCE LINE 170
            __M_writer(u'            </div>\n')
            # SOURCE LINE 171
        elif data_state == "discarded":
            # SOURCE LINE 172
            __M_writer(u'            <div>\n                The job creating this dataset was cancelled before completion.\n            </div>\n            <div>\n                <a href="')
            # SOURCE LINE 176
            __M_writer(unicode(h.url_for( controller='dataset', action='show_params', dataset_id=dataset_id )))
            __M_writer(u'" target="galaxy_main" title=\'')
            __M_writer(unicode(_("View Details")))
            __M_writer(u'\' class="icon-button information tooltip"></a>\n')
            # SOURCE LINE 177
            if for_editing:
                # SOURCE LINE 178
                __M_writer(u'                    <a href="')
                __M_writer(unicode(h.url_for( controller='tool_runner', action='rerun', id=data.id )))
                __M_writer(u'" target="galaxy_main" title=\'')
                __M_writer(unicode(_("Run this job again")))
                __M_writer(u'\' class="icon-button arrow-circle tooltip"></a>\n')
                pass
            # SOURCE LINE 180
            __M_writer(u'            </div>\n')
            # SOURCE LINE 181
        elif data_state == 'setting_metadata':
            # SOURCE LINE 182
            __M_writer(u'            <div>')
            __M_writer(unicode(_('Metadata is being Auto-Detected.')))
            __M_writer(u'</div>\n')
            # SOURCE LINE 183
        elif data_state == "empty":
            # SOURCE LINE 184
            __M_writer(u'            <div>')
            __M_writer(unicode(_('No data: ')))
            __M_writer(u'<i>')
            __M_writer(unicode(data.display_info()))
            __M_writer(u'</i></div>\n            <div>\n                <a href="')
            # SOURCE LINE 186
            __M_writer(unicode(h.url_for( controller='dataset', action='show_params', dataset_id=dataset_id )))
            __M_writer(u'" target="galaxy_main" title=\'')
            __M_writer(unicode(_("View Details")))
            __M_writer(u'\' class="icon-button information tooltip"></a>\n')
            # SOURCE LINE 187
            if for_editing:
                # SOURCE LINE 188
                __M_writer(u'                    <a href="')
                __M_writer(unicode(h.url_for( controller='tool_runner', action='rerun', id=data.id )))
                __M_writer(u'" target="galaxy_main" title=\'')
                __M_writer(unicode(_("Run this job again")))
                __M_writer(u'\' class="icon-button arrow-circle tooltip"></a>\n')
                pass
            # SOURCE LINE 190
            __M_writer(u'            </div>\n')
            # SOURCE LINE 191
        elif data_state in [ "ok", "failed_metadata" ]:
            # SOURCE LINE 192
            if data_state == "failed_metadata":
                # SOURCE LINE 193
                __M_writer(u'                <div class="warningmessagesmall" style="margin: 4px 0 4px 0">\n                    An error occurred setting the metadata for this dataset.\n')
                # SOURCE LINE 195
                if can_edit:
                    # SOURCE LINE 196
                    __M_writer(u'                        You may be able to <a href="')
                    __M_writer(unicode(h.url_for( controller='dataset', action='edit', dataset_id=dataset_id )))
                    __M_writer(u'" target="galaxy_main">set it manually or retry auto-detection</a>.\n')
                    pass
                # SOURCE LINE 198
                __M_writer(u'                </div>\n')
                pass
            # SOURCE LINE 200
            __M_writer(u'            <div>\n                ')
            # SOURCE LINE 201
            __M_writer(unicode(data.blurb))
            __M_writer(u'<br />\n                ')
            # SOURCE LINE 202
            __M_writer(unicode(_("format: ")))
            __M_writer(u' <span class="')
            __M_writer(unicode(data.ext))
            __M_writer(u'">')
            __M_writer(unicode(data.ext))
            __M_writer(u'</span>, \n                ')
            # SOURCE LINE 203
            __M_writer(unicode(_("database: ")))
            __M_writer(u'\n')
            # SOURCE LINE 204
            if data.dbkey == '?' and can_edit:
                # SOURCE LINE 205
                __M_writer(u'                    <a href="')
                __M_writer(unicode(h.url_for( controller='dataset', action='edit', dataset_id=dataset_id )))
                __M_writer(u'" target="galaxy_main">')
                __M_writer(unicode(_(data.dbkey)))
                __M_writer(u'</a>\n')
                # SOURCE LINE 206
            else:
                # SOURCE LINE 207
                __M_writer(u'                    <span class="')
                __M_writer(unicode(data.dbkey))
                __M_writer(u'">')
                __M_writer(unicode(_(data.dbkey)))
                __M_writer(u'</span>\n')
                pass
            # SOURCE LINE 209
            __M_writer(u'            </div>\n')
            # SOURCE LINE 210
            if data.display_info():
                # SOURCE LINE 211
                __M_writer(u'                <div class="info">')
                __M_writer(unicode(_('Info: ')))
                __M_writer(unicode(data.display_info()))
                __M_writer(u'</div>\n')
                pass
            # SOURCE LINE 213
            __M_writer(u'            <div>\n')
            # SOURCE LINE 214
            if data.has_data():
                # SOURCE LINE 215
                __M_writer(u'                    ')
                __M_writer(unicode(render_download_links( data, dataset_id )))
                __M_writer(u'\n                    \n                    <a href="')
                # SOURCE LINE 217
                __M_writer(unicode(h.url_for( controller='dataset', action='show_params', dataset_id=dataset_id )))
                __M_writer(u'" target="galaxy_main" title=\'')
                __M_writer(unicode(_("View Details")))
                __M_writer(u'\' class="icon-button information tooltip"></a>\n                    \n')
                # SOURCE LINE 219
                if for_editing:
                    # SOURCE LINE 220
                    __M_writer(u'                        <a href="')
                    __M_writer(unicode(h.url_for( controller='tool_runner', action='rerun', id=data.id )))
                    __M_writer(u'" target="galaxy_main" title=\'')
                    __M_writer(unicode(_("Run this job again")))
                    __M_writer(u'\' class="icon-button arrow-circle tooltip"></a>\n')
                    # SOURCE LINE 221
                    if app.config.get_bool( 'enable_tracks', False ) and data.ext in app.datatypes_registry.get_available_tracks():
                        # SOURCE LINE 222
                        __M_writer(u'                            ')

                        if data.dbkey != '?':
                            data_url = h.url_for( controller='tracks', action='list_tracks', dbkey=data.dbkey )
                            data_url = data_url.replace( 'dbkey', 'f-dbkey' )
                        else:
                            data_url = h.url_for( controller='tracks', action='list_tracks' )
                        
                        
                        # SOURCE LINE 228
                        __M_writer(u'\n                            <a href="javascript:void(0)" data-url="')
                        # SOURCE LINE 229
                        __M_writer(unicode(data_url))
                        __M_writer(u'" class="icon-button chart_curve tooltip trackster-add"\n                                action-url="')
                        # SOURCE LINE 230
                        __M_writer(unicode(h.url_for( controller='tracks', action='browser', dataset_id=dataset_id)))
                        __M_writer(u'"\n                                new-url="')
                        # SOURCE LINE 231
                        __M_writer(unicode(h.url_for( controller='tracks', action='index', dataset_id=dataset_id, default_dbkey=data.dbkey)))
                        __M_writer(u'" title="View in Trackster"></a>\n')
                        pass
                    # SOURCE LINE 233
                    if trans.user:
                        # SOURCE LINE 234
                        if not display_structured:
                            # SOURCE LINE 235
                            __M_writer(u'                                <div style="float: right">\n                                    <a href="')
                            # SOURCE LINE 236
                            __M_writer(unicode(h.url_for( controller='tag', action='retag', item_class=data.__class__.__name__, item_id=dataset_id )))
                            __M_writer(u'" target="galaxy_main" title="Edit dataset tags" class="icon-button tags tooltip"></a>\n                                    <a href="')
                            # SOURCE LINE 237
                            __M_writer(unicode(h.url_for( controller='dataset', action='annotate', id=dataset_id )))
                            __M_writer(u'" target="galaxy_main" title="Edit dataset annotation" class="icon-button annotate tooltip"></a>\n                                </div>\n')
                            pass
                        # SOURCE LINE 240
                        __M_writer(u'                            <div style="clear: both"></div>\n                            <div class="tag-area" style="display: none">\n                                <strong>Tags:</strong>\n                                <div class="tag-elt"></div>\n                            </div>\n                            <div id="')
                        # SOURCE LINE 245
                        __M_writer(unicode(dataset_id))
                        __M_writer(u'-annotation-area" class="annotation-area" style="display: none">\n                                <strong>Annotation:</strong>\n                                <div id="')
                        # SOURCE LINE 247
                        __M_writer(unicode(dataset_id))
                        __M_writer(u'-annotation-elt" style="margin: 1px 0px 1px 0px" class="annotation-elt tooltip editable-text" title="Edit dataset annotation"></div>\n                            </div>\n                            \n')
                        pass
                    # SOURCE LINE 251
                else:
                    # SOURCE LINE 254
                    __M_writer(u'                        <div style="clear: both"></div>\n')
                    pass
                # SOURCE LINE 256
                __M_writer(u'                    <div style="clear: both"></div>\n')
                # SOURCE LINE 257
                for display_app in data.datatype.get_display_types():
                    # SOURCE LINE 258
                    __M_writer(u'                        ')
                    target_frame, display_links = data.datatype.get_display_links( data, display_app, app, request.base ) 
                    
                    __M_writer(u'\n')
                    # SOURCE LINE 259
                    if len( display_links ) > 0:
                        # SOURCE LINE 260
                        __M_writer(u'                            ')
                        __M_writer(unicode(data.datatype.get_display_label(display_app)))
                        __M_writer(u'\n')
                        # SOURCE LINE 261
                        for display_name, display_link in display_links:
                            # SOURCE LINE 262
                            __M_writer(u'                                <a target="')
                            __M_writer(unicode(target_frame))
                            __M_writer(u'" href="')
                            __M_writer(unicode(display_link))
                            __M_writer(u'">')
                            __M_writer(unicode(_(display_name)))
                            __M_writer(u'</a> \n')
                            pass
                        # SOURCE LINE 264
                        __M_writer(u'                            <br />\n')
                        pass
                    pass
                # SOURCE LINE 267
                for display_app in data.get_display_applications( trans ).itervalues():
                    # SOURCE LINE 268
                    __M_writer(u'                        ')
                    __M_writer(unicode(display_app.name))
                    __M_writer(u' \n')
                    # SOURCE LINE 269
                    for link_app in display_app.links.itervalues():
                        # SOURCE LINE 270
                        __M_writer(u'                            <a target="')
                        __M_writer(unicode(link_app.url.get( 'target_frame', '_blank' )))
                        __M_writer(u'" href="')
                        __M_writer(unicode(link_app.get_display_url( data, trans )))
                        __M_writer(u'">')
                        __M_writer(unicode(_(link_app.name)))
                        __M_writer(u'</a> \n')
                        pass
                    # SOURCE LINE 272
                    __M_writer(u'                        <br />\n')
                    pass
                # SOURCE LINE 274
            elif for_editing:
                # SOURCE LINE 275
                __M_writer(u'                    <a href="')
                __M_writer(unicode(h.url_for( controller='dataset', action='show_params', dataset_id=dataset_id )))
                __M_writer(u'" target="galaxy_main" title=\'')
                __M_writer(unicode(_("View Details")))
                __M_writer(u'\' class="icon-button information tooltip"></a>\n                    <a href="')
                # SOURCE LINE 276
                __M_writer(unicode(h.url_for( controller='tool_runner', action='rerun', id=data.id )))
                __M_writer(u'" target="galaxy_main" title=\'')
                __M_writer(unicode(_("Run this job again")))
                __M_writer(u'\' class="icon-button arrow-circle tooltip"></a>\n')
                pass
            # SOURCE LINE 278
            __M_writer(u'    \n                </div>\n')
            # SOURCE LINE 280
            if data.peek != "no peek":
                # SOURCE LINE 281
                __M_writer(u'                    <div><pre id="peek')
                __M_writer(unicode(data.id))
                __M_writer(u'" class="peek">')
                __M_writer(unicode(_(h.to_unicode(data.display_peek()))))
                __M_writer(u'</pre></div>\n')
                pass
            # SOURCE LINE 283
        else:
            # SOURCE LINE 284
            __M_writer(u'            <div>')
            __M_writer(unicode(_('Error: unknown dataset state "%s".') % data_state))
            __M_writer(u'</div>\n')
            pass
        # SOURCE LINE 286
        __M_writer(u'           \n')
        # SOURCE LINE 288
        __M_writer(u'                          \n')
        # SOURCE LINE 289
        if len( data.children ) > 0:
            # SOURCE LINE 292
            __M_writer(u'            ')

            children = []
            for child in data.children:
                if child.visible:
                    children.append( child )
            
            
            # SOURCE LINE 297
            __M_writer(u'\n')
            # SOURCE LINE 298
            if len( children ) > 0:
                # SOURCE LINE 299
                __M_writer(u'                <div>\n                    There are ')
                # SOURCE LINE 300
                __M_writer(unicode(len( children )))
                __M_writer(u' secondary datasets.\n')
                # SOURCE LINE 301
                for idx, child in enumerate(children):
                    # SOURCE LINE 302
                    __M_writer(u'                        ')
                    __M_writer(unicode(render_dataset( child, idx + 1, show_deleted_on_refresh = show_deleted_on_refresh )))
                    __M_writer(u'\n')
                    pass
                # SOURCE LINE 304
                __M_writer(u'                </div>\n')
                pass
            pass
        # SOURCE LINE 307
        __M_writer(u'\n    <div style="clear: both;"></div>\n\n    </div>\n        \n        \n    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


