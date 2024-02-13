from setuptools import find_packages, setup
# launch imports
import subprocess, os, platform
from glob import glob

package_name = 'py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name,'launch'),
        glob('launch/*.py')),
        (os.path.join('share',package_name,'urdf'),
        glob('urdf/*'))

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ubuntu',
    maintainer_email='ubuntu@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
    	'console_scripts': [
	"py_node = py_pkg.node1:main",
    "robot = py_pkg.robot:main",
    "sub = py_pkg.subs:main",
    "control_turtle = py_pkg.control_turtle:main"
    ],
	},
)
