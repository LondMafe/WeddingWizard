from django.contrib import admin
from django.utils.safestring import SafeText
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'user_type', 'partner1_name', 'partner2_name', 'birth_year1', 'birth_year2', 'vendor_name', 'vendor_identifier')

    def user_type(self, obj):
        return obj.get_user_type_display()  # Muestra el valor legible del campo user_type
    
    def email(self, obj):
        return obj.user.email  # Muestra el email del usuario
    
    def partner1_name(self, obj):
        return obj.partner1_name if obj.user_type == 'client' else '-'  # Muestra el nombre del socio 1 solo para clientes

    def partner2_name(self, obj):
        return obj.partner2_name if obj.user_type == 'client' else '-'  # Muestra el nombre del socio 2 solo para clientes

    def birth_year1(self, obj):
        return obj.birth_year1 if obj.user_type == 'client' else '-'  # Muestra el año de nacimiento 1 solo para clientes

    def birth_year2(self, obj):
        return obj.birth_year2 if obj.user_type == 'client' else '-'  # Muestra el año de nacimiento 2 solo para clientes

    def vendor_name(self, obj):
        return obj.vendor_name if obj.user_type == 'vendor' else '-'  # Muestra el nombre del vendedor solo para vendedores

    def vendor_identifier(self, obj):
        return obj.vendor_identifier if obj.user_type == 'vendor' else '-'  # Muestra el identificador del vendedor solo para vendedores

admin.site.register(Profile, ProfileAdmin)
