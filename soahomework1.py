#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, redirect, request, make_response, url_for, session, jsonify, render_template
import weibo2, weibo
from web import jsonresult, _json_dumps
import flask
import urllib2
import gzip
import time
import logging
import json
import datetime
import threading
import base64
import hashlib
import db
import json
import urllib

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO


app = Flask(__name__)
ctx = threading.local()

APP_KEY = '2637837462'
APP_SECRET = 'a2179056bd5fe581bc80cfe6a88ed20d'
CALLBACK_URL = 'http://soahomework1.sinaapp.com/callback'

#def _format_user(u):
#    return dict(id=str(u.id), screen_name=u.screen_name, profile_url=u.profile_url, verified=u.verified, verified_type=u.verified_type, profile_image_url=u.profile_image_url)
#

def _format_user(u):
    if isinstance(u['name'], unicode):
    	return u"\n{\n\t'id': " + unicode(u['id']) + u",\n\t'screen_name': " + u['name'] + u",\n\t'friends_count': " + unicode(u['friends_count']) \
    			+ ",\n\t'followers_count': " + unicode(u['followers_count']) + ",\n\t'statuses_count': " + unicode(u['statuses_count']) + "\n}\n"

@app.route('/', methods=['GET'])
def main():
    cookie = request.cookies.get('uid', None)
    if not cookie:
        return render_template('login_button.html')
    else:
        client = weibo2.APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)        
        return render_template('logged_in.html', user_alias=cookie)

@app.route('/users', methods=['GET'])
def get_users():
    cookie = request.cookies.get('uid', None)
    if not cookie:
        return render_template('login_button.html')
    user = db.select('select * from users')
    #return str(user)
    users = u'['
    for u in user:
        users = users + _format_user(u)
    users = users + u']'
    rsp = make_response(users)
    rsp.headers['Content-Type'] = 'application/json'
    return rsp

@app.route('/posts/<uid>', methods=['GET'])
def get_posts(uid):
    cookie = request.cookies.get('uid', None)
    if not cookie:
        return render_template('login_button.html')
    query = db.select('select * from users where id=?', uid)
    if not query:
        return redirect(url_for('main'))
    u = query[0]
    post = db.select('select * from posts where uid=?', uid)
    if post:
        r = post[0]['posts']#.encode('utf-8')
    else:
        return redirect(url_for('main'))
    keyword = request.args.get('keyword', '')
    if keyword == '0' or keyword == '1':
        r = post[0]['posts']
        client = weibo.APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL) 
        client.set_access_token(u.auth_token, u.expired_time)
        r = client.statuses.user_timeline.get(count=100, uid=uid)
        rjson = json.loads(r)
        rtext = ''
        rlist = []
        
        for status in rjson['statuses']:
            rttext = status['text']
            rttext = urllib.quote_plus(rttext.encode('utf-8'))
            
            url = u'http://api.yutao.us/api/keyword/' + rttext
            
            try:
                response = urllib2.urlopen(url)
                rttext = response.read()
            except:
                rttext = ''
            rlist.append(status['text'])
            rtext += rttext
        
        rdict = {}
        for k, v, in rjson.iteritems():
            rdict[k] = v
        if keyword == '0':
        	rdict['statuses'] = rlist
        rdict['keywords'] = rtext    
        
        r = json.dumps(rdict, ensure_ascii=False, indent=2).encode('utf-8')
    #['posts']
  #  client = weibo.APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL) 
  #  client.set_access_token(u.auth_token, u.expired_time)
    
  #  r = client.statuses.user_timeline.get(count=100, uid=uid)
    
 #   keyword = request.args.get('keyword', '')
 #   if keyword:
 #   	r = json.loads(r)
 #       rlist = []
 #       rdict = {}
 #       for status in r['statuses']:
 #           if unicode(keyword) in status['text']:
 #               rlist.append(status)
 #       for k, v in r.iteritems():
 #           if k != 'statuses':
 #               rdict[k] = v
 #           else:
 #               rdict[k] = rlist
 #       r = json.dumps(rdict, ensure_ascii=False).encode('utf-8')

    rsp = make_response(r)
    rsp.headers['Content-Type'] = 'application/json'
    return rsp

@app.route('/login', methods=['GET'])
def login_with_weibo_credentials():
    client = weibo2.APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    url = client.get_authorize_url()
    return redirect(url)

@app.route('/logout', methods=['GET'])
def logout():
    rsp = make_response(redirect(url_for('main')))
    rsp.set_cookie('uid', expires=0)
    return rsp

@app.route('/callback', methods=['GET'])
def callback():
    client = weibo2.APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    code = request.args.get('code', '')
    r = client.request_access_token(code)
    logging.info('access token: %s' % json.dumps(r))
    
    access_token, expires_in, uid = r.access_token, r.expires_in, r.uid
    client.set_access_token(access_token=access_token, expires=expires_in)
    u = client.users.show.get(uid=uid)
    users = db.select('select * from users where id=?', uid)
    user = {"name": u.screen_name,
            "image_url":u.avatar_large or u.profile_image_url,
            "statuses_count":u.statuses_count,
            "friends_count":u.friends_count,
            "followers_count":u.followers_count,
            "verified":u.verified,
            "verified_type":u.verified_type,
            "auth_token":access_token,
            "expired_time":expires_in
            }
    
    if users:
        db.update_kw('users', 'id=?', uid, **user)
    	#client.set_access_token(u.auth_token, u.expired_time)
        
        response = urllib2.urlopen('https://api.weibo.com/2/statuses/user_timeline.json?uid=%s&access_token=%s' % (uid, access_token))
        r = weibo._read_body(response)
        #r = client.statuses.user_timeline.get(count=100, uid=uid)
        u2 = db.select('select * from posts where uid=?', uid)
        users2 = {"uid": uid, "posts": r}
        if u2:
            db.update_kw('posts', 'uid=?', uid, **users2)
        else:
            db.insert('posts', **users2)
    else:
        user['id'] = uid
        db.insert('users', **user)
        #db.insert('posts', **users2)
    logging.info('got user: %s' % uid)
    rsp = make_response(redirect(url_for('main')))
    rsp.set_cookie('uid', uid,
                   expires=datetime.datetime.now() + datetime.timedelta(seconds=int(expires_in)))
    return rsp

if __name__ == '__main__':
    app.run()
