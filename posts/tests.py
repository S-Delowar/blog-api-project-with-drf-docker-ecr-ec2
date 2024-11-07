from django.test import TestCase
from django.contrib.auth import get_user_model

from posts.models import Post

# Create your tests here.
class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@mail.com",
            password="testpass"
        )
        
        cls.post = Post.objects.create(
            author = cls.user,
            title = "A Good Title",
            body = "Nice Body Content"
        )
        
    def test_post_model(self):
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.title, "A Good Title")
        self.assertEqual(self.post.body, "Nice Body Content")
        self.assertEqual(str(self.post), "A Good Title")