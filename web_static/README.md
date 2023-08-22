
### W3C-VALIDATOR
To create a wrapper script for the W3C-Validator and make it accessible using a single command, you can follow a similar approach as the Betty wrapper script. Here's how you can do it:

1. **Create the Wrapper Script:**

   First, create a script that acts as a wrapper for the `w3c_validator.py` script. Create a file named `w3c-validator` (or any name you prefer) and add the following content to it:

   ```bash
   #!/bin/bash

   VALIDATOR_PATH="/path/to/W3C-Validator"  # Replace with the actual path to W3C-Validator directory
   VALIDATOR_SCRIPT="w3c_validator.py"

   if [ "$#" = "0" ]; then
       echo "No arguments passed."
       exit 1
   fi

   for argument in "$@" ; do
       echo -e "\n========== $argument =========="
       python3 "${VALIDATOR_PATH}/${VALIDATOR_SCRIPT}" "$argument"
   done
   ```

   Replace `/path/to/W3C-Validator` with the actual path to the directory where the `W3C-Validator` folder is located.

2. **Make the Script Executable:**

   After creating the script, make it executable with the following command:

   ```bash
   chmod a+x w3c-validator
   ```

3. **Move the Script to a Directory in PATH:**

   Next, move the `w3c-validator` script to a directory that is in your system's PATH. For example, you can use the `/usr/local/bin` directory:

   ```bash
   sudo mv w3c-validator /usr/local/bin/
   ```

4. **Usage:**

   Once the script is in a directory in your PATH, you can use it like this:

   ```bash
   w3c-validator <filename>
   ```

   Replace `<filename>` with the name of the HTML file you want to validate.

By creating this wrapper script, you're essentially creating a convenient way to run the W3C-Validator script from anywhere on your system. Just remember to replace `/path/to/W3C-Validator` with the actual path to the `W3C-Validator` directory and make sure that the `w3c_validator.py` script is located inside that directory.
