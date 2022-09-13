import logging

logging.basicConfig(
  filename='app.txt',
  format='%(name)s - %(levelname)s - %(message)s'
)

class Logger():
  def __init__(self, scope=None):   
    self._logger = self.setupLog(scope)
  
  def setupLog (self, name) :
    log = logging.getLogger(name)

    logging.basicConfig(format="%(levelname)s %(asctime)s %(funcName)s %(lineno)d %(message)s", filename='app.txt')

    log.setLevel(logging.DEBUG)

    log.addHandler( logging.handlers.RotatingFileHandler('%s.log' % name, mode='a', maxBytes=50000, backupCount=5) )

    return log
  
  def info(self, msg):
    return self._logger.info(f"{msg}")