'''
Created on May 17, 2022

@author: mballance
'''
from unittest.case import TestCase
from tbgen.template_rgy import TemplateRgy

class TestDiscovery(TestCase):
    
    def test_smoke(self):
        rgy = TemplateRgy.inst()
        
        print("Templates: %s" % str(rgy.templates))
        print("Path: %s" % rgy.templates[0].path)