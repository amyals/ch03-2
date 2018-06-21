from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.

class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

	def approved_comments(self):
		return self.comments.filter(approved_comment=True)
		# 와 오타 실화냐 comment->Comments
		# ㄴㄴㄴㄴ 뭐가 오탄ㄴ거지 왜 갑자기 되지??
	def like_count(self):
		return self.like.filter(like_count=True)


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Like(models.Model):
	post = models.ForeignKey('blog.Post', related_name='like')
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	# text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	like_count = models.BooleanField(default=False)

	def count(self):
		self.like_count = True
		self.save()

	# def __str__(self):
	# 	return self.text
