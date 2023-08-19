# Generated by Django 4.2.4 on 2023-08-19 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_tag_opportunities'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='opportunities',
        ),
        migrations.AddField(
            model_name='opportunity',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='opportunities', to='base.tag'),
        ),
    ]
