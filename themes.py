
def get_cyberpunk_theme():
    return """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

        :root {
            --bg: #04060d;
            --surface: #0b0f1a;
            --card: #111726;
            --border: #1f2840;
            --primary: #7cffc1;
            --accent: #56c2ff;
            --muted: #9fb1c7;
            --glow: 0 0 25px rgba(124, 255, 193, 0.35);
        }

        .stApp {
            background: radial-gradient(circle at 20% 20%, rgba(124, 255, 193, 0.08), transparent 30%),
                        radial-gradient(circle at 80% 10%, rgba(86, 194, 255, 0.08), transparent 25%),
                        var(--bg);
            color: var(--muted);
        }
        
        html, body, [class*="css"], [class*="st-"], .stApp {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif !important;
        }

        .block-container {
            padding: 2.5rem 2.5rem 3rem 2.5rem;
            max-width: 1100px;
        }

        h1, h2, h3 {
            color: var(--primary) !important;
            letter-spacing: 0.03em;
            text-shadow: var(--glow);
            font-weight: 600;
        }

        p, label, span, li {
            color: var(--muted);
        }

        .stButton>button {
            background: linear-gradient(120deg, var(--primary), var(--accent));
            color: #04060d;
            border: none;
            border-radius: 12px;
            padding: 0.6rem 1.2rem;
            font-weight: 600;
            letter-spacing: 0.02em;
            box-shadow: 0 10px 30px rgba(86, 194, 255, 0.35);
            transition: transform 0.15s ease, box-shadow 0.2s ease;
        }

        .stButton>button:hover {
            transform: translateY(-1px);
            box-shadow: 0 15px 40px rgba(124, 255, 193, 0.35);
        }

        .stTextInput>div>div>input,
        .stTextArea>div>div>textarea,
        .stSelectbox>div>div>div,
        .stMultiSelect>div>div>div {
            background: var(--card);
            border: 1px solid var(--border);
            color: var(--primary);
            border-radius: 12px;
            box-shadow: inset 0 0 0 1px rgba(124, 255, 193, 0.08);
        }

        .stTextInput>div>div>input:focus,
        .stTextArea>div>div>textarea:focus,
        .stSelectbox>div>div>div:focus {
            border: 1px solid var(--primary);
            box-shadow: var(--glow);
        }

        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, rgba(86, 194, 255, 0.12), rgba(86, 194, 255, 0.02));
            border-right: 1px solid var(--border);
        }

        div[data-testid="stDivider"] hr {
            border: none;
            border-top: 1px solid var(--border);
        }

        ::-webkit-scrollbar {
            width: 10px;
            background: var(--bg);
        }
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(var(--accent), var(--primary));
            border-radius: 10px;
        }

        h3 {
            margin-top: 1rem;
            margin-bottom: 0.35rem;
        }
    </style>
    """

def get_sunset_neon_theme():
    return """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

        :root {
            --bg: #0c0b1a;
            --glow1: #ff6a88;
            --glow2: #fce38a;
            --primary: #ff6a88;
            --accent: #fce38a;
            --card: #131228;
            --border: #2a2746;
            --text: #f7f8fb;
            --muted: #cfd2de;
        }

        .stApp {
            background: radial-gradient(circle at 15% 20%, rgba(255, 106, 136, 0.16), transparent 30%),
                        radial-gradient(circle at 85% 5%, rgba(252, 227, 138, 0.16), transparent 30%),
                        var(--bg);
            color: var(--text);
        }

        html, body, [class*="css"], [class*="st-"], .stApp {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif !important;
        }

        .block-container {
            padding: 2.4rem 2.4rem 3rem 2.4rem;
            max-width: 1080px;
        }

        h1, h2, h3 {
            color: var(--text) !important;
            letter-spacing: 0.01em;
            text-shadow: 0 4px 25px rgba(255, 106, 136, 0.35);
        }

        p, label, span, li {
            color: var(--muted);
        }

        .stButton>button {
            background: linear-gradient(120deg, var(--glow1), var(--glow2));
            color: #0c0b1a;
            border: none;
            border-radius: 14px;
            padding: 0.65rem 1.25rem;
            font-weight: 700;
            box-shadow: 0 12px 30px rgba(255, 106, 136, 0.35);
            transition: transform 0.12s ease, box-shadow 0.2s ease;
        }

        .stButton>button:hover {
            transform: translateY(-1px);
            box-shadow: 0 16px 38px rgba(252, 227, 138, 0.35);
        }

        .stTextInput>div>div>input,
        .stTextArea>div>div>textarea,
        .stSelectbox>div>div>div,
        .stMultiSelect>div>div>div {
            background: var(--card);
            border: 1px solid var(--border);
            color: var(--text);
            border-radius: 12px;
        }

        .stTextInput>div>div>input:focus,
        .stTextArea>div>div>textarea:focus,
        .stSelectbox>div>div>div:focus {
            border: 1px solid var(--glow1);
            box-shadow: 0 0 0 3px rgba(255, 106, 136, 0.2);
        }

        section[data-testid="stSidebar"] {
            background: rgba(19, 18, 40, 0.8);
            border-right: 1px solid var(--border);
        }
    </style>
    """

