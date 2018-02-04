class PriceMonitorException:
    """ Common parent class to all custom exceptions. """
    pass


class ConfigurationFileMissing(RuntimeError, PriceMonitorException):
    pass
