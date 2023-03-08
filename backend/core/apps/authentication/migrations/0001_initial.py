# Generated by Django 4.1.7 on 2023-03-08 16:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.CharField(max_length=150)),
                ('branch', models.CharField(max_length=150)),
                ('account_name', models.CharField(max_length=150)),
                ('account_number', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'authentication_bank_account',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('sex', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=6)),
                ('birthday', models.DateField(null=True)),
                ('id_card_number', models.CharField(blank=True, max_length=17)),
                ('id_card_image', models.ImageField(blank=True, upload_to='id-card-images/%Y-%m-%d/')),
                ('image', models.ImageField(blank=True, upload_to='user-images/%Y-%m-%d/')),
                ('address', models.TextField(blank=True)),
                ('phone_number', models.CharField(blank=True, max_length=12)),
                ('education_level', models.CharField(blank=True, choices=[('Primary School', 'Primary School'), ('Junior High School', 'Junior High School'), ('Senior High School', 'Senior High School'), ('Diploma Degree', 'Diploma Degree'), ('Bachelor Degrees', 'Bachelor Degrees'), ('Master Degrees', 'Master Degrees'), ('Doctoral Degrees', 'Doctoral Degrees'), ('Other', 'Other')], max_length=18)),
                ('occupation', models.CharField(blank=True, choices=[('Agriculture and Farming', 'Agriculture and Farming'), ('Education', 'Education'), ('Healthcare', 'Healthcare'), ('Hospitality and Tourism', 'Hospitality and Tourism'), ('Engineering and Manufacturing', 'Engineering and Manufacturing'), ('Entrepreneurship and Business', 'Entrepreneurship and Business'), ('Arts and Culture', 'Arts and Culture'), ('Construction and Architecture', 'Construction and Architecture'), ('Customer Service and Sales', 'Customer Service and Sales'), ('Finance and Accounting', 'Finance and Accounting'), ('Other', 'Other')], max_length=29)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('bank_account', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to='authentication.bankaccount')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'authentication_custom_user',
            },
        ),
    ]
