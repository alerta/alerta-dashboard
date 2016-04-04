Alerta Dashboard 2.0
====================

Version 2.0 of the alerta dashboard is a [flask](http://flask.pocoo.org/) wsgi application that uses server-side templating.

It has been updated to work with alerta 3.0 however, it is no longer actively supported and future development effort will
focus on improving the new [alerta webui](https://github.com/alerta/angular-alerta-webui) based on [AngularJS](https://angularjs.org/).

Example
-------

![dashboard](/docs/images/alerta-dashboard-v2.png?raw=true)


Installation
------------

To install the v2 dashboard, clone the repository and run:

    $ python setup.py install


Configuration
-------------

By default, the dashboard will assume the alerta API endpoint is located at port 8080 on the same domain
that the dashboard is served from ie. `http://localhost:8080` if the dashboard is at `http://localhost:5000`

Modify file `dashboard/assets/js/config.js` to use a different alerta API endpoint. For example:

    var appConfig = {
        'endpoint': 'http://api.alerta.io:8080'
    }


Run
---

To run the dashboard in development, simply run `alerta-dashboard` on the command-line:

    $ alerta-dashboard
    # => http://localhost:5000/dashboard/index.html

In production, the application should be served by any web server that supports wsgi web applications.


Dependencies
------------

All dependencies are included, however, for reference they are:

  * [jQuery](http://jquery.com/)
  * [DataTables](https://datatables.net/)
  * [Bootstrap 2.3](http://getbootstrap.com/2.3.2/)
  * [Sintony Font](http://www.google.com/fonts/specimen/Sintony)
  

License
-------

Copyright (c) 2014,2016 Nick Satterly. Available under the MIT License.
