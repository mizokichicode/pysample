# pysample
sample for python

## macOS

### create venv

```
> python3 -m venv .venv
```

### install packages

```
> source .venv/bin/activate
(.venv)> python -m pip install -r requirements.txt
(.venv)> deactivate
>
```

### build

```
> source .venv/bin/activate
(.venv)> cd pysample
(.venv)> pyinstaller --onefile pysample.py   (※)
(.venv)> deactivate
>
```

※ 2回目以降は `pyinstaller pysample.spec` でも可


### test

```
> source .venv/bin/activate
(.venv)> python -m unittest discover tests
(.venv)> deactivate
>
```

---

## Windows

### create venv

```
> py -m venv .venv
```

### install packages

```
> .venv\Scripts\activate
(.venv)> python -m pip install -r requirements.txt
(.venv)> deactivate
>
```

### build

```
> .venv\Scripts\activate
(.venv)> cd pysample
(.venv)> pyinstaller --onefile pysample.py    (※)
(.venv)> deactivate
>
```

※ 2回目以降は `pyinstaller pysample.spec` でも可

### test

```
> .venv\Scripts\activate
(.venv)> python -m unittest discover tests
(.venv)> deactivate
>
```
