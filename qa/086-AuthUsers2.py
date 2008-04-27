from base import *

CONF = """
vserver!default!rule!860!match = directory
vserver!default!rule!860!match!directory = /auth2users
vserver!default!rule!860!match!final = 0
vserver!default!rule!860!auth = plain
vserver!default!rule!860!auth!methods = basic
vserver!default!rule!860!auth!realm = Test with Users
vserver!default!rule!860!auth!passwdfile = %s
vserver!default!rule!860!auth!users = foo,Aladdin
"""

class Test (TestBase):
    def __init__ (self):
        TestBase.__init__ (self)
        self.name             = "Auth basic, with users II"
        self.request          = "GET /auth2users/ HTTP/1.0\r\n" +\
                                "Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==\r\n"
        self.expected_error   = 200

    def Prepare (self, www):
        d = self.Mkdir (www, "auth2users")
        self.WriteFile (d, "passwd", 0444, 'user:cherokee\n' + 'foo:bar\n' + 'Aladdin:open sesame\n')

        self.conf = CONF % (d+"/passwd")

