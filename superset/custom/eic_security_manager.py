from flask_appbuilder.security.sqla.manager import SecurityManager
from pdb import set_trace as bp
from superset.custom.user import MyUser, MyUserDBModelView
import logging

# logging.basicConfig(filename='loutre.log', level=logging.DEBUG)


class EicSupersetSecurityManager(SecurityManager):
    # user_model = MyUser
    userdbmodelview = MyUserDBModelView

    def __init__(self, appbuilder):
        super(EicSupersetSecurityManager, self).__init__(appbuilder)
        # logging.info('#########################################')
        # logging.info('We are here again')
        # logging.info('#########################################')