# Generated by Django 2.1 on 2018-10-20 09:38

import apps.events.models
import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField(blank=True, default='1997-11-1')),
                ('location', models.CharField(max_length=100)),
                ('description', ckeditor.fields.RichTextField(blank=True, max_length=5120)),
                ('imageFile', models.ImageField(blank=True, null=True, upload_to=apps.events.models.get_image_path)),
                ('lan', models.DecimalField(blank=True, decimal_places=145, max_digits=150, null=True)),
                ('lng', models.DecimalField(blank=True, decimal_places=145, max_digits=150, null=True)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InvolvedEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default='2006-10-25 14:30:59')),
                ('imageFile', models.ImageField(blank=True, null=True, upload_to=apps.events.models.get_image_path)),
                ('message', ckeditor.fields.RichTextField(max_length=256)),
                ('likes', models.IntegerField(default=0)),
                ('type', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('eventID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
            ],
        ),
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('eventID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
                ('postID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Post')),
            ],
        ),
        migrations.CreateModel(
            name='ReplyTo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postwriter', to='events.Post')),
                ('eventID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
                ('postID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='events.Post')),
                ('replier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postreplier', to='events.Post')),
            ],
        ),
    ]