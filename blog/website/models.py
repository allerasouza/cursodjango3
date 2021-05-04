from django.db import models

# Create your models here.
class Categorias(models.TextChoices):
    TECH = 'TC', 'Tecnologia'
    CR = 'CR', 'Curiosidades'
    GR = 'GR', 'Geral'

class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    content = models.TextField()
    categories = models.CharField(
        max_length=2,
        choices=Categorias.choices,
        default=Categorias.GR,
    )
    deleted = models.BooleanField(default=False)
    imagem = models.ImageField(upload_to='posts', null=True, blank=True)
    
    def __str__(self): # Return title instead of "Post object" on object's name
        return self.title

    def full_name(self): # Add a new filed to Post
        return self.title + self.sub_title

    def get_category_label(self):
        return self.get_categories_display()

    full_name.admin_order_field = 'title' # Allow new filed to be ordered