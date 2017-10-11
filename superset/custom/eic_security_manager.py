from flask_appbuilder.security.sqla.manager import SecurityManager
# from pdb import set_trace as bp
from superset.custom.user import MyUser, MyUserDBModelView


class EicSupersetSecurityManager(SecurityManager):
    user_model = MyUser
    userdbmodelview = MyUserDBModelView