def get_aqua_glow_theme():
    return """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

        :root {
            --bg: #031b29;
            --card: #0a2536;
            --border: #123549;
            --primary: #4de1c1;
            --accent: #4dabff;
            --text: #e3f5ff;
            --muted: #a6c3d3;
        }

        .stApp {
            background: radial-gradient(circle at 30% 20%, rgba(77, 225, 193, 0.18), transparent 32%),
                        radial-gradient(circle at 80% 0%, rgba(77, 171, 255, 0.16), transparent 30%),
                        var(--bg);
            color: var(--text);
        }

        html, body, [class*="css"], [class*="st-"], .stApp {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif !important;
        }

        .block-container {
            padding: 2.4rem 2.4rem 3rem 2.4rem;
            max-width: 1100px;
        }

        h1, h2, h3 {
            color: var(--text) !important;
            letter-spacing: -0.01em;
        }

        p, label, span, li {
            color: var(--muted);
        }

        .stButton>button {
            background: linear-gradient(135deg, var(--primary), var(--accent));
            color: #031b29;
            border: none;
            border-radius: 14px;
            padding: 0.65rem 1.25rem;
            font-weight: 700;
            box-shadow: 0 14px 34px rgba(77, 225, 193, 0.3);
            transition: transform 0.12s ease, box-shadow 0.2s ease;
        }

        .stButton>button:hover {
            transform: translateY(-1px);
            box-shadow: 0 18px 40px rgba(77, 171, 255, 0.28);
        }

        .stTextInput>div>div>input,
        .stTextArea>div>div>textarea,
        .stSelectbox>div>div>div,
        .stMultiSelect>div>div>div {
            background: var(--card);
            border: 1px solid var(--border);
            color: var(--text);
            border-radius: 12px;
            box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.02);
        }

        .stTextInput>div>div>input:focus,
        .stTextArea>div>div>textarea:focus,
        .stSelectbox>div>div>div:focus {
            border: 1px solid var(--primary);
            box-shadow: 0 0 0 3px rgba(77, 225, 193, 0.18);
        }

        section[data-testid="stSidebar"] {
            background: rgba(3, 27, 41, 0.9);
            border-right: 1px solid var(--border);
        }
    </style>
    """

def get_ember_glow_theme():
    return """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

        :root {
            --bg: #140b0f;
            --card: #1d1117;
            --border: #2a1a24;
            --primary: #ff9a3c;
            --accent: #ff4d79;
            --text: #fbeff4;
            --muted: #d8c7d0;
        }

        .stApp {
            background: radial-gradient(circle at 20% 10%, rgba(255, 154, 60, 0.2), transparent 30%),
                        radial-gradient(circle at 85% 0%, rgba(255, 77, 121, 0.18), transparent 30%),
                        var(--bg);
            color: var(--text);
        }

        html, body, [class*="css"], [class*="st-"], .stApp {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif !important;
        }

        .block-container {
            padding: 2.4rem 2.4rem 3rem 2.4rem;
            max-width: 1080px;
        }

        h1, h2, h3 {
            color: var(--text) !important;
            letter-spacing: -0.01em;
        }

        p, label, span, li {
            color: var(--muted);
        }

        .stButton>button {
            background: linear-gradient(135deg, var(--primary), var(--accent));
            color: #140b0f;
            border: none;
            border-radius: 14px;
            padding: 0.65rem 1.25rem;
            font-weight: 700;
            box-shadow: 0 14px 34px rgba(255, 154, 60, 0.25);
            transition: transform 0.12s ease, box-shadow 0.2s ease;
        }

        .stButton>button:hover {
            transform: translateY(-1px);
            box-shadow: 0 18px 40px rgba(255, 77, 121, 0.25);
        }

        .stTextInput>div>div>input,
        .stTextArea>div>div>textarea,
        .stSelectbox>div>div>div,
        .stMultiSelect>div>div>div {
            background: var(--card);
            border: 1px solid var(--border);
            color: var(--text);
            border-radius: 12px;
            box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.02);
        }

        .stTextInput>div>div>input:focus,
        .stTextArea>div>div>textarea:focus,
        .stSelectbox>div>div>div:focus {
            border: 1px solid var(--primary);
            box-shadow: 0 0 0 3px rgba(255, 154, 60, 0.18);
        }

        section[data-testid="stSidebar"] {
            background: rgba(20, 11, 15, 0.9);
            border-right: 1px solid var(--border);
        }
    </style>
    """

