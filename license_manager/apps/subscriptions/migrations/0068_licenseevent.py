# Generated by Django 4.2.13 on 2024-06-25 07:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0067_editable_desired_num_licenses'),
    ]

    operations = [
        migrations.CreateModel(
            name='LicenseEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('event_name', models.CharField(max_length=255)),
                ('license', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='events', to='subscriptions.license')),
            ],
            options={
                'verbose_name': 'License Triggered Event',
                'verbose_name_plural': 'License Triggered Events',
            },
        ),
    ]
