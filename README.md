> With great power comes great responsibility ~ Uncle Ben
>
# Doctor Octopus

![alt text](http://tiny.cc/yev4hz)

Doctor Octopus is a automation tool who do your toil for you and at the same time prevent you to get any RSI.

Yes, originally he is a anti hero but his utility are essentially awesome and as there is no more Tritium on planet earth we belive that now he is under control and will not get crazy again.

But don't fool yourself, if you get crazy while work with him WE WILL CALL SPIDER-MAN ON YOU!

Since this is a virtual character we add some improvements of course. 
Instead of only four arms he can use how many you like. Also he already has knowledge about some Azion's tools and will use them in order to do a better and fast work. He also is an open project among Azions and a easy use tool.

**Remember Uncle Ben.**

## Usage
Loading...
```
octo --help
octo --list
octo --help task
octo task
octo task --param 0
octo namespace.task
```

## Instalation
For obvious reasons Doctor Octopus it's not a PyPI oficial package so you need to install directly from our Github.
```
pip install git+ssh://git@github.com/tiagorkrebs/doctor-octopus.git
```
Make sure that you have an authorized private key for this.

## Configuration
Create a `~/.fabric.yaml` with this basic configuration
```
debug: true
run:
    echo: true
tasks:
  auto_dash_names: true
  collection_name: tasks
  search_root: /usr/local/lib/python3.7/site-packages/doctor-octopus
```
Note that `search_root` make reference to doctor_octopus installed source. This is normally found in `.../lib/python3.7/site-packages/doctor-octopus`.
If you want to learn mobe about fabric configuration see [here](http://docs.fabfile.org/en/2.5/concepts/configuration.html). 
Another alternative is point to your development source folder.

## Contributing

Clone this repository and install all requirements.
```
git clone git@github.com:tiagorkrebs/doctor-octopus.git
cd doctor-octopus
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
```
Make your branch and submit a PR.

## Base Projects
Doctor octopus is fundamentally based but not limited to these three open source projects:
- [Fabric](https://github.com/fabric/fabric/) A library designed to execute shell commands remotely over SSH.
- [Invoke](https://github.com/pyinvoke/invoke/) A task execution tool & library.
- [Paramiko](https://github.com/paramiko/paramiko/) A implementation of the SSHv2 protocol.