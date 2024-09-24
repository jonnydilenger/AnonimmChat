# Анонимный чат на Kubernetes

## Описание
Приложение представляет собой анонимный веб-чат, где пользователи могут отправлять и просматривать сообщения в реальном времени. Веб-интерфейс реализован на HTML и JavaScript, бэкенд — на Flask, а данные хранятся в MySQL.

## Как запустить

1. Клонировать репозиторий:
    ```bash
    git clone <repo_url>
    cd <repo_name>
    ```

2. Задеплоить все манифесты:
    ```bash
    kubectl apply -f deploy/
    ```

3. Открыть браузер и перейти по адресу `http://<Node_IP>:30001` для доступа к чату.

## Описание манифестов
- `deploy/mysql-secret.yaml` — секреты для базы данных MySQL.
- `deploy/mysql-deployment.yaml` — деплой MySQL.
- `deploy/mysql-service.yaml` — сервис для MySQL.
- `deploy/app-deployment.yaml` — деплой веб-приложения.
- `deploy/app-service.yaml` — сервис для веб-приложения через NodePort.
