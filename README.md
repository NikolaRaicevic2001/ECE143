# ECE143
ECE 143 - Programming For Data Analysis

## Docker
### Docker Image Installation
    docker pull continuumio/miniconda3

### Docker Container Run 
    docker run -i -t continuumio/miniconda3 /bin/bash
    
### Docker Container Run with Mount
    docker run -it --mount type=bind,source="C:\Users\nikra\Desktop\UCSD_2024_Fall\ECE 143 - Programming For Data Analysis",target=/mnt/ECE143_Container continuumio/miniconda3:latest /bin/bash
    
    docker run -it --mount type=bind,source="C:\Users\nikra\Desktop\UCSD_2024_Fall\ECE 143 - Programming For Data Analysis",target=/mnt/ECE143_Container ipython/ipython:latest /bin/bash