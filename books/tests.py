from django.test import TestCase
from django_test_migrations.contrib.unittest_case import MigratorTestCase
from django_test_migrations.migrator import Migrator

# Create your tests here.


class TestMigration(MigratorTestCase):
    """This class is used to test direct migrations."""

    migrate_from = ("books", "0001_initial")
    migrate_to = ("books", "0002_books_fiction")

    def prepare(self):
        """Prepare some data before the migration."""
        SomeItem = self.old_state.apps.get_model("books", "Books")
        SomeItem.objects.create(title="Moby Dick", author="Herman Melville", pages=378)

    def test_migration_books_0002(self):
        """Run the test itself."""
        SomeItem = self.new_state.apps.get_model("books", "Books")

        assert SomeItem.objects.count() == 3
        assert len(SomeItem._meta.get_fields()) == 5


class TestReverseMigration(MigratorTestCase):

    migrate_from = ("books", "0002_books_fiction")
    migrate_to = ("books", "0001_initial")

    def prepare(self):
        """Prepare some data before the migration."""
        SomeItem = self.old_state.apps.get_model("books", "Books")
        SomeItem.objects.create(
            title="Moby Dick", author="Herman Melville", pages=378, fiction=True
        )

    def test_reverse_migration_books_0002(self):
        """Run the test itself."""
        SomeItem = self.new_state.apps.get_model("books", "Books")

        assert SomeItem.objects.count() == 1
        assert len(SomeItem._meta.get_fields()) == 4
