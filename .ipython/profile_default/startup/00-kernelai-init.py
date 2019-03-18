import logging.config
import os
from IPython.core.magic import register_line_magic


@register_line_magic
def reload_kernelai(line=None):
    """"Line magic which reloads all kernel default variables
    """
    global proj_dir
    global proj_name
    global conf
    global io
    global parameters
    global startup_error
    try:
        import kernelai.config.default_logger
        from myproj.run import init_context

        proj_name = os.path.basename(proj_dir)
        logging.info("** KernelAI project {}".format(proj_name))

        os.chdir(proj_dir)  # Move to project root

        # Load KernelAI context (conf, io, parameters)
        conf, io, parameters = init_context(proj_dir)

        logging.info('Defined global variables proj_dir, proj_name, '
                     'conf, io and parameters')
    except ImportError as err:
        startup_error = err
        if 'init_context' in str(err):
            message = ('The function `init_context` is missing from '
                       'my_proj_res/src/python/'
                       'myproj/run.py.'
                       '\nEither restore this function, or update '
                       'my_proj_res/'
                       '.ipython/profile_default/startup/00-kernel-init.py.')
        else:
            message = 'KernelAI appears not to be installed in your ' \
                      'current environment.'
        logging.error(message)
        raise err
    except Exception as err:
        startup_error = err
        logging.error("KernelAI's ipython session startup script failed:\n%s",
                      str(err))
        raise err


# Find the project root (./../../../)
startup_error = None
proj_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                        os.pardir, os.pardir, os.pardir))
reload_kernelai()
