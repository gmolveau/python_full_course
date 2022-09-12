# Environment variables / Secrets

How to manage secrets in a python app ?

- 1. `.env`
    - gitignore
    - https://pypi.org/project/python-dotenv/
    - `.env.sample`

```python
from dotenv import load_dotenv
load_dotenv()
```

- 2. python flat config file

```python
# config.py
TOKEN_API = "blablabla"

# main.py
from config import TOKEN_API
<use TOKEN_API>
```

- 2bis. python dict config file

```python
# config.py
CONFIG = {
    "TOKEN_API" : "blablabla"
}

# main.py
from config import CONFIG
<use CONFIG['TOKEN_API']>
```

- 3. config file (yaml, json, toml, ini)

    - https://blog.nicolas.brondin-bernard.com/principaux-formats-fichiers-donnees-configuration-json-yaml-toml-xml-ini-csv/
    - https://www.barenakedcoder.com/blog/2020/03/config-files-ini-xml-json-yaml-toml/
    - https://zestedesavoir.com/billets/2613/json-yaml-toml-xml-ou-comment-se-compliquer-la-vie/

- 4. secret manager server (eg. Vault)

    - https://modularsystems.io/blog/securing-secrets-python-vault/

- config depending of the environement [production, development, testing]

take a look how flask is doing it

    - https://flask.palletsprojects.com/en/2.0.x/config/#configuring-from-data-files
    - https://flask.palletsprojects.com/en/2.0.x/config/#configuring-from-python-files