from flask.sessions import SecureCookieSessionInterface, NullSession
from flask_session.sessions import ServerSideSession
from urllib import parse
from pdb import set_trace as bp
from base64 import b64decode
import json
import hmac
from hashlib import sha1


class EicSupersetSecureSessionInterface(SecureCookieSessionInterface):

    def __init__(self, app):
        super(EicSupersetSecureSessionInterface, self).__init__()
        self.session_class = ServerSideSession
        self.app = app
        self.permanent = False

    def __call__(self, environ, start_response):
        self.open_session(environ, start_response)
        return self.app(environ, start_response)

    """Prevent creating session from API requests."""
    def open_session(self, environ, start_response):
        bp()
        cookie = start_response.cookies.get(environ.session_cookie_name)
        if cookie:
            session_data, digest = parse.unquote(cookie, 'utf-8').split('--')
            hmac_generated = hmac.new(bytes(environ.secret_key, 'utf-8'), bytes(session_data, 'utf-8'), sha1).hexdigest()
            if hmac.compare_digest(hmac_generated, digest):
                data = json.loads(b64decode(session_data).decode('utf-8'))
                return self.session_class(data['auth'], sid=data['session_id'], permanent=self.permanent)
        return None

    def make_null_session(self, app):
        return NullSession()

    def save_session(self, app, session, response):
        # need to find something to write the session cookie
        pass