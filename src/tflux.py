#!/usr/bin/python
import urllib, urllib2, cookielib, poster
import sys
import os
from poster.streaminghttp import register_openers
import MultipartPostHandler
import conf

#wireshark torrentflux upload
#Content-Disposition: form-data; name="upload_file"; filename="ugly-americans-4.jpg"
#Content-Length: 453735
#-----------------------------21829415731438
#Content-Disposition: form-data; name="upload_file"; filename="ugly-americans-4.jpg"
#Content-Type: image/jpeg

class tflux:
    def __init__(self, user, add, passw):
              self.username = user
              self.password = passw
              self.address = add
              register_openers()
              cookie_jar = cookielib.CookieJar()
              self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_jar), MultipartPostHandler.MultipartPostHandler)

    def login(self):
              login_data = urllib.urlencode({'username' : self.username, 'iamhim' : self.password})
              resp = self.opener.open('https://'+self.address+'/login.php', login_data)
              result = resp.read()

              if(result.lower().find('fail') != -1):
                    print 'Error logging in to torrent flux, check password/username: ' + self.username + ":" + self.password + "@" + self.address 
                    return False
              return True

    def upload_dir(self,directory):
              os.chdir(directory)
              files = [f for f in os.listdir('.') if os.path.isfile(f)]
	      for f in files:
                    if(f.lower().find('.torrent') != -1):
                        print 'uploading: ' + f + '...'
			file = open(f, 'rb')
                        myform = {"upload_file" : file}
                        resp = self.opener.open('https://'+self.address+'/index.php', myform)
                        result = resp.read()
			file.close()
                        if(result.lower().find(f) != -1):
                              print "error cannot upload file: " + f
                        else:
                            os.remove(f)
                    else:
                        print 'file: ' + f + '\nnot a torrent file, skipping...'
