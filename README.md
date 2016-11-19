# Instructions

- [Get Docker](https://www.docker.com/products/overview)
- [Get Docker Compose](https://docs.docker.com/compose/install/)
- Clone this repository
- `docker-compose build; docker-compose up;`
- Make changes to the code, and rerun the above line to test your changes.

## Todo:

- 

## Environments (dependencies and settings)

- *dev* - `docker-compose.yml` (The default)
- *prod* - `prod.yml`
- *stage* - `stage.yml`

So, to execute the app in the various environments:

- *dev* - `docker-compose build; docker-compose up;`
- *prod* - `docker-compose -f prod.yml build; docker-compose -f prod.yml up;`
- *stage* - `docker-compose -f stage.yml build; docker-compose -f stage.yml up;`

Each of these environments corresponds to a settings file `web/config/settings/**environment name**.py` and a requirements.txt-style list of dependencies `web/ksupcapp/requirements/**environment name**.txt`.

For global dependencies, use `web/ksupcapp/requirements/base.txt`, and for global settings, use `web/config/settings/base.py`.
