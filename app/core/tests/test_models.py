from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='test@afleh.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_sucessful(self):
        """Test creating a new user with a email is successful"""

        email = 'abhishekpaul180@gmail.com'
        password = 'meerapaulrocks'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test the email for a new user is normalized"""

        email = "abhishekpaul180@GMAIL.COM"
        user = get_user_model().objects.create_user(email, 'meerapaulrocks')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test creating user with no email raises error"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "abshdbas")

    def test_new_user_superuser(self):
        """test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'test1234'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """TEst the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Ripped style'

        )

        self.assertEqual(str(tag), tag.name)

    def test_store_link_str(self):
        """Test the ingredient string representation"""
        store_link = models.Store_link.objects.create(
            user=sample_user(),
            name='http://www.myntra.com'
        )

        self.assertEqual(str(store_link), store_link.name)

    def test_picUpload_str(self):
        """Test the upload string representation"""
        picUpload = models.PicUpload.objects.create(
            user=sample_user(),
            title='One Piece',
            price=5.00
        )

        self.assertEqual(str(picUpload), picUpload.title)

