# datacrunch-arena-generic

This is a generic API that anyone can use to quickly deploy its model to the datacrunch arena.

## Docker

This project include a Dockerfile ready to be build.

(require that you have [docker](https://www.docker.com/) installed on your computer (or server))

### Building

```
docker build -t datacrunch-arena .
```

### Running

```
docker run --rm -it -p 80:80 datacrunch-arena
```

## By Hand

If you do not want to use a docker environement, you can achieve the same result by installing it by hand.

(require that you have [python (> v3.7)](https://www.python.org/) installed on your computer (or server))

### Installation

To prepare your computer to handle this API, some commands must be done to install the required dependencies.

```
pip3 install -r requirements.txt
```

### Running

```
uvicorn --port 80 app:app
```

## Accessing it

Accessing your code is easy: [localhost:80](http://localhost:80)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
