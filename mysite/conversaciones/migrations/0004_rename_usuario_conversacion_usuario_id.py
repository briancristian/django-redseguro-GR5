# Generated by Django 5.1 on 2024-09-10 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversaciones', '0003_rename_usuario_id_conversacion_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversacion',
            old_name='usuario',
            new_name='usuario_id',
        ),
    ]