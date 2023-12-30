from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse


class Author(models.Model):
    autorUser = models.OneToOneField(User,on_delete = models.CASCADE)
    rating = models.SmallIntegerField(default = 0)


    def update_rating(self):
        postRat = self.post_set.aggregate(postRating= Sum('rating'))
        pRat = 0
        pRat += postRat.get('postRating')

        commentRat = self.autorUser.comment_set.agregate(commentRating=Sum('rating'))
        cRat = 0
        cRat += commentRat.get('commentRating')

        self.rating = pRat * 3 + cRat
        self.save()

class Category(models.Model):
    name = models.CharField(max_length = 64, unique =True)
    subscribers = models.ManyToManyField(User, related_name='subscribers',flat = True)
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=128, null=False)
    postAuthor = models.ForeignKey(Author, on_delete=models.CASCADE)
    dateTime = models.DateTimeField(auto_now_add =True)
    postCategory = models.ManyToManyField(Category, through='PostCategory')
    text = models.TextField(default= 'Some Text')
    rating = models.SmallIntegerField(default = 0)
    NEWS = 'NW'
    ARTICLE = "AR"
    CAT_CHOICES = [
        (NEWS, 'новость'),
        (ARTICLE, 'статья')]
    categoryType = models.CharField(max_length=2,choices = CAT_CHOICES,default = ARTICLE)

    added_at = models.DateTimeField(
         auto_now=True
     )

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f'{self.title}...' \
               f'{self.text[:123]}'

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])
    def __str__(self):
        return f'{self.title}: {self.text[:20]}'

class PostCategory(models.Model):
    postTrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryTrough = models.ForeignKey(Category, on_delete = models.CASCADE)

class Comment(models.Model):
    postComment = models.ForeignKey(Post, on_delete = models.CASCADE)
    userComment = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(default = 'Текст комментария')
    dt = models.DateTimeField(auto_now_add =True)
    rating = models.SmallIntegerField(default = 0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

