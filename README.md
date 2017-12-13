# Django Blog Demo

Python 3.6.3
Django 1.11.7

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

在虛擬環境中安裝 Django 1.11.7

```shell
pip install django==1.11.7
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
