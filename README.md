# 
current pipeline:

```
[ scraper ] --> [redis] --> [consumer]
```

planned pipeline:
```
[ scraper ] --> [redis] 
                  |---> [data persitor ] --> [mongoDB]
                  |---> [data processor] -->    ???
```


# invocation
build all required images and fire away. remote images should be pulled in automatically.
the default config should do its thing automatically.

## build

```bash
docker-compose build
```

## run

```bash
docker-compose up -d
docker-compose logs -f
```

The consumer currently does not terminate on its own,
but will catch SIGTERM (`CTRL + C` or `docker-compose stop consumer`) or SIGKILL and terminate.
