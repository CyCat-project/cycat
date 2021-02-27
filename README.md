# CyCAT.org Python library

Minimal CyCAT.org Python library to handle [CyCAT.org url](https://cycat.org/services/concept/).

# Installation

~~~
pip3 install .
~~~

# Usage

## Generating CyCAT.org url

~~~python
from cycat import url

cycat_url = url.generate(publisher="samratashok", project="nishang")
~~~

## Validating CyCAT.org url

~~~python
from cycat import url

url.validate(url="misp:event:91b49dee-6d22-468a-87f4-fbd08997a2d4")
~~~

## Building valid CyCAT.org url

~~~python
from cycat import url

url.build(publisher="misp", project="EVENT", uuid="5c48e0b6-e9f6-455e-a228-90723004e65c")
~~~

# License

This library is free software/open source released a two-clause BSD license.

~~~
Copyright (c) 2021 Alexandre Dulaunoy
Copyright (c) 2021 CyCAT.org project

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
~~~

