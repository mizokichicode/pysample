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
```

### build

```
> source .venv/bin/activate
(.venv)> cd pysample
(.venv)> pyinstaller --onefile pysample.py   (※)
```

※ 2回目以降は `pyinstaller pysample.spec` でも可

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
```

### build

```
> .venv\Scripts\activate
(.venv)> cd pysample
(.venv)> pyinstall --onefile pysample.py    (※)
```

※ 2回目以降は `pyinstaller pysample.spec` でも可