# Generated by Django 3.1 on 2020-12-10 19:24

import dcim.fields
from django.db import migrations, models
import django.db.models.deletion
import ipam.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("ipam", "0037_ipaddress_assignment"),
        ("dcim", "0116_rearport_max_positions"),
    ]

    operations = [
        migrations.CreateModel(
            name="BgpPeering",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("created", models.DateField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                ("local_as", dcim.fields.ASNField()),
                ("remote_ip", ipam.fields.IPAddressField()),
                ("remote_as", dcim.fields.ASNField()),
                ("peer_name", models.CharField(blank=True, max_length=64)),
                ("description", models.CharField(blank=True, max_length=200)),
                (
                    "device",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="dcim.device"
                    ),
                ),
                (
                    "local_ip",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="ipam.ipaddress"
                    ),
                ),
                (
                    "site",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="dcim.site",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
