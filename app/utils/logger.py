import logging



class Logger():
  def __init__(self, scope=None):   
    self._scope = scope
    self._logger = self.setupLog(scope)
  
  def setupLog (self, name) :
    log = logging.getLogger(name)

    logging.basicConfig(
      filename='logger.txt',
      format='%(name)s - %(levelname)s - %(message)s'
    )

    log.setLevel(logging.DEBUG)

    return log
  
  def info(self, msg):
    return self._logger.info(f"{msg}")