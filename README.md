# starter repo

This repository is dedicated to the conversion of your OpenTofu-based code into immutable workflows. These workflows are designed to be launchable and shareable for others to utilize. 

This repository provide samples files and skeleton directories where you can add your Terraform/OpenTofu code. It is structured as follows:

- `shellouts/_config0_configs/`
   - This folder contains a sample script for installing `kubectl` specifically for Amazon Elastic Kubernetes Service (EKS).

- `execgroups/_config0_configs/`
   - This folder contains
      - a template for copying/renaming to __\<new execgroup>__, adding your existing Terraform code, and checking the code in.
      - an example for creating an EC2 VM execgroup named "__ec2_server__".

- `stacks/_config0_configs/`: 
   - This folder contains
     - a template for copying/renaming to __\<new stack>__ to serve as the entry point to __\< new execgroup>__ containing the unmodified Terraform code.
     - an example for creating a stack (entry point) called "__aws_ec2_server__" for the `execgroup` "__ec2_server__".
      
- `sample/doks`:
    - This folder contains
       - __OpenTofu__ folder - contains sample unmodified OpenTofu files for creating Digital Ocean Kubernetes (doks)
       - __Config0__ folder - contains sample Config0 file to create a stack or entry point for DOKS
