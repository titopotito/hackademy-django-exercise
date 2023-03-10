from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class TestViews(TestCase):
    def setUp(self):
        self.first_name = 'james'
        self.last_name = 'tito'
        self.username = 'jamestito'
        self.email = 'test_email@gmail.com'
        self.password = 'testpassword12345'

    def test_register_view_GET(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_register_view_POST(self):
        response = self.client.post(reverse('register'), data={
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'email': self.email,
            'password1': self.password,
            'password2': self.password
        })

        # test if REGISTER_VIEW successfully redirected to LOGIN PAGE after successful registration
        self.assertRedirects(response, expected_url=reverse('login'), status_code=302,
                             target_status_code=200, fetch_redirect_response=True)

        # test if USER object is created after successful registration
        users = User.objects.all()
        self.assertEqual(users.count(), 1)

        # test if the created USER object has a PROFILE object after successful registration
        user = users[0]
        self.assertIsNotNone(user.profile)
