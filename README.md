# REST API demo for Model Deployment

After finished the model development, it's time to deploy it. This repository is a REST API demo for model deployment.

The follow tools are used:

1. Flask: web micro-framework
2. Flask-RESTplus: help to build REST APIs quick and easy.
3. Swagger-ui: tools for documenting RESTful web services. it helps us to make test query with a webpage.
4. gunicorn: restart the service while the service crashed
5. Docker: deploy micro-service

```shell script
export PYTHONPATH=./:$PYTHONPATH
python api_demo/app.py 
```

# TODO
- Query data type
    - [ ] Normal query data
    - [ ] Image query data
- [ ] gunicorn setting
- [ ] Micro-service with Docker


# Ref

1. [Building beautiful REST APIs using Flask, Swagger UI and Flask-RESTPlus](https://michal.karzynski.pl/blog/2016/06/19/building-beautiful-restful-apis-using-flask-swagger-ui-flask-restplus/)
