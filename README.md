# soahomework1
Tiny website using Weibo's OAuth2 API. Experiment mode. Only limited Weibo users are allowed.

## Website
[http://soahomework1.sinaapp.com](http://soahomework1.sinaapp.com)

## API
`/users`: show all users in JSON format.

`/posts/<uid>`: show the first 100 posts of user with uid `<uid>` in JSON format

`/posts/<uid>?keywords=1`: show the first 100 posts of user with uid `<uid>` in JSON format, with "keywords" field

`/posts/<uid>?keywords=0`: same as keywords=1, but simplified the "statuses" field with only "text"
