# Django Easy Poll

Installation
------------

```
sudo pip install django-easy-poll
```

Install latest from github:
```
sudo pip install -e git+https://github.com/hmtanbir/django-easy-poll.git#egg=django-easy-poll
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
        url(r'^', include("poll.urls", namespace='poll')),
    ]
    ```

3. Run ```python manage.py migrate poll```

4. Go to site's admin area and create a new poll:

![screenshot from 2018-02-20 09-01-26](https://user-images.githubusercontent.com/14236200/36405904-5cac302c-161d-11e8-8217-4a0919edf7f3.png)

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


7. Make vote:

![screenshot from 2018-02-20 09-03-04](https://user-images.githubusercontent.com/14236200/36405922-851ae0a8-161d-11e8-8151-cda995757b53.png)

8. See the results:

![screenshot from 2018-02-20 09-06-12](https://user-images.githubusercontent.com/14236200/36405923-854cf7f0-161d-11e8-90a9-31ef13390423.png)

Customization
-------------

Of course, you can (and probably, should) customize Easy Poll's templates. You can easily do this by overriding `base.html`, `poll.html` and `result.html` in `templates/poll` directory.




