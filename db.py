import sqlite3
from datetime import datetime

DB_FILE = "roadmap.db"

def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    c = conn.cursor()
    
    # Roadmaps Table
    c.execute('''CREATE TABLE IF NOT EXISTS roadmaps (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    raw_text TEXT,
                    created_at TEXT
                )''')
    
    # Timeframes Table
    c.execute('''CREATE TABLE IF NOT EXISTS timeframes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    roadmap_id INTEGER,
                    label TEXT NOT NULL,
                    granularity TEXT NOT NULL,
                    parent_id INTEGER,
                    FOREIGN KEY(roadmap_id) REFERENCES roadmaps(id),
                    FOREIGN KEY(parent_id) REFERENCES timeframes(id)
                )''')
    
    # Tasks Table
    c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timeframe_id INTEGER,
                    title TEXT NOT NULL,
                    details TEXT,
                    is_done BOOLEAN DEFAULT 0,
                    created_at TEXT,
                    FOREIGN KEY(timeframe_id) REFERENCES timeframes(id)
                )''')
    
    conn.commit()
    conn.close()

def save_roadmap(name, raw_text):
    conn = get_connection()
    c = conn.cursor()
    c.execute("INSERT INTO roadmaps (name, raw_text, created_at) VALUES (?, ?, ?)", 
              (name, raw_text, datetime.now().isoformat()))
    roadmap_id = c.lastrowid
    conn.commit()
    conn.close()
    return roadmap_id

def save_timeframe(roadmap_id, label, granularity, parent_id=None):
    conn = get_connection()
    c = conn.cursor()
    # Check if exists to avoid duplicates if re-parsing (simple check)
    # For now, we assume fresh import or we just insert. 
    # Let's just insert for simplicity as per requirements.
    c.execute("INSERT INTO timeframes (roadmap_id, label, granularity, parent_id) VALUES (?, ?, ?, ?)",
              (roadmap_id, label, granularity, parent_id))
    tf_id = c.lastrowid
    conn.commit()
    conn.close()
    return tf_id

def save_task(timeframe_id, title, details=""):
    conn = get_connection()
    c = conn.cursor()
    c.execute("INSERT INTO tasks (timeframe_id, title, details, created_at) VALUES (?, ?, ?, ?)",
              (timeframe_id, title, details, datetime.now().isoformat()))
    conn.commit()
    conn.close()

def get_roadmaps():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM roadmaps ORDER BY created_at DESC")
    res = [dict(row) for row in c.fetchall()]
    conn.close()
    return res

def get_timeframes(roadmap_id, granularity=None):
    conn = get_connection()
    c = conn.cursor()
    query = "SELECT * FROM timeframes WHERE roadmap_id = ?"
    params = [roadmap_id]
    
    if granularity and granularity != "All":
        query += " AND granularity = ?"
        params.append(granularity.lower())
        
    c.execute(query, params)
    res = [dict(row) for row in c.fetchall()]
    conn.close()
    return res

def get_tasks(roadmap_id, timeframe_id=None):
    conn = get_connection()
    c = conn.cursor()
    
    # Join to filter by roadmap via timeframe
    query = '''SELECT t.*, tf.label as timeframe_label, tf.granularity 
               FROM tasks t
               JOIN timeframes tf ON t.timeframe_id = tf.id
               WHERE tf.roadmap_id = ?'''
    params = [roadmap_id]
    
    if timeframe_id:
        query += " AND t.timeframe_id = ?"
        params.append(timeframe_id)
        
    c.execute(query, params)
    res = [dict(row) for row in c.fetchall()]
    conn.close()
    return res

def update_task_status(task_id, is_done):
    conn = get_connection()
    c = conn.cursor()
    c.execute("UPDATE tasks SET is_done = ? WHERE id = ?", (is_done, task_id))
    conn.commit()
    conn.close()

def delete_roadmap(roadmap_id):
    conn = get_connection()
    c = conn.cursor()
    
    # Delete tasks associated with timeframes of this roadmap
    c.execute('''DELETE FROM tasks 
                 WHERE timeframe_id IN (SELECT id FROM timeframes WHERE roadmap_id = ?)''', (roadmap_id,))
    
    # Delete timeframes
    c.execute("DELETE FROM timeframes WHERE roadmap_id = ?", (roadmap_id,))
    
    # Delete roadmap
    c.execute("DELETE FROM roadmaps WHERE id = ?", (roadmap_id,))
    
    conn.commit()
    conn.close()

def rename_roadmap(roadmap_id, new_name):
    conn = get_connection()
    c = conn.cursor()
    c.execute("UPDATE roadmaps SET name = ? WHERE id = ?", (new_name, roadmap_id))
    conn.commit()
    conn.close()
