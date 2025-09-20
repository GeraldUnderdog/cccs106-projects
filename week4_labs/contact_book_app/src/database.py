import sqlite3
import os


def get_db_path():
    """Get the path to the database file in the storage directory."""
    storage_dir = os.path.join(os.path.dirname(__file__), "storage")
    os.makedirs(storage_dir, exist_ok=True)
    return os.path.join(storage_dir, "contacts.db")


def init_database():
    """Initialize the database and create the contacts table if it doesn't exist."""
    db_path = get_db_path()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT,
            email TEXT
        )
    ''')
    
    conn.commit()
    conn.close()


def add_contact_db(name, phone, email):
    """Add a new contact to the database."""
    db_path = get_db_path()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)",
        (name, phone, email)
    )
    
    conn.commit()
    conn.close()


def get_all_contacts_db(search_term=None):
    """Get all contacts from the database, optionally filtered by search term."""
    db_path = get_db_path()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    if search_term:
        cursor.execute(
            "SELECT id, name, phone, email FROM contacts WHERE name LIKE ? ORDER BY name",
            (f"%{search_term}%",)
        )
    else:
        cursor.execute("SELECT id, name, phone, email FROM contacts ORDER BY name")
    
    contacts = cursor.fetchall()
    conn.close()
    
    return contacts


def delete_contact_db(contact_id):
    """Delete a contact from the database by ID."""
    db_path = get_db_path()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
    
    conn.commit()
    conn.close()


def update_contact_db(contact_id, name, phone, email):
    """Update an existing contact in the database."""
    db_path = get_db_path()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute(
        "UPDATE contacts SET name = ?, phone = ?, email = ? WHERE id = ?",
        (name, phone, email, contact_id)
    )
    
    conn.commit()
    conn.close()