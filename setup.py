
from setuptools import setup
setup(**{'author': 'Jan-Eric Duden',
 'author_email': 'jan-eric.duden@kpn.com',
 'classifiers': ['Development Status :: 5 - Production/Stable',
                 'Environment :: Web Environment',
                 'Intended Audience :: Developers',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Topic :: Internet :: WWW/HTTP'],
 'description': 'A python bridge to the detox greybox testing library',
 'include_package_data': True,
 'install_requires': [],
 'long_description': 'Detox Python Bridge\n'
                     '===========================\n'
                     '\n'
                     '.. image:: '
                     'https://secure.travis-ci.org/kpn-digital/py-detox-bridge.svg?branch=master\n'
                     '    :target:  '
                     'http://travis-ci.org/kpn-digital/py-detox-bridge?branch=master\n'
                     '\n'
                     '.. image:: '
                     'https://img.shields.io/codecov/c/github/kpn-digital/py-detox-bridge/master.svg\n'
                     '    :target: '
                     'http://codecov.io/github/kpn-digital/py-detox-bridge?branch=master\n'
                     '\n'
                     '.. image:: '
                     'https://img.shields.io/pypi/v/detox-bridge.svg\n'
                     '    :target: https://pypi.python.org/pypi/detox-bridge\n'
                     '\n'
                     '.. image:: '
                     'https://readthedocs.org/projects/detox-bridge/badge/?version=latest\n'
                     '    :target: '
                     'http://detox-bridge.readthedocs.org/en/latest/?badge=latest\n'
                     '\n'
                     'A bridge to enable python code to use the detox grey-box '
                     'testing API ( https://github.com/wix/detox )\n'
                     '\n'
                     '\n'
                     'Requirements\n'
                     '============\n'
                     '\n'
                     'NVM\n'
                     '---\n'
                     '\n'
                     'The package requires nvm to be installed. Either the NVM '
                     'environment variable needs to contain the full path of '
                     'the nvm.sh script, or \n'
                     'the NVM_DIR environment variable needs to point at the '
                     'root directory of nvm containing the nvm.sh script.\n'
                     '\n'
                     'NODE\n'
                     '----\n'
                     '\n'
                     'The code emitted by this bridge requires node 8 or '
                     'higher. Node 7.6 should work but is not tested.\n'
                     '\n'
                     '\n'
                     'Python\n'
                     '------\n'
                     '\n'
                     '3.5 or 3.6 is required to use the package.\n'
                     '\n'
                     'Detox\n'
                     '-----\n'
                     '\n'
                     'Follow the getting started guide from detox ( '
                     'https://github.com/wix/detox/blob/master/docs/Introduction.GettingStarted.md '
                     ')\n'
                     '\n'
                     '\n'
                     'Usage\n'
                     '=====\n'
                     '\n'
                     '.. code:: python\n'
                     '\n'
                     '   from detox_bridge import await, by, detox, device, '
                     'element, expect, node_with_detox\n'
                     '\n'
                     '   app_path = "detox/examples/demo-react-native"\n'
                     '\n'
                     '   # Start Node server in app_path root folder that '
                     'contains node_modules\n'
                     '\n'
                     '   with node_with_detox(app_path=app_path, '
                     'default_timeout=10) as appserver:\n'
                     '\n'
                     '       # Detox Config (we could also load this from '
                     'package.json)\n'
                     '\n'
                     '       ios_sim_release = {\n'
                     '           "binaryPath": '
                     '"ios/build/Build/Products/Release-iphonesimulator/example.app",\n'
                     '           "type": "ios.simulator",\n'
                     '           "name": "iPhone 7 Plus"\n'
                     '       }\n'
                     '\n'
                     '       configurations_obj = {"configurations": '
                     '{"ios.sim.release": ios_sim_release}}\n'
                     '\n'
                     '       # Longer timeout since the app may be installed\n'
                     '\n'
                     '       appserver(await(detox.init(configurations_obj)), '
                     'timeout=360)\n'
                     '\n'
                     '       # Reload react native\n'
                     '\n'
                     '       appserver(await(device.reloadReactNative()))\n'
                     '\n'
                     '       # Expectation\n'
                     '\n'
                     '       '
                     "appserver(await(expect(element(by.id('welcome'))).toBeVisible()))\n"
                     '\n'
                     '       # Cleanup\n'
                     '\n'
                     '       appserver(await(detox.cleanup()))\n'
                     '\n'
                     'Development\n'
                     '===========\n'
                     '\n'
                     '\n'
                     'Requirements\n'
                     '------------\n'
                     '\n'
                     'Both python 3.5 and python 3.6 are required to run the '
                     'suite suite.\n'
                     '\n'
                     'Checkout\n'
                     '--------\n'
                     '\n'
                     'After checkout run::\n'
                     '\n'
                     '   git submodule update --init --recursive \n'
                     '\n'
                     '\n'
                     'Running tests\n'
                     '-------------\n'
                     '\n'
                     'To run the test suite::\n'
                     '\n'
                     '    make test\n'
                     '\n'
                     '\n'
                     'Once the venv is there you can also run some tests via '
                     'tox::\n'
                     '\n'
                     '    venv/bin/tox -e py35 -- -k <regex>\n',
 'name': 'detox-bridge',
 'packages': ['detox_bridge'],
 'tests_require': ['tox'],
 'url': 'ssh://git@github.com:kpn-digital/py-detox-bridge.git',
 'version': '1.0.2+1.g62ebd6d',
 'zip_safe': False})
