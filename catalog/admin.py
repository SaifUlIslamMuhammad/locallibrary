from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

# admin.site.register(Language)
# admin.site.register(Book)
# admin.site.register(BookInstance)
# admin.site.register(Author, AuthorAdmin)
admin.site.register(Author)
admin.site.register(Genre)

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    pass

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance 
    pass

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]
    pass

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )
    pass
    
