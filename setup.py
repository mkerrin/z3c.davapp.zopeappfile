from setuptools import setup, find_packages

setup(name = "z3c.davapp.zopeappfile",
      version = "1.0b2",
      author = "Michael Kerrin",
      author_email = "michael.kerrin@openapp.ie",
      url = "http://launchpad.net/z3c.dav",
      description = open("README.txt").read(),
      long_description = (
          open("src/z3c/davapp/zopeappfile/properties.txt").read() +
          "\n\n" +
          open("CHANGES.txt").read()),
      license = "ZPL",
      classifiers = ["Environment :: Web Environment",
                     "Intended Audience :: Developers",
                     "License :: OSI Approved :: Zope Public License",
                     "Programming Language :: Python",
                     "Framework :: Zope3",
                     ],

      packages = find_packages("src"),
      package_dir = {"": "src"},
      namespace_packages = ["z3c", "z3c.davapp"],
      install_requires = ["setuptools",
                          "z3c.dav",
                          "zope.app.file",
                          ],

      include_package_data = True,
      zip_safe = False)
