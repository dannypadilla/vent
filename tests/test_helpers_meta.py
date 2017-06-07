from vent.helpers.meta import Containers
from vent.helpers.meta import Core
from vent.helpers.meta import Docker
from vent.helpers.meta import Images
from vent.helpers.meta import Services
from vent.helpers.meta import System
from vent.helpers.meta import Timestamp
from vent.helpers.meta import Tools
from vent.helpers.meta import Uptime
from vent.helpers.meta import Version

def test_version():
    """ Test the version function """
    version = Version()
    assert version != ''

def test_system():
    """ Test the system function """
    system = System()
    assert system != ''

def test_docker():
    """ Test the docker function """
    docker = Docker()
    assert type(docker) == dict
    assert type(docker['server']) == dict

def test_containers():
    """ Test the containers function """
    containers = Containers()
    containers = Containers(vent=False)
    assert type(containers) == list

def test_images():
    """ Test the images function """
    images = Images()
    images = Images(vent=False)
    assert type(images) == list

def test_tools():
    """ Test the tools function """
    tools = Tools()
    assert type(tools) == list

def test_services():
    """ Test the services function """
    services = Services()
    assert type(services) == list
    services = Services(vent=False)
    assert type(services) == list

def test_core():
    """ Test the core function """
    core = Core()
    assert type(core) == dict

def test_timestamp():
    """ Test the timestamp function """
    timestamp = Timestamp()
    assert type(timestamp) == str

def test_uptime():
    """ Test the uptime function """
    uptime = Uptime()
    assert type(uptime) == str