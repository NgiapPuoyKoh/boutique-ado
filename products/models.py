from django.db import models

# python3 manage.py makemigrations --dry-run

# python -m pip install Pillow to use the image field

# python3 manage.py makemigrations
# Migrations for 'account':
#   /workspace/.pip-modules/lib/python3.8/site-packages/allauth/account/migrations/0003_auto_20210705_1504.py
#     - Alter field id on emailaddress
#     - Alter field id on emailconfirmation
# Migrations for 'products':
#   products/migrations/0001_initial.py
#     - Create model Category
#     - Create model Product
# Migrations for 'socialaccount':
#   /workspace/.pip-modules/lib/python3.8/site-packages/allauth/socialaccount/migrations/0004_auto_20210705_1504.py
#     - Alter field id on socialaccount
#     - Alter field id on socialapp
#     - Alter field id on socialtoken

# python3 manage.py migrate --plan
# Planned operations:
# account.0003_auto_20210705_1504
#     Alter field id on emailaddress
#     Alter field id on emailconfirmation
# products.0001_initial
#     Create model Category
#     Create model Product
# socialaccount.0004_auto_20210705_1504
#     Alter field id on socialaccount
#     Alter field id on socialapp
#     Alter field id on socialtoken

# python3  manage.py migrate products
# Operations to perform:
#   Apply all migrations: products
# Running migrations:
#   Applying products.0001_initial... OK

# python3 manage.py loaddata categories
# python3 manage.py loaddata product

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    # required
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # end required
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
