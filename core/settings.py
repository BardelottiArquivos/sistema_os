"""
Django settings for core project.
"""

from pathlib import Path
import os
from decouple import config
import dj_database_url  # <--- Certifique-se de ter rodado: pip install dj-database-url

BASE_DIR = Path(__file__).resolve().parent.parent

# ============================================
# CONFIGURAÇÕES DO .env (SEGURAS)
# ============================================
SECRET_KEY = config('SECRET_KEY', default='django-insecure-chave-temporaria-mude-em-producao')
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1,localhost').split(',')

# ============================================
# APLICATIVOS INSTALADOS
# ============================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third party
    'crispy_forms',
    'crispy_bootstrap5',
    'django_filters',
    'rest_framework',
    
    # Local apps
    'apps.usuarios',
    'apps.clientes',
    'apps.computadores',
    'apps.ordens_servico',
    'apps.relatorios',
]

# ============================================
# MIDDLEWARE
# ============================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

# ============================================
# TEMPLATES
# ============================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# ============================================
# BANCO DE DADOS (PostgreSQL Dinâmico)
# ============================================
# # No topo do arquivo, certifique-se de ter:
import dj_database_url

# Substitua o bloco DATABASES por este:
DATABASES = {
    'default': dj_database_url.config(
        # Ele tenta ler DATABASE_URL. Se não existir (como no seu PC), usa o SQLite ou o que você definir.
        default=config('DATABASE_URL', default='postgres://postgres:2530@localhost:5432/sistema'),
        conn_max_age=600
    )
}

# ============================================
# VALIDAÇÃO DE SENHA
# ============================================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ============================================
# INTERNACIONALIZAÇÃO
# ============================================
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# ============================================
# ARQUIVOS ESTÁTICOS E MÍDIA
# ============================================
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ============================================
# CRISPY FORMS (Bootstrap 5)
# ============================================
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'

# ============================================
# AUTENTICAÇÃO
# ============================================
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'login'

AUTH_USER_MODEL = 'usuarios.Usuario'

# ============================================
# REST FRAMEWORK
# ============================================
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

# ============================================
# IMPRESSORA
# ============================================
PRINTER_CONFIG = {
    'name': config('PRINTER_NAME', default='PDF Printer'),
    'type': config('PRINTER_TYPE', default='pdf'),
    'output_dir': BASE_DIR / 'relatorios_impressos'
}

BASE_URL = config('BASE_URL', default='http://localhost:8000')