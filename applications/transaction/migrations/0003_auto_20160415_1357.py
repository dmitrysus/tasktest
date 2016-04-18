# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_auto_20160415_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='account',
            field=models.DecimalField(null=True, verbose_name=b'\xd1\x81\xd1\x87\xd0\xb5\xd1\x82', max_digits=10, decimal_places=2, blank=True),
            preserve_default=True,
        ),
    ]
