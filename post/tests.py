from django.test import TestCase
from .models import Hashtag, Post
from django.contrib.auth import get_user_model


class HashtagModelTest(TestCase):
    def test_hashtag_creation(self):
        hashtag = Hashtag.objects.create(name="testhashtag")
        self.assertEqual(str(hashtag), "testhashtag")


class PostModelTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            email="test@example.com",
            password="testpassword",
            first_name="John",
            last_name="Doe",
        )
        self.hashtag1 = Hashtag.objects.create(name="testhashtag1")
        self.hashtag2 = Hashtag.objects.create(name="testhashtag2")

    def test_post_creation(self):
        post = Post.objects.create(
            owner=self.user,
            title="Test Post",
            text="This is a test post.",
        )
        post.hashtags.add(self.hashtag1, self.hashtag2)

        self.assertEqual(str(post), "Test Post")
        self.assertEqual(post.owner, self.user)
        self.assertEqual(post.text, "This is a test post.")
        self.assertEqual(post.hashtags.count(), 2)
