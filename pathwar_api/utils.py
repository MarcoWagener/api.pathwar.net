from app import app


def request_get_user(request):
    auth = request.authorization
    if auth.get('username'):
        if auth.get('password'):  # user:pass
            app.logger.warn('FIXME: check password')
            return app.data.driver.db['users'].find_one({
                'login': auth.get('username'),
                'active': True
            })
        else:  # token
            user_token = app.data.driver.db['user-tokens'] \
                                        .find_one({
                                            'token': auth.get('username')
                                        })
            if user_token:
                return app.data.driver.db['users'] \
                                      .find_one({'_id': user_token['user']})
    return None


def default_session():
    return app.data.driver.db['sessions'].find_one({
        'name': 'Worldwide'
    })
