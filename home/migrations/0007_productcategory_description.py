from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0006_alter_productcategory_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="productcategory",
            name="description",
            field=models.TextField(
                blank=True,
                null=True,
            ),
        ),
    ]