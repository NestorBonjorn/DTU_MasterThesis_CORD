class SDNCLayerInterface:

    def deploy_sdnc(sdnc_service):
        """ Deploy the given SDN controller.

        :param sdnc_service: (XOS SDNCService) SDNCService model object.

        return: (Boolean) success (1 if success, 0 if fail)
        """

    def add_early_configuration(sdnc_service, sdnc_app):
        """ Add early configuration values to the given SDN controller.

        :param sdnc_service: (XOS SDNCService) SDNCService model object.
        :param sdnc_app: (XOS SDNCApp) SDNCApp model object.

        return: (Boolean) success (1 if success, 0 if fail)
        """

    def add_component_configuration(sdnc_service, sdnc_app):
        """ Add component configuration values to the given SDN controller.

        :param sdnc_service: (XOS SDNCService) SDNCService model object.
        :param sdnc_app: (XOS SDNCApp) SDNCApp model object.

        return: (Boolean) success (1 if success, 0 if fail)
        """

    def add_configuration(sdnc_service, sdnc_app):
        """ Add configuration values to the given SDN controller.

        :param sdnc_service: (XOS SDNCService) SDNCService model object.
        :param sdnc_app: (XOS SDNCApp) SDNCApp model object.

        return: (Boolean) success (1 if success, 0 if fail)
        """

    def install_app(sdnc_service, sdnc_app):
        """ Install application in the given SDN controller.

        :param sdnc_service: (XOS SDNCService) SDNCService model object.
        :param sdnc_app: (XOS SDNCApp) SDNCApp model object.

        return: (Boolean) success (1 if success, 0 if fail)
        """

    def activate_app(sdnc_service, sdnc_app):
        """ Activate application in the given SDN controller.

        :param sdnc_service: (XOS SDNCService) SDNCService model object.
        :param sdnc_app: (XOS SDNCApp) SDNCApp model object.

        return: (Boolean) success (1 if success, 0 if fail)
        """

    def post_route(data, fabric_service):
        """ Send REST API POST call to the given fabric_service (SDN controller) with the body generated from the 
        given data.

        :param data: (Python dictionary) data used to generate the body of the REST API POST call.
        :param fabric_service: (XOS FabricService) SDN controller.
        
        :returns: (Boolean) success (1 if success, 0 if fail)
        """
