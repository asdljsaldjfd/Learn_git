" Hi Everyone  today i am leaning about git"
print("Hello world everyone")
print("letssee if this adds")
print("I WANT TO CHECK IF HTIS ALSO EXISTS")
import os
import zipfile
import subprocess
from pathlib import Path

def pack_pbit_file_python():
    """
    Pack an unpacked Power BI template (.pbit) folder back into a .pbit file
    using Python's zipfile module
    """
    # REPLACE THIS with your actual folder path containing the unpacked .pbit files
    unpacked_folder_path = ""
    
    # Output path - this will create abc.pbit in the same directory as the script
    output_pbit_path = ""
    
    # Validate input path
    unpacked_path = Path(unpacked_folder_path)
    if not unpacked_path.exists() or not unpacked_path.is_dir():
        print(f"ERROR: The path {unpacked_folder_path} does not exist or is not a directory")
        return
    
    # Create zip file
    print(f"Packing {unpacked_folder_path} into {output_pbit_path} using Python zipfile...")
    
    try:
        with zipfile.ZipFile(output_pbit_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(unpacked_folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    # Create relative path for files in the zip
                    arcname = os.path.relpath(file_path, unpacked_folder_path)
                    zipf.write(file_path, arcname)
        
        # Get absolute path for clearer output
        abs_output_path = os.path.abspath(output_pbit_path)
        print(f"SUCCESS: Packed .pbit file created at: {abs_output_path}")
        return abs_output_path
        
    except Exception as e:
        print(f"ERROR: Failed to create .pbit file: {str(e)}")
        return None

def pack_pbit_file_pbi_tools():
    """
    Pack an unpacked Power BI template (.pbit) folder back into a .pbit file
    using PBI Tools
    """
    # REPLACE THIS with your actual folder path containing the unpacked .pbit files
    unpacked_folder_path = ""
    
    # Output path - this will create abc.pbit in the same directory as the script
    output_pbit_path = ""
    
    # REPLACE THIS with the path to your PBITools.exe
    pbi_tools_path = ""
    
    # Validate input path
    unpacked_path = Path(unpacked_folder_path)
    if not unpacked_path.exists() or not unpacked_path.is_dir():
        print(f"ERROR: The path {unpacked_folder_path} does not exist or is not a directory")
        return
    
    # Validate PBI Tools path
    pbi_tools_file = Path(pbi_tools_path)
    if not pbi_tools_file.exists() or not pbi_tools_file.is_file():
        print(f"ERROR: PBI Tools not found at {pbi_tools_path}")
        print("Falling back to Python zipfile method...")
        return pack_pbit_file_python()
    
    # Check the version and commands of PBI Tools
    try:
        # First try to get help to see available commands
        help_cmd = [pbi_tools_path, "-h"]
        help_result = subprocess.run(help_cmd, capture_output=True, text=True)
        print(f"PBI Tools help output: {help_result.stdout}")
        
        # Try several common command formats for different versions
        
        # Option 1: "pack" command
        cmd = [pbi_tools_path, "pack", "-folder", unpacked_folder_path, "-pbitFile", output_pbit_path]
        print(f"Attempting: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"Command failed: {result.stderr}")
            
            # Option 2: "extract" with "-pack" flag
            cmd = [pbi_tools_path, "extract", "-pack", "-folder", unpacked_folder_path, "-target", output_pbit_path]
            print(f"Attempting: {' '.join(cmd)}")
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode != 0:
                print(f"Command failed: {result.stderr}")
                
                # Option 3: Using lowercase flags
                cmd = [pbi_tools_path, "pack", "-folder", unpacked_folder_path, "-output", output_pbit_path]
                print(f"Attempting: {' '.join(cmd)}")
                result = subprocess.run(cmd, capture_output=True, text=True)
                
                if result.returncode != 0:
                    print(f"Command failed: {result.stderr}")
                    print("All PBI Tools commands failed. Falling back to Python zipfile method...")
                    return pack_pbit_file_python()
        
        # Get absolute path for clearer output
        abs_output_path = os.path.abspath(output_pbit_path)
        print(f"SUCCESS: Packed .pbit file created at: {abs_output_path}")
        print(f"PBI Tools output: {result.stdout}")
        return abs_output_path
        
    except Exception as e:
        print(f"ERROR: Failed to run PBI Tools: {str(e)}")
        print("Falling back to Python zipfile method...")
        return pack_pbit_file_python()

if __name__ == "__main__":
    # Choose which method to use - set to True to use PBI Tools, False to use Python zipfile
    use_pbi_tools = True
    
    if use_pbi_tools:
        pack_pbit_file_pbi_tools()
    else:
        pack_pbit_file_python()


print("learning pull request")

print("need to write down for all the steps")
print("hello indeed")
