Spittalpond
===========
<!-- The closest Bermuda's got to an Oasis! -->

What is it?
-----------

Spittalpond is an Python interface for the Oasis Django API  webservices
(currently compatible with versions R1.3 and R1.4).
It acts as a front-end that allows you to run models, exposures and other
useful webservices in Oasis.
Effectively, it's turns you Oasis style .csv files into useful GUL data!

Installation
------------

You can quickly install this package by simply `pip install`ing it:

``` sh
$ pip install spittalpond
```

Usage
-----

Spittalpond can be quickly run by using the config interface. Note that you will
have modify the [example.toml][] (by creating your own) TOML configuration file to
point to your specific Oasis .csv files and you Oasis server. Then simply use
that config file as seen here:

```sh
$ python -m spittalpond.config_interface path/to/my_config.toml
```

Alternatively, if you have downloaded the Spittalpond code you can run the
config interface file directly:
```sh
$ cd path/to/spittalpond/
$ python ./spittalpond/config_interface.py ../examples/example.toml
```

Documentation on the config interface can be found [here].

Dependencies
------------

Spittalpond mainly depends on the Python [Requests], and [pytoml] packages.
These will be installed automatically when you `pip install` spittalpond.
If not, you can always manually `pip install` them necessary 

Also, of course, you will need to have [IPython] installed (as well as the
notebooks part of it) if you intend to view and run the IPython notebook
examples.

Potential Patches
-----------------

Note: If you are using Oasis R1.4 then you **do not** need to do this!

As of Oasis version R1.3, the Oasis Django server will need to be patched so
that Spittalpond will run correctly. Patches will be placed in the
`spittalpond/data` directory. You must apply all of the patches as so:

1. Move the patches onto the Oasis Django server into the `/var/www/django/`
   directory. (i.e use WinSCP to do this.)
2. Apply the patches one by one with the standard Unix [patch] command on
   the Oasis Django server:

   ```sh
   $ cd /var/www/django
   $ patch -p1 < file_upload.patch
   (Stripping trailing CRs from patch.)
   patching file oasis/app/views.py
   Hunk #1 succeeded at 8069 (offset -1274 lines).
   ```

   As you can see above, the output succeeded for hunk #3. If it happens
   to fail, you are probably not patching the correct server version.

   Note that `file_upload.patch` should be replaced with whatever patch
   you need to apply.
3. You will also need to restart the Apache server on the Oasis Django
   server: Run the following command:

   ```sh
   $ service apache2 restart
   ```

You should now be able to successfully run Spittalpond!

Contribute
----------

Additional features, patches, bug fixes, and pull request are welcome!
Please see the file [CONTRIBUTING.md]

Documentation
-------------

Documentation is available at
<http://beckettsimmons.github.io/spittalpond/docs/>


[example.toml]: <./examples/example.toml>
[here]: <http://beckettsimmons.github.io/spittalpond/docs/usage/config_interface.html>
[Requests]: <http://docs.python-requests.org/en/latest/>
[pytoml]: <https://github.com/avakar/pytoml>
[IPython]: <http://ipython.org/>
[patch]: <http://linux.about.com/od/commands/l/blcmdl1_patch.htm>
[CONTRIBUTING.md]: <./CONTRIBUTING.md>
