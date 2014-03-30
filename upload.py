import urllib, urllib2, cookielib
import sys
import os

def main():
    username = 'wh'
    password = 'f'
    address = 'thoe'
    cookie_jar = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_jar))
    login_data = urllib.urlencode({'username' : username, 'iamhim' : password})
    resp = opener.open('https://'+address+'/login.php', login_data)
    
    os.chdir('watch')
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        myform = {"url": f,"aid":"2"}
        myform_data = urllib.urlencode(myform)
        opener.open('https://'+address+'/dispatcher.php?action=urlUpload',myform_data)


    return 0


if __name__=="__main__":
  main()
