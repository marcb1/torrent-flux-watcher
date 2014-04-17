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


def main():
    username = conf.username
    password = conf.password
    address = conf.address

    register_openers()
    cookie_jar = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_jar), MultipartPostHandler.MultipartPostHandler)
    login_data = urllib.urlencode({'username' : username, 'iamhim' : password})
    resp = opener.open('https://'+address+'/login.php', login_data)
    result = resp.read()

    if(result.lower().find('fail') != -1):
          print 'Error logging in to torrent flux, password/username error'
          return

    os.chdir('watch')
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
      if(f.lower().find('.torrent') != -1):
        print 'uploading: ' + f + '\n ...'
        myform = {"upload_file" : open(f, "rb")}
        resp = opener.open('https://'+address+'/index.php', myform)
      else:
        print 'file: ' + f + '\nnot a torrent file, skipping...'

    return 0


if __name__=="__main__":
  main()
