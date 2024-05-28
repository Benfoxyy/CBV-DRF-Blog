{% extends "mail_templated/base.tpl" %}

{% block subject %}
Reset verification code
{% endblock %}

{% block html %}
<a href='http://127.0.0.1:8000/accounts/verify/{{token}}'>VERIFIY</a>
{% endblock %}