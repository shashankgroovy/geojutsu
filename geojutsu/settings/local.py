DEBUG = True

SECRET_KEY = 'zyk135#fb9k!fshlxrnv%(@9)ym82fa95d*_u__ug@jsc2*q9m'


import mongoengine

_MONGODB_USER = ''
_MONGODB_PASSWD = ''
_MONGODB_HOST = 'localhost'
_MONGODB_NAME = 'mozio'

if _MONGODB_USER:
    _MONGODB_DATABASE_HOST = 'mongodb://%s:%s@%s/%s' % (
        _MONGODB_USER, _MONGODB_PASSWD, _MONGODB_HOST, _MONGODB_NAME)
#_MONGODB_DATABASE_HOST = 'mongodb://%s/%s' % (_MONGODB_HOST, _MONGODB_NAME)

# using a mongolab instance instead.
# TODO: Move the URI to a config variable. Don't expose the DB URI. 
_MONGODB_DATABASE_HOST = 'mongodb://test:test@ds013564.mlab.com:13564/mozio'

mongoengine.connect(_MONGODB_NAME, host=_MONGODB_DATABASE_HOST)
