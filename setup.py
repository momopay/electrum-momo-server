from setuptools import setup

setup(
    name="electrum-momo-server",
    version="1.0",
    scripts=['run_electrum_momo_server','electrum-momo-server'],
    install_requires=['plyvel','jsonrpclib', 'irc >= 11, <=14.0', 'x11_hash'],
    package_dir={
        'electrumserver':'src'
        },
    py_modules=[
        'electrumserver.__init__',
        'electrumserver.utils',
        'electrumserver.storage',
        'electrumserver.deserialize',
        'electrumserver.networks',
        'electrumserver.blockchain_processor',
        'electrumserver.server_processor',
        'electrumserver.processor',
        'electrumserver.version',
        'electrumserver.ircthread',
        'electrumserver.stratum_tcp'
    ],
    description="momo Electrum Server",
    author="Thomas Voegtlin ,ELM4ever, Propulsion, TheLazieR",
    author_email="thomasv@electrum.org, thelazier@gmail.com",
    license="MIT Licence",
    url="https://github.com/spesmilo/electrum-server/ , https://github.com/thelazier/electrum-momo-server/",
    long_description="""Server for the Electrum Lightweight momo Wallet"""
)
