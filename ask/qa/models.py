from django.db import models
from django.contrib.auth.models import User

"""
Question - вопрос
title - заголовок вопроса
text - полный текст вопроса
added_at - дата добавления вопроса
rating - рейтинг вопроса (число)
author - автор вопроса
likes - список пользователей, поставивших "лайк"

QuestionManager - менеджер модели Question
new - метод возвращающий последние добавленные вопросы
popular - метод возвращающий вопросы отсортированные по рейтингу

Answer - ответ
text - текст ответа
added_at - дата добавления ответа
question - вопрос, к которому относится ответ
author - автор ответа

В качестве модели пользователя - используйте django.contrib.auth.models.User  из стандартной системы авторизации Django.
"""
class Question(models.Model):
	objects = QuestionManager()
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	likes = models.ManyToManyField(User, related_name='question_like_user')

	
class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	question = models.OneToOneField(Question)
	author = models.ForeignKey(User, on_delete=models.CASCADE)


class QuestionManager(models.Manager):
	def new(self):
		return self.order_by('-added_at')
	
	def popular(self):
		return self.order_by('-rating')
