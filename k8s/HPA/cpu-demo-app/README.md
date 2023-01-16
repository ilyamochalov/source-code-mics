# Demo app for K8S HPA with CPU rule

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
$ curl http://127.0.0.1:5000/
UP
```

5. Build
```
$ docker build -t ilyamochalov/k8s-autoscaling-cpu-demo:latest .
```

6. Run some load with `ab` and monitor app CPU usage 
```sh
$ ab -n 10000000 -c 2 http://127.0.0.1:5000/cpu
```