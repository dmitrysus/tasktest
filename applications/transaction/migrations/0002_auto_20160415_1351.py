# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='account',
            field=models.DecimalField(null=True, verbose_name=b'\xd1\x81\xd1\x87\xd0\xb5\xd1\x82', max_digits=2, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='vatin',
            field=models.PositiveIntegerField(null=True, verbose_name=b'\xd0\x98\xd0\x9d\xd0\x9d', blank=True),
            preserve_default=True,
        ),
    ]
