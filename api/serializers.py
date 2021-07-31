from django.db.models import fields
from rest_framework import serializers
from .models import Question,QuestionComment,Answer,Tag
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    questions = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    asnwers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username','questions','answers']

class QuestionCommentSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = QuestionComment
        fields = ['pk','body', 'user','question']

class AnswerSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Answer
        fields = ['pk','body', 'user','question']

class TagSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source='user.username')
    # questions = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Tag
        fields = ['id', 'name']        

class QuestionSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source='user.username')
    question_comments = QuestionCommentSerializer(many=True, read_only=True)
    answers = AnswerSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ['pk','body','user','question_comments','answers','tags']

