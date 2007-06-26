from setuptools import setup, find_packages

setup(name = "z3c.davapp.zopeappfile",
      version = "0.9",
      author = "Michael Kerrin",
      author_email = "michael.kerrin@openapp.ie",
      url = "http://launchpad.net/z3c.dav",
      description = "WebDAV support for zope.app.file content objects",
      license = "ZPL",

      packages = find_packages("src"),
      package_dir = {"": "src"},
      namespace_packages = ["z3c", "z3c.davapp"],
      install_requires = ["setuptools",
                          "z3c.dav",
                          "zope.app.file",
                          ],

      extras_require = dict(test = ["cElementTree"]),

      include_package_data = True,
      zip_safe = False)
