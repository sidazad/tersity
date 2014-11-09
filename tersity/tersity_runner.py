"""
    @author Sid Azad
"""

import os
import sys
import shutil
from core import *


class TersityGen(object):
    def __init__(self):
        pass


class AngularGen(TersityGen):
    def __init__(self, app):
        self.app = app
        self.artifacts = {}
        self.debug = 4

    def gen_dirs(self):
        self.gendir = self.app.genpath
        if os.path.exists(self.gendir):
            shutil.rmtree(self.gendir)
        os.makedirs(self.gendir)
        self.tmpltdir = "%s/templates" % self.gendir
        os.makedirs(self.tmpltdir)
        self.jsdir = "%s/js" % self.gendir
        os.makedirs(self.jsdir)
        self.cssdir = "%s/css" % self.gendir
        os.makedirs(self.cssdir)
        self.imgdir = "%s/images" % self.gendir
        os.makedirs(self.imgdir)


    def copy_user_files(self):
        shutil.copyfile("../data/tersity_%s_services.js" % self.app.name, self.jsdir+"/tersity_%s_services.js" % self.app.name)


    def pre_process(self):
        if self.debug > 3:
            print "pre_process"
        # generate a list of all pages in this app
        self.app.pages = []
        for attr in dir(self.app):
            attrval = getattr(self.app, attr)
            if isinstance(attrval, Page):
                pagename = attrval.name
                self.app.pages.append(attrval)
                if 'layout' in dir(attrval):
                    layout = getattr(attrval, 'layout')
                    print "has layout:",layout
                    for layout_attr in dir(layout):
                        layout_attr_val = getattr(layout, layout_attr)
                        if isinstance(layout_attr_val, Section):
                            section = getattr(layout, layout_attr)
                            print "Got section:", section
                            for row in section.rows:
                                if hasattr(row, 'widgets'):
                                    for widget in row.widgets:
                                        print "Widget=", widget, " in pagename=",pagename
                                        if not pagename in self.artifacts:
                                            self.artifacts[pagename] = []
                                        page_artifacts = self.artifacts[pagename]
                                        page_artifacts.append(widget.get_artifacts())


        print self.app.pages


    def get_state_str(self):
        statestr = ""
        for page in self.app.pages:
            url = "/" if page.name == "landing" else "/%s" % page.name
            statestr += """

.state('{PAGE_NAME}', {{
    url: "{PAGE_URL}",
        templateUrl: '{STATIC_ROOT}/templates/{PAGE_NAME}.html',
        controller: "{PAGE_NAME}Ctrl"
    }})
""".format(STATIC_ROOT=self.app.static_root, PAGE_NAME=page.name, PAGE_URL=url)
        statestr += ";"
        return statestr

    def gen_app(self):
        print "gen_app"
        self.pre_process()
        self.gen_dirs()
        self.copy_user_files()
        appfile = open("%s/app.js" % self.jsdir, 'w')
        state_str = self.get_state_str()
        appfile.write("""

'use strict';
var app = angular.module('{APPNAME}', ['ui.router', 'ui.bootstrap']).config(["$stateProvider", "$locationProvider", function($stateProvider, $locationProvider) {{
    $stateProvider
        {STATE_STR}
    $locationProvider
            .html5Mode(true)
            .hashPrefix('!');
}}]);

app.run(['$state', function ($state) {{
   $state.transitionTo('landing');
}}])

""".format(APPNAME=self.app.name, STATE_STR=state_str))
        self.gen_base()
        self.gen_controllers()
        self.gen_templates()
        self.gen_css()

    def gen_base(self):
        """
            Generate the base.html file
        """
        appfile = open("%s/base.html" % self.tmpltdir, 'w')
        appfile.write(
            """
<!DOCTYPE html>
<html ng-app="{APP_NAME}">
<head>
    <meta charset="utf-8"/>
    <base href="/">
    <title>UberNotify</title>
    <!-- Angular library -->
    <script src="http://cdnjs.cloudflare.com/ajax/libs/angular.js/1.2.20/angular.js"></script>
    <!-- Angular UI Router -->
    <script src="http://cdnjs.cloudflare.com/ajax/libs/angular-ui-router/0.2.10/angular-ui-router.js"></script>
    <!-- AngularJS Bootstrap -->
    <script src="http://cdnjs.cloudflare.com/ajax/libs/angular-ui-bootstrap/0.10.0/ui-bootstrap-tpls.min.js"></script>

    <!-- local app files -->
    <script src="{STATIC_ROOT}/js/app.js"></script>
    <script src="{STATIC_ROOT}/js/tersity_ubernotify_services.js"></script>
    <script src="{STATIC_ROOT}/js/controllers.js"></script>

    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="{STATIC_ROOT}/css/style.css"/>
</head>

<body>
<div id="wrap" ui-view style="font-family: candara; font-size: 11pt;">

</div>
<footer class="footer">
    <p>This website is built generated using tersity</p>
</footer>
</body>

</html>
            """.format(APP_NAME=self.app.name, STATIC_ROOT=self.app.static_root)
        )

    def gen_controllers(self):
        if self.debug > 3:
            print "gen_controllers"
        for page in self.app.pages:
            ctrlname = "%sCtrl" % page.name
            print "generating controller ", ctrlname
            appfile = open("%s/controllers.js" % self.jsdir, 'a')
            ctrl_funcs = ""
            if page.name in self.artifacts:
                print "ctrl for ", page.name, ' has some artifacts'
                page_artifacts = self.artifacts.get(page.name)
                if not page_artifacts:
                    continue
                print "page_artifacts=",page_artifacts
                for page_artifact in page_artifacts:
                    if not page_artifact:
                        continue
                    if 'CTRL_SCOPE_FUNC' in page_artifact:
                        ctrl_funcs += "\n%s\n" % page_artifact.get('CTRL_SCOPE_FUNC')
            print "artifactstr=",ctrl_funcs
            services_str, services_str2 = "", ""
            for service in self.app.services:
                services_str += """'%s',""" % service
                services_str2 += """%s,""" % service
            services_str = services_str[0:-1]
            services_str2 = services_str2[0:-1]
            appfile.write("""
app.controller('{CTRL_NAME}', ["$scope", {MODULES}, function ($scope, {MODULES2}) {{

    console.log("{CTRL_NAME}");

    $scope.model = {{

    }};

    {CTRL_FUNCS}

}}]);
""".format(CTRL_NAME=ctrlname, CTRL_FUNCS=ctrl_funcs, MODULES=services_str, MODULES2=services_str2))

    def gen_menu(self, pagename, menu):
        menustr = """ <div id='{PAGE_NAME}_menu'> """.format(PAGE_NAME=pagename)
        for item in menu:
            menustr += """<a ui-sref='{ROUTE}'>{MENU_ITEM}</a> """.format(MENU_ITEM=item.get("name"), ROUTE=item.get("route"))
        menustr += "</div>"
        return menustr

    def gen_templates(self):
        print "gen_templates"
        for page in self.app.pages:
            tmpltname = "%s.html" % page.name
            print "Generating ",tmpltname
            tmpltfile = open("%s/%s" %(self.tmpltdir, tmpltname) , 'w')
            tmpltfile.write("<div id='{PAGE_NAME}_page'>".format(PAGE_NAME=page.name))
            if hasattr(page, 'layout'):
                renderstr = page.render_str()
                print renderstr
                tmpltfile.write(page.render_str())

    def gen_css(self):
        shutil.copyfile("../templates/style.css", self.cssdir+"/style.css")


class Tersity(object):
    def run(self, cfgfile):
        config = {}
        execfile(cfgfile, config)
        app = config.get("app")
        self.app = app
        self.gen()

    def gen(self):
        print "gen"
        if self.app.framework == "angularjs":
            self.gen_for_angular()

    def gen_for_angular(self):
        print "gen_for_angular"
        gen = AngularGen(self.app)
        gen.gen_app()


def usage():
    print "Usage: python tersity_runner.py <path to site description file>"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()
        sys.exit(-1)
    tersity = Tersity()
    tersity.run(sys.argv[1])