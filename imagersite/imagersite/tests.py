from django.test import TestCase


class LoginTest(TestCase):
    def test_login(self):
        """ test for successful login """
        self.client  # client fpr testing requests

        response = self.client.post('/accounts/login/', {'username': 'tester2',
                                    'password': 'code@1234'})
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        """ test to see if login page is loading when users go to the
            login route """
        self.client
        response = self.client.get('/accounts/login/')
        # import pdb; pdb.set_trace()
        self.assertEqual(response.template_name[0], 'registration/login.html')

    def test_home_page(self):
        """ test if message passed onto home page is present when
            users go to home page route """
        self.client
        response = self.client.get('/')
        # import pdb; pdb.set_trace()
        self.assertEqual(response.context[-1]['message'], 'Hello World')

    def test_registration_page(self):
        """ test to see if login page is loading when users go to the
            registration route  """
        self.client
        response = self.client.get('/accounts/register/')
        # import pdb; pdb.set_trace()
        self.assertEqual(response.template_name[0],
                         'registration/registration_form.html')
