# Nozbe source data

## Obtaining token

1. Retrieve (e.g. from KeePass) client ID for your Nozbe app.
2. In a web browser go to the `https://api.nozbe.com:3000/login?client_id=<client_ID>`
3. Allow access using your Nozbe credentials (e-mail and passoword)
3. You will be redirected to a faulty page (404 error). Copy the token from the URL:
   `https://our.application.redirect.uri.com/app?access_token=<token>&email=pawel.k.lonca@gmail.com`
4. Save the token in the *src/credentials/token.json*. The token is valid for 365 days.

## Testing

```shell
cd ~/PycharmProjects/NozbeDashboard
source .venv/bin/activate
pytest src/tests/
```

## Execution

Make sure the *src/credentials/token.json* file exists:

```json
{
  "token": "<token>"
}
```

```shell
cd ~/PycharmProjects/NozbeDashboard
source .venv/bin/activate
python src/main.py --data-provider local
```

All options:
```shell
usage: main.py [-h] [--data-provider {api,local}] [--projects-file PROJECTS_FILE] [--tasks-file TASKS_FILE] [--token-file TOKEN_FILE] [--log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}]

Fetch and process project and task data.

options:
  -h, --help            show this help message and exit
  --data-provider {api,local}
                        Specify the data provider to use: 'api' for Rest API, 'local' for Local Storage. Defaults to 'api'.
  --projects-file PROJECTS_FILE
                        Path to the projects JSON file (used with --data-provider local).
  --tasks-file TASKS_FILE
                        Path to the tasks JSON file (used with --data-provider local).
  --token-file TOKEN_FILE
                        Path to the token JSON file (used with --data-provider api).
  --log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        Set the logging level. Defaults to INFO.
```
