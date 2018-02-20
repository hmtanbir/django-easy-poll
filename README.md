Django easy poll application.

Installation
------------

```
pip install django-easy-poll
```

Install latest from github:
```
pip install -e git+https://github.com/hmtanbir/django-easy-poll.git#egg=django-easy-poll
```

Requirements
------------
Django 1.10+, Python 2.7, 3.4+

Usage
-----

1. Add 'poll' application in the ``INSTALLED_APPS`` settings:

    ```
    INSTALLED_APPS = (
        ...
        'poll',
    )
    ```

2. Add the poll's url to your urls.py.

    ```
    urlpatterns = [
        ...
        url(r'^poll/', include('poll.urls')),
    ]
    ```

3. Run ```python manage.py migrate```

4. Go to site's admin area and create a new poll:


5. Add this tags in your template file to show the poll:

    ```
    {% load poll_tags %}
    ...
    {% poll %}
    ```

6. Check if jQuery is already included on the page. If don't — add it:
```
<script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
```

7. Make vote, see the results:


Customization
-------------

Of course, you can (and probably, should) customize Simple Poll's templates. You can simply do this by overriding `base.html`, `poll.html` and `result.html` in `templates/poll` directory.
