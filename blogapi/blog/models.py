from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=20)
    joined = models.DateTimeField(auto_now_add=True)
    bio = models.TextField(max_length=10000)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Article(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    content = models.TextField(max_length=100000)
    written_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
    
class Comments(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE,related_name="comment")
    comment = models.TextField(max_length=100000,null=True,blank=True)
    written_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.comment[:100]}..."
    

