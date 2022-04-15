from django import setup
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_markdown.settings')
setup()
from registration.models import User


user, created = User.objects.get_or_create(
    username='admin', email='admin@admin.com',
    is_superuser=True, is_staff=True, is_active=True,
    employee_number=1
)
if created:
    user.set_password('testuser')
    user.save()

user, created = User.objects.get_or_create(
    username='test01', email='test01@test.com',
    is_superuser=False, is_staff=True, is_active=True,
    employee_number=2
)
if created:
    user.set_password('testuser')
    user.save()

user, created = User.objects.get_or_create(
    username='test02', email='test02@test.com',
    is_superuser=False, is_staff=True, is_active=True,
    employee_number=3
)
if created:
    user.set_password('testuser')
    user.save()

user, created = User.objects.get_or_create(
    username='test03', email='test03@test.com',
    is_superuser=False, is_staff=True, is_active=True,
    employee_number=4
)
if created:
    user.set_password('testuser')
    user.save()

