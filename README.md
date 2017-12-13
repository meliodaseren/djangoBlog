# Django Blog Demo

Python 3.6.3

Django 2.0

---

## 使用 virtualenv 建立虛擬環境

https://virtualenv.pypa.io/en/stable/userguide/

### 安裝 virtualenv

```shell
$ pip install virtualenv
```

### 建立一個虛擬環境 venv

```shell
$ virtualenv venv
```

### 激活腳本

```shell
$ . venv/bin/activate
```

或

```shell
$ source bin/activate
```

在虛擬環境中安裝 Django 2.0

```shell
pip install django==2.0
```

確認 pip 內有 Django

https://pip.pypa.io/en/stable/reference/pip_freeze/

```
pip freeze | grep Django
```

### 停用腳本

```shell
$ deactivate
```

---

## 運行伺服器

```shell
$ python manage.py runserver 8000
```

後台管理頁面：`127.0.0.1:8000/admin`

Blog：`127.0.0.1:8000/blog`

## 建立超級用戶以便管理後台

```shell
$ python manage.py createsuperuser
```

Cheat sheet
https://www.mercurytide.co.uk/media/resources/django-cheat-sheet.pdf

---

# Django 2.0 測試除錯

此 Repo 使用 Django 2.0，它已經不再支援 Python 2，版本升級請參考下列官方文件：

https://docs.djangoproject.com/en/2.0/howto/upgrade-version/

## 測試

```shell
$ python -Wall manage.py test
```

## 除錯

1. Django 2.0 ForeignKey 需加上 on_delete

```
TypeError: __init__() missing 1 required positional argument: 'on_delete'
```

http://www.jianshu.com/p/2610fec14d26

2. User matching query does not exist

```
django.contrib.auth.models.DoesNotExist: User matching query does not exist.
```

