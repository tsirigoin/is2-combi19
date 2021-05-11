from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.

class UserManagerTests(TestCase):
	def test_create_user(self):
		User = get_user_model()
		user = User.objects.create_user(
			username='user',
			email='normal@user.com',
			first_name='user',
			last_name='resu',
			fecha_nacimiento='1970-01-01',
			password = 'foo'
		)
		self.assertEqual(user.username, 'user')
		self.assertEqual(user.email, 'normal@user.com')
		self.assertEqual(user.first_name, 'user')
		self.assertEqual(user.last_name, 'resu')
		self.assertEqual(user.fecha_nacimiento, '1970-01-01')
		self.assertFalse(user.is_staff)
		self.assertFalse(user.is_superuser)
		with self.assertRaises(TypeError):
			User.objects.create_user()
		with self.assertRaises(TypeError):
			User.objects.create_user(email='')
		with self.assertRaises(ValueError):
			User.objects.create_user(email='', password='foo')
	def test_create_superuser(self):
		User = get_user_model()
		admin_user = User.objects.create_superuser('super@user.com','foo')
		self.assertEqual(admin_user.email,'super@user.com')
		self.assertTrue(admin_user.is_active)
		self.assertTrue(admin_user.is_staff)
		self.assertTrue(admin_user.is_superuser)
		with self.assertRaises(ValueError):
			User.objects.create_superuser(
				email='super@user.com',
				password='foo',
				is_superuser = False
			)