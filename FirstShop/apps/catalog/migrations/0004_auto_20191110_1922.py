# Generated by Django 2.2.4 on 2019-11-10 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20191109_1826'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['INDX'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='INDX',
            field=models.IntegerField(default=0, help_text='Specify index number for sorting order'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(help_text='Enter a book category (e.g. Classic)', max_length=25),
        ),
        migrations.AlterField(
            model_name='category',
            name='top_category',
            field=models.ForeignKey(help_text='Enter a book top category (e.g. Language, Genre)', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_category', to='catalog.Category'),
        ),
    ]