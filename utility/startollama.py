import subprocess
import os

def start_ollama_process():
    """
    Starts the Ollama server as a background process.
    Returns the subprocess Popen object if successful, None otherwise.
    """
    #print("Attempting to start Ollama server...")
    try:
        cmd = ["ollama", "serve"] 

        # Use platform-specific methods to detach the process
        if os.name == 'nt':  # Windows
            # CREATE_NO_WINDOW prevents a console window from popping up
            # DETACHED_PROCESS detaches it from the parent process
            process = subprocess.Popen(cmd,
                                    creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NO_WINDOW,
                                    stdout=subprocess.DEVNULL, 
                                    stderr=subprocess.DEVNULL) 
        else: # Unix-like systems (Linux, macOS)
            process = subprocess.Popen(cmd,
                                    stdout=subprocess.DEVNULL,
                                    stderr=subprocess.DEVNULL,
                                    preexec_fn=os.setsid) # Detach process group
        #print(f"Ollama server process started with PID: {process.pid}")
        return process
    except FileNotFoundError:
        #print("Error: 'ollama' command not found. Please ensure Ollama is installed and in your system's PATH.")
        return None
    except Exception as e:
        #print(f"Error starting Ollama server: {e}")
        return None