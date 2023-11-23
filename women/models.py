from django.db import models
from django.db.models import PROTECT, CASCADE
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Women.Status.PUBLISHED)


class Women(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=255, verbose_name='title')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')
    content = models.TextField(blank=True, verbose_name='content')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='time_create')
    time_update = models.DateTimeField(auto_now=True, verbose_name='time_update')
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT, verbose_name='is_published')
    cat = models.ForeignKey(to='Category', on_delete=CASCADE, related_name='posts', verbose_name='category')
    tags = models.ManyToManyField('TagPost', blank=True, related_name='tags', verbose_name='tags')
    husband = models.OneToOneField('Husband', on_delete=models.SET_NULL, null=True,
                                   blank=True, related_name='woman', verbose_name='husband')

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'famous women'
        verbose_name_plural = 'famous womens'
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='category_name')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='category_slug')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})


class Husband(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    m_count = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.name
