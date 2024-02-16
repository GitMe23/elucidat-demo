import utilities

def before_scenario(context, scenario):
    context.driver = utilities.initialise_driver()
      
def after_scenario(context, scenario):
    context.driver.quit()

