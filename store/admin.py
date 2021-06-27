from django.contrib import admin
from django.db import models
from .models import Product, Variation, reviewRating, ProductGallery
import admin_thumbnails

# Register your models here.
@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name','price', 'stock', 'category','modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    list_display_links = ('id', 'product_name', 'price', 'stock')
    inlines = [ProductGalleryInline]


class VariationAdmin(admin.ModelAdmin):
    list_display  = ('id','product', 'variation_category', 'variation_value' ,'is_active')
    list_display_links = ('id','product', 'variation_category', 'variation_value' )
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value' )

admin.site.register(Product, ProductAdmin)

admin.site.register(Variation, VariationAdmin)
admin.site.register(reviewRating)

admin.site.register(ProductGallery)