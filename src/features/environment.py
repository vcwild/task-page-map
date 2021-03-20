from selenium.webdriver import Remote
import ipdb

def setup_debug_on_error(userdata):
    global BEHAVE_DEBUG_ON_ERROR
    BEHAVE_DEBUG_ON_ERROR = userdata\
        .getbool("BEHAVE_DEBUG_ON_ERROR")

def before_all(context):
    setup_debug_on_error(context.config.userdata)
    browser_name = context.config.userdata.get('browser')
    context.browser = Remote(
        desired_capabilities={
            'browserName': browser_name,
            'browserTimeout': 10
        }
    )

def after_step(context, step):
    if BEHAVE_DEBUG_ON_ERROR and step.status == 'failed':
        ipdb.spost_mortem(step.exec_traceback)

def after_all(context):
    context.browser.quit()