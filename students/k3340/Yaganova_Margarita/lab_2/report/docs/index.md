# Задание:

Реализовать сайт, используя фреймворк Django 3
и СУБД PostgreSQL, в соответствии с вариантом
задания лабораторной работы.

## Вариант:

*Список туров туристической фирмы*

Хранится информация о названии тура, турагенстве, описании
тура, периоде проведения тура, условиях оплаты.

Необходимо реализовать следующий функционал:
1. Регистрация новых пользователей.
1. Просмотр и резервирование туров. Пользователь должен иметь возможность
редактирования и удаления своих резервирований.
1. Написание отзывов к турам. При добавлении комментариев, должны
сохраняться даты тура, текст комментария, рейтинг (1-10), информация о
комментаторе.
1. Администратор должен иметь возможность подтвердить резервирование
тура средствами Django-admin.
1. В клиентской части должна формироваться таблица, отображающая все
проданные туры по странам.