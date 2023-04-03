# bot-template
## about
Bot environment for fast creating and deploying of telegram bots.

## todo
- [ ] setup docker compose environment
    - [ ] to support any number of bots
    - [ ] secrets folder
- [x] create nginx container
- [ ] create `bot interface`
    - [ ] env vars
        - [x] define required env variables
            * ADMINS="<telegram-id>,<telegram-id>"
            * TELEGRAM_TOKEN="<token>"
            * WEBHOOK_PATH="<endpoint>"
            * WEBAPP_HOST="127.0.0.1"
            * WEBAPP_PORT=9991
            * PG_PORT="5432"
            * PG_HOST="postgres"
            * PG_USER="impresaone"
            * PG_PASSWORD="123"
        - [x] env variables should be set in .env file `bot/secrets/.env`

    - [ ] config
        - [ ] config compatible for admin interface
            - [ ] stored in database

    - [ ] health check
    - [ ] restarter worker
        - [ ] on event in redis restart bot
    - [ ] failure telegram notification
        - [ ] messanger worker that reads redis

- [ ] create echo echo-bot repo using `bot interface`
    - [ ] auto restart of bot on update of configuration
- [x] create postgres container
- [ ] create admin interface for echo bot
    * set env variables
    * set database config variables
- [ ] setup test environment for bot
