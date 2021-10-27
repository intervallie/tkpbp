from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
class UserAccountTests(TestCase):
    def test_new_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser(
            'tes@tesapp.com',
            'tes',
            password = 'password'
        )
        self.assertEqual(str(super_user),'tes')
        self.assertEqual(super_user.email,'tes@tesapp.com')
        self.assertEqual(super_user.name, 'tes')
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_active)

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                'tes@tesapp.com',
                'tes',
                True,
                password = 'password',
                is_staff = False, 
                is_superuser = False
            )
    def test_new_user(self):
        db = get_user_model()
        super_user = db.objects.create_superuser(
            'tes@tesapp.com',
            'tes',
            password = 'password'
        )
        