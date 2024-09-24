# AnonimChat

AnonimChat — это приложение для обмена сообщениями, работающее с базой данных MySQL, развернутое в Kubernetes. В этом проекте используется Docker, Kubernetes, а также MySQL для хранения сообщений.

## Описание

AnonimChat — это чат-приложение, которое позволяет пользователям обмениваться сообщениями, сохраняющимися в базе данных MySQL. Приложение и база данных развёрнуты в Kubernetes с использованием конфигурационных файлов YAML для управления сервисами, деплойментами и хранилищами.

## Структура проекта

```bash
├── deploy/
│   ├── anonimchat-deployment.yaml                      # Deployment для приложения
│   ├── anonimchat-database-deployment.yaml             # Deployment для базы данных MySQL
│   ├── anonimchat-database-cm1-configmap.yaml          # ConfigMap с инициализацией БД
│   ├── anonimchat-service.yaml                         # Сервис для приложения
│   └── anonimchat-database-service.yaml                # Сервис для базы данных
├── app/
│   ├── templates                    # Папка с шаблонами страниц
│       └── index.html               # Шаблон главной страницы
│   ├── Dockerfile                   # Dockerfile для создания образа приложения
│   ├── requirements.txt             # requirements со списком зависимостей
│   └── app.py                       # Основной код приложения (Flask)
└── README.md                        # Текущий файл
```

## Требования

Для локального развертывания приложения вам потребуются следующие инструменты:

- Docker
- Kubernetes

## Установка и запуск

Установите Docker и Kubernetes, если они ещё не установлены.

Склонируйте репозиторий:

```bash
git clone https://github.com/jonnydilenger/AnonimmChat.git
cd AnonimmChat
```

Создайте Docker-образы для приложения и базы данных:

```bash
docker build --pull --rm -f "app/Dockerfile" -t anonimmchat:latest "app"
```

Опубликуйте образ в Docker Hub (или другой реестр контейнеров):

```bash
docker push ujinpavlovich/anonimchat:latest
```

Примените все конфигурации Kubernetes:

```bash
kubectl apply -f deploy/
```

Убедитесь, что поды и сервисы запущены и работают:

```bash
kubectl get pods
kubectl get svc
```

Приложение будет доступно через `NodePort`.

## Конфигурация

- MySQL конфигурация:
  - Имя базы данных: `my_database`
  - Пользователь: `my_user`
  - Пароль: `my_password`
  - Root пароль: `my_secret_password`

Эти параметры можно изменить в файле `anonimchat-database-deployment.yaml`.

- Приложение:
  - Порт по умолчанию для сервиса: `30080`

Этот порт можно изменить в файле `anonimchat-service.yaml`.
