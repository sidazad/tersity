"""
    @author Sid Azad
"""

class Widget(object):
    def __init__(self, id="widget_id", colspan=1):
        self.id = id
        self.colspan = colspan

    def get_artifacts(self):
        return []

    def render_str(self):
        """
        This method must be overridden in the derived classes. It is supposed to return the
        actual HTML that would render this widget.
        """
        return ""

class RawHtml(Widget):
    def __init__(self, html):
        super(RawHtml, self).__init__()
        self.html = html

    def render_str(self):
        return self.html



class MenuWidget(Widget):
    def __init__(self, id, colspan, menu):
        super(MenuWidget, self).__init__(id, colspan)
        self.id = id
        self.colspan = colspan
        self.menu = menu

    def render_str(self):
        menustr = """
         <div id="{WIDGET_ID}">
        <div class="col-xs-{COLSPAN}">
         """.format(WIDGET_ID=self.id, COLSPAN=self.colspan)
        for item in self.menu:
            menustr += """<a ui-sref='{ROUTE}'>{MENU_ITEM}</a> """.format(MENU_ITEM=item.get("name"),
                                                                          ROUTE=item.get("route"))
        menustr += "</div></div>"
        return menustr


class BasicLoginWidget(Widget):
    def __init__(self, id, colspan, onlogin=None):
        super(BasicLoginWidget, self).__init__(id, colspan)
        self.debug = 5
        self.onlogin = onlogin

    def get_artifacts(self):
        if self.onlogin:
            print "HAVE ONLOGIN"
            return {"CTRL_SCOPE_FUNC": """
        {CODE}
            """.format(CODE=self.onlogin.code)}
        else:
            return {"CTRL_SCOPE_FUNC": """
        $scope.on_login = function() {
                window.console.log("login clicked");
        };
            """}

    def render_str(self):
        if self.debug > 3:
            print "BasicLoginWidget.render_str"
        return """
<div id="{WIDGET_ID}">
    <div class="col-xs-{COLSPAN}">
        Username:<input type="text" ng-model="model.username">
        Password:<input type="password" ng-model="model.password">
        <input type="button" value="Login" ng-click="on_login();"/>
    </div>
</div>
        """.format(WIDGET_ID=self.id, COLSPAN=self.colspan)


class EmptyRows(Widget):
    """
        Widget to enter a number of empty rows (assumes bootstrap grid system)
    """
    def __init__(self, numrows):
        """
        @param numrows Number of empty rows to generate
        """
        super(EmptyRows, self).__init__()
        self.numrows = numrows

    def render_str(self):
        empty_row = """ <div class="row">&nbsp;</div> """
        empty_rows = ""
        for i in range(self.numrows):
            empty_rows += empty_row
        return empty_rows


class Template(object):
    """
        Representation of a template or HTML file.
    """
    def __init__(self, filename=""):
        # filename is the file from which the template would be loaded
        self.filename = filename
        # templateUrl is the url from which the template would be loaded
        self.templateUrl = ""
    def render_str(self):
        # todo: implement for templateUrl
        if self.filename:
            with open(self.filename, 'r') as tmpltfile:
                return tmpltfile.read()



class Layout(object):
    pass


class Col(object):
    def __init__(self):
        pass


class Row(object):
    def __init__(self):
        self.debug = 3
        self.cols = []
        self.widgets = []

    def render_str(self):
        print "Row.render_str"
        rowstr = """<div class='row'>"""
        for widget in self.widgets:
            rowstr += widget.render_str()
        rowstr += """</div>"""
        return rowstr


class Section(object):
    def __init__(self, numrows):
        self.debug = 3
        self.rows = []
        for i in range(numrows):
            self.rows.append(Row())

    def render_str(self):
        if self.debug > 3:
            print "Section.render_str"
            print self.rows
        section_str = ""
        for row in self.rows:
            section_str += "%s\n" % row.render_str()
        if self.debug > 4:
            print section_str
        return section_str


class HorizontalLayout(Layout):
    """
        A simple layout with a single section with a number of rows.
    """

    def __init__(self, numrows):
        self.debug = 3
        self.section = Section(numrows)

    def render_str(self):
        if self.debug > 3:
            print "HorizontalLayout.render_str"
        return self.section.render_str()

class Function(object):
    def __init__(self, name, code):
        self.name = name
        self.code = code

class Tab(object):
    def __init__(self, title, section):
        self.title = title
        self.section = section


class TabbedLayout(Layout):
    def __init__(self, tabs):
        self.tabs = tabs
        self.debug = 5

    def render_str(self):
        if self.debug > 3:
            print "TabbedLayout.render_str"
        tabbed_str = "<tabset>"
        for tab in self.tabs:
            tabbed_str += """<tab heading="%s"> """ % tab.title
            tabbed_str += tab.section.render_str()
            tabbed_str += """</tab>"""
        tabbed_str += "</tabset>"
        return tabbed_str





class HeaderCenterFooter(Layout):
    def __init__(self):
        self.debug = 3
        self.header = Section(1)
        self.center = Section(1)
        self.footer = Section(1)

    def render_str(self):
        if self.debug > 3:
            print "HeaderCenterFooter.render_str"
        hdrstr = self.header.render_str()
        centerstr = self.center.render_str()
        footerstr = self.footer.render_str()
        return "%s%s%s" % (hdrstr, centerstr, footerstr)


class Page(object):
    def __init__(self, name):
        self.debug = 3
        self.name = name

    def render_str(self):
        if self.debug > 3:
            print "Page.render_str"
        if hasattr(self, "layout"):
            return self.layout.render_str()


class TersityApp(object):
    def __init__(self, name):
        self.name = name
