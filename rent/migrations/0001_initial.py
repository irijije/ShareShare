# Generated by Django 2.1.7 on 2019-06-13 10:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('item', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservationTime', models.DateTimeField(auto_now_add=True)),
                ('rentDateTime', models.DateTimeField(default=django.utils.timezone.now)),
                ('dueDateTime', models.DateTimeField(default=django.utils.timezone.now)),
                ('extensionTime', models.DateTimeField(null=True)),
                ('star', models.CharField(choices=[('1', '1'), ('1.5', '1.5'), ('2', '2'), ('2.5', '2.5'), ('3', '3'), ('3.5', '3.5'), ('4', '4'), ('4.5', '4.5'), ('5', '5')], default='3', max_length=10)),
                ('review', models.TextField()),
                ('returnTime', models.DateTimeField(null=True)),
                ('returnStatus', models.CharField(choices=[('worst', 'worst'), ('bad', 'bad'), ('normal', 'normal'), ('good', 'good'), ('best', 'best')], default='good', max_length=10)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='item.Item')),
                ('sharee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]