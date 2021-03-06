# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-01-25 22:30
from __future__ import unicode_literals

from django.db import migrations

def update_tags_with_dbmodel(apps, schema_editor):

    Tag = apps.get_model('typeclasses', 'Tag')

    ObjectDB = apps.get_model('objects', 'ObjectDB')
    for obj in ObjectDB.objects.all().exclude(db_tags__db_model="objectdb"):
        for tag in obj.db_tags.all().exclude(db_model="objectdb"):
            obj.db_tags.remove(tag)
            newtag = Tag(db_key=tag.db_key, db_category=tag.db_category,
                         db_data=tag.db_data, db_tagtype=tag.db_tagtype, db_model="objectdb")
            newtag.save()
            obj.db_tags.add(newtag)

    PlayerDB = apps.get_model('players', 'PlayerDB')
    for obj in PlayerDB.objects.all().exclude(db_tags__db_model="playerdb"):
        for tag in obj.db_tags.all().exclude(db_model="playerdb"):
            obj.db_tags.remove(tag)
            newtag = Tag(db_key=tag.db_key, db_category=tag.db_category,
                         db_data=tag.db_data, db_tagtype=tag.db_tagtype, db_model="playerdb")
            newtag.save()
            obj.db_tags.add(newtag)

    ScriptDB = apps.get_model('scripts', 'ScriptDB')
    for obj in ScriptDB.objects.all().exclude(db_tags__db_model="scriptdb"):
        for tag in obj.db_tags.all().exclude(db_model="scriptdb"):
            obj.db_tags.remove(tag)
            newtag = Tag(db_key=tag.db_key, db_category=tag.db_category,
                         db_data=tag.db_data, db_tagtype=tag.db_tagtype, db_model="scriptdb")
            newtag.save()
            obj.db_tags.add(newtag)

    ChannelDB = apps.get_model('comms', 'ChannelDB')
    for obj in ChannelDB.objects.all().exclude(db_tags__db_model="channeldb"):
        for tag in obj.db_tags.all().exclude(db_model="channeldb"):
            obj.db_tags.remove(tag)
            newtag = Tag(db_key=tag.db_key, db_category=tag.db_category,
                         db_data=tag.db_data, db_tagtype=tag.db_tagtype, db_model="channeldb")
            newtag.save()
            obj.db_tags.add(newtag)

    HelpEntry = apps.get_model('help', 'HelpEntry')
    for obj in HelpEntry.objects.all().exclude(db_tags__db_model="helpentry"):
        for tag in obj.db_tags.all().exclude(db_model="helpentry"):
            obj.db_tags.remove(tag)
            newtag = Tag(db_key=tag.db_key, db_category=tag.db_category,
                         db_data=tag.db_data, db_tagtype=tag.db_tagtype, db_model="helpentry")
            newtag.save()
            obj.db_tags.add(newtag)

    Msg = apps.get_model('comms', 'Msg')
    for obj in Msg.objects.all().exclude(db_tags__db_model="msg"):
        for tag in obj.db_tags.all().exclude(db_model="msg"):
            obj.db_tags.remove(tag)
            newtag = Tag(db_key=tag.db_key, db_category=tag.db_category,
                         db_data=tag.db_data, db_tagtype=tag.db_tagtype, db_model="msg")
            newtag.save()
            obj.db_tags.add(newtag)


class Migration(migrations.Migration):

    dependencies = [
        ('typeclasses', '0006_auto_add_dbmodel_value_for_tags_attributes'),
    ]

    operations = [

        migrations.AlterUniqueTogether(
            name='tag',
            unique_together=set([('db_key', 'db_category', 'db_tagtype', 'db_model')]),
        ),
        migrations.AlterIndexTogether(
            name='tag',
            index_together=set([('db_key', 'db_category', 'db_tagtype', 'db_model')]),
        ),

        migrations.RunPython(update_tags_with_dbmodel)
    ]
