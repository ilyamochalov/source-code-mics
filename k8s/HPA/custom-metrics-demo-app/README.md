# Demo app for K8S HPA with custom metrics

## Local development
1. Install python3
2. Create virtual env
```sh
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv) $ pip install -r requirements.txt 
```
3. Run the app
```sh
$ python app.py

```
4. In new terminal test endpoint
```sh
$ curl http://127.0.0.1:5050/
UP
```

5. Build
```
$ docker build -t ilyamochalov/k8s-autoscaling-custom-metrics-task-demo:latest .
```

6. Run some load with `ab` 
```sh
$ ab -n 10000000 -c 10 http://127.0.0.1:5050/task
```