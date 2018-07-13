class VIMLayerInterface:

    def create_site(site, controller):
        """ Create given site in the given controller.

        :param site: (XOS Site) site to be created.
        :param controller: (XOS Controller) controller.

        :returns: (String) site id.
        """

    def create_slice(slice, controller):
        """ Create given slice in the given controller.

        :param slice: (XOS Slice) slice to be created.
        :param controller: (XOS Controller) controller.

        :returns: (String) slice id.
        """

    def create_user(user, controller):
        """ Create given user in the given controller.

        :param user: (XOS User) user to be created
        :param controller: (XOS Controller) controller

        :returns: (String) user id
        """

    def create_network(network, controller):
        """ Create given network in the given controller.

        :param network: (XOS Network) network to be created.
        :param controller: (XOS Controller) controller.

        :returns: (String) network id.
        """

    def create_subnet_to_network(subnet_name, network_name, cidr, gateway_ip, controller, start_ip=None, end_ip=None):
        """ Create and add subnet to the network whose name matches the given network_name of the given controller 
        using the given parameters.

        :param subnet_name: (String) name of the subnet to be created.
        :param network_name: (String) name of the network the subnet is attached to.
        :param cidr: (String) Classless Inter-Domain Routing (CIDR) representation of the subnet that should be 
                     assigned to the subnet (e.g., 10.123.0.0/24).
        :param gateway_ip: (String) IP that is assigned to the gateway for this subnet (e.g., 10.123.0.1).
        :param controller: (XOS Controller) controller.
        :param start_ip (optional): (String) starting address from which the IP should be allocated from the subnet 
                                    pool.
        :param end_ip (optional): (String) last IP that should be assigned from the subnet pool.

        :returns: (String) subnet id.
        """

    def add_image(image, controller):
        """  Add given image in the given controller.

        :param image: (XOS Image) image to be added
        :param controller: (XOS Controller) controller

        :returns: (String) image id
        """

    def add_user_role(role, user, controller, site=None, slice=None):
        """ Add given role to given user on the given site or slice of the given controller.
        
        :param role: (XOS Role) role to be added to the given user
        :param user: (XOS User) user that gets the role
        :param controller: (XOS Controller) controller
        :param site: (XOS Site) site where the user belongs
        :param slice: (XOS Slice) slice hwere the user belongs

        :returns: (Boolean) success (1 if success, 0 if fail)
        """

    def create_instance(instance, image_name, nics, user_data, availability_zone, metadata, controller):
        """ Create given compute instance in the given controller using the specified parameters.

        :param instance: (XOS Instance) instance to be created. 
        :param image_name: (String) name of the image to be instantiated.
        :param user_data: (String) opaque blob of data which is made available to the instance.
        :param nics: (dictionary) list of networks to which the instance’s interface should be attached 
                     (e.g., [{"kind": "net", "value": 1}].
        :param availability_zone_filter: (String) availability zone in which to create the server 
                                         (e.g., "nova:remarkable-behavior").
        :param metadata: (dictionary) key value pairs that should be provided as a metadata to the new instance 
                         (e.g, {"cpu_cores": 4})
        :param controller: (XOS Controller) controller

        :returns: (String List) [instance_id, instance_uuid, hostname]. intance_id is the id of the created instance, 
                  instance_uuid is a unique key identifier for the created instance, and hostname is the hostname of the 
                  hypervisor.
        """

    def create_port(port, controller):
        """ Create given port in the given controller.

        :param port: (XOS Port) port to be created.
        :param controller: (XOS Controller) controller.
        
        :returns: (dictionary) dictionary with information of the created port (id, fixed_ips, mac_address)
        """

    def create_role(role, controller):
        """ Create given role in the given controller.

        :param role: (XOS Role) role to be created
        :param controller: (XOS Controller) controller

        :returns: (Boolean) success (1 if success, 0 if fail)
        """

    def quotas_update(slice_id, max_instances, controller):
        """ Update quotas for the given slice in the given controller.

        :param slice_id: (String) slice id.
        :param max_instances: (int) maximum number of instances in this slice.
        :param controller: (XOS Controller) controller.

        :returns: (Boolean) success (1 if success, 0 if fail)
        """

    def get_networks(controller):
        """ Retrieve a listing of networks from the given controller.
        
        :param controller: (XOS Controller) controller.

        :returns: (list of dictionaries) list of dictionaries with networks information from the controller
        """

    def get_images(controller):
        """ Retrieve a listing of images from the given controller.
        
        :param controller: (XOS Controller) controller.

        :returns: (list of dictionaries) list of dictionaries with images information from the controller
        """

    def get_ports(controller):
        """ Retrieve a listing of ports from the given controller.
        
        :param controller: (XOS Controller) controller.

        :returns: (list of dictionaries) list of dictionaries with ports information from the controller
        """

    def get_admin_role(controller):
        """ Retrieve the admin role from the given controller.
        
        :param controller: (XOS Controller) controller.

        :returns: (String) admin role name.
        """    

    def delete_site(site_id, controller):
        """ Delete site whose id matches the given site_id from the given controller.

        :param site_id: (String) site_id of the site to be deleted.
        :param controller: (XOS Controller) controller.

        :returns: (Boolean) success (1 if success, 0 if fail)
        """

    def delete_slice(slice_name, controller):
        """ Delete given slice whose name matches the given slice_name from the given controller.

        :param slice_name: (String) name of the slice to be deleted.
        :param controller: (XOS Controller) controller.

        :returns: (Boolean) success (1 if success, 0 if fail)
        """

    def delete_user(user_id, controller):
        """ Delete user whose id matches the given user_id from the given controller.
        
        :param user_id: (String) user_id of the user to be deleted.
        :param controller: (XOS Controller) controller.

        :returns: (Boolean) success (1 if success, 0 if fail)
        """

    def delete_network(network_name, controller):
        """ Delete network whose name matches the given network_name from the given controller.

        :param network_name: (String) name of the network to be deleted.
        :param controller: (XOS Controller) controller.

        :returns: (Boolean) success (1 if success, 0 if fail)
        """

    def delete_user_role(role_name, user_id, controller, site_id=None, slice_id=None):
        """ Delete role whose name matches the given role_name from the user whose id matches the given user_id from 
        the given controller in the given site or slice whose id match the given site_id or slice_id respectively.

        :param role_name: (String) name of the role to be deleted. 
        :param user_id: (String) id of the user.
        :param controller: (XOS Controller) controller.
        :param site_id: (String) id of the site.
        :param slice_id: (String) id of the slice.

        :returns: (Boolean) success (1 if success, 0 if fail)
        """

    def delete_instance(instance_name, controller):
         """ Delete instance whose name matches the given instance_name from the given controller.

        :param instance_name: (String) name of the instance to be deleted.
        :param controller: (XOS Controller) controller.

        :returns: (Boolean) success (1 if success, 0 if fail)
        """

    def delete_port(port_id, controller):
        """ Delete port whose id matches the given port_id from the given controller.
        
        :param port_id: (String) id of the port to be deleted.
        :param controller: (XOS Controller) controller.

        :returns: (Boolean) success (1 if success, 0 if fail)
        """