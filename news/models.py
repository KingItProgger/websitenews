from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse



# Create your models here.



class Author(models.Model):
    author=models.OneToOneField(User,on_delete=models.CASCADE)

    rating=models.IntegerField(default=0)

    def update_rating(self):
        post_rating=self.post_set.aggregate(rating_post=Sum('rating'))
        post_r=0
        post_r+=post_rating.get('rating_post')

        comment_rating = self.comment_set.aggregate(rating_comment=Sum('rating'))
        comment_r = 0
        comment_r += comment_rating.get('rating_comment')

        self.rating=comment_r+post_r*3
        self.save()

class Category(models.Model):
    topic=models.CharField(max_length=64,unique=True)

class Post(models.Model):
    CHOICE = [('news', 'новость'), ('article', 'статья')]

    title=models.CharField(max_length=64)
    category=models.CharField(max_length=16,choices=CHOICE)
    datetime=models.DateTimeField(auto_now_add=True)
    text=models.TextField()
    rating=models.IntegerField(default=0)
    author= models.ForeignKey(Author,on_delete=models.CASCADE)
    categories=models.ManyToManyField(Category,through='PostCategory')



    def like(self):
        self.rating+=1
        self.save()

    def dislike(self):
        self.rating-=1
        self.save()

    def preview(self):
        return f'{self.text[:123]}...'

    def get_absolute_url(self):
        return reverse('post', args=[str(self.id)])

    def __str__(self):
        return self.title.title()

class PostCategory(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)


class Comment(models.Model):
    datetime=models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField()
    rating=models.IntegerField(default=0)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

