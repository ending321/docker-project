# web-service/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'appdb',
        'USER': 'root',
        'PASSWORD': 'chenjiewei',
        'HOST': 'mysql',  # MySQL主库地址
        'PORT': '3306',
    }
}
