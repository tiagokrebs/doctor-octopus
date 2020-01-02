> With great power comes great responsibility ~ Uncle Ben
>
# Doctor Octopus

![alt text](http://tiny.cc/yev4hz)

Doctor Octopus is a automation tool who do your toil for you and at the same time prevent you to get any RSI.

Yes, originally he is a anti hero but his utility are essentially awesome and as there is no more Tritium on planet 
earth we belive that now he is under control and will not get crazy again.

But don't fool yourself, if you get crazy while work with him WE WILL CALL SPIDER-MAN ON YOU!

Since this is a virtual character we add some improvements of course. 
Instead of only four arms he can use how many you like. Also he already has knowledge about some Azion's tools and will 
use them in order to do a better and fast work. He also is an open project among Azions and a easy use tool.

**Remember Uncle Ben.**

## Instalation
For obvious reasons Doctor Octopus it's not a PyPI official package so you need to install directly from our Github.
```console
$ pip install git+ssh://git@github.com/tiagorkrebs/doctor-octopus.git
```
Make sure that you have an authorized private key for this.

## Configuration
Create a `~/.fabric.yaml` with this basic configuration
```yaml
debug: true
run:
    echo: true
tasks:
  auto_dash_names: true
  collection_name: tasks
  search_root: /usr/local/lib/python3.7/site-packages/doctor-octopus
user: <Your username>
connect_kwargs:
  key_filename: <Absolute path to your private key>
  passphrase: <Passphrase of your private key>
```
Note that `search_root` make reference to doctor_octopus installed source. This is normally found in 
`.../lib/python3.7/site-packages/doctor-octopus`.
If you want to learn more about fabric configuration see [here](http://docs.fabfile.org/en/2.5/concepts/configuration.html). 
Another alternative is to point this at your development source folder. 
Just make sure to point at `doctor-cotopus` root.

If you have permission to connect on Azion's servers over SSH your public key will be published over our network.
This type of connection only works when this key is used.

## Usage
**`doctor U octopus = octo`**

The `octo` command is based on `fab` and `invoke` tools so all functions of them are available.

For a complete help
```console
$ octo -h
```

For help of one task
```console
$ octo -h task-name
```

To run one task
```console
$ octo task-name
$ octo task-name --param1 value1 --param2 value2
$ octo task-name --param value1,value2,value3
```

The first thing you need to do is configure AWS Client with your access key and secret. If you do not have a AWS account 
ask for one.
Make sure to use `us-east-1` as region name and `json` as output format.
```console
$ octo aws-configure
AWS Access Key ID [****************]: XXXXXX
AWS Secret Access Key [****************]: ZZZZZZ
Default region name [us-east-1]: us-east-1
Default output format [json]: json
```

Octo has a built-in way to get Azion's servers (see `octo -h get-ifra`) but if you want to inform hosts manually this
is possible by using `-H|--host` parameter
```console
# this will run on all stage 'app' servers on Azion infrastructure
$ octo exec --cmd "ls -la /tmp" --app app --env s

# this will run only on app-orf-aws001s host
$ octo exec --cmd "ls -la /tmp" -H app-orf-aws001s
```

### PRO Tip
Use the `time` command to check how much time octo has saved you.
```console
$ time octo exec --cmd "ls -la /tmp" --app app --env s
...

real    0m7.860s
user    0m1.645s
sys     0m0.456s
``` 

## Private Tasks
If you want to create and use your own obscure and private tasks you will need to run at a development environment.
See **Contributing** and install the package locally with pip.
```console
$ pip install -e .
```

Add a `mytasks` module inside `doctor-octopus/tasks/`.
```console
doctor-octopus
    └── tasks
        ├── __init__.py
        ├── aws
        ├── generic
        └── mytasks
            ├── __init__.py
            └── mytasks.py

```

#### **`__init__.py`**
```python
from .mytasks import *
```

#### **`mystasks.py`**
```python
from fabric import task


@task(name='hello', help={'name': "Name for hello"})
def hello(c, name=None):
    """
    Say hello to someone
    """
    print("Hello {}!".format(name))
```

To see your private task run:
```console
$ octo -h

Available tasks:

  aws-configure   Starts AWS Client configurarion (mandatory)
  exec            Run one line command on remote server
  get-infra       Get server list from .infra.azion.net zone
  my.hello        Say hello to someone

```

## Contributing

Clone this repository and install all requirements.
```console
$ git clone git@github.com:tiagorkrebs/doctor-octopus.git
$ cd doctor-octopus
$ virtualenv -p python3 env
$ source env/bin/activate
$ pip install -r requirements.txt
```
Make your branch and submit a PR.

## Base Projects
This project is fundamentally based but not limited to these three open source projects:
- [Fabric](https://github.com/fabric/fabric/) A library designed to execute shell commands remotely over SSH.
- [Invoke](https://github.com/pyinvoke/invoke/) A task execution tool & library.
- [Paramiko](https://github.com/paramiko/paramiko/) A implementation of the SSHv2 protocol.
