#!/usr/bin/python
# coding: utf8
import getpass
import urllib
import urllib2


def ip_register(conf):
    env_url = "http://dyn.value-domain.com/cgi-bin/dyn.fcg?ip"
    admin_url = "https://ss1.coressl.jp/www.%s.coreserver.jp/jp/admin.cgi" % (conf['server'])
    message = u"データベースに追加しました。反映には５〜１０分程度掛かります。"

    myip = urllib2.urlopen(env_url).read()

    try:
        post_data = {
            'ssh2': 'SSH登録',
            'remote_host': myip,
            'id': conf['id'],
            'pass': conf['pass']
        }
        admin = urllib2.urlopen(admin_url, urllib.urlencode(post_data))
    except urllib2.HTTPError as e:
        print "HTTPError:", e.code
    except urllib2.URLError as e:
        print e.reason
    else:
        if message in unicode(admin.read(), 'shift_jis'):
            print "Your IP (%s) was successfully registered." % (myip)
        else:
            print "Your IP (%s) was detected, but registration failed." % (myip)
            print unicode(admin.read(), 'shift_jis')


if __name__ == '__main__':
    try:
        from coreconf import conf
    except ImportError:
        print "[ERROR] Write server name and user name in coreconf.py."
    else:
        conf["pass"] = getpass.getpass()
        ip_register(conf)
