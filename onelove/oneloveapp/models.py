from django.db import models

class BlogPost(models.Model):
    """
    Model representing a blog post.

    Attributes:
        title (CharField): The title of the blog post, limited to 255 characters.
        content (TextField): The content or body of the blog post.
        date_posted (DateTimeField): The date and time when the blog post was created,
                                    automatically set to the current date and time when the post is added.
    """

    title = models.CharField(max_length=255)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
