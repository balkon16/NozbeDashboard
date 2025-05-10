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
python main.py
```
