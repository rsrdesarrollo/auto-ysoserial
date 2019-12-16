# auto-ysoserial

Auto Ysoserial is a **simple script** to run all [ysoserial](https://github.com/frohoff/ysoserial) payloads with a custom 
Burp Collaborator (or similar) link, in order to test all de payloads in a easy way (with Intruder for example) and only
get info from the payloads that succeed in the attack. 

Commands will be crafted to generate a custom DNS request with the information of the de-serialization payload used. So,
in collaborator (or others), you will see request with something like `<usedMethod>.<collaboratorId>.burpcollaborator.net`.
Hopefully this will help you to test in a easy way all possible payloads and identify possible ways to exploit 
[unsafe Java object deserialization](https://github.com/GrrrDog/Java-Deserialization-Cheat-Sheet)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install auto-ysoserial
```

## Usage

```bash
$ auto-ysoserial -h
usage: auto-ysoserial [-h] -c COLLABORATOR -o OUT [-d]

optional arguments:
  -h, --help            show this help message and exit
  -c COLLABORATOR, --collaborator COLLABORATOR
                        Burp Collaborator hostname
  -o OUT, --out OUT     Output file for intruder
  -d, --debug           Set debug info
```

Output file will contain all payloads (one per line) encoded in base64. You sould use Burp Intruder 
[preprocessors](https://portswigger.net/burp/documentation/desktop/tools/intruder/payloads/processing) 
(or similar) to fit your needs.
 

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)