# Task page mapper

All page interactions mapped to code.

## About

This project is an implementation of Page Object Model (POM) design pattern. It was created by using Selenium to map all page iterables into a Domain-specific language (DML). 

The DML is used as a interface of interaction between the browser webdriver and the code to manipulate the browser itself and the page iterables.

POM design pattern is generally used in test automation for enhancing code quality and maintentance.

## Requirements

- [Docker](https://www.docker.com/)
- [Docker-compose](https://docs.docker.com/compose/install/)
- [Poetry](https://python-poetry.org/) (optional)

### Installing project dependencies

You can install the project dependencies using either pip or poetry.

- Using pip

```sh
pip install -r requirements.txt
```

- Using poetry

```sh
poetry install
```

## Testing using BDD

To apply tests you will need *Selenium Hub* and a remote browser instance.

Simply run:

```sh
docker-compose up -d
```

and then

```sh
pytest -v $(pwd)/tests/test_page_mapper.py
```

## References

MENDES, E. [*Selenium course*](https://github.com/dunossauro/curso-python-selenium). 2020.
