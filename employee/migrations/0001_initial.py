# Generated by Django 2.2.12 on 2022-03-24 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=256)),
                ('password', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'accounts',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numberHouse', models.CharField(max_length=256)),
                ('street', models.CharField(max_length=256)),
                ('district', models.CharField(max_length=256)),
                ('city', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'address',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookName', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('barcode', models.CharField(max_length=20)),
                ('quantity', models.IntegerField()),
                ('stt', models.IntegerField()),
            ],
            options={
                'db_table': 'books',
            },
        ),
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('barcode', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=10)),
                ('quantity', models.IntegerField()),
                ('stt', models.IntegerField()),
            ],
            options={
                'db_table': 'clothes',
            },
        ),
        migrations.CreateModel(
            name='Electronic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('producer', models.CharField(max_length=50)),
                ('barcode', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20)),
                ('quantity', models.IntegerField()),
                ('stt', models.IntegerField()),
            ],
            options={
                'db_table': 'electronic',
            },
        ),
        migrations.CreateModel(
            name='Fullname',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=256)),
                ('midName', models.CharField(max_length=256)),
                ('lastName', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'fullnames',
            },
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('display', models.CharField(max_length=50)),
                ('producer', models.CharField(max_length=50)),
                ('barcode', models.CharField(max_length=20)),
                ('chip', models.CharField(max_length=20)),
                ('camera', models.CharField(max_length=10)),
                ('GPU', models.CharField(max_length=20)),
                ('quantity', models.IntegerField()),
                ('stt', models.IntegerField()),
            ],
            options={
                'db_table': 'laptop',
            },
        ),
        migrations.CreateModel(
            name='MobilePhone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('display', models.CharField(max_length=50)),
                ('producer', models.CharField(max_length=50)),
                ('barcode', models.CharField(max_length=20)),
                ('chip', models.CharField(max_length=20)),
                ('camera', models.CharField(max_length=10)),
                ('quantity', models.IntegerField()),
                ('stt', models.IntegerField()),
            ],
            options={
                'db_table': 'mobile_phone',
            },
        ),
        migrations.CreateModel(
            name='Shose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('barcode', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=10)),
                ('quantity', models.IntegerField()),
                ('stt', models.IntegerField()),
            ],
            options={
                'db_table': 'shose',
            },
        ),
        migrations.CreateModel(
            name='LaptopItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('discount', models.CharField(max_length=256)),
                ('price', models.IntegerField(null=True)),
                ('urlImage', models.CharField(max_length=500)),
                ('laptop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.Laptop')),
            ],
            options={
                'db_table': 'laptop_items',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=256)),
                ('code', models.CharField(max_length=256)),
                ('position', models.CharField(max_length=256)),
                ('dob', models.DateField(null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Account')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Address')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Fullname')),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.CreateModel(
            name='ClothesItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('discount', models.CharField(max_length=256)),
                ('price', models.IntegerField(null=True)),
                ('urlImage', models.CharField(max_length=500)),
                ('clothes', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.Clothes')),
            ],
            options={
                'db_table': 'clothes_items',
            },
        ),
        migrations.CreateModel(
            name='BookItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('discount', models.CharField(max_length=256)),
                ('price', models.IntegerField(null=True)),
                ('urlImage', models.CharField(max_length=500)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.Book')),
            ],
            options={
                'db_table': 'book_items',
            },
        ),
    ]
