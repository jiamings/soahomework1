# soahomework1
Tiny website using Weibo's OAuth2 API. Experiment mode. Only limited Weibo users are allowed.

## Website
[http://soahomework1.sinaapp.com](http://soahomework1.sinaapp.com)

## API
`/users`: show all users in JSON format.

`/posts/<uid>`: show the first 100 posts of user with uid `<uid>` in JSON format

`/posts/<uid>?keywords=1`: show the first 100 posts of user with uid `<uid>` in JSON format, with "keywords" field

`/posts/<uid>?keywords=0`: same as keywords=1, but simplified the "statuses" field with only "text"

## Examples
### `/users`
```[json]
[
{
	'id': 5554103544,
	'screen_name': 宋假名,
	'friends_count': 5,
	'followers_count': 2,
	'statuses_count': 4
}

{
	'id': 5574908775,
	'screen_name': jiamingmajia,
	'friends_count': 34,
	'followers_count': 1,
	'statuses_count': 0
}

{
	'id': 2190259880,
	'screen_name': 沈光耀_,
	'friends_count': 236,
	'followers_count': 308,
	'statuses_count': 63
}
]
```
### `/posts/5554103544`
```[json]
{"statuses":[{"created_at":"Mon Mar 30 11:13:57 +0800 2015","id":3826051551879944,"mid":"3826051551879944","idstr":"3826051551879944","text":"(Test) My favorite game calls that “Defense of the Ancient”. Short title is DotA. It’s a game from Blizzard. You can choose a hero to use. And you should play with other nine players. This is near-health and natural disasters of war. I enjoy the time to win the game.","source_allowclick":0,"source_type":1,"source":"<a href=\"http://weibo.com/\" rel=\"nofollow\">微博 weibo.com</a>","favorited":false,"truncated":false,"in_reply_to_status_id":"","in_reply_to_user_id":"","in_reply_to_screen_name":"","pic_urls":[],"geo":null,"user":{"id":5554103544,"idstr":"5554103544","class":1,"screen_name":"宋假名","name":"宋假名","province":"11","city":"8","location":"北京 海淀区","description":"","url":"","profile_image_url":"http://tp1.sinaimg.cn/5554103544/50/0/1","profile_url":"u/5554103544","domain":"","weihao":"","gender":"m","followers_count":2,"friends_count":5,"pagefriends_count":0,"statuses_count":4,"favourites_count":0,"created_at":"Fri Mar 13 22:50:22 +0800 2015","following":false,"allow_all_act_msg":false,"geo_enabled":true,"verified":false,"verified_type":-1,"remark":"","ptype":0,"allow_all_comment":true,"avatar_large":"http://tp1.sinaimg.cn/5554103544/180/0/1","avatar_hd":"http://tp1.sinaimg.cn/5554103544/180/0/1","verified_reason":"","verified_trade":"","verified_reason_url":"","verified_source":"","verified_source_url":"","follow_me":false,"online_status":0,"bi_followers_count":1,"lang":"zh-cn","star":0,"mbtype":0,"mbrank":0,"block_word":0,"block_app":0,"credit_score":80,"urank":2},"reposts_count":0,"comments_count":0,"attitudes_count":0,"mlevel":0,"visible":{"type":0,"list_id":0},"darwin_tags":[]},{"created_at":"Mon Mar 30 11:13:35 +0800 2015","id":3826051459573309,"mid":"3826051459573309","idstr":"3826051459573309","text":"(Test) I had the first bicycle which only belong to me is on my 5 years old birthday. A friend of my father sent me the present. But I have not used to play it until I am 7 years old. And after that time, I haven’t had it. Now a bicycle is forward me.","source_allowclick":0,"source_type":1,"source":"<a href=\"http://weibo.com/\" rel=\"nofollow\">微博 weibo.com</a>","favorited":false,"truncated":false,"in_reply_to_status_id":"","in_reply_to_user_id":"","in_reply_to_screen_name":"","pic_urls":[],"geo":null,"user":{"id":5554103544,"idstr":"5554103544","class":1,"screen_name":"宋假名","name":"宋假名","province":"11","city":"8","location":"北京 海淀区","description":"","url":"","profile_image_url":"http://tp1.sinaimg.cn/5554103544/50/0/1","profile_url":"u/5554103544","domain":"","weihao":"","gender":"m","followers_count":2,"friends_count":5,"pagefriends_count":0,"statuses_count":4,"favourites_count":0,"created_at":"Fri Mar 13 22:50:22 +0800 2015","following":false,"allow_all_act_msg":false,"geo_enabled":true,"verified":false,"verified_type":-1,"remark":"","ptype":0,"allow_all_comment":true,"avatar_large":"http://tp1.sinaimg.cn/5554103544/180/0/1","avatar_hd":"http://tp1.sinaimg.cn/5554103544/180/0/1","verified_reason":"","verified_trade":"","verified_reason_url":"","verified_source":"","verified_source_url":"","follow_me":false,"online_status":0,"bi_followers_count":1,"lang":"zh-cn","star":0,"mbtype":0,"mbrank":0,"block_word":0,"block_app":0,"credit_score":80,"urank":2},"reposts_count":0,"comments_count":0,"attitudes_count":0,"mlevel":0,"visible":{"type":0,"list_id":0},"darwin_tags":[]},{"created_at":"Mon Mar 30 11:12:16 +0800 2015","id":3826051128423695,"mid":"3826051128423695","idstr":"3826051128423695","text":"(Test) 程序员眼中--别人的bug和自己的bug，心理专家的剖析？不，这明明就是程序员的自白，笑cry","source_allowclick":0,"source_type":1,"source":"<a href=\"http://weibo.com/\" rel=\"nofollow\">微博 weibo.com</a>","favorited":false,"truncated":false,"in_reply_to_status_id":"","in_reply_to_user_id":"","in_reply_to_screen_name":"","pic_urls":[],"geo":null,"user":{"id":5554103544,"idstr":"5554103544","class":1,"screen_name":"宋假名","name":"宋假名","province":"11","city":"8","location":"北京 海淀区","description":"","url":"","profile_image_url":"http://tp1.sinaimg.cn/5554103544/50/0/1","profile_url":"u/5554103544","domain":"","weihao":"","gender":"m","followers_count":2,"friends_count":5,"pagefriends_count":0,"statuses_count":4,"favourites_count":0,"created_at":"Fri Mar 13 22:50:22 +0800 2015","following":false,"allow_all_act_msg":false,"geo_enabled":true,"verified":false,"verified_type":-1,"remark":"","ptype":0,"allow_all_comment":true,"avatar_large":"http://tp1.sinaimg.cn/5554103544/180/0/1","avatar_hd":"http://tp1.sinaimg.cn/5554103544/180/0/1","verified_reason":"","verified_trade":"","verified_reason_url":"","verified_source":"","verified_source_url":"","follow_me":false,"online_status":0,"bi_followers_count":1,"lang":"zh-cn","star":0,"mbtype":0,"mbrank":0,"block_word":0,"block_app":0,"credit_score":80,"urank":2},"reposts_count":0,"comments_count":0,"attitudes_count":0,"mlevel":0,"visible":{"type":0,"list_id":0},"darwin_tags":[]},{"created_at":"Thu Mar 19 00:11:21 +0800 2015","id":3821898536514864,"mid":"3821898536514864","idstr":"3821898536514864","text":"#我的第一条微博#","source_allowclick":0,"source_type":1,"source":"<a href=\"http://weibo.com/\" rel=\"nofollow\">微博 weibo.com</a>","favorited":false,"truncated":false,"in_reply_to_status_id":"","in_reply_to_user_id":"","in_reply_to_screen_name":"","pic_urls":[],"geo":null,"user":{"id":5554103544,"idstr":"5554103544","class":1,"screen_name":"宋假名","name":"宋假名","province":"11","city":"8","location":"北京 海淀区","description":"","url":"","profile_image_url":"http://tp1.sinaimg.cn/5554103544/50/0/1","profile_url":"u/5554103544","domain":"","weihao":"","gender":"m","followers_count":2,"friends_count":5,"pagefriends_count":0,"statuses_count":4,"favourites_count":0,"created_at":"Fri Mar 13 22:50:22 +0800 2015","following":false,"allow_all_act_msg":false,"geo_enabled":true,"verified":false,"verified_type":-1,"remark":"","ptype":0,"allow_all_comment":true,"avatar_large":"http://tp1.sinaimg.cn/5554103544/180/0/1","avatar_hd":"http://tp1.sinaimg.cn/5554103544/180/0/1","verified_reason":"","verified_trade":"","verified_reason_url":"","verified_source":"","verified_source_url":"","follow_me":false,"online_status":0,"bi_followers_count":1,"lang":"zh-cn","star":0,"mbtype":0,"mbrank":0,"block_word":0,"block_app":0,"credit_score":80,"urank":2},"reposts_count":0,"comments_count":0,"attitudes_count":0,"mlevel":0,"visible":{"type":0,"list_id":0},"darwin_tags":[]}],"marks":[],"hasvisible":false,"previous_cursor":0,"next_cursor":0,"total_number":4,"interval":0}
```
### `/posts/5554103544?keywords=1`
```[json]
{
  "interval": 0, 
  "hasvisible": false, 
  "total_number": 4, 
  "previous_cursor": 0, 
  "next_cursor": 0, 
  "marks": [], 
  "keywords": "程序员,心理专家,自白,bug bug,", 
  "statuses": [
    {
      "reposts_count": 0, 
      "truncated": false, 
      "text": "(Test) My favorite game calls that “Defense of the Ancient”. Short title is DotA. It’s a game from Blizzard. You can choose a hero to use. And you should play with other nine players. This is near-health and natural disasters of war. I enjoy the time to win the game.", 
      "visible": {
        "type": 0, 
        "list_id": 0
      }, 
      "in_reply_to_status_id": "", 
      "id": 3826051551879944, 
      "mid": "3826051551879944", 
      "source": "<a href=\"http://weibo.com/\" rel=\"nofollow\">微博 weibo.com</a>", 
      "attitudes_count": 0, 
      "in_reply_to_screen_name": "", 
      "in_reply_to_user_id": "", 
      "pic_urls": [], 
      "darwin_tags": [], 
      "favorited": false, 
      "source_allowclick": 0, 
      "idstr": "3826051551879944", 
      "source_type": 1, 
      "user": {
        "bi_followers_count": 1, 
        "domain": "", 
        "avatar_large": "http://tp1.sinaimg.cn/5554103544/180/0/1", 
        "verified_source": "", 
        "ptype": 0, 
        "block_word": 0, 
        "star": 0, 
        "id": 5554103544, 
        "verified_reason_url": "", 
        "city": "8", 
        "verified": false, 
        "credit_score": 80, 
        "block_app": 0, 
        "follow_me": false, 
        "verified_reason": "", 
        "followers_count": 2, 
        "location": "北京 海淀区", 
        "verified_trade": "", 
        "mbtype": 0, 
        "verified_source_url": "", 
        "profile_url": "u/5554103544", 
        "province": "11", 
        "avatar_hd": "http://tp1.sinaimg.cn/5554103544/180/0/1", 
        "statuses_count": 4, 
        "description": "", 
        "friends_count": 5, 
        "online_status": 0, 
        "mbrank": 0, 
        "idstr": "5554103544", 
        "profile_image_url": "http://tp1.sinaimg.cn/5554103544/50/0/1", 
        "allow_all_act_msg": false, 
        "allow_all_comment": true, 
        "geo_enabled": true, 
        "class": 1, 
        "name": "宋假名", 
        "lang": "zh-cn", 
        "weihao": "", 
        "remark": "", 
        "favourites_count": 0, 
        "screen_name": "宋假名", 
        "url": "", 
        "gender": "m", 
        "created_at": "Fri Mar 13 22:50:22 +0800 2015", 
        "verified_type": -1, 
        "following": false, 
        "pagefriends_count": 0, 
        "urank": 2
      }, 
      "geo": null, 
      "created_at": "Mon Mar 30 11:13:57 +0800 2015", 
      "mlevel": 0, 
      "comments_count": 0
    }, 
    {
      "reposts_count": 0, 
      "truncated": false, 
      "text": "(Test) I had the first bicycle which only belong to me is on my 5 years old birthday. A friend of my father sent me the present. But I have not used to play it until I am 7 years old. And after that time, I haven’t had it. Now a bicycle is forward me.", 
      "visible": {
        "type": 0, 
        "list_id": 0
      }, 
      "in_reply_to_status_id": "", 
      "id": 3826051459573309, 
      "mid": "3826051459573309", 
      "source": "<a href=\"http://weibo.com/\" rel=\"nofollow\">微博 weibo.com</a>", 
      "attitudes_count": 0, 
      "in_reply_to_screen_name": "", 
      "in_reply_to_user_id": "", 
      "pic_urls": [], 
      "darwin_tags": [], 
      "favorited": false, 
      "source_allowclick": 0, 
      "idstr": "3826051459573309", 
      "source_type": 1, 
      "user": {
        "bi_followers_count": 1, 
        "domain": "", 
        "avatar_large": "http://tp1.sinaimg.cn/5554103544/180/0/1", 
        "verified_source": "", 
        "ptype": 0, 
        "block_word": 0, 
        "star": 0, 
        "id": 5554103544, 
        "verified_reason_url": "", 
        "city": "8", 
        "verified": false, 
        "credit_score": 80, 
        "block_app": 0, 
        "follow_me": false, 
        "verified_reason": "", 
        "followers_count": 2, 
        "location": "北京 海淀区", 
        "verified_trade": "", 
        "mbtype": 0, 
        "verified_source_url": "", 
        "profile_url": "u/5554103544", 
        "province": "11", 
        "avatar_hd": "http://tp1.sinaimg.cn/5554103544/180/0/1", 
        "statuses_count": 4, 
        "description": "", 
        "friends_count": 5, 
        "online_status": 0, 
        "mbrank": 0, 
        "idstr": "5554103544", 
        "profile_image_url": "http://tp1.sinaimg.cn/5554103544/50/0/1", 
        "allow_all_act_msg": false, 
        "allow_all_comment": true, 
        "geo_enabled": true, 
        "class": 1, 
        "name": "宋假名", 
        "lang": "zh-cn", 
        "weihao": "", 
        "remark": "", 
        "favourites_count": 0, 
        "screen_name": "宋假名", 
        "url": "", 
        "gender": "m", 
        "created_at": "Fri Mar 13 22:50:22 +0800 2015", 
        "verified_type": -1, 
        "following": false, 
        "pagefriends_count": 0, 
        "urank": 2
      }, 
      "geo": null, 
      "created_at": "Mon Mar 30 11:13:35 +0800 2015", 
      "mlevel": 0, 
      "comments_count": 0
    }, 
    {
      "reposts_count": 0, 
      "truncated": false, 
      "text": "(Test) 程序员眼中--别人的bug和自己的bug，心理专家的剖析？不，这明明就是程序员的自白，笑cry", 
      "visible": {
        "type": 0, 
        "list_id": 0
      }, 
      "in_reply_to_status_id": "", 
      "id": 3826051128423695, 
      "mid": "3826051128423695", 
      "source": "<a href=\"http://weibo.com/\" rel=\"nofollow\">微博 weibo.com</a>", 
      "attitudes_count": 0, 
      "in_reply_to_screen_name": "", 
      "in_reply_to_user_id": "", 
      "pic_urls": [], 
      "darwin_tags": [], 
      "favorited": false, 
      "source_allowclick": 0, 
      "idstr": "3826051128423695", 
      "source_type": 1, 
      "user": {
        "bi_followers_count": 1, 
        "domain": "", 
        "avatar_large": "http://tp1.sinaimg.cn/5554103544/180/0/1", 
        "verified_source": "", 
        "ptype": 0, 
        "block_word": 0, 
        "star": 0, 
        "id": 5554103544, 
        "verified_reason_url": "", 
        "city": "8", 
        "verified": false, 
        "credit_score": 80, 
        "block_app": 0, 
        "follow_me": false, 
        "verified_reason": "", 
        "followers_count": 2, 
        "location": "北京 海淀区", 
        "verified_trade": "", 
        "mbtype": 0, 
        "verified_source_url": "", 
        "profile_url": "u/5554103544", 
        "province": "11", 
        "avatar_hd": "http://tp1.sinaimg.cn/5554103544/180/0/1", 
        "statuses_count": 4, 
        "description": "", 
        "friends_count": 5, 
        "online_status": 0, 
        "mbrank": 0, 
        "idstr": "5554103544", 
        "profile_image_url": "http://tp1.sinaimg.cn/5554103544/50/0/1", 
        "allow_all_act_msg": false, 
        "allow_all_comment": true, 
        "geo_enabled": true, 
        "class": 1, 
        "name": "宋假名", 
        "lang": "zh-cn", 
        "weihao": "", 
        "remark": "", 
        "favourites_count": 0, 
        "screen_name": "宋假名", 
        "url": "", 
        "gender": "m", 
        "created_at": "Fri Mar 13 22:50:22 +0800 2015", 
        "verified_type": -1, 
        "following": false, 
        "pagefriends_count": 0, 
        "urank": 2
      }, 
      "geo": null, 
      "created_at": "Mon Mar 30 11:12:16 +0800 2015", 
      "mlevel": 0, 
      "comments_count": 0
    }, 
    {
      "reposts_count": 0, 
      "truncated": false, 
      "text": "#我的第一条微博#", 
      "visible": {
        "type": 0, 
        "list_id": 0
      }, 
      "in_reply_to_status_id": "", 
      "id": 3821898536514864, 
      "mid": "3821898536514864", 
      "source": "<a href=\"http://weibo.com/\" rel=\"nofollow\">微博 weibo.com</a>", 
      "attitudes_count": 0, 
      "in_reply_to_screen_name": "", 
      "in_reply_to_user_id": "", 
      "pic_urls": [], 
      "darwin_tags": [], 
      "favorited": false, 
      "source_allowclick": 0, 
      "idstr": "3821898536514864", 
      "source_type": 1, 
      "user": {
        "bi_followers_count": 1, 
        "domain": "", 
        "avatar_large": "http://tp1.sinaimg.cn/5554103544/180/0/1", 
        "verified_source": "", 
        "ptype": 0, 
        "block_word": 0, 
        "star": 0, 
        "id": 5554103544, 
        "verified_reason_url": "", 
        "city": "8", 
        "verified": false, 
        "credit_score": 80, 
        "block_app": 0, 
        "follow_me": false, 
        "verified_reason": "", 
        "followers_count": 2, 
        "location": "北京 海淀区", 
        "verified_trade": "", 
        "mbtype": 0, 
        "verified_source_url": "", 
        "profile_url": "u/5554103544", 
        "province": "11", 
        "avatar_hd": "http://tp1.sinaimg.cn/5554103544/180/0/1", 
        "statuses_count": 4, 
        "description": "", 
        "friends_count": 5, 
        "online_status": 0, 
        "mbrank": 0, 
        "idstr": "5554103544", 
        "profile_image_url": "http://tp1.sinaimg.cn/5554103544/50/0/1", 
        "allow_all_act_msg": false, 
        "allow_all_comment": true, 
        "geo_enabled": true, 
        "class": 1, 
        "name": "宋假名", 
        "lang": "zh-cn", 
        "weihao": "", 
        "remark": "", 
        "favourites_count": 0, 
        "screen_name": "宋假名", 
        "url": "", 
        "gender": "m", 
        "created_at": "Fri Mar 13 22:50:22 +0800 2015", 
        "verified_type": -1, 
        "following": false, 
        "pagefriends_count": 0, 
        "urank": 2
      }, 
      "geo": null, 
      "created_at": "Thu Mar 19 00:11:21 +0800 2015", 
      "mlevel": 0, 
      "comments_count": 0
    }
  ]
}
```

### `/posts/5554103544?keywords=0`
```[json]
{
  "interval": 0, 
  "hasvisible": false, 
  "total_number": 4, 
  "previous_cursor": 0, 
  "next_cursor": 0, 
  "marks": [], 
  "keywords": "程序员,心理专家,自白,bug bug,", 
  "statuses": [
    "(Test) My favorite game calls that “Defense of the Ancient”. Short title is DotA. It’s a game from Blizzard. You can choose a hero to use. And you should play with other nine players. This is near-health and natural disasters of war. I enjoy the time to win the game.", 
    "(Test) I had the first bicycle which only belong to me is on my 5 years old birthday. A friend of my father sent me the present. But I have not used to play it until I am 7 years old. And after that time, I haven’t had it. Now a bicycle is forward me.", 
    "(Test) 程序员眼中--别人的bug和自己的bug，心理专家的剖析？不，这明明就是程序员的自白，笑cry", 
    "#我的第一条微博#"
  ]
}
```
