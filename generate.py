import yaml
import json
import pprint
import requests

stream = open('config.yml', 'r') 
config = yaml.safe_load(stream)

pp = pprint.PrettyPrinter(indent=2)

def parse_git(source, language, configlist, retval):
    url = f"{source['path']}/{language}/{source['filename']}"
    print(f"Downloading Source File: {url}")
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        for c in configlist:
            name = data.get(c.upper() if source['uckeys'] else c)
            if name:
                if not retval.get(c):
                    retval[c] = {}
                retval[c][language] = name
            else:
                print(f"didnt find: {name}")


def main():
    countries = {}
    languages = {}

    for language in config['languages']:
        parse_git(config['source_country'], language, config['countries'], countries) 
        parse_git(config['source_language'], language, config['languages'], languages)

    pp.pprint(countries)
    pp.pprint(languages)

    with open(config['source_country']['output'], 'w') as outfile:
        json.dump(countries, outfile)
    with open(config['source_language']['output'], 'w') as outfile:
        json.dump(countries, outfile)

if __name__== "__main__":
   main()
