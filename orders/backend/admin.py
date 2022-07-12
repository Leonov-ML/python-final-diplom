from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from backend.models import User, Shop, Category, Product, ProductInfo, Parameter, ProductParameter, Order, OrderItem, \
    Contact, ConfirmEmailToken

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Панель управления пользователями
    """
    model = User

    fieldsets = (
        (None, {'fields': ('email', 'password', 'type')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'company', 'position')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')

class CategoryInLine(admin.TabularInline):
    model = Category.shops.through
    extra = 1

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url', 'user', 'state')
    inlines = [CategoryInLine]
    list_filter = ['name', 'state']
    search_fields = ['name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [CategoryInLine]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    list_filter = ['name', 'category']


class ProductParametrInline(admin.TabularInline):
    model = ProductParameter
    extra = 1


@admin.register(ProductInfo)
class ProductInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'external_id', 'product', 'shop', 'quantity', 'price', 'price_rrc')
    list_filter = ['model', 'product', 'price']
    inlines = [ProductParametrInline]
    search_fields = ['id', 'model', 'external_id']
    list_editable = ['quantity', 'price']
    list_per_page = 10


@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(ProductParameter)
class ProductParameterAdmin(admin.ModelAdmin):
    list_display = ['product_info', 'parameter', 'value']


class OrderItemInline(admin.TabularInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'dt', 'state', 'contact']
    list_filter = ['user', 'dt', 'state']
    inlines = [OrderItemInline]
    search_fields = ['id', 'user']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product_info', 'quantity']
    list_editable = ['quantity']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['user', 'city', 'street', 'house', 'structure', 'building', 'apartment', 'phone']


@admin.register(ConfirmEmailToken)
class ConfirmEmailTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'key', 'created_at',)
