from django.db import models
from django.urls import reverse_lazy

# Create your models here.
class News(models.Model):
    # тип varchar, обязательный аргумент кол-во символов
    title = models.CharField(max_length=150, verbose_name='Наименование')
    # тип Text, необязательный аргумент blank - означает что поля необязательное для заполнение
    content = models.TextField(blank=True, verbose_name='Контент')
    # типа дата и время, auto_now_add=True - означает что дата ставиться только при создании контента
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    # auto_now=True - означает что дата обновляется при каждом обновлении контента
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    # upload_to - можно указать куда именно сохранять файл, с указанием года, месяца, дня
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    # так как в аргументе обращаемся в классу который находиться ниже, берем еще в ковычки 'Category'
    # on_delete=models.PROTECT не позволяет удалить связанные строки
    # при добавлении строк в сущ. таблицу нам приходится заполнять некоторые значение NULL, включаем null=True
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    # для того чтобы название новости отобразались нормально
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости' # в множественном числе
        ordering = ['-created_at'] # для сортировки

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def get_absolute_url(self):
        return reverse_lazy('category', kwargs={"category_id": self.pk}) # 1 (аргум) названия маршрута, 2 (аргум) необходимый параметр для данного маршрута

    # для того чтобы название категории отобразались нормально
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории' # в множественном числе
        ordering = ['title'] # для сортировки