# Generated by Django 4.0.3 on 2022-07-20 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_delete_category_remove_post_author_post_file_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hook_text',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
