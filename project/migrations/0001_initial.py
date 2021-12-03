# Generated by Django 3.2.9 on 2021-12-03 08:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Название проекта', max_length=100)),
                ('purpose', models.TextField(help_text='Цель(-ли) проекта')),
                ('issue', models.TextField(help_text='Задача(-и) проекта')),
                ('managment_info', models.TextField(help_text='Обязательные мероприятия по скраму')),
                ('calendar_info', models.TextField(help_text='План работ и контрольные точки')),
                ('result_info', models.TextField(help_text='Результаты проекта')),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название ресурса проекта', max_length=40)),
                ('link', models.URLField(help_text='Ссылка на проектный ресурс', max_length=100)),
                ('type', models.CharField(choices=[('GH', 'GitHub'), ('GL', 'GitLab'), ('JR', 'Jira'), ('CF', 'Confluence'), ('WK', 'Wiki'), ('TH', 'Other')], default='TH', help_text='Тип ресурса проекта', max_length=2)),
                ('project', models.ForeignKey(help_text='Проект этого ресурса', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resources', related_query_name='resource', to='project.project')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='ФИО участника команды', max_length=40)),
                ('specialization', models.CharField(help_text='Компетенция участника команды', max_length=40)),
                ('telegram', models.CharField(help_text='Контакты участника в телеграм', max_length=40)),
                ('mail', models.EmailField(help_text='Почта участника', max_length=40)),
                ('phone', models.CharField(help_text='Номер телефона участника', max_length=17, validators=[django.core.validators.RegexValidator(message='Номер телефона должен быть введен в формате: "+999999999". Максимальная длина номера - 15 символов.', regex='^\\+?1?\\d{9,15}$')])),
                ('project', models.ForeignKey(help_text='Проект участника команды', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='members', related_query_name='member', to='project.project')),
            ],
        ),
        migrations.CreateModel(
            name='AccessRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(help_text='Ссылка на ресурс в IDM', max_length=100)),
                ('template_content', models.TextField(help_text='Заготовка заявки на получение доступа')),
                ('resource', models.OneToOneField(help_text='Ресурс проекта', on_delete=django.db.models.deletion.CASCADE, related_name='access', related_query_name='access', to='project.resource')),
            ],
        ),
    ]
