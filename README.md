# akkio-iframe-demo

Demo for showcasing iframe embedding

## Installation and Setup

### Python Dependencies

You can get these as follows.

```shell
brew install pyenv
pyenv install 3.11.0
python -m pip install poetry
cd web
python -m venv venv #optional and poetry install auto creates a .venv
source venv/bin/activate #optional and poetry install auto creates a .venv
poetry install
```

## Getting Started

1. Navigate to `http://45.33.80.22/`

NOTE: There is no certificate for HTTPS added, but there is server security including ufw, and port blocking implemented

2. Navigate to the `Register` tab and fill out the form. This will secure and encrypt credentials in the postgres backend db.

NOTE: You will be automatically logged in, however next time you use the app, you just need to navigate to the `Login` tab.

3. Fill out all configurations in the `Setup` tab and select Submit.

4. The app is now configured and you can see all iframe embedded endpoints in the left sidebar.

## Notes:

- Public Chat Explore, Public Dashboard, Public Insights Report, and Public Web App can be iframed.
- For any feature enhancements, please create an Github Issue for tracking and create a new branch for implementation (e.g., sudheer-dev)
