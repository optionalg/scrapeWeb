from configparser import SafeConfigParser

def writeConfig():
  config = SafeConfigParser()
  config.read('config.ini')
  config.add_section('main')
  config.set('main', 'protocol', 'http')
  config.set('main', 'domain', 'www.eveonline.com')

  with open('config.ini', 'w') as f:
    config.write(f)

def readConfig( section, key ):
  config = SafeConfigParser()
  config.read('config.ini')
  return config.get(section, key)