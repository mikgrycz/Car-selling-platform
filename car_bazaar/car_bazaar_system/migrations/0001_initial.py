# Generated by Django 5.0.6 on 2024-05-30 15:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
            fields=[
                ("CarID", models.AutoField(primary_key=True, serialize=False)),
                ("Make", models.CharField(max_length=255)),
                ("Model", models.CharField(max_length=255)),
                ("Year", models.IntegerField()),
                ("Price", models.IntegerField()),
                ("Mileage", models.IntegerField()),
                ("Description", models.CharField(max_length=255)),
                ("PictureLink", models.CharField(max_length=255)),
                ("BodyType", models.CharField(max_length=255)),
                ("NumberOfReviews", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                ("MessageID", models.AutoField(primary_key=True, serialize=False)),
                ("Sender", models.CharField(max_length=255)),
                ("Recipient", models.CharField(max_length=255)),
                ("Content", models.CharField(max_length=255)),
                ("TimeStamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sender", models.CharField(max_length=255)),
                ("receiver", models.CharField(max_length=255)),
                ("amount", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("UserID", models.AutoField(primary_key=True, serialize=False)),
                ("UserName", models.CharField(max_length=255)),
                ("UserPassword", models.CharField(max_length=255)),
                ("UserEmail", models.EmailField(max_length=255)),
                ("UserPhone", models.CharField(max_length=255)),
                ("FirstName", models.CharField(max_length=255)),
                ("LastName", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="SuperUser",
            fields=[
                (
                    "user_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="car_bazaar_system.user",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("password", models.CharField(max_length=255)),
                ("email", models.CharField(max_length=255)),
            ],
            bases=("car_bazaar_system.user",),
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                ("ReviewID", models.AutoField(primary_key=True, serialize=False)),
                ("Rating", models.IntegerField()),
                ("Comment", models.CharField(max_length=255)),
                (
                    "CarSold",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="car_bazaar_system.car",
                    ),
                ),
                (
                    "Reviewer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="car_bazaar_system.user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Listing",
            fields=[
                ("listing_id", models.AutoField(primary_key=True, serialize=False)),
                ("listing_name", models.CharField(max_length=255)),
                ("listing_description", models.CharField(max_length=255)),
                ("listing_price", models.IntegerField()),
                ("listing_location", models.CharField(max_length=255)),
                ("listing_image", models.CharField(max_length=255)),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="car_bazaar_system.car",
                    ),
                ),
                (
                    "seller",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="car_bazaar_system.user",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="car",
            name="Seller",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="car_bazaar_system.user"
            ),
        ),
        migrations.CreateModel(
            name="RealTransaction",
            fields=[
                (
                    "transaction_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        to="car_bazaar_system.transaction",
                    ),
                ),
                ("TransactionID", models.AutoField(primary_key=True, serialize=False)),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("status", models.CharField(max_length=255)),
                (
                    "buyer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="buyer",
                        to="car_bazaar_system.user",
                    ),
                ),
                (
                    "car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="car_bazaar_system.car",
                    ),
                ),
                (
                    "seller",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="seller",
                        to="car_bazaar_system.user",
                    ),
                ),
            ],
            bases=("car_bazaar_system.transaction",),
        ),
        migrations.CreateModel(
            name="ProxyTransaction",
            fields=[
                (
                    "transaction_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="car_bazaar_system.transaction",
                    ),
                ),
                (
                    "realTransaction",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="car_bazaar_system.realtransaction",
                    ),
                ),
            ],
            bases=("car_bazaar_system.transaction",),
        ),
    ]
