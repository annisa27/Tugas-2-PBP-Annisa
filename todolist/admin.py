from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
user = User.objects.create_user('annisaui', 'annisa.az@ui.ac.id','annisa123')
user.save()