# Generated by Django 2.1.9 on 2019-07-12 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_store_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='PicUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('designer_details', models.CharField(blank=True, max_length=255)),
                ('contact_info', models.CharField(blank=True, max_length=255)),
                ('store_link', models.ManyToManyField(to='core.Store_link')),
                ('tags', models.ManyToManyField(to='core.Tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]