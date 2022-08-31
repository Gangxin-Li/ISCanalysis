# here is the basic usage framework

1. Transfer the vtc file to nii file.

Open the "Transfer_vtc_to_nii.py" at the last line
Change to the folder you wanna transfer, it will automatically	transfer the all of the vtc files to the Wii files.

2. Transfer the msg file to nii file.

Open the "Transfer_msk_to_nii.py" file and roll down to the last line
Change to the folder which the mask exist. And it will output the correct mask.

3. Using "isc_cli.py" to calculate the Intern subject calculations.

At the command line input the following command 
        python3 isc_cli.py --input s1.nii.gz s2.nii.gz s3.nii.gz \\
        --output isc --mask mask.nii.gz --zscore --fisherz

        python3 isc_cli.py --input s*.nii.gz --output iscs.nii.gz \\
        --mask mask.nii.gz --zscore --summarize stack

        python3 isc_cli.py --input s*.nii.gz --output mean_isc.nii.gz \\
        --mask mask.nii.gz --zscore --summarize mean
You will get the result on where the folder you given.