from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from .models import User
from django import forms

class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

class CustomUserAdmin(UserAdmin):
    model = User
    add_form = CustomUserCreationForm
    list_display = ("email" , "is_superuser" , "is_active")
    list_filter = ("email" , "is_superuser" , "is_active")
    search_fields = ("email",)
    ordering = ("email",)

    fieldsets = (

        ('Authentication', {
            "fields": (
                'email', 'password'
            ),
        }),
         
        ('Permission', {
            "fields": (
                'is_staff', 'is_active','is_superuser'
            ),
        }),

        ('group Permission', {
            "fields": (
                'groups', 'user_permissions'
            ),
        }),

        ('important date', {
            "fields": (
                'last_login',
            ),
        }),
     )
    add_fieldsets = (
        ("Add New User", {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser'
            ),
        }),
    )
admin.site.register(User,CustomUserAdmin)