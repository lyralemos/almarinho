from django.db import models
from django.core.urlresolvers import reverse_lazy

STATUS_CHOICE = (
    ('private','Privado'),
    ('published','Publicado'),
)

# Create your models here.
class Entry(models.Model):
    titulo = models.CharField(max_length=100)
    slug = models.SlugField()
    status = models.CharField(max_length=20,choices=STATUS_CHOICE,default='private')
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_publicacao = models.DateTimeField(blank=True,null=True)
    texto = models.TextField()
    imagem = models.ImageField(upload_to='images',blank=True,null=True)

    def __unicode__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse_lazy('entry-detail',kwargs={'slug':self.slug})