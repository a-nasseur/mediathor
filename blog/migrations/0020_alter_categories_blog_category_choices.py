# Generated by Django 3.2 on 2021-04-16 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_article_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='blog_category_choices',
            field=models.CharField(choices=[('Actualité', 'Actualité'), ('Littérature', 'Littérature'), ('Culture', 'Culture'), ('Evènement', 'Evènement'), ('Best Sellers', 'Best Sellers')], default='Actualité', max_length=20),
        ),
    ]
