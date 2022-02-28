from faker import Faker

fake = Faker(locale='en_CA')

# ---------------------locators session-------------------
app = 'Moodle'
admin_username = 'Lilyliu'
admin_password = 'Spring2022@'
app_homepage_url = 'http://52.39.5.126/'
app_homepage_title = 'Software Quality Assurance Testing'
app_login_url = 'http://52.39.5.126/login/index.php'
app_login_title = 'Software Quality Assurance Testing: Log in to the site'
app_dashboard_url = 'http://52.39.5.126/my/'
app_dashboard_title = 'Dashboard'
app_addnewuser_title = 'SQA: Administration: Users: Accounts: Add a new user'
app_user_mainpage_url = 'http://52.39.5.126/admin/user.php'
app_user_mainpage_title = 'SQA: Administration: Users: Accounts: Browse list of users'

# --------------------data session--------------------
first_name = fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'
middle_name = fake.first_name()
user_name = f'{first_name}{last_name}'.lower()
email = f'{user_name}@{fake.free_email_domain()}'
password = fake.password()
moodle_net_profile = f'https://moodle net/{user_name}'
city = fake.city()
country = fake.current_country()
description = f'User added by {admin_username} via Python Automated Script'
# or description=fake.sentence(nb_words=100)
pic_desc = f'Pic uploaded by {full_name}'
list_of_interests = [fake.job(), fake.job(), fake.job(), fake.job()]
web_page = fake.url()
icq_num = fake.pyint(111111, 999999)
sky_id = user_name
aim_id = f'{last_name.lower()}{fake.pyint(11, 999)}'
yahoo_id = user_name
msn_id = f'{last_name.lower()}{fake.pyint(11, 99)}{country}'
id_num = fake.pyint(1111111, 9999999)
institution = fake.company()
department = fake.catch_phrase()
phone = fake.phone_number()
mobile_phone = fake.phone_number()
address = fake.address().replace("\n", " ")
list_opt = ['Web page', 'ICQ number', 'Skype ID', 'AIM ID', 'Yahoo ID', 'MSN ID',
            'ID number', 'Institution', 'Department',
            'Phone', 'Mobile phone', 'Address']
list_ids = ['id_url', 'id_icq', 'id_skype', 'id_aim', 'id_yahoo', 'id_msn',
            'id_idnumber', 'id_institution', 'id_department',
            'id_phone1', 'id_phone2', 'id_address']
list_val = [web_page, icq_num, sky_id, aim_id, yahoo_id, msn_id, id_num, institution, department, phone, mobile_phone,
            address]

# print(list_val)
# print(list_of_interests)
