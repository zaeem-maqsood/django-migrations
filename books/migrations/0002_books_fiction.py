# Generated by Django 3.2.8 on 2021-10-17 22:13

from django.db import migrations, models


def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    Book = apps.get_model("books", "Books")
    db_alias = schema_editor.connection.alias
    Book.objects.using(db_alias).bulk_create(
        [
            Book(
                title="Lord of the Rings",
                author="J.R.R. Tolkien",
                pages=500,
                fiction=True,
            ),
            Book(title="Scary Smart", author="Mo Gawdat", pages=300, fiction=False),
        ]
    )


def reverse_func(apps, schema_editor):
    # forwards_func() creates two Book instances,
    # so reverse_func() should delete them.
    Book = apps.get_model("books", "Books")
    db_alias = schema_editor.connection.alias
    Book.objects.using(db_alias).filter(
        title="Lord of the Rings", author="J.R.R. Tolkien"
    ).delete()
    Book.objects.using(db_alias).filter(
        title="Scary Smart", author="Mo Gawdat"
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="books",
            name="fiction",
            field=models.BooleanField(default=True),
        ),
        migrations.RunPython(forwards_func, reverse_func),
    ]