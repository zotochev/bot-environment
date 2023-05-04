# bot-environment
## about
Bot environment for fast creating and deploying of telegram bots.

## Deploy
- Create `.env` file in `app` directory and set there varibales that relaited to all bots.
- Set `WEBHOOK_HOST` env variable in `.env` file to your server exposed url or ip address.
```bash
docker compose up -d
```

## Bot Interface
- all requiered variables (api token) setup in `app/secrets/<bot-name>.env` file and connected to `/run/secrets` folder using secrets statment in `docker-compose.yaml` file
    - TELEGRAM_TOKEN
    - WEBHOOK_PATH
- common env variables for all bots setup in `app/.env` file and connected to every bot using env-file statement in `docker-compose.yaml` file
    - WEBHOOK_HOST
- register worker (not sure if need):
    - register and unregister bot.
    - sets webhook on telegram API.

## todo
- [ ] Service registration mechanism:
    - Create simple self written registration mechanism
        - **Why?**:
            - To setup nginx routing for webhook mechanism.
            - To get url from nginx container for webhook registration on telegram API.
        - [ ] Script that sends requests to `services register`:
            - on start up - register;
            - on stop - unregister;
            - on fail? - uregister by healthchecker?.
        - [ ] Services register server in nginx container:
            - listens for requests from services;
            - on register:
                - creates nginx config and puts it to `/etc/nginx/bots` directory.
                - sends back endpoint to register bot in telegram API.
            - in unregister:
                - deletes ngxin config from `/etc/nginx/bots`
    - Heath checker for unregistration of stopped services.
    - format of registration request with:
        - required env variables;
        - bot name (unique);
        - webhook: bool;
    - Patterns
        - [Server side discovery](https://microservices.io/patterns/server-side-discovery.html)
        - [Service registry](https://microservices.io/patterns/service-registry.html)
        - [Self registration](https://microservices.io/patterns/self-registration.html)
    - [x] split nginx config on common part and part for one bot
    - [x] send http request to nginx container

- [ ] register worker (example):
    - **Why?**:
        - register and unregister bot.
        - sets webhook on telegram API.
        - maybe no need to create such worker.

- [ ] create `bot interface`
    - [x] define common info for all bots
        - [x] database credentials and type
    - [x] env vars
        - [x] define required env variables
            - TELEGRAM_TOKEN="<token>"
        - env variables should be set in .env file `bot/secrets/.env`
            - should have `bot/secrets/.env.sample` file

    - [ ] config
        - [ ] config compatible for admin interface
            - [ ] stored in database

    - [ ] each bot has separate database
    - [ ] health check
    - [ ] restarter worker
        - [ ] on event in redis restart bot
    - [ ] failure telegram notification
        - [ ] messanger worker that reads redis

- bots to deploy:
    - [Shop list](https://github.com/zotochev/shop-list-telegram-bot)
    - [Deutschesverb](https://github.com/lama-imp/deutschesverb_bot)

- [ ] Create frontend admin interface for echo bot
    - [ ] html template for admin settings
        - [ ] yaml config for template
        - [ ] api calls for triggering changes
    - [ ] Config applier worker
        - receives api request makes changes to database
    - set env variables

- [x] create nginx container
- [x] create postgres container

- [x] create echo echo-bot repo using `bot interface`
    - [ ] auto restart of bot on update of configuration
    - [x] setup test environment for bot

- [x] create echo-bot with webhook
  - [x] nginx config for server
  - [x] nginx config nginx container

- [x] setup docker compose environment
    - [x] to support any number of bots
        - support any number of bots will be achived by creating bot interface
    - secrets folder
