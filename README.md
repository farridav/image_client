# Image Client

A wrapper library around PIL for image manipulations

### Getting Started

Make a virtualenv and install dependencies

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r dev_requirements.txt

### Development

    git checkout develop
    git pull origin develop
    git checkout -b <your_username>/<your_cool_feature>

Write well tested code you can be proud of

    git commit -am "Commit message in the imperative"
    git push origin <your_username>/<your_cool_feature>

Make a pull request against develop, have it reviewed and merged by somebody else

### Testing

    tox

### Deployment

Bump the version in setup.py, make a pull request into `master`, use the PR description to detail your changes
(think release notes)

Review and merge, deployments are done within CI on merge, a python package will be packaged up and uploaded to our
pypi server
