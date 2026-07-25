# coding: utf-8
import streamlit as st
from streamlit.components.v1 import html
import base64
from pathlib import Path
import glob

st.set_page_config(
    page_title="Consultorio Dr. Bruna Fabián Alberto",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ═══════════════════════════════════════════════════════
# CARGA DE IMAGEN - DETECTA AUTOMÁTICAMENTE EL FORMATO
# ═══════════════════════════════════════════════════════
def get_image_base64(image_path: str) -> str:
    """Convierte una imagen local a base64."""
    path = Path(image_path)
    if not path.exists():
        return ""
    with open(path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode("utf-8")
    ext = path.suffix.lower().lstrip('.')
    mime = f"image/{'jpeg' if ext == 'jpg' else ext}"
    return f"data:{mime};base64,{encoded}"

# Buscar doctor.jpg, doctor.jpeg, doctor.png, etc.
_ruta_doctor = None
for patron in ["doctor.jpg", "doctor.jpeg", "doctor.png", "doctor.webp"]:
    candidato = Path(__file__).parent / patron
    if candidato.exists():
        _ruta_doctor = candidato
        break

if _ruta_doctor is None:
    resultados = glob.glob(str(Path(__file__).parent / "doctor.*"))
    if resultados:
        _ruta_doctor = Path(resultados[0])

doctor_img_b64 = get_image_base64(str(_ruta_doctor)) if _ruta_doctor else ""

# Placeholder si no hay imagen
if not doctor_img_b64:
    doctor_img_b64 = "data:image/svg+xml;base64," + base64.b64encode(
        b'<svg xmlns="http://www.w3.org/2000/svg" width="300" height="400" viewBox="0 0 300 400"><rect fill="#1e293b" width="300" height="400"/><text fill="#D4AF37" font-family="serif" font-size="18" x="150" y="200" text-anchor="middle">Dr. Bruna F. Alberto</text></svg>'
    ).decode("utf-8")

st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp {background: transparent;}
</style>
""", unsafe_allow_html=True)

html_code = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Consultorio Dr. Bruna Fabián Alberto</title>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-dark: #0f172a;
            --gold: #D4AF37;
            --gold-gradient: linear-gradient(135deg, #D4AF37 0%, #F3E5AB 50%, #C5A028 100%);
            --text-light: #F8FAFC;
            --text-muted: #94A3B8;
            --glass-bg: rgba(15, 23, 42, 0.6);
            --glass-border: rgba(255, 255, 255, 0.1);
            --font-serif: 'Playfair Display', serif;
            --font-sans: 'Inter', sans-serif;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: var(--font-sans);
            color: var(--text-light);
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%);
            min-height: 100vh;
            padding: 40px 20px;
        }}
        .main-container {{
            max-width: 1000px;
            margin: 0 auto;
        }}
        .header {{
            text-align: center;
            margin-bottom: 40px;
            padding: 40px 30px;
            background: var(--glass-bg);
            backdrop-filter: blur(16px);
            border: 1px solid var(--glass-border);
            border-radius: 16px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.5);
        }}
        .header h1 {{
            font-family: var(--font-serif);
            font-size: 2.2rem;
            color: #fff;
            margin-bottom: 10px;
        }}
        .header .subtitle {{
            color: var(--gold);
            font-size: 0.85rem;
            letter-spacing: 3px;
            text-transform: uppercase;
            font-weight: 500;
        }}
        .section-title {{
            font-family: var(--font-serif);
            font-size: 1.8rem;
            text-align: center;
            margin: 40px 0 24px 0;
            color: #fff;
            position: relative;
        }}
        .section-title::after {{
            content: '';
            display: block;
            width: 60px;
            height: 2px;
            background: var(--gold);
            margin: 10px auto 0;
        }}
        
        /* --- SECCIÓN DOCTOR (CORREGIDA) --- */
        .doctor-section {{
            display: grid;
            grid-template-columns: 340px 1fr;
            gap: 35px;
            background: var(--glass-bg);
            backdrop-filter: blur(16px);
            border: 1px solid var(--glass-border);
            border-radius: 16px;
            padding: 35px;
            margin-bottom: 40px;
            align-items: start;
        }}
        .doctor-photo-container {{
            position: relative;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 8px 32px rgba(0,0,0,0.5);
            border: 2px solid var(--gold);
            background: #1e293b;
        }}
        .doctor-photo-container img {{
            width: 100%;
            height: auto;
            max-height: 650px;
            object-fit: contain;
            display: block;
        }}
        .doctor-info {{
            padding-top: 10px;
        }}
        .doctor-info h2 {{
            font-family: var(--font-serif);
            font-size: 1.8rem;
            color: var(--gold);
            margin-bottom: 8px;
        }}
        .doctor-info .title {{
            color: var(--text-muted);
            font-size: 0.85rem;
            letter-spacing: 2px;
            text-transform: uppercase;
            margin-bottom: 20px;
            padding-bottom: 15px;
            border-bottom: 1px solid rgba(212, 175, 55, 0.3);
        }}
        .doctor-info p {{
            line-height: 1.8;
            color: var(--text-light);
            margin-bottom: 15px;
            font-size: 0.95rem;
        }}
        .doctor-info .credentials {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 20px;
        }}
        .credential-tag {{
            background: rgba(212, 175, 55, 0.15);
            color: var(--gold);
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 0.8rem;
            border: 1px solid rgba(212, 175, 55, 0.3);
        }}
        
        .booking-card {{
            background: var(--glass-bg);
            backdrop-filter: blur(16px);
            border: 1px solid var(--glass-border);
            border-radius: 16px;
            padding: 40px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.5);
            margin-bottom: 40px;
        }}
        .form-label {{
            display: block;
            font-size: 0.85rem;
            color: var(--text-muted);
            margin-bottom: 8px;
            font-weight: 500;
        }}
        .booking-info {{
            background: rgba(212, 175, 55, 0.1);
            border: 1px solid rgba(212, 175, 55, 0.3);
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 20px;
        }}
        .booking-info p {{
            color: var(--text-light);
            margin-bottom: 10px;
            font-size: 0.9rem;
        }}
        .booking-info p:last-child {{
            margin-bottom: 0;
        }}
        .btn-gold {{
            width: 100%;
            padding: 16px;
            border: none;
            border-radius: 8px;
            background: var(--gold-gradient);
            color: #0f172a;
            font-family: var(--font-sans);
            font-weight: 600;
            font-size: 1rem;
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
            box-shadow: 0 4px 15px rgba(212, 175, 55, 0.3);
            text-decoration: none;
            display: inline-block;
            text-align: center;
        }}
        .btn-gold:hover {{ 
            transform: translateY(-2px); 
            box-shadow: 0 6px 20px rgba(212, 175, 55, 0.5);
        }}
        .btn-disabled {{
            width: 100%;
            padding: 16px;
            border: none;
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.1);
            color: var(--text-muted);
            font-family: var(--font-sans);
            font-weight: 600;
            font-size: 1rem;
            cursor: not-allowed;
            opacity: 0.5;
        }}
        .info-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 40px;
        }}
        .info-card {{
            background: var(--glass-bg);
            backdrop-filter: blur(16px);
            border: 1px solid var(--glass-border);
            border-radius: 12px;
            padding: 25px;
        }}
        .info-card h3 {{
            color: var(--gold);
            font-family: var(--font-serif);
            margin-bottom: 15px;
            font-size: 1.2rem;
        }}
        .info-card p, .info-card li {{
            color: var(--text-light);
            line-height: 1.8;
            font-size: 0.95rem;
        }}
        .info-card ul {{
            list-style: none;
            padding-left: 0;
        }}
        .info-card li::before {{
            content: "•";
            color: var(--gold);
            font-weight: bold;
            display: inline-block;
            width: 1em;
            margin-left: -1em;
        }}
        .contact-bar {{
            background: var(--gold-gradient);
            color: #0f172a;
            padding: 20px;
            border-radius: 12px;
            text-align: center;
            margin-bottom: 40px;
            font-weight: 600;
        }}
        .contact-bar a {{
            color: #0f172a;
            text-decoration: none;
            font-size: 1.1rem;
        }}
        .video-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 20px;
            margin-bottom: 40px;
        }}
        .video-card {{
            position: relative;
            aspect-ratio: 16/9;
            background: #000;
            border-radius: 12px;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.1);
            cursor: pointer;
            transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        }}
        .video-card:hover {{
            transform: translateY(-8px) scale(1.02);
            border-color: var(--gold);
            box-shadow: 0 12px 30px rgba(212, 175, 55, 0.2);
        }}
        .video-card video {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            opacity: 0.8;
            transition: opacity 0.3s;
        }}
        .video-card:hover video {{ opacity: 1; }}
        .play-overlay {{
            position: absolute;
            top: 50%; left: 50%;
            transform: translate(-50%, -50%);
            width: 60px; height: 60px;
            background: rgba(212, 175, 55, 0.9);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            pointer-events: none;
            transition: transform 0.3s, background 0.3s;
        }}
        .video-card:hover .play-overlay {{
            transform: translate(-50%, -50%) scale(1.1);
            background: #fff;
        }}
        .play-icon {{
            width: 0; height: 0;
            border-top: 10px solid transparent;
            border-bottom: 10px solid transparent;
            border-left: 16px solid #0f172a;
            margin-left: 4px;
        }}
        .video-title {{
            position: absolute;
            bottom: 0; left: 0; right: 0;
            padding: 15px;
            background: linear-gradient(to top, rgba(0,0,0,0.9), transparent);
            font-size: 0.9rem;
            font-weight: 500;
            opacity: 0;
            transform: translateY(10px);
            transition: all 0.3s;
        }}
        .video-card:hover .video-title {{
            opacity: 1;
            transform: translateY(0);
        }}
        .social-links {{
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 30px;
        }}
        .social-links a {{
            color: var(--text-light);
            font-size: 1rem;
            text-decoration: none;
            padding: 10px 20px;
            border: 1px solid var(--gold);
            border-radius: 8px;
            transition: all 0.3s;
        }}
        .social-links a:hover {{
            background: var(--gold);
            color: #0f172a;
        }}
        @media (max-width: 768px) {{
            .header h1 {{ font-size: 1.6rem; }}
            .doctor-section {{ grid-template-columns: 1fr; }}
            .info-grid {{ grid-template-columns: 1fr; }}
            .video-grid {{ grid-template-columns: 1fr; }}
        }}
    </style>
</head>
<body>
    <div class="main-container">
        <div class="header">
            <h1>Consultorio Dr. Bruna Fabián Alberto</h1>
            <div class="subtitle">Medicina Humanista · Atención Integral</div>
        </div>

        <h2 class="section-title">Sobre el Doctor</h2>
        <div class="doctor-section">
            <div class="doctor-photo-container">
                <img src="{doctor_img_b64}" alt="Dr. Bruna Fabián Alberto en su consultorio">
            </div>
            <div class="doctor-info">
                <h2>Dr. Bruna Fabián Alberto</h2>
                <div class="title">Médico Humanista · Atención Integral</div>
                <p>
                    "Bienvenidos a mi consultorio. Como médico humanista, mi prioridad es brindar 
                    una atención integral y centrada en la persona. Ofrezco un espacio dedicado 
                    a la salud y el bienestar, combinando la práctica profesional con un trato 
                    cercano y personalizado."
                </p>
                <p>
                    Con años de experiencia en medicina interna y preventiva, me especializo 
                    en el manejo de enfermedades crónicas como diabetes, hipertensión, obesidad 
                    y trastornos metabólicos, siempre con un enfoque centrado en mejorar la 
                    calidad de vida de mis pacientes.
                </p>
                <div class="credentials">
                    <span class="credential-tag">Medicina Interna</span>
                    <span class="credential-tag">Diabetes</span>
                    <span class="credential-tag">HTA</span>
                    <span class="credential-tag">Obesidad</span>
                    <span class="credential-tag">Sarcopenia</span>
                    <span class="credential-tag">Osteoporosis</span>
                </div>
            </div>
        </div>

        <div class="contact-bar">
            📞 Consultas Online: <a href="tel:3874412712">3874412712</a> | 
             WhatsApp: <a href="https://wa.me/543876112742" target="_blank">3876112742</a>
        </div>

        <div class="booking-card">
            <h2 style="font-family: var(--font-serif); text-align: center; margin-bottom: 25px; color: #fff;">Reservar Turno</h2>
            
            <div class="booking-info">
                <p>📍 <strong>Consulta en Salta - Cardiomed</strong></p>
                <p>📅 Horarios: Lunes a Viernes 14:00 - 17:00</p>
                <p>🏥 Dirección: Ameghino 243, Salta</p>
                <p style="color: var(--gold); margin-top: 10px;">
                    <em>Próximamente: Campo Quijano y Consulta Online</em>
                </p>
            </div>
            
            <a href="https://calendar.app.google/1qaDYyotnpVG1Ens6" target="_blank" class="btn-gold">
                RESERVAR TURNO EN SALTA
            </a>
        </div>

        <h2 class="section-title">Información de Consulta</h2>
        <div class="info-grid">
            <div class="info-card">
                <h3> Direcciones</h3>
                <ul>
                    <li><strong>Salta:</strong> Ameghino 243 - Cardiomed<br>
                    <em>Lunes a Viernes: 14-17 HS</em></li>
                    <li style="margin-top: 15px;"><strong>Campo Quijano:</strong><br>
                    <em>Lunes a Viernes: 8-12 HS y 19-21 HS</em></li>
                </ul>
            </div>
            <div class="info-card">
                <h3>⏰ Horarios de Atención</h3>
                <p><strong>Lunes a Viernes:</strong></p>
                <ul>
                    <li>Mañana: 8:00 - 12:00</li>
                    <li>Tarde: 14:00 - 17:00</li>
                    <li>Noche: 19:00 - 21:00</li>
                </ul>
            </div>
            <div class="info-card">
                <h3>✅ Obras Sociales</h3>
                <p>✓ Se reciben principales obras sociales y prepagas</p>
                <p>✓ Consultas online programadas</p>
                <p>✓ Atención personalizada y humanista</p>
            </div>
        </div>

        <h2 class="section-title">Especialidades y Temas Médicos</h2>
        <div class="info-card" style="margin-bottom: 40px;">
            <ul style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 10px;">
                <li>Diabetes</li>
                <li>Obesidad</li>
                <li>Dislipemia</li>
                <li>Hipertensión Arterial</li>
                <li>Sarcopenia</li>
                <li>Osteoporosis</li>
                <li>Medicina Preventiva</li>
                <li>Chequeos Generales</li>
            </ul>
        </div>

        <h2 class="section-title">Videos Educativos</h2>
        <div class="video-grid">
            <div class="video-card" onclick="toggleVideo(this)">
                <video loop muted playsinline>
                    <source src="videos/agua.mp4" type="video/mp4">
                </video>
                <div class="play-overlay"><div class="play-icon"></div></div>
                <div class="video-title">Importancia del Agua</div>
            </div>
            <div class="video-card" onclick="toggleVideo(this)">
                <video loop muted playsinline>
                    <source src="videos/ejercicios.mp4" type="video/mp4">
                </video>
                <div class="play-overlay"><div class="play-icon"></div></div>
                <div class="video-title">Ejercicios para la Salud</div>
            </div>
            <div class="video-card" onclick="toggleVideo(this)">
                <video loop muted playsinline>
                    <source src="videos/viajar.mp4" type="video/mp4">
                </video>
                <div class="play-overlay"><div class="play-icon"></div></div>
                <div class="video-title">Consejos para Viajar</div>
            </div>
        </div>

        <h2 class="section-title">Seguime en Redes</h2>
        <div class="info-card" style="text-align: center;">
            <p style="margin-bottom: 20px;">Seguime en mis redes sociales para más consejos de salud</p>
            <div class="social-links">
                <a href="https://facebook.com/fabian.bruna.perez" target="_blank">📘 Facebook</a>
                <a href="https://instagram.com/fabian.bruna.perez" target="_blank">📷 Instagram</a>
            </div>
        </div>

        <footer style="text-align: center; margin-top: 50px; padding: 20px; color: var(--text-muted); font-size: 0.9rem;">
            <p>© 2024 Consultorio Dr. Bruna Fabián Alberto</p>
            <p>Medicina Humanista y Centrada en la Persona</p>
        </footer>
    </div>

    <script>
        function toggleVideo(card) {{
            const video = card.querySelector('video');
            if (video.paused) {{
                document.querySelectorAll('video').forEach(v => {{
                    if (v !== video) {{
                        v.pause();
                        v.currentTime = 0;
                    }}
                }});
                video.play();
            }} else {{
                video.pause();
            }}
        }}
    </script>
</body>
</html>
"""

html(html_code, height=3200, scrolling=False)
