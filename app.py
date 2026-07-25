import json
from flask import Flask

app = Flask(__name__)

def load_team_data():
    """Load the team data from the JSON file."""
    try:
        with open('team_data.json', 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

@app.route('/')
def display_roster():
    """Display the team roster as a beautiful HTML page."""
    team = load_team_data()
    
    if not team:
        return """
        <html>
            <head><title>Team Roster</title></head>
            <body style="font-family: Arial, sans-serif; text-align: center; margin-top: 50px;">
                <h1>🚀 Our Awesome DevOps Team</h1>
                <p style="color: red;">The team is empty. Add your profiles!</p>
            </body>
        </html>
        """
    
    # Build the HTML page dynamically
    html_content = """
    <html>
        <head>
            <title>Our DevOps Team</title>
            <style>
                body { font-family: Arial, sans-serif; background: #f4f4f9; margin: 0; padding: 20px; }
                .container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
                h1 { text-align: center; color: #333; }
                .member { background: #f9f9ff; margin: 15px 0; padding: 15px; border-radius: 8px; border-left: 4px solid #4CAF50; }
                .name { font-size: 1.2em; font-weight: bold; color: #2c3e50; }
                .role { color: #3498db; }
                .tech { color: #e67e22; }
                .footer { text-align: center; margin-top: 30px; color: #888; font-size: 0.9em; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🚀 Our Awesome DevOps Team</h1>
    """
    
    for member in team:
        name = member.get('name', 'N/A')
        role = member.get('role', 'N/A')
        tech = member.get('tech', 'N/A')
        html_content += f"""
                <div class="member">
                    <div class="name">👤 {name}</div>
                    <div class="role">💻 Role: {role}</div>
                    <div class="tech">🌍 Favorite Tech: {tech}</div>
                </div>
        """
    
    html_content += """
                <div class="footer">
                    🐳 Deployed with Docker | Built by the DevOps Class
                </div>
            </div>
        </body>
    </html>
    """
    
    return html_content

if __name__ == '__main__':
    # Run the app on all network interfaces so Docker can expose it
    app.run(host='0.0.0.0', port=8080)
