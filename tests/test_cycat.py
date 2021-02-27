from cycat import __version__
from cycat import url

def test_version():
    assert __version__ == '0.1.0'

def test_url_generate():
    url.generate(publisher="misp", project="eveNT")
    cycat_url = url.generate(publisher="samratashok", project="nishang")
    return cycat_url

def test_url_validate():
    return url.validate(url="misp:event:91b49dee-6d22-468a-87f4-fbd08997a2d4")

def test_url_build():
    return url.build(publisher="misp", project="EVENT", uuid="5c48e0b6-e9f6-455e-a228-90723004e65c")

test_version()
assert test_url_generate() == 'samratashok:nishang:2605ff5e-342c-5326-8744-96a34b7e581e'
assert test_url_validate()
assert test_url_build() == 'misp:event:5c48e0b6-e9f6-455e-a228-90723004e65c'
