from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1292428814.065079
_template_filename=u'templates/display_base.mako'
_template_uri=u'/display_base.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding=None
_exports = ['body', 'render_content', 'title', 'center_panel', 'right_panel', 'stylesheets', 'render_item', 'init', 'render_item_header', 'render_item_links', 'javascripts']


# SOURCE LINE 1

def inherit( context ):
    if context.get('no_panels'):
        return '/base.mako'
    else:
        return '/webapps/galaxy/base_panels.mako'

from galaxy.model import History, StoredWorkflow, Page
from galaxy.web.framework.helpers import iff


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 13
    ns = runtime.Namespace('__anon_0x66f1a90', context._clean_inheritance_tokens(), templateuri=u'/display_common.mako', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, '__anon_0x66f1a90')] = ns

    # SOURCE LINE 12
    ns = runtime.Namespace('__anon_0x66f1850', context._clean_inheritance_tokens(), templateuri=u'/tagging_common.mako', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, '__anon_0x66f1850')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, (inherit( context )), _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x66f1a90')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x66f1850')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element'])
        __M_writer = context.writer()
        # SOURCE LINE 10
        __M_writer(u'\n')
        # SOURCE LINE 11
        __M_writer(u'\n')
        # SOURCE LINE 12
        __M_writer(u'\n')
        # SOURCE LINE 13
        __M_writer(u'\n\n')
        # SOURCE LINE 18
        __M_writer(u'\n')
        # SOURCE LINE 21
        __M_writer(u'\n\n')
        # SOURCE LINE 31
        __M_writer(u'\n\n')
        # SOURCE LINE 110
        __M_writer(u'\n\n')
        # SOURCE LINE 150
        __M_writer(u'\n\n')
        # SOURCE LINE 154
        __M_writer(u'\n\n')
        # SOURCE LINE 162
        __M_writer(u'\n\n')
        # SOURCE LINE 166
        __M_writer(u'\n\n')
        # SOURCE LINE 171
        __M_writer(u'\n\n')
        # SOURCE LINE 176
        __M_writer(u'\n\n\n')
        # SOURCE LINE 226
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x66f1a90')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x66f1850')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 169
        __M_writer(u'\n\t')
        # SOURCE LINE 170
        __M_writer(unicode(self.render_content()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_content(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x66f1a90')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x66f1850')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element'])
        get_item_name = _import_ns.get('get_item_name', context.get('get_item_name', UNDEFINED))
        get_item_plural = _import_ns.get('get_item_plural', context.get('get_item_plural', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        item = _import_ns.get('item', context.get('item', UNDEFINED))
        get_class_display_name = _import_ns.get('get_class_display_name', context.get('get_class_display_name', UNDEFINED))
        get_controller_name = _import_ns.get('get_controller_name', context.get('get_controller_name', UNDEFINED))
        item_data = _import_ns.get('item_data', context.get('item_data', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 182
        __M_writer(u'\n    \n')
        # SOURCE LINE 185
        __M_writer(u'    ')

        ##TODO: is there a better way to create this URL? Can't use 'f-username' as a key b/c it's not a valid identifier.
        controller_name = get_controller_name( item )
        item_plural = get_item_plural( item )
        href_to_all_items = h.url_for( controller='/' + controller_name, action='list_published')
        href_to_user_items = h.url_for( controller='/' + controller_name, action='list_published', xxx=item.user.username)
        href_to_user_items = href_to_user_items.replace( 'xxx', 'f-username')
            
        
        # SOURCE LINE 192
        __M_writer(u'\n    \n    <div class="unified-panel-header" unselectable="on">\n\t\t<div class="unified-panel-header-inner">\n')
        # SOURCE LINE 196
        if item.published:    
            # SOURCE LINE 197
            __M_writer(u'\t                <a href="')
            __M_writer(unicode(href_to_all_items))
            __M_writer(u'">Published ')
            __M_writer(unicode(item_plural))
            __M_writer(u'</a> | \n\t                <a href="')
            # SOURCE LINE 198
            __M_writer(unicode(href_to_user_items))
            __M_writer(u'">')
            __M_writer(unicode(item.user.username))
            __M_writer(u'</a>\n')
            # SOURCE LINE 199
        elif item.importable:
            # SOURCE LINE 200
            __M_writer(u'\t\t\t\tAccessible ')
            __M_writer(unicode(get_class_display_name( item.__class__ )))
            __M_writer(u'\n')
            # SOURCE LINE 201
        elif item.users_shared_with:
            # SOURCE LINE 202
            __M_writer(u'\t\t\t\tShared ')
            __M_writer(unicode(get_class_display_name( item.__class__ )))
            __M_writer(u'\n')
            # SOURCE LINE 203
        else:
            # SOURCE LINE 204
            __M_writer(u'\t\t\t\tPrivate ')
            __M_writer(unicode(get_class_display_name( item.__class__ )))
            __M_writer(u'\n')
        # SOURCE LINE 206
        __M_writer(u'\t\t\t| ')
        __M_writer(unicode(get_item_name( item )))
        __M_writer(u'\n\t    </div>\n    </div>\n    \n    <div class="unified-panel-body">\n        <div style="overflow: auto; height: 100%;">        \n            <div class="page-body">\n                <div style="float: right">\n                    ')
        # SOURCE LINE 214
        __M_writer(unicode(self.render_item_links( item )))
        __M_writer(u'\n                </div>\n                <div>\n                    ')
        # SOURCE LINE 217
        __M_writer(unicode(self.render_item_header( item )))
        __M_writer(u'\n                </div>\n                \n                ')
        # SOURCE LINE 220
        __M_writer(unicode(self.render_item( item, item_data )))
        __M_writer(u'\n            </div>\n        \n\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x66f1a90')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x66f1850')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element'])
        item = _import_ns.get('item', context.get('item', UNDEFINED))
        get_class_display_name = _import_ns.get('get_class_display_name', context.get('get_class_display_name', UNDEFINED))
        get_item_name = _import_ns.get('get_item_name', context.get('get_item_name', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 19
        __M_writer(u'\n    Galaxy | ')
        # SOURCE LINE 20
        __M_writer(unicode(iff( item.published, "Published ", iff( item.importable , "Accessible ", iff( item.users_shared_with, "Shared ", "Private " ) ) ) + get_class_display_name( item.__class__ )))
        __M_writer(u' | ')
        __M_writer(filters.html_escape(unicode(get_item_name( item ) )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x66f1a90')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x66f1850')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 174
        __M_writer(u'\n\t')
        # SOURCE LINE 175
        __M_writer(unicode(self.render_content()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_panel(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x66f1a90')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x66f1850')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element'])
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        get_item_plural = _import_ns.get('get_item_plural', context.get('get_item_plural', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        render_community_tagging_element = _import_ns.get('render_community_tagging_element', context.get('render_community_tagging_element', UNDEFINED))
        num_ratings = _import_ns.get('num_ratings', context.get('num_ratings', UNDEFINED))
        item = _import_ns.get('item', context.get('item', UNDEFINED))
        get_class_display_name = _import_ns.get('get_class_display_name', context.get('get_class_display_name', UNDEFINED))
        user_item_rating = _import_ns.get('user_item_rating', context.get('user_item_rating', UNDEFINED))
        get_controller_name = _import_ns.get('get_controller_name', context.get('get_controller_name', UNDEFINED))
        render_individual_tagging_element = _import_ns.get('render_individual_tagging_element', context.get('render_individual_tagging_element', UNDEFINED))
        ave_item_rating = _import_ns.get('ave_item_rating', context.get('ave_item_rating', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 228
        __M_writer(u'\n\n    ')
        # SOURCE LINE 230

        ## FIXME: duplicated from above for now
        controller_name = get_controller_name( item )
        item_plural = get_item_plural( item )
        href_to_all_items = h.url_for( controller='/' + controller_name, action='list_published')
        href_to_user_items = h.url_for( controller='/' + controller_name, action='list_published', xxx=item.user.username)
        href_to_user_items = href_to_user_items.replace( 'xxx', 'f-username')
            
        
        # SOURCE LINE 237
        __M_writer(u'\n\n    <div class="unified-panel-header" unselectable="on">\n        <div class="unified-panel-header-inner">\n            About this ')
        # SOURCE LINE 241
        __M_writer(unicode(get_class_display_name( item.__class__ )))
        __M_writer(u'\n        </div>\n    </div>\n    \n    <div class="unified-panel-body">\n        <div style="overflow: auto; height: 100%;">\n            <div style="padding: 10px;">\n            \n                <div style="float: right;"><img src="http://www.gravatar.com/avatar/')
        # SOURCE LINE 249
        __M_writer(unicode(h.md5(item.user.email)))
        __M_writer(u'?d=identicon"></div>\n            \n                <h4>Author</h4>\n                \n                <p>')
        # SOURCE LINE 253
        __M_writer(filters.html_escape(unicode(item.user.username )))
        __M_writer(u'</p>\n                \n')
        # SOURCE LINE 256
        __M_writer(u'                <h4>Related ')
        __M_writer(unicode(item_plural))
        __M_writer(u'</h4>\n                <p>\n                    <a href="')
        # SOURCE LINE 258
        __M_writer(unicode(href_to_all_items))
        __M_writer(u'">All published ')
        __M_writer(unicode(item_plural.lower()))
        __M_writer(u'</a><br>\n                    <a href="')
        # SOURCE LINE 259
        __M_writer(unicode(href_to_user_items))
        __M_writer(u'">Published ')
        __M_writer(unicode(item_plural.lower()))
        __M_writer(u' by ')
        __M_writer(filters.html_escape(unicode(item.user.username )))
        __M_writer(u'</a>\n                \n')
        # SOURCE LINE 262
        __M_writer(u'                <h4>Rating</h4>\n\n                ')
        # SOURCE LINE 264

        label = "ratings"
        if num_ratings == 1:
            label = "rating"
                        
        
        # SOURCE LINE 268
        __M_writer(u'\n                <div style="padding-bottom: 0.75em; float: left">\n                    Community<br>\n                    <span style="font-size:80%">\n                        (<span id="num_ratings">')
        # SOURCE LINE 272
        __M_writer(unicode(num_ratings))
        __M_writer(u'</span> ')
        __M_writer(unicode(label))
        __M_writer(u', \n                         <span id="ave_rating">')
        # SOURCE LINE 273
        __M_writer(unicode("%.1f" % ave_item_rating))
        __M_writer(u'</span> average)\n                    <span>\n                </div>\n                <div style="float: right">\n                    <input name="star1" type="radio" class="community_rating_star star" disabled="disabled" value="1"\n')
        # SOURCE LINE 278
        if ave_item_rating > 0 and ave_item_rating <= 1.5:
            # SOURCE LINE 279
            __M_writer(u'                        checked="checked"\n')
        # SOURCE LINE 281
        __M_writer(u'                    \n                    />\n                    <input name="star1" type="radio" class="community_rating_star star" disabled="disabled" value="2"\n')
        # SOURCE LINE 284
        if ave_item_rating > 1.5 and ave_item_rating <= 2.5:
            # SOURCE LINE 285
            __M_writer(u'                        checked="checked"\n')
        # SOURCE LINE 287
        __M_writer(u'                    />\n                    <input name="star1" type="radio" class="community_rating_star star" disabled="disabled" value="3"\n')
        # SOURCE LINE 289
        if ave_item_rating > 2.5 and ave_item_rating <= 3.5:
            # SOURCE LINE 290
            __M_writer(u'                        checked="checked"\n')
        # SOURCE LINE 292
        __M_writer(u'                    />\n                    <input name="star1" type="radio" class="community_rating_star star" disabled="disabled" value="4"\n')
        # SOURCE LINE 294
        if ave_item_rating > 3.5 and ave_item_rating <= 4.5:
            # SOURCE LINE 295
            __M_writer(u'                        checked="checked"\n')
        # SOURCE LINE 297
        __M_writer(u'                    />\n                    <input name="star1" type="radio" class="community_rating_star star" disabled="disabled" value="5"\n')
        # SOURCE LINE 299
        if ave_item_rating > 4.5:
            # SOURCE LINE 300
            __M_writer(u'                        checked="checked"\n')
        # SOURCE LINE 302
        __M_writer(u'                    />\n                </div>\n                <div style="clear: both;"></div>\n')
        # SOURCE LINE 305
        if trans.get_user():
            # SOURCE LINE 306
            __M_writer(u'                    <div style="float: left">\n                        Yours<br><span id="rating_feedback" style="font-size:80%; display: none">(thanks!)</span>\n                    </div>\n                    <div style="float: right">\n                        <input name="star2" type="radio" class="user_rating_star" value="1"\n')
            # SOURCE LINE 311
            if user_item_rating == 1:
                # SOURCE LINE 312
                __M_writer(u'                            checked="checked"\n')
            # SOURCE LINE 314
            __M_writer(u'                        />\n                        <input name="star2" type="radio" class="user_rating_star" value="2"\n')
            # SOURCE LINE 316
            if user_item_rating == 2:
                # SOURCE LINE 317
                __M_writer(u'                            checked="checked"\n')
            # SOURCE LINE 319
            __M_writer(u'                        />\n                        <input name="star2" type="radio" class="user_rating_star" value="3"\n')
            # SOURCE LINE 321
            if user_item_rating == 3:
                # SOURCE LINE 322
                __M_writer(u'                            checked="checked"\n')
            # SOURCE LINE 324
            __M_writer(u'                        />\n                        <input name="star2" type="radio" class="user_rating_star" value="4"\n')
            # SOURCE LINE 326
            if user_item_rating == 4:
                # SOURCE LINE 327
                __M_writer(u'                            checked="checked"\n')
            # SOURCE LINE 329
            __M_writer(u'                        />\n                        <input name="star2" type="radio" class="user_rating_star" value="5"\n')
            # SOURCE LINE 331
            if user_item_rating == 5:
                # SOURCE LINE 332
                __M_writer(u'                            checked="checked"\n')
            # SOURCE LINE 334
            __M_writer(u'                        />\n                    </div>\n')
        # SOURCE LINE 337
        __M_writer(u'                <div style="clear: both;"></div>\n                        \n')
        # SOURCE LINE 340
        __M_writer(u'                <h4>Tags</h4>\n                <p>\n')
        # SOURCE LINE 343
        __M_writer(u'                <div>\n                    Community:\n                    ')
        # SOURCE LINE 345
        __M_writer(unicode(render_community_tagging_element( tagged_item=item, tag_click_fn='community_tag_click', use_toggle_link=False )))
        __M_writer(u'\n')
        # SOURCE LINE 346
        if len ( item.tags ) == 0:
            # SOURCE LINE 347
            __M_writer(u'                        none\n')
        # SOURCE LINE 349
        __M_writer(u'                </div>\n')
        # SOURCE LINE 351
        if trans.get_user():
            # SOURCE LINE 352
            __M_writer(u'                    <p>\n                    <div>\n                        Yours:\n                        ')
            # SOURCE LINE 355
            __M_writer(unicode(render_individual_tagging_element( user=trans.get_user(), tagged_item=item, elt_context='view.mako', use_toggle_link=False, tag_click_fn='community_tag_click' )))
            __M_writer(u'\n                    </div>\n')
        # SOURCE LINE 358
        __M_writer(u'            </div>    \n        </div>\n    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x66f1a90')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x66f1850')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 112
        __M_writer(u'\n    ')
        # SOURCE LINE 113
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n    ')
        # SOURCE LINE 114
        __M_writer(unicode(h.css( "autocomplete_tagging", "embed_item", "trackster", "jquery.rating" )))
        __M_writer(u'\n    \n    <style type="text/css">\n        .page-body {\n            padding: 10px;\n')
        # SOURCE LINE 121
        __M_writer(u'        }\n        .page-meta {\n            float: right;\n            width: 27%;\n            padding: 0.5em;\n            margin: 0.25em;\n            vertical-align: text-top;\n            border: 2px solid #DDDDDD;\n            border-top: 4px solid #DDDDDD;\n        }\n        \n')
        # SOURCE LINE 133
        __M_writer(u'        .historyItemContainer, .toolForm {\n            max-width: 500px;\n        }\n        \n')
        # SOURCE LINE 138
        __M_writer(u'        div.toolForm{\n            margin-top: 10px;\n            margin-bottom: 10px;\n        }\n        \n')
        # SOURCE LINE 144
        __M_writer(u'        .historyItemContainer {\n            padding-right: 3px;\n            border-right-style: solid;\n            border-right-color: #66AA66;\n        }\n    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_item(context,item,item_data=None):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x66f1a90')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x66f1850')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element'])
        __M_writer = context.writer()
        # SOURCE LINE 164
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x66f1a90')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x66f1850')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 23
        __M_writer(u'\n')
        # SOURCE LINE 24

        self.has_left_panel=False
        self.has_right_panel=True
        self.message_box_visible=False
        self.active_view="shared"
        self.overlay_visible=False
        
        
        # SOURCE LINE 30
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_item_header(context,item):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x66f1a90')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x66f1850')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element'])
        get_item_name = _import_ns.get('get_item_name', context.get('get_item_name', UNDEFINED))
        get_class_display_name = _import_ns.get('get_class_display_name', context.get('get_class_display_name', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 156
        __M_writer(u'\n    <h3>Galaxy ')
        # SOURCE LINE 157
        __M_writer(unicode(get_class_display_name( item.__class__ )))
        __M_writer(u" '")
        __M_writer(filters.html_escape(unicode(get_item_name( item ))))
        __M_writer(u"'</h3>\n")
        # SOURCE LINE 158
        if hasattr( item, "annotation") and item.annotation is not None:
            # SOURCE LINE 159
            __M_writer(u'        <div class="annotation">Annotation: ')
            __M_writer(unicode(item.annotation))
            __M_writer(u'</div>\n')
        # SOURCE LINE 161
        __M_writer(u'    <hr/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_item_links(context,item):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x66f1a90')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x66f1850')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element'])
        __M_writer = context.writer()
        # SOURCE LINE 152
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x66f1a90')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x66f1850')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        get_controller_name = _import_ns.get('get_controller_name', context.get('get_controller_name', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        item = _import_ns.get('item', context.get('item', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 33
        __M_writer(u'\n    ')
        # SOURCE LINE 34
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n    ')
        # SOURCE LINE 35
        __M_writer(unicode(h.js( "jquery", "jquery.tipsy", "galaxy.base", "json2", "class", "jquery.jstore", "jquery.autocomplete", "jquery.rating", "autocomplete_tagging", "trackster" )))
        __M_writer(u'\n\n    <script type="text/javascript">\n        \n        // Handle click on community tag.\n        function community_tag_click(tag_name, tag_value) {\n            ')
        # SOURCE LINE 41
        controller_name = get_controller_name( item ) 
        
        __M_writer(u"\n            var href = '")
        # SOURCE LINE 42
        __M_writer(unicode(h.url_for ( controller='/' + controller_name , action='list_published')))
        __M_writer(u'\';\n            href = href + "?f-tags=" + tag_name;\n            if (tag_value != undefined && tag_value != "") {\n                href = href + ":" + tag_value;\n            }\n            self.location = href;\n        }\n        \n        // Map item rating to number of stars to show.\n        function map_rating_to_num_stars(rating) {\n            if (rating <= 0)\n                return 0;\n            else if (rating > 0 && rating <= 1.5)\n                return 1;\n            else if (rating > 1.5 && rating <= 2.5)\n                return 2;\n            else if (rating > 2.5 && rating <= 3.5)\n                return 3;\n            else if (rating > 3.5 && rating <= 4.5)\n                return 4;\n            else if (rating > 4.5)\n                return 5;\n        }\n        \n        // Init. on document load.\n        $(function() {\n            // Set links to Galaxy screencasts to open in overlay.\n            $(this).find("a[href^=\'http://screencast.g2.bx.psu.edu/\']").each( function() {\n                $(this).click( function() {\n                    var href = $(this).attr(\'href\');\n                    show_in_overlay(\n                        {\n                            url: href,        \n                            width: 640,\n                            height: 480,\n                            scroll: \'no\'  \n                        }\n                    );\n                    return false;\n                });\n            });\n            \n            // Init history boxes.\n            init_history_items( $("div.historyItemWrapper"), false, "nochanges" );\n            \n            // Init user item rating.\n            $(\'.user_rating_star\').rating({\n                callback: function(rating, link) {\n                    $.ajax({\n                        type: "GET",\n                        url: "')
        # SOURCE LINE 92
        __M_writer(unicode(h.url_for ( controller='/' + controller_name , action='rate_async' )))
        __M_writer(u'",\n                        data: { id : "')
        # SOURCE LINE 93
        __M_writer(unicode(trans.security.encode_id( item.id )))
        __M_writer(u'", rating : rating },\n                        dataType: \'json\',\n                        error: function() { alert( "Rating submission failed" ); },\n                        success: function( community_data ) {\n                            $(\'#rating_feedback\').show();\n                            $(\'#num_ratings\').text(Math.round(community_data[1]*10)/10);\n                            $(\'#ave_rating\').text(community_data[0]);\n                            $(\'.community_rating_star\').rating(\'readOnly\', false);\n                            $(\'.community_rating_star\').rating(\'select\', map_rating_to_num_stars(community_data[0])-1);\n                            $(\'.community_rating_star\').rating(\'readOnly\', true);\n                        }\n                    });\n                },\n                required: true // Hide cancel button.\n            });\n        });    \n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


