# fastapi_docker_postgres_example
FastApi app with Docker + PostgreSQL study example

Порядок запуска приложения:
- создать poetry окружение на основе Python ^3.11
- в терминале прописать poetry install
- дождаться установки всех библиотек и сборки проекта (`Installing the current project: project (0.1.0)`)
- в терминале прописать docker compose up
- дождаться пока база данных будет готова (`database system is ready to accept connections`)
- подключиться к базе (DBeaver, DataGrip, PGadmin и т.д.)
- выполнить в базе скрипты из папки scripts для создания схемы и таблицы
- запустить файл src/project/main.py
- При успешном запуске будет написано:
  - `INFO:     Application startup complete.`
  - `INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)`

Важно:
- обратите внимание на файл src/project/core/config.py
- в нем руками перебиты значения из переменных сред из .env файла
- это временное решение, пока бэкенд не будет контейнеризирован

Swagger:
- после успешного запуска приложения, по адресу http://localhost:8000/docs будет доступен swagger

P.S перезапуск готового проекта:

  Поднимаем заново контейнер
  ```bash
  docker-compose up --build
  ```
  Выбираем свободный порт:
  ```bash
  poetry run uvicorn src.main:app --host 0.0.0.0 --port 8007
  ```


  

