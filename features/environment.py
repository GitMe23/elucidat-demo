import utilities

def before_all(context):
   utilities.write_properties()

def before_scenario(context, scenario):
    context.driver = utilities.initialise_driver()
      
def after_scenario(context, scenario):
    context.driver.quit()

