# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0002_auto_20160929_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='char_class',
            field=models.CharField(choices=[('ARCANE DUELIST', 'Arcane Duelist'), ('BARBARIAN', 'Barbarian'), ('BARD', 'Bard'), ('CLERIC', 'Cleric'), ('DRUID', 'Druid'), ('FIGHTER', 'Fighter'), ('IMMOLATOR', 'Immolator'), ('PALADIN', 'Paladin'), ('RANGER', 'Ranger'), ('THIEF', 'Thief'), ('WIZARD', 'Wizard')], max_length=255),
        ),
    ]
