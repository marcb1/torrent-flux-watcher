#!/usr/bin/python
import conf, tflux



def main():
    username = conf.username
    password = conf.password
    address = conf.address

    torrentflux = tflux.tflux(username, address, password)
    torrentflux.login()
    torrentflux.upload_dir('watch')

if __name__=="__main__":
  main()
