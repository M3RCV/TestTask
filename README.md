Описание задачи:
  
В данной задаче вам предстоит разработать небольшую систему социальной сети, включающую регистрацию и вход пользователей, а также функционал управления постами. Пользователи должны иметь возможность создавать учетные записи, входить в систему с использованием своих учетных данных и публиковать, редактировать и удалять свои посты.

Стэк технологии использованных в решении этой задачи: 

  1) Python

  2) FastAPI

  3) PostgreSQL(sqlalchemy)

  4) Docker

  5) Другие зависимости можно посмотреть в файле requirements.txt

Как запустить:

1) Убедитесь что у вас установлен Make, а так же Docker Desctop

2) Клонируйте репозиторий(находясь в инициализированном пустом репозитории, в командной строке пропишите следующую команду)
   
       git clone -b master https://github.com/M3RCV/TestTask.git
   
3) Убедившись что вы находитесь в корневом дирректории проекта пропишите в терминал команду:

       make start

4) Список всех команд вводимых в терминал(убедитесь, что вы находитесь в корневой дирректории проекта):

  Сборка и запуск docker-compose файла:
      
      make start

  Только сборка файла:

      make build

  Только запуск файла:

      make up

  Остановка:

      make down

  Получение логов:

      make logs

  5) Ссылка на документацию по работе с API (Swagger UI) появится по адресу:

  http://localhost:9999/docs#/
