from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import User, UserProfile


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="test@example.com",
            password="testpassword",
            first_name="John",
            last_name="Doe",
        )

    def test_create_user(self):
        self.assertTrue(isinstance(self.user, User))
        self.assertEqual(self.user.email, "test@example.com")
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

    def test_create_superuser(self):
        superuser = User.objects.create_superuser(
            email="admin@example.com",
            password="adminpassword",
            first_name="Admin",
            last_name="User",
        )
        self.assertTrue(isinstance(superuser, User))
        self.assertEqual(superuser.email, "admin@example.com")
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)


class UserProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="test@example.com",
            password="testpassword",
            first_name="John",
            last_name="Doe",
        )
        self.profile = UserProfile.objects.create(
            owner=self.user,
            username="johndoe",
            profile_picture=None,
            bio="Test bio",
        )

    def test_user_profile_creation(self):
        self.assertTrue(isinstance(self.profile, UserProfile))
        self.assertEqual(self.profile.owner, self.user)
        self.assertEqual(self.profile.username, "johndoe")
        self.assertEqual(self.profile.bio, "Test bio")
