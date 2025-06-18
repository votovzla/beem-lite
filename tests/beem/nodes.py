# -*- coding: utf-8 -*-
from beem.nodelist import NodeList
from beem import Hive


def get_hive_nodes():
    nodelist = NodeList()
    nodes = nodelist.get_hive_nodes()
    nodelist.update_nodes(blockchain_instance=Hive(node=nodes, num_retries=10))
    return nodelist.get_hive_nodes()
    #return "https://beta.openhive.network"

