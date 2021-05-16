# Generated by Django 3.1.7 on 2021-05-07 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=150)),
                ('logo_image_url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=20)),
                ('type', models.IntegerField(choices=[(0, 'Normal'), (1, 'Workshop'), (2, 'Sparepartshop')])),
                ('contact_no', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('status', models.IntegerField(choices=[(0, 'Deleted'), (1, 'Pending'), (2, 'Apprved'), (3, 'Blacklist')])),
                ('created_by', models.CharField(max_length=20)),
                ('created_date', models.DateTimeField()),
                ('modified_by', models.CharField(max_length=20)),
                ('modified_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=150)),
                ('vehicle_image_url', models.CharField(max_length=200)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Stakeholder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('short_code', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('contact_number', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('alibaba_profile', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=100)),
                ('status', models.IntegerField(choices=[(0, 'Deleted'), (1, 'Pending'), (2, 'Apprved')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('stakeholder_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='data.stakeholder')),
                ('agent_code', models.CharField(max_length=6)),
            ],
            bases=('data.stakeholder',),
        ),
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('stakeholder_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='data.stakeholder')),
                ('courier_code', models.CharField(max_length=6)),
            ],
            bases=('data.stakeholder',),
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('stakeholder_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='data.stakeholder')),
                ('supplier_code', models.CharField(max_length=6)),
            ],
            bases=('data.stakeholder',),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=150)),
                ('tag_name', models.CharField(max_length=150)),
                ('inventory_code', models.CharField(max_length=8)),
                ('oem', models.CharField(max_length=50)),
                ('hs_code', models.CharField(max_length=20)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('length', models.DecimalField(decimal_places=2, max_digits=6)),
                ('width', models.DecimalField(decimal_places=2, max_digits=6)),
                ('height', models.DecimalField(decimal_places=2, max_digits=6)),
                ('volume', models.DecimalField(decimal_places=2, max_digits=8)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('image_url', models.CharField(max_length=200)),
                ('threshold', models.IntegerField()),
                ('status', models.IntegerField(choices=[(0, 'Deleted'), (1, 'Pending'), (2, 'Apprved')])),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.brand')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.model')),
            ],
        ),
        migrations.CreateModel(
            name='ContactPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact_number', models.CharField(max_length=20)),
                ('wechat_number', models.CharField(max_length=20)),
                ('whatsapp_number', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('status', models.IntegerField(choices=[(0, 'Deleted'), (1, 'Pending'), (2, 'Apprved')])),
                ('stakeholder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.stakeholder')),
            ],
        ),
    ]
