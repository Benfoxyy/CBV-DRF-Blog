{% extends "mail_templated/base.tpl" %}

{% block subject %}
Verification code
{% endblock %}

{% block html %}
<a href='http://127.0.0.1:8000/accounts/password/reset/conf/{{token}}'>VERIFIY</a>
{% endblock %}