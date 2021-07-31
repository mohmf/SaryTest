from django.db import models

# Base model of comments
class Comment(models.Model):
    body = models.TextField(blank=False)
    user = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.body

class Question(models.Model):
    body = models.CharField(max_length=300)
    user = models.ForeignKey('auth.User', related_name='questions', on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.body

class QuestionComment(Comment):
    question = models.ForeignKey('Question', related_name='question_comments', on_delete=models.CASCADE)
    
class Answer(models.Model):
    body = models.TextField(blank=False)
    user = models.ForeignKey('auth.User', related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey('Question', related_name='answers', on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.body

class Tag(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    user = models.ForeignKey('auth.User', related_name='tags', on_delete=models.CASCADE)
    questions = models.ManyToManyField('Question', related_name='tags', blank=True)
    def __str__(self) -> str:
        return self.name

# class QuestionComment(models.Model):
#     body = models.TextField(blank=False)
#     user = models.ForeignKey('auth.User', related_name='question_comments', on_delete=models.CASCADE)
#     question = models.ForeignKey('Question', related_name='question_comments', on_delete=models.CASCADE)
#     def __str__(self) -> str:
#         return self.body

