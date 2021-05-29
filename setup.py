from setuptools import setup

setup(
    version_config={
        "dirty_template": "{tag}.dev{ccount}",
    },
    setup_requires=['setuptools-git-versioning']
)
