from django.core.management import call_command
from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Очищает таблицы Category и Product и загружает данные из фикстуры'

    def handle(self, *args, **options):
        # 1. Удаляем старые записи (сначала продукты, потом категории)
        self.stdout.write('Очистка базы данных...')
        Product.objects.all().delete()
        Category.objects.all().delete()

        # 2. Загружаем данные из фикстуры
        self.stdout.write('Загрузка данных из фикстуры...')
        call_command('loaddata', 'initial_data.json')

        # 3. Выводим сообщение об успехе зеленым цветом
        self.stdout.write(
            self.style.SUCCESS('База данных успешно перезаполнена!')
        )
