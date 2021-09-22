import json

from django.core.management.base import BaseCommand
from products.models import Product, ProductCategory, ProductImage

class Command(BaseCommand):
    help = 'imports data from "garment_items.jl" file'
    def add_arguments(self, parser):

        parser.add_argument(
            '--batch_size',
            action='store',
            dest='batch_size',
            help='Batch size for importing data',
            type=int
        )

        parser.add_argument(
            '--filepath',
            action='store',
            dest='filepath',
            help='Path of the file to import',
            type=str
        )

    def populate_data(self, data):
        product_id = data.get("product_id")
        try:
            description, colour = data.get("product_description").split("colour:  ")
            colour = colour.lower()
        except ValueError:
            description, colour = data.get("product_description"), None
        self.product_instances.append(
            Product(
                product_id=product_id,
                url=data.get("url"),
                title=data.get("product_title"),
                description=description,
                source=data.get("source"),
                gender=data.get("gender"),
                price=data.get("price"),
                discount=data.get("discount"),
                currency_code=data.get("currency_code"),
                colour=colour,
                imgs_src=data.get("product_imgs_src")[0],
                stock=data.get("stock"),
            )
        )
        self.product_related_data[product_id] = {
            "images": [],
            "categories": []
        }

        # create category and add the key in data store to be added later
        for category in data.get("product_categories"):
            if self.product_categories.get(category) is None:
                pc, created = ProductCategory.objects.get_or_create(name=category)
                self.product_categories[category] = pc.id
            self.product_related_data[product_id]["categories"].append(self.product_categories[category])

        # add images data to the data store
        images = data.get("images")
        positions = data.get("position")
        for idx in range(len(images)):
            temp = {}
            temp.update(images[idx])
            temp["position"] = positions[idx]
            self.product_related_data[product_id]["images"].append(temp)

    def process_batch(self):
        # bulk create products
        Product.objects.bulk_create(self.product_instances)

        instances = Product.objects.filter(product_id__in=self.product_related_data.keys())
        product_categories = []
        product_images = []
        for instance in instances:
            data = self.product_related_data.get(instance.product_id)
            if not data:
                continue
            for img in data["images"]:
                product_images.append(
                    ProductImage(
                        product_id=instance.id,
                        **img
                    )
                )

            for cat in data["categories"]:
                product_categories.append(
                    Product.categories.through(
                        product_id=instance.id,
                        productcategory_id=cat
                    )
                )

        # bulk create image instances
        ProductImage.objects.bulk_create(product_images)

        # bulk create the relationship b/w product and categories
        Product.categories.through.objects.bulk_create(product_categories)

    def handle(self, *args, **options):
        filepath = options.get("filepath") or "garment_items.jl"
        batch_size = options.get("batch_size") or 1000
        self.product_categories = {}
        self.product_instances = []
        self.product_related_data = {}
        current_idx = 0
        with open(filepath, 'r') as my_file:
            for line in my_file.readlines():
                self.populate_data(json.loads(line))
                if current_idx < batch_size:
                    current_idx += 1
                else:
                    self.process_batch()
                    current_idx = 0
                    self.product_categories = {}
                    self.product_instances = []
                    self.product_related_data = {}

            # process last batch
            if current_idx:
                self.process_batch()
