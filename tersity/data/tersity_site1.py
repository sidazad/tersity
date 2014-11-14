
from core import *
from data.tersity_ubernotify_artifacts import *

# LANDING PAGE

landing_page = Page("landing")
landing_page.layout = HeaderCenterFooter()
landing_page.layout.menu = [
    {"name": "Home", "route": "landing"},
    {"name": "Dashboard", "route": "dashboard"},
]

landing_page.layout.header.rows[0].widgets = [
    MenuWidget(id="landing_menu", colspan=4, menu=[
        {"name": "Home", "route": "landing"},
        {"name": "Dashboard", "route": "dashboard"},
    ]),
    EmptyRows(2)
]

landing_page.layout.center.rows[0].widgets = [
    BasicLoginWidget(id="landing_login", colspan=3, onlogin=onlogin)
]

# DASHBOARD PAGE

dashboard_page = Page("dashboard")
dashboard_page.layout = HorizontalLayout(2)
dashboard_page.layout.section.rows[0] = RawHtml(html="<label>Please select one of the tabs below</label>")

tab_one_section = Section(1)
tab_one_section.rows[0] = RawHtml("Notifications")

tab_two_section = Section(1)
#tab_two_section.rows[0] = RawHtml("This is tab two")
tab_two_section.rows[0] = Template(filename="data/notifications.html")

dashboard_page.layout.section.rows[1] = TabbedLayout(tabs=[Tab("Notifications", tab_one_section),
                                                           Tab("Manage Notifications", tab_two_section)])

# BASIC APP SETUP

app = TersityApp("ubernotify")
app.static_root = "/static"
# template url for django (will require load_template url to provide templates)
app.template_url_prefix="/load_template?name="
# normal template url
#app.template_url_prefix="/templates"
app.genpath = "/Users/sidazad/dev/tersity/tersity/genapps/ubernotify"
app.baseurl = "ubernotify.com"
app.framework = "angularjs"
app.backend = ""
app.landing = landing_page
app.dashboard = dashboard_page
app.services = ["LoginAPI"]
