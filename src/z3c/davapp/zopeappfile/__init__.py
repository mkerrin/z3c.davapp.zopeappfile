import zope.component
import zope.interface
import zope.publisher.interfaces.http
import zope.app.file.interfaces

import z3c.dav.coreproperties

class DAVFileGetSchema(object):
    """
    Storage adapter for the `{DAV:}getcontentlength` and `{DAV:}getcontenttype`
    WebDAV properties for a content object implementing
    zope.app.file.interfaces.IFile interface.

      >>> from zope.app.file.file import File
      >>> from zope.interface.verify import verifyObject
      >>> file = File('some data for the file', 'text/plain')
      >>> adapter = DAVFileGetSchema(file, None)
      >>> verifyObject(z3c.dav.coreproperties.IDAVGetcontentlength, adapter)
      True
      >>> verifyObject(z3c.dav.coreproperties.IDAVGetcontenttype, adapter)
      True

      >>> adapter.getcontentlength
      22
      >>> adapter.getcontenttype
      'text/plain'

    """
    zope.interface.implements(z3c.dav.coreproperties.IDAVGetcontentlength,
                              z3c.dav.coreproperties.IDAVGetcontenttype)
    zope.component.adapts(zope.app.file.interfaces.IFile,
                          zope.publisher.interfaces.http.IHTTPRequest)

    def __init__(self, context, request):
        self.context = context

    @property
    def getcontentlength(self):
        return self.context.getSize()

    @property
    def getcontenttype(self):
        return self.context.contentType
