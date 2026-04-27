data = """{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{{ name }} | Portfolio</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: Arial, sans-serif; background: #f0f2f5; color: #333; }
    header { background: linear-gradient(135deg, #1a1a2e, #16213e, #0f3460); color: white; padding: 60px 20px; text-align: center; }
    .profile-pic { width: 150px; height: 150px; border-radius: 50%; object-fit: cover; border: 4px solid #e94560; margin-bottom: 20px; box-shadow: 0 0 20px rgba(233,69,96,0.5); }
    header h1 { font-size: 2.5em; margin-bottom: 8px; color: #fff; }
    header .subtitle { font-size: 1.1em; color: #e94560; font-weight: bold; margin-bottom: 8px; }
    header .meta { font-size: 0.95em; opacity: 0.75; }
    .badge { display: inline-block; background: #e94560; color: white; padding: 5px 15px; border-radius: 20px; font-size: 0.85em; margin-top: 10px; }
    .container { max-width: 1000px; margin: 40px auto; padding: 0 20px; }
    .section { background: white; border-radius: 12px; padding: 30px; margin-bottom: 25px; box-shadow: 0 4px 15px rgba(0,0,0,0.08); }
    .section h2 { color: #0f3460; margin-bottom: 20px; border-bottom: 3px solid #e94560; padding-bottom: 10px; font-size: 1.4em; }
    .skills { display: flex; flex-wrap: wrap; gap: 10px; }
    .skills span { background: linear-gradient(135deg, #0f3460, #e94560); color: white; padding: 8px 18px; border-radius: 20px; font-size: 0.9em; }
    .projects-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 20px; }
    .project-card { background: #f8f9fa; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.1); transition: transform 0.3s, box-shadow 0.3s; }
    .project-card:hover { transform: translateY(-8px); box-shadow: 0 8px 25px rgba(233,69,96,0.3); }
    .project-card img { width: 100%; height: 180px; object-fit: cover; }
    .project-card .info { padding: 15px; }
    .project-card h3 { color: #0f3460; margin-bottom: 8px; }
    .project-card p { font-size: 0.9em; color: #666; margin-bottom: 12px; }
    .project-card a { color: white; background: #e94560; text-decoration: none; font-size: 0.85em; font-weight: bold; padding: 6px 14px; border-radius: 20px; display: inline-block; }
    .project-card a:hover { background: #0f3460; }
    .social a { display: inline-block; margin-right: 15px; color: white; background: linear-gradient(135deg, #0f3460, #e94560); text-decoration: none; font-weight: bold; padding: 10px 20px; border-radius: 25px; margin-top: 5px; }
    .social a:hover { opacity: 0.85; }
    footer { text-align: center; padding: 25px; background: #1a1a2e; color: #aaa; font-size: 0.9em; margin-top: 20px; }
  </style>
</head>
<body>
  <header>
    <img src="{% static 'images/pavel.jpg' %}" alt="Pavel Rahman" class="profile-pic">
    <h1>Hi, I'm {{ name }} 👋</h1>
    <p class="subtitle">{{ title }}</p>
    <p class="meta">🏢 {{ company }} &nbsp;|&nbsp; 📍 {{ location }}</p>
    <span class="badge">✅ Available for Freelance & Fulltime</span>
  </header>
  <div class="container">
    <div class="section">
      <h2>👤 About Me</h2>
      <p>{{ about }}</p>
    </div>
    <div class="section">
      <h2>🛠️ Skills</h2>
      <div class="skills">
        {% for skill in skills %}<span>{{ skill }}</span>{% endfor %}
      </div>
    </div>
    <div class="section">
      <h2>🎨 Projects</h2>
      <div class="projects-grid">
        {% for project in projects %}
        <div class="project-card">
          <img src="{{ project.image }}" alt="{{ project.name }}">
          <div class="info">
            <h3>{{ project.name }}</h3>
            <p>{{ project.description }}</p>
            <a href="{{ project.link }}" target="_blank">View on Behance</a>
          </div>
        </div>
        {% endfor %}
      </div>
    </div>
    <div class="section">
      <h2>🌐 Find Me Online</h2>
      <div class="social">
        <a href="{{ social.facebook }}" target="_blank">📘 Facebook</a>
        <a href="{{ social.behance }}" target="_blank">🎨 Behance</a>
      </div>
    </div>
  </div>
  <footer><p>© 2026 {{ name }} — All rights reserved.</p></footer>
</body>
</html>"""

with open('main/Templates/home.html', 'w', encoding='utf-8') as f:
    f.write(data)
print('Done! Template written successfully!')