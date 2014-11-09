

CONCEPTS
========

Tersity
-------

Tersity is a way of describing a website in Python and then generating the website from this description. The
idea is that once described a website can then be generated using any framework such as AngularJS, Backbone etc.
The current implementation is using AngularJS but the eventual goal is to provide implementations for other
frameworks as well.

The basic idea is as follows:

1. Describe a site via a Python file (see tersity_site1.py for an example)
2. Run tersity_runner.py with the file written in (1.) as an input
3. Your site should have been generated, test it with a web server


App or Site
-----------

A tersity app is the root level object which represents the site or SPA (Single Page Application) that the tersity
file describes. A site consistes of multiple pages.

Pages
-----

A Page is a Python class that represents a page in a site or SPA. A page can further contain layouts. For example if
your site has a landing page that would be a Page instance. Another page, say Dashboard would be another Page instance.

Layout
------

A layout is a standard way of organizing a site's page. A layout usually has one or more Section instances. A few
layouts are provided out of the box by Tersity and more can be written by users.

A Layout can contain Sections which can contain other Layouts, and hence a composite/nested hierarchy can be
created.

- HorizontalLayout - A simple layout with a single section with a number of rows.

- TabbedLayout - A TabbedLayout contains multiple tabs (horizontal or vertical). The contents of each tab are within a
section.

- HeaderCenterFooter - A typical layout that gives the page a top section (header) that usually contains a menu,
a middle section that usually contains the content and a bottom section (footer) to a website.

As an example, a website may have a HeaderCenterFooter Layout with the Header containing a Menu and the center
section containing a TabbedLayout.

Section
-------

A section is an abstraction that represents a portion of a page. A Section typically contains one or more Row
instances.

Row
---

A Row contains a number of columns. Rows and columns together provide a grid system to organize page elements/widgets
in a layout

Column
------


Artifacts
---------
Artifacts are code snippets that are generated when a widget that they are associated with is used by the site. For
example the "BasicLoginWidget" may have the 'onlogin' Function associated with it. This is regarded to be an artifact.
The definition of this function can be provided by the user using the "Function" class.

Widget
------

Widgets are typically generic UI elements with some code that fulfil a specific function. For example, there may
 be a LoginWidget which shows a username and password input box on the screen with a "Login" button. Once the user
 presses this button, this widget executes a user-provided function.

Function
--------

The function class is used to represent JavaScript functions that are associated with certain widgets.

ToDo
----

- Implementation for other Frameworks (Backbone, Ember, Knockout)
- Read code artifacts from flat file
- More widgets
  - Grid widget with option of which grid to use (tablesorter, ng-grid)
- Page patterns
  - for example a pattern would be a page with a form and a grid with a search button. On pressing search the
  grid gets populated
- CSS support
- Add footer to generated site ("This site has been generated using Tersity")


USAGE
=====

WEB SERVER
----------

1. Generate the site
python tersity_runner.py <site-file-path>

2. Run the server
pushd ~/dev/tersity/tersity/genapps/ubernotify/;  python -m SimpleHTTPServer 8001; popd

2.