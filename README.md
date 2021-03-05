# datacrunch-arena-generic

This is a generic API that anyone can use to quickly deploy its model to the datacrunch arena.

## Docker

This project includes a Dockerfile ready to be build.

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

If you do not want to use a docker environment, you can achieve the same result by installing it by hand.

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

## Your data

Your data must be put in the `data/` directory.

This directory contains a `.gitignore` to ensure that your are not uploading by mistake your model online. Remember, with datacrunch, you are the owner of your model!

By default, you must names your file with the following:

| Target | File                |
|--------|---------------------|
| R      | data/model_target_r |
| G      | data/model_target_g |
| B      | data/model_target_b |

This can be changed in the [inference.py](inference.py) file.

## Accessing it

Accessing your code is easy: [localhost:80](http://localhost:80)

## Testing

We included a small testing utility to make sure that everything is working.

```
python3 fake_generator.py --help
```

### Basic Usage

#### Change feature count

This exemple will send 12 features (named `feature_xyz`) to `http://localhost:80/infer` thanks to the `-f <count>` option.

```
python3 fake_generator.py -P -f 12 http://localhost:80/infer
```

#### Send more than one request at a time

To avoid spamming your server, we are sending multiple infer request at the same time. To customize this parameter, use the `-c <count>` option.

```
python3 fake_generator.py -P -c 10 http://localhost:80/infer
```

#### Combine

The `-f <n>` and `-c <n>` options are meant to be used together.

This example will send `4` infer requests with `12` features each.
```
python3 fake_generator.py -P -f 12 -c 4 http://localhost:80/infer
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
