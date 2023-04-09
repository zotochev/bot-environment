# bot-template
## about
Bot environment for fast creating and deploying of telegram bots.

## Bot Interface
- all requiered variables (api token) setup in `app/secrets/<bot-name>.env` file and connected to `/run/secrets` folder using secrets statment in `docker-compose.yaml` file
    - TELEGRAM_TOKEN
    - WEBHOOK_PATH
- common env variables for all bots setup in `app/.env` file and connected to every bot using env-file statement in `docker-compose.yaml` file
    - WEBHOOK_HOST

## todo
- [x] setup docker compose environment
    - [x] to support any number of bots
        - support any number of bots will be achived by creating bot interface
    - secrets folder

- [ ] create `bot interface`
    - [x] define common info for all bots
        - [x] database credentials and type
    - [x] env vars
        - [x] define required env variables
            - TELEGRAM_TOKEN="<token>"
        - env variables should be set in .env file `bot/secrets/.env`
            - should have `bot/secrets/.env.sample` file

    - [ ] self registration mechanism
        - send http request to nginx container
        - format of registration request with:
            - required env variables;
            - bot name (unique);
            - webhook: bool;

    - [ ] config
        - [ ] config compatible for admin interface
            - [ ] stored in database

    - [ ] each bot has separate database
    - [ ] health check
    - [ ] restarter worker
        - [ ] on event in redis restart bot
    - [ ] failure telegram notification
        - [ ] messanger worker that reads redis

- [ ] create echo echo-bot repo using `bot interface`
    - [ ] auto restart of bot on update of configuration
    - [ ] setup test environment for bot

- [ ] create echo-bot with webhook
  - [ ] nginx config for server
  - [ ] nginx config nginx container

- [ ] shop list bot
    - [ ] remake for `bot interface`
    - [ ] deploy in this environment

- [ ] create admin interface for echo bot
    - [ ] html template for admin settings
        - [ ] yaml config for template
        - [ ] http calls for triggering changes
    - [ ] config applier worker
        - receives http request makes changes to database
    - set env variables
    - set database config variables
    - set predefined messages

- [x] create nginx container
- [x] create postgres container
