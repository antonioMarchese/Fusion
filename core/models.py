import uuid
from django.db import models
from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    extension = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{extension}'
    return filename

class Base(models.Model): 
    created_at = models.DateField('Data de criação', auto_now_add=True) # auto_now_add atualiza esse campo assim que o elemento for criado
    updated_at = models.DateField("Atualizado em", auto_now=True) # auto_now atualiza a data toda vez que o objeto for modificado
    active = models.BooleanField("Ativo?", default=True)

    class Meta:
        abstract = True

class Service(Base):
    ICONE_CHOICES = (
        ("lni-cog", "Gear"),
        ("lni-stats-up", "Graph"),
        ("lni-users", "User"),
        ("lni-layers", "Designs"),
        ("lni-mobile", "Mobile"),
        ("lni-rocket", "Rocket"),
    )
    name = models.CharField('Serviço', max_length=50)
    description = models.CharField("Descrição", max_length=150)
    logo = models.CharField("Icone", max_length=12, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Serviço' # Nome de apresentação
        verbose_name_plural = 'Serviços'# Nome de apresentação no plural
    
    def __str__(self):
        return self.name

class Role(Base):
    role = models.CharField("Função", max_length=35)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.role
  
class Teammate(Base):
    name = models.CharField("Nome", max_length=35)
    role = models.ForeignKey('core.Role', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.CharField("Biografia", max_length=150)
    avatar = StdImageField('Avatar', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}}, force_min_size=True)
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Membro'
        verbose_name_plural = "Membros"
    
    def __str__(self):
        return self.name