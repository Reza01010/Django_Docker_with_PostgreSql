from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.auth import get_user_model


class TestAcconts(TestCase):
    def setUp(self):
        user = get_user_model().objects.create(username='reza',)
        user.set_password('12345')
        user.save()

        l = self.client.login(username="reza", password="12345")
        self.assertTrue(l)
        self.client.logout()

    def test_and_login(self):
        response = self.client.post(reverse('login'), {
            'username': 'reza',
            'password': '12345',
        })
        self.assertEqual(response.status_code,302)

        response = self.client.post(reverse('login'), {
            'username': 'reza',
            'password': '12345',
        },follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'WELCOME TO HOME !')

    def test_and_signup(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'signup')
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')
        response = self.client.post(reverse('signup'), data={
            'email': 'th85g4jt6347@gmail.com',
            'username': 'nina',
            'password1': 'j54y9yH797gt6r5d',
            'password2': 'j54y9yH797gt6r5d',
        },follow=True)
        self.assertTemplateUsed(response,'registration/login.html')
        self.assertContains(response, 'login')
        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 2)