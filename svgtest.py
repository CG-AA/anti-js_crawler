import svgwrite
from svgwrite import cm, mm
import cairosvg

def create_svg(d, filename):
    dwg = svgwrite.Drawing(filename, profile='tiny')
    dwg.add(dwg.path(d=d, transform="scale(1, 1)"))
    dwg.save()