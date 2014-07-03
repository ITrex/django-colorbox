django-colorbox
===============

[Colorbox github repository](https://github.com/jackmoore/colorbox)

## Usage

* To install package run python setup.py install in your virtualenv
* Add django\_colorbox into your INSTALLED_APPS

```python
INSTALLED_APPS=[
# ...
    'django_colorbox',
# ...
]
```
* Load javascript in your template
```html

<link rel="stylesheet" href="{% static 'django_colorbox/css/colorbox.css' %}"/>
<script type="text/javascript" src="{% static 'django_colorbox/js/jquery.colorbox-min.js' %}"></script>
```
