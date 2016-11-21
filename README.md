# Instructions

- [Get Docker](https://www.docker.com/products/overview)
- [Get Docker Compose](https://docs.docker.com/compose/install/)
- Clone this repository
- `docker-compose build; docker-compose up;`
- Make changes to the code.

## Todo:

- 

## Wishlist:

- [Wagtail](https://wagtail.io/) for managing news postings and images
- Paypal integration for keeping accouts paid up
- Instagram - schedule posts
- Twitter - tweet on news post
- Facebook - post in FB group & FB page on news post


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

## Notes

- While many types of third-party logins will eventually be available, we will require a user to sign up with either Facebook or our site's native account system first.  **Only then** will linking with Instagram, Twitter, etc. be allowed.
