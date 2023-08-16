# Generated by Django 4.2.4 on 2023-08-16 03:26

from django.db import migrations


def add_default_data(apps, schema_editor):
    Book = apps.get_model("books", "Book")
    Author = apps.get_model("authors", "Author")
    Category = apps.get_model("books", "Category")
    categories = Category.objects.bulk_create([
        Category(name="Science Fiction", description="This is a science fiction category."),
        Category(name="Horror", description="This is a horror category."),
        Category(name="Comedy", description="This is a comedy category."),
        Category(name="Action", description="This is an action category."),
    ])
    book_data = [
        {
            'title': 'A smile in the mind',
            'author': Author.objects.create(first_name="Jack", last_name="Daniels"),
            'summary': 'A vivid title for a book about graphic design.',
        },
        {
            'title': 'The Power of Now',
            'author': Author.objects.create(first_name="Carlos", last_name="Martini"),
            'summary': 'The powerful take out of this book is that we waste huge amounts of energy in guilt, regret and pain etc. focusing on the past; as well as worry and uncertainty about the future.',
        },
        {
            'title': 'Lean In',
            'author': Author.objects.create(first_name="Carlos", last_name="Martini"),
            'summary': 'This book was published less than a year ago and already the term ‘Lean in’ has become a widely used for female empowerment and success.',
        },
    ]
    books_results = Book.objects.bulk_create([
        Book(**item)
        for item in book_data
    ])

    index = 0
    for result in books_results:
        result.categories.add(categories[index])
        index += 1


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(add_default_data),
    ]
