import os

input_dir = 'data'
output_dir = 'output'

command = 'ogr2ogr -f "ESRI Shapefile" {output} {input}'
for file in os.listdir(input_dir):
  if file.endswith('.gpkg'):
    input = os.path.join(input_dir, file)
    filename = os.path.splitext(os.path.basename(file))[0]
    output =  os.path.join(output_dir, filename + '.shp')
    os.system(command.format(input=input, output=output))