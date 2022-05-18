'''
Created on May 17, 2022

@author: mballance
'''
from unittest.case import TestCase
from tbgen.template_rgy import TemplateRgy
import sys
from uvmf_yaml_utils.uvmf_core.yaml2uvmf import DataClass
from test_base import TestBase
import traceback
from uvmf_yaml_utils.library import Library
from uvmf_yaml_utils.gen_spec import GenSpec

class TestDiscovery(TestBase):
    
    def test_smoke(self):
        rgy = TemplateRgy.inst()
        
        env1 = self.createFile("env1.yaml", 
        """
        uvmf:
          environments:
            env1: {}
        """)        
        
        print("Templates: %s" % str(rgy.templates))
        print("Path: %s" % rgy.templates[0].path)
        
        lib = Library()
        lib.addPath(env1)
        
        lib.load()
        
        spec = GenSpec(
            template_path='/project/fun/uvmf/pytbgen-templates-pyuvm/src/tbgen_templates_pyuvm/share/template_files',
            outdir="my_bench"
            )
        
        lib.generate(spec)

        print("sys.argv=%s" % str(sys.argv))
        