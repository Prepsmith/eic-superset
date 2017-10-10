"""
This is the main user class
"""
from flask_appbuilder.security.sqla.models import User
from flask_appbuilder.security.views import UserDBModelView
from flask.ext.babel import lazy_gettext


class MyUser(User):
    private_fields = 'access_toke refresh_token signature instance_url'.split()
    public_fields = 'id_url username user_id issued_at display_name email license sobject extra'.split()
    fields = private_fields + public_fields

    def __init__(self, params):
        super(MyUser, self).__init__()
        self._read_fields_from(params)

    @property
    def fields(self):
        return self.fields

    def read_from(self, session):
        return self._read_fields_from(session, 'auth')

    def write_to(self, session):
        self._write_fields_to(session, 'auth')

    def sign_in(self):
        return getattr(self, 'user_id', None)

    def _read_fields_from(self, source, prefix=None):
        for field in self.fields:
            if prefix:
                return field, source[prefix][field] if prefix in source else field
            else:
                return source, source[field]

    def _write_fields_to(self, destination, prefix=None):
        for field in self.fields:
            if prefix:
                destination.update({prefix: {} if prefix not in destination else destination[prefix]})
                destination[prefix].update(field)
            else:
                destination.update({field: field})


class MyUserDBModelView(UserDBModelView):
    """
        View that add DB specifics to User view.
        Override to implement your own custom view.
        Then override userdbmodelview property on SecurityManager
    """

    show_fieldsets = [
        (lazy_gettext('User info'),
         {'fields': ['username', 'active', 'roles', 'login_count']}),
        (lazy_gettext('Personal Info'),
         {'fields': ['first_name', 'last_name', 'email'], 'expanded': True}),
        (lazy_gettext('Audit Info'),
         {'fields': ['last_login', 'fail_login_count', 'created_on',
                     'created_by', 'changed_on', 'changed_by'], 'expanded': False}),
    ]

    user_show_fieldsets = [
        (lazy_gettext('User info'),
         {'fields': ['username', 'active', 'roles', 'login_count']}),
        (lazy_gettext('Personal Info'),
         {'fields': ['first_name', 'last_name', 'email'], 'expanded': True}),
    ]

    add_columns = ['first_name', 'last_name', 'username', 'active', 'email', 'roles', 'password', 'conf_password']
    list_columns = ['first_name', 'last_name', 'username', 'email', 'active', 'roles']
    edit_columns = ['first_name', 'last_name', 'username', 'active', 'email', 'roles']