def get_titanium_theme():
    return """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

        :root {
            --bg: #0f1218;
            --card: #151a22;
            --border: #1f2633;
            --primary: #cfd6df;
            --accent: #9da7b2;
            --text: #e8ecf2;
            --muted: #b4bdc9;
        }

        .stApp {
            background: radial-gradient(circle at 10% 10%, rgba(207, 214, 223, 0.12), transparent 30%),
                        radial-gradient(circle at 90% 0%, rgba(157, 167, 178, 0.12), transparent 30%),
                        var(--bg);
            color: var(--text);
        }

        html, body, [class*="css"], [class*="st-"], .stApp {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif !important;
        }

        .block-container {
            padding: 2.4rem 2.4rem 3rem 2.4rem;
            max-width: 1100px;
        }

        h1, h2, h3 {
            color: var(--text) !important;
            letter-spacing: -0.01em;
        }

        p, label, span, li {
            color: var(--muted);
        }

        .stButton>button {
            background: linear-gradient(135deg, #e6edf5, #b5bfcc);
            color: #0f1218;
            border: none;
            border-radius: 14px;
            padding: 0.65rem 1.25rem;
            font-weight: 700;
            box-shadow: 0 14px 34px rgba(157, 167, 178, 0.25);
            transition: transform 0.12s ease, box-shadow 0.2s ease;
        }

        .stButton>button:hover {
            transform: translateY(-1px);
            box-shadow: 0 18px 40px rgba(207, 214, 223, 0.25);
        }

        .stTextInput>div>div>input,
        .stTextArea>div>div>textarea,
        .stSelectbox>div>div>div,
        .stMultiSelect>div>div>div {
            background: var(--card);
            border: 1px solid var(--border);
            color: var(--text);
            border-radius: 12px;
            box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.02);
        }

        .stTextInput>div>div>input:focus,
        .stTextArea>div>div>textarea:focus,
        .stSelectbox>div>div>div:focus {
            border: 1px solid var(--primary);
            box-shadow: 0 0 0 3px rgba(207, 214, 223, 0.18);
        }

        section[data-testid="stSidebar"] {
            background: rgba(15, 18, 24, 0.9);
            border-right: 1px solid var(--border);
        }
    </style>
    """

def get_antigravity_theme():
    return """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');

        :root {
            --bg: #050505;
            --card: rgba(20, 20, 35, 0.4);
            --border: rgba(100, 100, 255, 0.1);
            --primary: #a259ff;
            --accent: #1abcf9;
            --text: #ffffff;
            --muted: #8b9bb4;
            --glass: blur(20px) saturate(180%);
        }

        .stApp {
            background: 
                radial-gradient(circle at 50% 0%, rgba(162, 89, 255, 0.15), transparent 50%),
                radial-gradient(circle at 0% 100%, rgba(26, 188, 249, 0.15), transparent 50%),
                var(--bg);
            color: var(--text);
        }

        html, body, [class*="css"], [class*="st-"], .stApp {
            font-family: 'Outfit', sans-serif !important;
        }

        .block-container {
            padding: 2.4rem 2.4rem 3rem 2.4rem;
            max-width: 1100px;
        }

        h1, h2, h3 {
            background: linear-gradient(135deg, #fff 0%, #a259ff 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
            letter-spacing: -0.02em;
        }

        p, label, span, li {
            color: var(--muted);
        }

        /* Glass Cards */
        .stTextInput>div>div>input,
        .stTextArea>div>div>textarea,
        .stSelectbox>div>div>div,
        .stMultiSelect>div>div>div {
            background: var(--card);
            backdrop-filter: var(--glass);
            -webkit-backdrop-filter: var(--glass);
            border: 1px solid var(--border);
            color: var(--text);
            border-radius: 16px;
            transition: all 0.3s ease;
        }

        .stTextInput>div>div>input:focus,
        .stTextArea>div>div>textarea:focus,
        .stSelectbox>div>div>div:focus {
            border-color: var(--primary);
            box-shadow: 0 0 30px rgba(162, 89, 255, 0.2);
            transform: translateY(-2px);
        }

        /* Levitating Buttons */
        .stButton>button {
            background: linear-gradient(135deg, rgba(162, 89, 255, 0.8), rgba(26, 188, 249, 0.8));
            backdrop-filter: blur(10px);
            color: white;
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 16px;
            padding: 0.7rem 1.5rem;
            font-weight: 600;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }

        .stButton>button:hover {
            transform: translateY(-4px) scale(1.02);
            box-shadow: 0 20px 40px rgba(162, 89, 255, 0.4);
        }

        section[data-testid="stSidebar"] {
            background: rgba(5, 5, 5, 0.8);
            backdrop-filter: blur(20px);
            border-right: 1px solid var(--border);
        }
        
        div[data-testid="stDivider"] hr {
            border-color: var(--border);
        }
    </style>
    """
