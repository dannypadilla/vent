from vent.api.plugins import Plugin
from vent.api.templates import Template

def test_add():
    """ Test the add function """
    instance = Plugin(base_dir='/tmp/', vent_dir='/tmp/', vendor_dir='/tmp/', scripts_dir='/tmp/')
    status = instance.add('https://github.com/cyberreboot/vent', build=False)
    assert status[0] == True
    status = instance.add('https://github.com/cyberreboot/vent.git', build=True)
    assert status[0] == True
    bad_instance = Plugin()
    status = bad_instance.add('https://github.com/cyberreboot/vent', build=False)
    assert status[0] == False
    instance = Plugin(base_dir='/tmp/', vent_dir='/tmp/', vendor_dir='/tmp/', scripts_dir='/tmp/')
    status = instance.add('https://github.com/cyberreboot/vent', build=False, user='foo', pw='bar')
    assert status[0] == True
    instance = Plugin(base_dir='/tmp/', vent_dir='/tmp/', vendor_dir='/tmp/', scripts_dir='/tmp/')
    status = instance.add('https://github.com/cyberreboot/vent', build=False, overrides=[('.', 'HEAD')])
    assert status[0] == True
    instance = Plugin(base_dir='/tmp/', vent_dir='/tmp/', vendor_dir='/tmp/', scripts_dir='/tmp/')
    status = instance.add('https://github.com/cyberreboot/vent', build=False, tools=[('.', 'HEAD')], overrides=[('.', 'HEAD')])
    assert status[0] == True

def test_get_tool_matches():
    """ Test the get_tool_matches function """
    instance = Plugin(base_dir='/tmp/', vent_dir='/tmp/', vendor_dir='/tmp/', scripts_dir='/tmp/')
    instance.tools = []
    matches = instance.get_tool_matches()
    assert matches == []

def test_add_image():
    """ Test the add_image function """
    Plugin.add_image('foo')

def test_builder():
    """ Test the builder function """
    instance = Plugin(base_dir='/tmp/', vent_dir='/tmp/', vendor_dir='/tmp/', scripts_dir='/tmp/')
    template = Template()
    template = instance.builder(template, 'bad_path', 'image_name', 'section', build=True, branch='master', version='HEAD')
    template = instance.builder(template, 'bad_path', 'image_name', 'section')

def test_build_tools():
    """ Test the _build_tools function """
    instance = Plugin()
    status = instance._build_tools(256)
    assert status[0] == False

def test_remove():
    """ Test the remove function """
    instance = Plugin(base_dir='/tmp/', vent_dir='/tmp/', vendor_dir='/tmp/', scripts_dir='/tmp/')
    status = instance.remove()
    assert status[0] == True

def test_tools():
    """ Test the tools function """
    instance = Plugin(base_dir='/tmp/', vent_dir='/tmp/', vendor_dir='/tmp/', scripts_dir='/tmp/')
    tools = instance.tools()
    assert tools == []

def test_versions():
    """ Test the versions function """
    instance = Plugin(base_dir='/tmp/', vent_dir='/tmp/', vendor_dir='/tmp/', scripts_dir='/tmp/')
    versions = instance.versions('foo')
    assert versions == []

def test_current_version():
    """ Test the current_version function """
    instance = Plugin(base_dir='/tmp/', vent_dir='/tmp/', vendor_dir='/tmp/', scripts_dir='/tmp/')
    versions = instance.current_version('foo')
    assert versions == []

def test_state():
    """ Test the state function """
    instance = Plugin(base_dir='/tmp/', vent_dir='/tmp/', vendor_dir='/tmp/', scripts_dir='/tmp/')
    states = instance.state('foo')
    assert states == []

def test_enable():
    """ Test the enable function """
    instance = Plugin(base_dir='/tmp/', vent_dir='/tmp/', vendor_dir='/tmp/', scripts_dir='/tmp/')
    status = instance.enable('foo')
    assert status[0] == False

def test_disable():
    """ Test the disable function """
    instance = Plugin(base_dir='/tmp/', vent_dir='/tmp/', vendor_dir='/tmp/', scripts_dir='/tmp/')
    status = instance.disable('foo')
    assert status[0] == False
