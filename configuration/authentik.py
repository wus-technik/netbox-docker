from os import environ
from netbox.configuration import *

#############
# Docker
#############

# python-social-auth configuration
SOCIAL_AUTH_OIDC_OIDC_ENDPOINT = environ.get('SOCIAL_AUTH_OIDC_OIDC_ENDPOINT')
SOCIAL_AUTH_OIDC_KEY = environ.get('SOCIAL_AUTH_OIDC_KEY')
SOCIAL_AUTH_OIDC_SECRET = environ.get('SOCIAL_AUTH_OIDC_SECRET')
SOCIAL_AUTH_OIDC_SCOPE = environ.get('SOCIAL_AUTH_OIDC_SCOPE', 'openid profile email').split(' ')
SOCIAL_AUTH_PROTECTED_USER_FIELDS = ['groups']
LOGOUT_REDIRECT_URL = environ.get('LOGOUT_REDIRECT_URL', '/')
