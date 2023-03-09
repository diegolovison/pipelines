# Copyright 2023 The Kubeflow Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import setuptools

NAME = 'kfp-kubernetes'
VERSION = '0.0.1'
REQUIREMENTS = [
    'protobuf>=3.13.0,<4',
    'kfp>=2.0.0-beta.13',
]
DEV_REQUIREMENTS = [
    'docformatter==1.4',
    'isort==5.10.1',
    'mypy==0.941',
    'pre-commit==2.19.0',
    'pycln==2.1.1',
    'pytest==7.1.2',
    'pytest-xdist==2.5.0',
    'types-protobuf-4.22.0.0',
    'yapf==0.32.0',
]

setuptools.setup(
    name=NAME,
    version=VERSION,
    description='Kubernetes platform configuration library and generated protos.',
    author='google',
    author_email='kubeflow-pipelines@google.com',
    url='https://github.com/kubeflow/pipelines',
    packages=setuptools.find_namespace_packages(include=['kfp.*']),
    python_requires='>=3.7.0',
    install_requires=REQUIREMENTS,
    include_package_data=True,
    extras_require={
        'dev': DEV_REQUIREMENTS,
    },
    license='Apache 2.0',
)
