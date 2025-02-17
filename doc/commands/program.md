# Programs

1. [create](#create)
2. [write](#write)
3. [activate](#activate)
4. [read](#read)

## create

Create executable program

```bash
sapcli program create "ZHELLOWORLD" "Just a description" "$TMP"
```

## write

Change code of an executable program without activation.

```
sapcli program write [OBJECT_NAME|-] [FILE_PATH+|-] [--corrnr TRANSPORT] [--activate]
```

* _OBJECT\_NAME_ either program name or - when it should be deduced from FILE\_PATH
* _FILE\_PATH_ if OBJECT\_NAME is not -, single file path or - for reading _stdin_; otherwise space separated list of file paths
* _--corrnr TRANSPORT_ specifies CTS Transport Request Number if needed
* _--activate_ activate after finishing the write operation

## activate

Activate an executable program.

```bash
sapcli program activate "ZHELLOWORLD"
```

## read

Download source codes

```bash
sapcli program read ZHELLOWORLD
```

