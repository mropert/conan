import os
import unittest

from conans.server.server_launcher import load_authentication_plugin
from conans.test.utils.test_files import temp_folder
from conans.util.files import save


class AuthenticatorPluginTest(unittest.TestCase):

    def instance_authenticator_test(self):
        folder = temp_folder()
        plugin_path = os.path.join(folder, "plugins", "authenticator", "my_auth.py")
        my_plugin = '''
def get_class():
    return MyAuthenticator()


class MyAuthenticator(object):
    def valid_user(self, username, plain_password):
        return username == "foo" and plain_password == "bar"
'''
        save(plugin_path, my_plugin)

        plugin = load_authentication_plugin(folder, "my_auth")
        self.assertTrue(plugin.valid_user("foo", "bar"))
        self.assertFalse(plugin.valid_user("foo2", "bar2"))
