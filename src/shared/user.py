import json

import requests

# from variables import API_cfg


class User:
    bearer = None

    def __init__(self, username=None, userpass=None):
        self._username = username
        self._userpass = userpass

    @property
    def username(self):
        return self._username

    @property
    def userpass(self):
        return self._userpass

    @property
    def auth_bearer(self):
        return self.bearer

    @staticmethod
    def default_user():
        return User(API_cfg['user_name'], API_cfg['user_pass'])

    # possibility to check getting data when authorized
    @staticmethod
    def no_user():
        return User()

    def login(self):
        # assume that current user is no_user
        if not self.username:
            User.bearer = ''
            return

        r = requests.get(f'{API_cfg["auth_url"]}/{API_cfg["tenant_id"]}/oauth2/v2.0/authorize', params={
            'client_id': API_cfg['client_id'],
            'response_type': 'id_token',
            'redirect_uri': API_cfg['base_url'],
            'response_mode': 'fragment',
            'scope': 'openid profile',
            'state': 12345,
            'prompt': 'select_account',
            'nonce': '67890'
        })

        fpc_cookie = r.cookies['fpc']
        buid_cookie = r.cookies['buid']
        esctx_cookie = r.cookies['esctx']

        cfg = str(r.content)
        cfg = cfg.split('$Config=')[1].split(';')[0]
        cfg = cfg.replace(cfg.split('"sSMSCtryPhoneData":"')[1].split('"')[0], '')
        cfg = json.loads(cfg)

        ctx = cfg.get('sCtx', None)
        canary = cfg.get('canary', None)
        flow_token = cfg.get('sFT', None)
        request_id = r.headers.get('x-ms-request-id', None)

        r = requests.post(f'{API_cfg["auth_url"]}/{API_cfg["tenant_id"]}/login',
                          allow_redirects=False,
                          data={
                              'login': self.username,
                              'passwd': self.userpass,
                              'ctx': ctx,
                              'canary': canary,
                              'hpgrequestid': request_id,
                              'flowToken': flow_token,
                              'LoginOptions': 3,
                          },
                          headers={
                              'Cookie': ';'.join([f'buid={buid_cookie}', f'fpc={fpc_cookie}', f'esctx={esctx_cookie}'])
                          })

        location = r.headers.get('Location', None)
        User.bearer = location.split('id_token=')[1].split('&')[0]
