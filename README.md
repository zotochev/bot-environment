# bot-environment
## about
Bot environment for fast creating and deploying of telegram bots.

## Deploy
Set `WEBHOOK_HOST` env variable in `.env` file to your server exposed url or ip address.
```bash
docker compose up -d
```

## Bot Interface
- all requiered variables (api token) setup in `app/secrets/<bot-name>.env` file and connected to `/run/secrets` folder using secrets statment in `docker-compose.yaml` file
    - TELEGRAM_TOKEN
    - WEBHOOK_PATH
- common env variables for all bots setup in `app/.env` file and connected to every bot using env-file statement in `docker-compose.yaml` file
    - WEBHOOK_HOST

## todo
- [ ] Registration mechanism:
    - Create simple self written registration mechanism
        - [ ] Script that sends requests to `services register`:
            - on start up - register;
            - on stop - unregister.
        - [ ] Services register server in nginx container:
            - listens for requests from services;
            - on register:
                - creates nginx config and puts it to `/etc/nginx/bots` directory
                - sends back some payload
            - in unregister:
                - deletes ngxin config from `/etc/nginx/bots`
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

    - [ ] config
        - [ ] config compatible for admin interface
            - [ ] stored in database

    - [ ] each bot has separate database
    - [ ] health check
    - [ ] restarter worker
        - [ ] on event in redis restart bot
    - [ ] failure telegram notification
        - [ ] messanger worker that reads redis

- [x] create echo echo-bot repo using `bot interface`
    - [ ] auto restart of bot on update of configuration
    - [x] setup test environment for bot

- [x] create echo-bot with webhook
  - [x] nginx config for server
  - [x] nginx config nginx container

- [ ] shop list bot
    - [ ] remake for `bot interface`
    - [ ] deploy in this environment

- [ ] Create frontend admin interface for echo bot
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
