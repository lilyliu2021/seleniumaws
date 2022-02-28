import unittest
import moodle_locators as locators
import moodle_methods as methods


class MoodleAppPositiveTestCases(unittest.TestCase):  #create class

    @staticmethod              #signals to unittest that this is a static method
    def test_create_new_user():
        methods.setUp()
        methods.log_in(locators.admin_username,locators.admin_password)
        methods.add_user()
        methods.search_user()
        methods.log_out()
        methods.log_in(locators.user_name,locators.password)
        methods.check_new_user_can_login()
        methods.log_out()
        methods.log_in(locators.admin_username,locators.admin_password)
        methods.delete_user()
        methods.log_out()
        methods.tearDown()


# # create new use
# setUp()
# log_in(locators.admin_username, locators.admin_password)
# add_user()
# search_user()
# log_out()
#
# # login new_user
# log_in(locators.user_name, locators.password)
# check_new_user_can_login()
# sleep(0.25)
# log_out()
# logger('create')
#
# #delete new_user
# log_in(locators.admin_username,locators.admin_password)
# delete_user()
# log_out()
#
# tearDown()

