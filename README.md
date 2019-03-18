# My Project


## Overview

This is your new kernelai project which was generated using KernelAI `0.12.1` by running:

```
kernelai new
```

To get started, visit our [Getting Started Guide](https://github.com/quantumblack/asset-kernel-ai/wiki/Get-Started).
You can find our wiki [here](https://github.com/quantumblack/asset-kernel-ai/wiki).

## Rules and guidelines

In order to get the best out of the template:
 * please don't remove any lines from the provided `.gitignore` file
 * make sure your results can be reproduced by adding the necessary data in `data/01_raw` only
 * don't commit any data to your repository
 * don't commit any credentials or local configuration to your repository
 * keep all credentials or local configuration in `conf/local/`

## Installing dependencies

Dependencies are declared in src/python/requirements.txt.
To install them

```
kernelai install
```

## Running

```
kernelai run
```

## Testing

``kernelai test``

Please have a look at the file `src/python/tests/test_example.py` for instructions on how to write your tests.

To configure the coverage threshold, please have a look at the file `.coveragerc`.


## Linting

```
kernelai lint
```

To configure pylint, have a look at the file `.pylintrc`


## Configure CI/CD

The project comes with a template that configures the steps to be run on CircleCI.
Please have a look at the file `.circleci/config.yml` for details.

To enable CI/CD for you project, go to [CircleCi](https://circleci.com/dashboard) and log in with your GitHub account.
Then click "Add project" on the left sidebar, find your repository, and click the "Set Up Project" button. Finally, click the "Start building" button.

Now, every time you push code to github CircleCI is going to run all the steps you have specified in `.circleci/config.yml` and will notify you about the results.
Finally, you can configure GitHub to only allow merging code to `master` and `develop` if the build is green, by going into your GitHub's repository settings. 

### Working with KernelAI from notebooks

In order to use notebooks in your KernelAI project, you need to install jupyter:

    $ pip install jupyter
    
For using Jupyter Lab, you need to install it:

    $ pip install jupyterlab

After installing Jupyter, you can start a local notebook server:
    
    $ kernelai jupyter notebook

You can also start Jupyter Lab:
    
    $ kernelai jupyter lab
 
And if you want to run an ipython session:
    
    $ kernelai ipython

Running Jupyter or ipython this way provides the following variables in 
scope: `proj_dir`, `proj_name`, `conf`, `io`, `parameters`, `startup_error`

#### Ignoring notebook output cells in git

In order to automatically strip out all output cell contents before commiting 
to git, you can run `kernelai activate-nbstripout`. This will add a hook in
`.git/config` which will run `nbstripout` before anything is commited to git. 
Note that your output cells will be left intact locally.

## Visualising the final pipeline

In order to visualise your pipeline, you need to install `kernelviz` from 
QB's PyPI repository:

    $ pip install kernelviz

After you have the visualisation tool installed, you can run it by calling:

    $ kernelai viz

## Package the project

In order to package the project's python code in `.egg` and/or a `.wheel` file,
you can run:

    $ kernelai package

After running that, you can find the two packages in `src/python/dist/`

## Building API documentation

To build API docs for your code using sphnix, run

    $ kernelai build-docs

See your documentation by opening `docs/build/html/index.html`


## Docker

If working with docker, please have a look at the `Dockerfile` and the `kernelai docker` group of commands:

```
$ kernelai docker --help

Usage: kernelai docker [OPTIONS] COMMAND [ARGS]...

  Dockerize project

Options:
  -h, --help  Show this message and exit.

Commands:
  build    Build a Docker image for the project.
  ipython  Run ipython in Docker container.
  jupyter  Run jupyter lab / notebook in Docker container.
  run      Run the pipeline in Docker container.
```
