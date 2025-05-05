import subprocess
import shutil
import os
from pypdl import Pypdl
import tarfile
import json

env_port = int(os.environ.get('K_PORT')) or 8080

appsettings = {}
with open('lagrange/appsettings.json','r',encoding='utf-8') as f:
    appsettings = json.loads(f.read())
appsettings['Implementations'][0]['Port'] = env_port
with open('lagrange/appsettings.json','w',encoding='utf-8') as f:
    f.write(json.dumps(appsettings))

print(f'now connect host.docker.internal:{env_port}')

LAGRANGE = os.path.join(os.getcwd(),'lagrange','config','lagrange')

shutil.copy('lagrange/appsettings.json','lagrange/config/appsettings.json')

if not os.path.exists(LAGRANGE):
    dl = Pypdl()
    dl.start('https://github.com/LagrangeDev/Lagrange.Core/releases/download/nightly/Lagrange.OneBot_linux-x64_net9.0_SelfContained.tar.gz','lagrange/config/lagrange.tar.gz')
    with tarfile.open('lagrange/config/lagrange.tar.gz') as tar:
        member = tar.getmember('./Lagrange.OneBot/bin/Release/net9.0/linux-x64/publish/Lagrange.OneBot')
        member.name = 'lagrange'
        tar.extract(member,'lagrange/config')
    os.remove('lagrange/config/lagrange.tar.gz')

subprocess.run(LAGRANGE,cwd='lagrange/config')
