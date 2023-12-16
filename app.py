from flask import Flask, render_template, request
import subprocess
import webbrowser
import pyperclip

app = Flask(__name__)



# Function to handle system commands on macOS
def perform_system_command(command):
    try:
        subprocess.Popen(['sh', '-c', command])
        return f"System command executed: {command}"
    except Exception as e:
        return f"Error executing system command {command}: {str(e)}"

# Function to open a specific website
def open_website(website_url):
    try:
        webbrowser.open(website_url)
        return f"Website opened: {website_url}"
    except Exception as e:
        return f"Error opening website {website_url}: {str(e)}"

# Function to launch an application
def launch_application(application_name):
    try:
        subprocess.Popen(['open', '-a', application_name])
        return f"Application launched: {application_name}"
    except Exception as e:
        return f"Error launching application {application_name}: {str(e)}"

# Function to perform multimedia controls (e.g., play, pause, volume)
def multimedia_controls(action):
    try:
        # Implement your multimedia control logic here
        return f"Multimedia control executed: {action}"
    except Exception as e:
        return f"Error executing multimedia control {action}: {str(e)}"

# Function to execute custom scripts or commands
def run_custom_script(script_path):
    try:
        subprocess.Popen(['sh', '-c', script_path])
        return f"Custom script executed: {script_path}"
    except Exception as e:
        return f"Error executing custom script {script_path}: {str(e)}"

# Function to perform clipboard management actions
def clipboard_management(action):
    try:
        if action == 'undo':
            # Implement undo logic
            pass
        elif action == 'redo':
            # Implement redo logic
            pass
        elif action == 'selectall':
            # Implement select all logic
            pass
        elif action == 'save':
            # Implement save logic
            pass
        else:
            # Use pyperclip for basic clipboard actions
            if action == 'clear':
                pyperclip.copy('')
            elif action == 'copy':
                pyperclip.copy(pyperclip.paste())
            elif action == 'paste':
                # Implement paste logic
                pass
            elif action == 'cut':
                # Implement cut logic
                pass
        return f"Clipboard management executed: {action}"
    except Exception as e:
        return f"Error executing clipboard management {action}: {str(e)}"

@app.route('/')
def index():
    return render_template('index.html')

# Example route to launch an application
@app.route('/launch/<application_name>')
def launch_route(application_name):
    result = launch_application(application_name)
    return result

# Example route to perform a system command
@app.route('/system/<command>')
def system_route(command):
    result = perform_system_command(command)
    return result

# Example route to open a website
@app.route('/open/<website_url>')
def open_website_route(website_url):
    result = open_website(website_url)
    return result

# Example route to perform multimedia controls
@app.route('/multimedia/<action>')
def multimedia_controls_route(action):
    result = multimedia_controls(action)
    return result

# Example route to run a custom script
@app.route('/script/<script_path>')
def run_custom_script_route(script_path):
    result = run_custom_script(script_path)
    return result

# Example route for clipboard management
@app.route('/clipboard/<action>')
def clipboard_management_route(action):
    result = clipboard_management(action)
    return result

# Example route to open a website using POST method
@app.route('/open-website', methods=['POST'])
def open_website_post_route():
    data = request.get_json()
    url = data.get('url', '')
    result = open_website(url)
    return result

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
