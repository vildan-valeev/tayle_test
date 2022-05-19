from src.settings.components import config, BASE_DIR

print('LOCAL SETTINGS!!!!')

DATABASES = {'default': {
    'ENGINE': config("SQL_ENGINE"),
    'NAME': BASE_DIR / config("SQL_DATABASE"),
}
}
ALLOWED_HOSTS = ['*']
