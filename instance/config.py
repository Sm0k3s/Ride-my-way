
class Config(object):
	DEBUG = False

class DevelopmentConfig(Config):
	"""Configs for development"""
	DEBUG = True

class TestingConfig(Config):
	"""Configs for testing"""
	TESTING = True
	DEBUG = True

class StagingConfig(Config):
	"""Configurations for config"""
	DEBUG = True

class ProductionConfig(Config):
	"""Set the production config to False cause we are currently in development"""
	DEBUG = False
	TESTING = False

app_config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'staging': StagingConfig,
	'production': ProductionConfig,
}
