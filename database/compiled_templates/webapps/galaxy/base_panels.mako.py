# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1336498137.8906419
_template_filename=u'templates/webapps/galaxy/base_panels.mako'
_template_uri=u'/webapps/galaxy/base_panels.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['masthead', 'javascripts', 'title']


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
    return runtime._inherit_from(context, u'/base_panels.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 4
        __M_writer(u'\n\n')
        # SOURCE LINE 9
        __M_writer(u'\n\n')
        # SOURCE LINE 236
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_masthead(context):
    context.caller_stack._push_frame()
    try:
        AssertionError = context.get('AssertionError', UNDEFINED)
        h = context.get('h', UNDEFINED)
        app = context.get('app', UNDEFINED)
        util = context.get('util', UNDEFINED)
        def tab(id,display,href,target='_parent',visible=True,extra_class='',menu_options=None):
            context.caller_stack._push_frame()
            try:
                self = context.get('self', UNDEFINED)
                len = context.get('len', UNDEFINED)
                __M_writer = context.writer()
                # SOURCE LINE 20
                __M_writer(u'\n')
                # SOURCE LINE 23
                __M_writer(u'    \n        ')
                # SOURCE LINE 24

                cls = ""
                a_cls = ""
                extra = ""
                if extra_class:
                    cls += " " + extra_class
                if self.active_view == id:
                    cls += " active"
                if menu_options:
                    cls += " dropdown"
                    a_cls += " dropdown-toggle"
                    extra = "<b class='caret'></b>"
                style = ""
                if not visible:
                    style = "display: none;"
                
                
                # SOURCE LINE 39
                __M_writer(u'\n        <li class="')
                # SOURCE LINE 40
                __M_writer(unicode(cls))
                __M_writer(u'" style="')
                __M_writer(unicode(style))
                __M_writer(u'">\n')
                # SOURCE LINE 41
                if href:
                    # SOURCE LINE 42
                    __M_writer(u'                <a class="')
                    __M_writer(unicode(a_cls))
                    __M_writer(u'" data-toggle="dropdown" target="')
                    __M_writer(unicode(target))
                    __M_writer(u'" href="')
                    __M_writer(unicode(href))
                    __M_writer(u'">')
                    __M_writer(unicode(display))
                    __M_writer(unicode(extra))
                    __M_writer(u'</a>\n')
                    # SOURCE LINE 43
                else:
                    # SOURCE LINE 44
                    __M_writer(u'                <a class="')
                    __M_writer(unicode(a_cls))
                    __M_writer(u'" data-toggle="dropdown">')
                    __M_writer(unicode(display))
                    __M_writer(unicode(extra))
                    __M_writer(u'</a>\n')
                    pass
                # SOURCE LINE 46
                if menu_options:
                    # SOURCE LINE 47
                    __M_writer(u'                <ul class="dropdown-menu">\n')
                    # SOURCE LINE 48
                    for menu_item in menu_options:
                        # SOURCE LINE 49
                        if not menu_item:
                            # SOURCE LINE 50
                            __M_writer(u'                            <li class="divider"></li>\n')
                            # SOURCE LINE 51
                        else:
                            # SOURCE LINE 52
                            __M_writer(u'                            <li>\n')
                            # SOURCE LINE 53
                            if len ( menu_item ) == 1:
                                # SOURCE LINE 54
                                __M_writer(u'                                ')
                                __M_writer(unicode(menu_item[0]))
                                __M_writer(u'\n')
                                # SOURCE LINE 55
                            elif len ( menu_item ) == 2:
                                # SOURCE LINE 56
                                __M_writer(u'                                ')
                                name, link = menu_item 
                                
                                __M_writer(u'\n                                <a href="')
                                # SOURCE LINE 57
                                __M_writer(unicode(link))
                                __M_writer(u'">')
                                __M_writer(unicode(name))
                                __M_writer(u'</a>\n')
                                # SOURCE LINE 58
                            else:
                                # SOURCE LINE 59
                                __M_writer(u'                                ')
                                name, link, target = menu_item 
                                
                                __M_writer(u'\n                                <a target="')
                                # SOURCE LINE 60
                                __M_writer(unicode(target))
                                __M_writer(u'" href="')
                                __M_writer(unicode(link))
                                __M_writer(u'">')
                                __M_writer(unicode(name))
                                __M_writer(u'</a>\n')
                                pass
                            # SOURCE LINE 62
                            __M_writer(u'                            </li>\n')
                            pass
                        pass
                    # SOURCE LINE 65
                    __M_writer(u'                </ul>\n')
                    pass
                # SOURCE LINE 67
                __M_writer(u'        </li>\n    ')
                return ''
            finally:
                context.caller_stack._pop_frame()
        trans = context.get('trans', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 12
        __M_writer(u'\n\n')
        # SOURCE LINE 15
        __M_writer(u'    <div style="position: relative; right: -50%; float: left;">\n    <div style="display: block; position: relative; right: 50%;">\n\n    <ul class="nav" border="0" cellspacing="0">\n    \n    ')
        # SOURCE LINE 68
        __M_writer(u'\n\n')
        # SOURCE LINE 71
        __M_writer(u'    ')
        __M_writer(unicode(tab( "analysis", _("Analyze Data"), h.url_for( controller='/root', action='index' ) )))
        __M_writer(u'\n    \n')
        # SOURCE LINE 74
        __M_writer(u'    ')
        __M_writer(unicode(tab( "workflow", _("Workflow"), h.url_for( controller='/workflow', action='index' ) )))
        __M_writer(u'\n    \n')
        # SOURCE LINE 77
        __M_writer(u'    ')

        menu_options = [ 
                        [ _('Data Libraries'), h.url_for( controller='/library', action='index') ],
                        None,
                        [ _('Published Histories'), h.url_for( controller='/history', action='list_published' ) ],
                        [ _('Published Workflows'), h.url_for( controller='/workflow', action='list_published' ) ]
                       ]
        if app.config.get_bool( 'enable_tracks', False ):
            menu_options.append( [ _('Published Visualizations'), h.url_for( controller='/visualization', action='list_published' ) ] )        
        if app.config.get_bool( 'enable_pages', False ):
            menu_options.append( [ _('Published Pages'), h.url_for( controller='/page', action='list_published' ) ] )
        tab( "shared", _("Shared Data"), h.url_for( controller='/library', action='index'), menu_options=menu_options )
            
        
        # SOURCE LINE 89
        __M_writer(u'\n    \n')
        # SOURCE LINE 92
        __M_writer(u'    ')

        menu_options = [
                         [ _('Sequencing Requests'), h.url_for( controller='/requests', action='index' ) ],
                         [ _('Find Samples'), h.url_for( controller='/requests', action='find_samples_index' ) ],
                         [ _('Help'), app.config.get( "lims_doc_url", "http://main.g2.bx.psu.edu/u/rkchak/p/sts" ), "galaxy_main" ]
                       ]
        tab( "lab", "Lab", None, menu_options=menu_options, visible=( trans.user and ( trans.user.requests or trans.app.security_agent.get_accessible_request_types( trans, trans.user ) ) ) )
            
        
        # SOURCE LINE 99
        __M_writer(u'\n\n')
        # SOURCE LINE 102
        if app.config.get_bool( 'enable_tracks', False ):
            # SOURCE LINE 103
            __M_writer(u'        ')

            menu_options = [
                             [_('New Visualization'), h.url_for( controller='/tracks', action='index' ) ],
                             [_('Saved Visualizations'), h.url_for( controller='/visualization', action='list' ) ]
                           ]
            tab( "visualization", _("Visualization"), h.url_for( controller='/visualization', action='list'), menu_options=menu_options )
                    
            
            # SOURCE LINE 109
            __M_writer(u'\n')
            pass
        # SOURCE LINE 111
        __M_writer(u'\n')
        # SOURCE LINE 113
        if app.config.get_bool( 'enable_cloud_launch', False ):
            # SOURCE LINE 114
            __M_writer(u'        ')

            menu_options = [
                             [_('New Cloud Cluster'), h.url_for( controller='/cloud', action='index' ) ],
                           ]
            tab( "cloud", _("Cloud"), h.url_for( controller='/cloud', action='index'), menu_options=menu_options )
                    
            
            # SOURCE LINE 119
            __M_writer(u'\n')
            pass
        # SOURCE LINE 121
        __M_writer(u'\n')
        # SOURCE LINE 123
        __M_writer(u'    ')
        __M_writer(unicode(tab( "admin", "Admin", h.url_for( controller='/admin', action='index' ), extra_class="admin-only", visible=( trans.user and app.config.is_admin_user( trans.user ) ) )))
        __M_writer(u'\n    \n')
        # SOURCE LINE 126
        __M_writer(u'    ')

        menu_options = [
                            [_('Support'), app.config.get( "support_url", "http://wiki.g2.bx.psu.edu/Support" ), "_blank" ],
                            [_('Galaxy Wiki'), app.config.get( "wiki_url", "http://wiki.g2.bx.psu.edu/" ), "_blank" ],
                            [_('Video tutorials (screencasts)'), app.config.get( "screencasts_url", "http://galaxycast.org" ), "_blank" ],
                            [_('How to Cite Galaxy'), app.config.get( "citation_url", "http://wiki.g2.bx.psu.edu/Citing%20Galaxy" ), "_blank" ]
                        ]
        tab( "help", _("Help"), None, menu_options=menu_options)
            
        
        # SOURCE LINE 134
        __M_writer(u'\n    \n')
        # SOURCE LINE 137
        __M_writer(u'    ')
  
        # Menu for user who is not logged in.
        menu_options = [ [ _("Login"), h.url_for( controller='/user', action='login' ), "galaxy_main" ] ]
        if app.config.allow_user_creation:
            menu_options.append( [ _("Register"), h.url_for( controller='/user', action='create', cntrller='user', webapp='galaxy' ), "galaxy_main" ] ) 
        extra_class = "loggedout-only"
        visible = ( trans.user == None )
        tab( "user", _("User"), None, visible=visible, menu_options=menu_options )
        
        # Menu for user who is logged in.
        if trans.user:
            email = trans.user.email
        else:
            email = ""
        menu_options = [ [ '<a>Logged in as <span id="user-email">%s</span></a>' %  email ] ]
        if app.config.use_remote_user:
            if app.config.remote_user_logout_href:
                menu_options.append( [ _('Logout'), app.config.remote_user_logout_href, "_top" ] )
        else:
            menu_options.append( [ _('Preferences'), h.url_for( controller='/user', action='index', cntrller='user', webapp='galaxy' ), "galaxy_main" ] )
            if app.config.get_bool( 'enable_tracks', False ):
                menu_options.append( [ 'Custom Builds', h.url_for( controller='/user', action='dbkeys' ), "galaxy_main" ] )
            if app.config.require_login:
                logout_url = h.url_for( controller='/root', action='index', m_c='user', m_a='logout', webapp='galaxy' )
            else:
                logout_url = h.url_for( controller='/user', action='logout', webapp='galaxy' )
            menu_options.append( [ 'Logout', logout_url, "_top" ] )
            menu_options.append( None )
        menu_options.append( [ _('Saved Histories'), h.url_for( controller='/history', action='list' ), "galaxy_main" ] )
        menu_options.append( [ _('Saved Datasets'), h.url_for( controller='/dataset', action='list' ), "galaxy_main" ] )
        if app.config.get_bool( 'enable_pages', False ):
            menu_options.append( [ _('Saved Pages'), h.url_for( controller='/page', action='list' ), "_top" ] )
        menu_options.append( [ _('API Keys'), h.url_for( controller='/user', action='api_keys', cntrller='user', webapp='galaxy' ), "galaxy_main" ] )
        if app.config.use_remote_user:
            menu_options.append( [ _('Public Name'), h.url_for( controller='/user', action='edit_username', cntrller='user', webapp='galaxy' ), "galaxy_main" ] )
        
        extra_class = "loggedin-only"
        visible = ( trans.user != None )
        tab( "user", "User", None, visible=visible, menu_options=menu_options )
            
        
        # SOURCE LINE 176
        __M_writer(u'\n    \n')
        # SOURCE LINE 180
        __M_writer(u'    </ul>\n\n    </div>\n    </div>\n    \n')
        # SOURCE LINE 186
        __M_writer(u'    <div class="title">\n        <a href="')
        # SOURCE LINE 187
        __M_writer(unicode(app.config.get( 'logo_url', '/' )))
        __M_writer(u'">\n        <img border="0" src="')
        # SOURCE LINE 188
        __M_writer(unicode(h.url_for('/static/images/galaxyIcon_noText.png')))
        __M_writer(u'">\n        Galaxy\n')
        # SOURCE LINE 190
        if app.config.brand:
            # SOURCE LINE 191
            __M_writer(u'            <span>/ ')
            __M_writer(unicode(app.config.brand))
            __M_writer(u'</span>\n')
            pass
        # SOURCE LINE 193
        __M_writer(u'        </a>\n    </div>\n\n')
        # SOURCE LINE 197
        __M_writer(u'    ')

        bar_style = "quota-meter-bar"
        usage = 0
        percent = 0
        quota = None
        try:
            usage = trans.app.quota_agent.get_usage( trans=trans )
            quota = trans.app.quota_agent.get_quota( trans.user )
            percent = trans.app.quota_agent.get_percent( usage=usage, quota=quota )
            if percent is not None:
                if percent >= 100:
                    bar_style += " quota-meter-bar-error"
                elif percent >= 85:
                    bar_style += " quota-meter-bar-warn"
            else:
                percent = 0
        except AssertionError:
            pass # Probably no history yet
        tooltip = None
        if not trans.user and quota and trans.app.config.allow_user_creation:
            if trans.app.quota_agent.default_registered_quota is None or trans.app.quota_agent.default_unregistered_quota < trans.app.quota_agent.default_registered_quota:
                tooltip = "Your disk quota is %s.  You can increase your quota by registering a Galaxy account." % util.nice_size( quota )
            
        
        # SOURCE LINE 219
        __M_writer(u'\n\n    <div class="quota-meter-container">\n')
        # SOURCE LINE 222
        if tooltip:
            # SOURCE LINE 223
            __M_writer(u'        <div id="quota-meter" class="quota-meter tooltip" title="')
            __M_writer(unicode(tooltip))
            __M_writer(u'">\n')
            # SOURCE LINE 224
        else:
            # SOURCE LINE 225
            __M_writer(u'        <div id="quota-meter" class="quota-meter">\n')
            pass
        # SOURCE LINE 227
        __M_writer(u'            <div id="quota-meter-bar" class="')
        __M_writer(unicode(bar_style))
        __M_writer(u'" style="width: ')
        __M_writer(unicode(percent))
        __M_writer(u'px;"></div>\n')
        # SOURCE LINE 228
        if quota is not None:
            # SOURCE LINE 229
            __M_writer(u'                <div id="quota-meter-text" class="quota-meter-text">Using ')
            __M_writer(unicode(percent))
            __M_writer(u'%</div>\n')
            # SOURCE LINE 230
        else:
            # SOURCE LINE 231
            __M_writer(u'                <div id="quota-meter-text" class="quota-meter-text">Using ')
            __M_writer(unicode(util.nice_size( usage )))
            __M_writer(u'</div>\n')
            pass
        # SOURCE LINE 233
        __M_writer(u'        </div>\n    </div>\n    \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 6
        __M_writer(u'\n    ')
        # SOURCE LINE 7
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n    ')
        # SOURCE LINE 8
        __M_writer(unicode(h.js( "jquery.tipsy" )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'Galaxy')
        return ''
    finally:
        context.caller_stack._pop_frame()


