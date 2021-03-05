import json
import random
import sys
import traceback

import click
import requests


def _random_and_round(round_to):
    return round(random.uniform(0.0, 1.0), round_to)


@click.command()
@click.option("-c", "--request-count", default=1, type=click.IntRange(0), help="Number of fake request to send")
@click.option("-f", "--feature-count", default=3, type=click.IntRange(0), help="Number of feature to generate")
@click.option("-F", "--feature-format", default="feature_{}", help="Feature's name format")
@click.option("-P", "--pretty", default=False, is_flag=True, help="Prettify the JSON")
@click.option("-x", default=None, type=click.FloatRange(0.0, 1.0), help="Default value to all features")
@click.option("--round", default=4.0, type=click.IntRange(0), help="")
@click.option("-q", "--quiet", default=False, is_flag=True, help="Do not print anything in the console")
@click.argument("url")
def main(request_count, feature_count, feature_format, pretty, x, round, url, quiet):
    """Test your endpoint with simple data."""
    
    indent = 4 if pretty else None
        
    body = {
        "features": [
            {
                feature_format.format(i): x if x is not None else _random_and_round(round) for i in range(feature_count)
            } for _ in range(request_count)
        ]
    };
    
    try:
        if not quiet:
            print(f"Sending ({url}):")
            print(json.dumps(body, indent=indent))
            print()
        
        response = requests.post(url, json=body)
        response.raise_for_status()
        
        if not quiet:
            print(f"Received ({response.status_code}):")
            
            decoded = response.content.decode("utf-8")
            
            if indent:
                print(json.dumps(json.loads(decoded), indent=indent))
            else:
                print(decoded)
    except:
        if not quiet:
            traceback.print_exc(file=sys.stderr)
        
        exit(1)


if __name__ == "__main__":
    main()
