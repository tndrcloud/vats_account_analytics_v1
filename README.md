<h2>VATS Account Analytics (Анализатор ВАТС)</h2>

- REST API Сервис для проверки логов вызовов из ЛК ВАТС на наличие причин непрохождения входящих и исходящих звонков, проблем со слышимостью, каналами связи, а также проверка корректности настроек ЛК.

- Анализатор ВАТС позволит проверять:

  В настройках ЛК: 
    1. Настройки личного кабинета ВАТС
    2. Активные регистрации пользователей
    3. Доступ для домена (тестовый период или коммерческий)
    4. Маршрутизацию вызовов для номеров и пользователей
    5. Наличие блокировки домена (финансовая/административная/добровольная)
    6. Проблемы с каналами входящей/исходящей связи
    7. Корректность указанных номеров для переадресации
    8. Алгоритм распределения вызовов в группе
    9. Активные контакты пользователей
    10. Доступность голосовую почты для пользователя или группы
    11. Настройки IVR-сценариев
    12. Настройки SIP-Trunk
     
  В логах вызовов:
    1. Логи вызовов в личном кабинете ВАТС
    2. Наличие проблем с настройками оборудования:
       - некорректно сформированное поле SIP-пакета
       - некорректный размер RTP-пакета
       - включенный DND
       - несовпадение кодеков между клиентом и SBC
    3. Ответы платформы ВАТС:
       - ограничение направления вызова для домена
       - ограничения направления вызова для пользователя (МН/МГ/внутренние)
       - проблема с настройками тарифа
       - недостаточно средств на балансе для совершения звонка
         
Сервис в ответ на запрос отправляет результат проверки с рекомендациями по устранению проблемы


<h2>Требования</h2>

- python 3.11
- fastapi, fastapi-users
- sqlalchemy
- postgresql
- alembic
- uvicorn
- dockerfile, docker-compose

Зависимости можно установить через: pip install -r requirements.txt 

<h2>Процесс развёртывания (деплоя) на сервере</h2>

1. Установить (для Ubuntu):

- Docker:
    - sudo apt update
    - sudo apt install apt-transport-https ca-certificates curl software-properties-common
    - curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    - sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
    - sudo apt update
    - apt-cache policy docker-ce
    - sudo apt install docker-ce

- Docker-compose:
    - sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)"
    -o /usr/local/bin/docker-compose
    - sudo chmod +x /usr/local/bin/docker-compose

2. Создать файл .env в директории ./vats_account_analytics_v1 и заполнить переменные окружения, где: 

- DB_USER={логин пользователя PostgreSQL}
- DB_PASSWORD={пароль от пользователя PostgreSQL}
- DB_NAME={название БД в PostgreSQL}
- DB_PATH={путь для доступа к БД - postgresql+asyncpg://login:password@ip:port/dbname}
- DB_PORT={порт для доступа к БД}
- SERVER_HOST={IP-адрес для приложения app}
- SERVER_PORT={порт для приложения app}
- JWT_SECRET={секретный ключ для JWT токена аутентификации}
- RESET_VERIF_SECRET={секретный ключ для сброса или верификации}

3. Запустить команду: docker-compose -f docker-compose-app.yaml up -d из директории ./vats_account_analytics_v1
