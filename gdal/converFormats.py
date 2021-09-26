import os 

#Get all Shape file directory
input_files = [file for file in os.listdir() if file.endswith('.shp')]

# GDAL commage to convert fileformats
command = 'ogr2ogr -f "GPKG" {output} {input}' 

# Iterate to convert all file as GeoPackage  
for input in input_files:
    
    # Construct output file with directory name 
    output = os.path.join('output', input.split('.')[0] + '.gpkg') 

    # Using String formats to replave input and output file name  
    os.system(command.format(input=input, output=output))

    # Display path when conversation is successful
    print('created {}'.format(output))