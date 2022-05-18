
import os

from tbgen import TemplateRgy
from tbgen.template_data import TemplateData


print("TODO: register plug-in")

pkgdir = os.path.dirname(os.path.abspath(__file__))
data = TemplateData(
    name="pyuvm",
    path=os.path.join(pkgdir, "share/template_files"),
    short_desc="PyUVM Templates")

TemplateRgy.inst().addTemplate(data)

