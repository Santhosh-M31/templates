import os 

input_files = [file for file in os.listdir() if file.endswith('.shp')]
print(input_files) 

command = 'ogr2ogr -f "GPKG" {output} {input}' 

for input in input_files:
    output = os.path.join('output', input.split('.')[0] + '.gpkg')
    os.system(command.format(input=input, output=output))
    print('created {}'.format(output)) 
