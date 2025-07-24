from django.contrib import admin
from .models import Product, ProductReview, ProductCertificate, Store

class ProductReviewInline(admin.TabularInline):
    model = ProductReview
    extra = 2

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'price', 'date_added')
    inlines = [ProductReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('store', )  

class ProductCertificateAdmin(admin.ModelAdmin):
    list_display = ('product',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ProductCertificate, ProductCertificateAdmin)
