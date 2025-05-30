Джанго ДРФ. 
    
##
        python manage.py runserver

##
        python manage.py runserver 0.0.0.0:8001


2 ендпоинта. На первом 'webhook/bank/' создается Банковский Платеж.

Запускаем на разных портах, Пробрасываем джейсон на первом и смотрим на втором ендпоинте 'organizations/<int:inn>/<int:amount>' создается Платеж.

1 подход.