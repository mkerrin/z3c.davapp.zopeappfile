import os
import unittest
import doctest

import z3c.etree.testing
import z3c.dav.testing
import z3c.davapp.zopeappfile

davlayer = z3c.dav.testing.WebDAVLayer(z3c.davapp.zopeappfile)


def setUp(test):
    z3c.dav.testing.functionalSetUp(test)
    test.globs["getRootFolder"] = davlayer.getRootFolder


def tearDown(test):
    z3c.dav.testing.functionalTearDown(test)
    del test.globs["getRootFolder"]


def test_suite():
    properties = doctest.DocFileSuite(
        "properties.txt",
        setUp = setUp,
        tearDown = tearDown,
        checker = z3c.etree.testing.xmlOutputChecker,
        optionflags = doctest.REPORT_NDIFF | doctest.NORMALIZE_WHITESPACE)
    properties.layer = davlayer

    return unittest.TestSuite((
        doctest.DocTestSuite("z3c.davapp.zopeappfile"),
        properties,
        ))
