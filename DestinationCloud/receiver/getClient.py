from keystoneauth1.identity import v3
from keystoneauth1 import session
from novaclient import client as novClient
from neutronclient.v2_0 import client as neutClient
from glanceclient import Client as glanceClient
from glanceclient.common import utils

<<<<<<< HEAD
def getNeutronClient(auth_url, username, password, project_name, user_domain_name, project_domain_name):
    auth = v3.Password(auth_url= auth_url,
=======
def getNeutronClient(controllerIP, username, password, project_name, user_domain_name, project_domain_name):
    auth = v3.Password(auth_url= 'http://'+controllerIP+':35357/v3',
>>>>>>> 20d128af4b6809f5a311e57da1a2b8835663a8dd
                           username = username,
                           password= password,
                           project_name = project_name,
                           user_domain_name = user_domain_name,
                           project_domain_name = project_domain_name)
    sess = session.Session(auth=auth)
    neutron = neutClient.Client(session=sess)
    return neutron

<<<<<<< HEAD
def getNovaClient(auth_url, username, password, project_name, user_domain_name, project_domain_name):
    auth = v3.Password(auth_url= auth_url,
=======
def getNovaClient(controllerIP, username, password, project_name, user_domain_name, project_domain_name):
    auth = v3.Password(auth_url= 'http://'+controllerIP+':35357/v3',
>>>>>>> 20d128af4b6809f5a311e57da1a2b8835663a8dd
                           username = username,
                           password= password,
                           project_name = project_name,
                           user_domain_name = user_domain_name,
                           project_domain_name = project_domain_name)
    sess = session.Session(auth=auth)
    nova = novClient.Client("2.1", session=sess)

    return nova


<<<<<<< HEAD
def getGlanceClient(auth_url, username, password, project_name, user_domain_name, project_domain_name):
    auth = v3.Password(auth_url= auth_url,
=======
def getGlanceClient(controllerIP, username, password, project_name, user_domain_name, project_domain_name):
    auth = v3.Password(auth_url= 'http://'+controllerIP+':35357/v3',
>>>>>>> 20d128af4b6809f5a311e57da1a2b8835663a8dd
                           username = username,
                           password= password,
                           project_name = project_name,
                           user_domain_name = user_domain_name,
                           project_domain_name = project_domain_name)
    sess = session.Session(auth=auth)
    glance = glanceClient("2", session=sess)

    return glance

<<<<<<< HEAD
=======

"""
if __name__=='__main__':
    neutron =  getNeutronClient('172.26.17.153', 'admin', '2229', 'admin', 'default', 'default')
    nova =  getNovaClient('172.26.17.153', 'admin', '2229', 'admin', 'default', 'default')
    #networkInfo = {'name': 'mynetwork', 'admin_state_up': True, 'router:external':True, 'provider:network_type':'vxlan', 'shared': True}
   networkID =  nova.networks.find(label='Extnet').id
    for subnet in  neutron.list_subnets()["subnets"]:
              if subnet["network_id"] == networkID:
                      subnetID = subnet["id"]
    router = createRouter(neutron, "routerTest", networkID, "true", "172.26.17.49", subnetID, "true") 
    print router["router"]["id"]  
    configFilePath = "/home/controller2/testCode/configuration.json"
    configureNetwork(configFilePath, neutron, nova)"""
>>>>>>> 20d128af4b6809f5a311e57da1a2b8835663a8dd
