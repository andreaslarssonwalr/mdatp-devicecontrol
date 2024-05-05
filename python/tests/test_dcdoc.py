import mdedevicecontrol.dcdoc as doc
import os
import xml.etree.ElementTree as ET

class DcDocArgs: 

    def __init__(self):

        self.query = None
        self.scenarios = None
        self.in_file = None

        self.source_path = doc.dir_path(".")
        self.format = "text"
        self.out_file = None
        self.dest = doc.dir(".")

        self.templates_path = doc.path_array("templates")
        self.template = "dcutil.j2"
        self.readme_template = "readme.j2"
        self.description_template = "description.j2"
        self.readme_file = "readme.md"
        
        self.generated_files_locations = None
        
        
    def set_source_path(self,path):
        self.source_path = doc.dir_path(path)

    
    def set_dest(self,dest):
        self.dest = doc.dir(dest)

    def set_templates_path(self,templates_path):
        self.templates_path = doc.path_array(templates_path)

    
        

        

def test_generate_mac_docs():
        
    args = DcDocArgs()
    args.set_source_path(os.getcwd()+"/../macOS/policy/samples")
    args.set_dest(os.getcwd()+"/../macOS/policy/samples")
    args.scenarios = os.getcwd()+"/../macOS/policy/samples/scenarios.json"
    

    doc.main(args)
    return True
    
