import flet as ft
from database import init_database, add_contact_db, get_all_contacts_db, delete_contact_db


class ContactBookApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Contact Book"
        self.page.window.width = 800
        self.page.window.height = 600
        self.page.theme_mode = ft.ThemeMode.LIGHT
        
        # Initialize database
        init_database()
        
        # UI Components
        self.search_field = ft.TextField(
            label="Search contacts...",
            prefix_icon=ft.Icons.SEARCH,
            on_change=self.on_search_change,
            expand=True
        )
        
        self.name_input = ft.TextField(
            label="Name",
            prefix_icon=ft.Icons.PERSON,
            expand=True
        )
        
        self.phone_input = ft.TextField(
            label="Phone",
            prefix_icon=ft.Icons.PHONE,
            expand=True
        )
        
        self.email_input = ft.TextField(
            label="Email",
            prefix_icon=ft.Icons.EMAIL,
            expand=True
        )
        
        self.contacts_list = ft.Column(
            spacing=10,
            scroll=ft.ScrollMode.AUTO,
            expand=True
        )
        
        # Theme toggle switch
        self.theme_switch = ft.Switch(
            label="Dark Mode",
            value=False,
            on_change=self.toggle_theme
        )
        
        # Confirmation dialog
        self.delete_dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Confirm Delete"),
            content=ft.Text("Are you sure you want to delete this contact?"),
            actions=[
                ft.TextButton("Cancel", on_click=self.close_delete_dialog),
                ft.TextButton("Delete", on_click=self.confirm_delete, style=ft.ButtonStyle(color=ft.Colors.RED))
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        
        self.contact_to_delete = None
        
        self.build_ui()
        self.load_contacts()
    
    def build_ui(self):
        """Build the main UI layout."""
        # Header with theme toggle
        header = ft.Row([
            ft.Text("Contact Book", size=24, weight=ft.FontWeight.BOLD),
            ft.Container(expand=True),  # Spacer
            self.theme_switch
        ])
        
        # Search section
        search_section = ft.Container(
            content=self.search_field,
            padding=ft.padding.symmetric(vertical=10)
        )
        
        # Add contact form
        add_contact_form = ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Text("Add New Contact", size=18, weight=ft.FontWeight.BOLD),
                    ft.Row([
                        self.name_input,
                        self.phone_input,
                        self.email_input
                    ]),
                    ft.Row([
                        ft.ElevatedButton(
                            "Add Contact",
                            icon=ft.Icons.ADD,
                            on_click=self.add_contact,
                            style=ft.ButtonStyle(
                                bgcolor=ft.Colors.BLUE,
                                color=ft.Colors.WHITE
                            )
                        ),
                        ft.OutlinedButton(
                            "Clear",
                            icon=ft.Icons.CLEAR,
                            on_click=self.clear_form
                        )
                    ])
                ]),
                padding=20
            ),
            elevation=2
        )
        
        # Contacts list section
        contacts_section = ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Text("Contacts", size=18, weight=ft.FontWeight.BOLD),
                    ft.Container(
                        content=self.contacts_list,
                        height=300
                    )
                ]),
                padding=20
            ),
            elevation=2
        )
        
        # Main layout
        self.page.add(
            ft.Container(
                content=ft.Column([
                    header,
                    search_section,
                    add_contact_form,
                    contacts_section
                ]),
                padding=20
            )
        )
        
        # Add dialog to page overlay
        self.page.overlay.append(self.delete_dialog)
    
    def add_contact(self, e):
        """Add a new contact with input validation."""
        name = self.name_input.value.strip() if self.name_input.value else ""
        phone = self.phone_input.value.strip() if self.phone_input.value else ""
        email = self.email_input.value.strip() if self.email_input.value else ""
        
        # Input validation - check if name is empty
        if not name:
            self.name_input.error_text = "Name cannot be empty"
            self.page.update()
            return
        
        # Clear any previous error
        self.name_input.error_text = None
        
        try:
            add_contact_db(name, phone, email)
            self.clear_form(None)
            self.load_contacts()
            
            # Show success message
            snack_bar = ft.SnackBar(
                content=ft.Text(f"Contact '{name}' added successfully!"),
                bgcolor=ft.Colors.GREEN
            )
            self.page.snack_bar = snack_bar
            snack_bar.open = True
            self.page.update()
        except Exception as ex:
            snack_bar = ft.SnackBar(
                content=ft.Text(f"Error adding contact: {str(ex)}"),
                bgcolor=ft.Colors.RED
            )
            self.page.snack_bar = snack_bar
            snack_bar.open = True
            self.page.update()
    
    def clear_form(self, e):
        """Clear all input fields."""
        self.name_input.value = ""
        self.phone_input.value = ""
        self.email_input.value = ""
        self.name_input.error_text = None
        self.page.update()
    
    def load_contacts(self, search_term=None):
        """Load and display contacts from database."""
        self.contacts_list.controls.clear()
        
        try:
            contacts = get_all_contacts_db(search_term)
            
            if not contacts:
                self.contacts_list.controls.append(
                    ft.Container(
                        content=ft.Text(
                            "No contacts found" if search_term else "No contacts yet. Add your first contact above!",
                            size=16,
                            color=ft.Colors.GREY_600,
                            text_align=ft.TextAlign.CENTER
                        ),
                        alignment=ft.alignment.center,
                        padding=20
                    )
                )
            else:
                for contact in contacts:
                    contact_id, name, phone, email = contact
                    self.contacts_list.controls.append(
                        self.create_contact_card(contact_id, name, phone, email)
                    )
            
            self.page.update()
        except Exception as ex:
            snack_bar = ft.SnackBar(
                content=ft.Text(f"Error loading contacts: {str(ex)}"),
                bgcolor=ft.Colors.RED
            )
            self.page.snack_bar = snack_bar
            snack_bar.open = True
    
    def create_contact_card(self, contact_id, name, phone, email):
        """Create a modern card for displaying contact information."""
        return ft.Card(
            content=ft.Container(
                content=ft.Row([
                    # Contact info section
                    ft.Column([
                        ft.Text(name, size=16, weight=ft.FontWeight.BOLD),
                        ft.Row([
                            ft.Icon(ft.Icons.PHONE, size=16, color=ft.Colors.BLUE),
                            ft.Text(phone or "No phone", size=14)
                        ]) if phone else ft.Text("No phone", size=14, color=ft.Colors.GREY_600),
                        ft.Row([
                            ft.Icon(ft.Icons.EMAIL, size=16, color=ft.Colors.GREEN),
                            ft.Text(email or "No email", size=14)
                        ]) if email else ft.Text("No email", size=14, color=ft.Colors.GREY_600)
                    ], expand=True),
                    
                    # Actions section
                    ft.Column([
                        ft.IconButton(
                            icon=ft.Icons.DELETE,
                            icon_color=ft.Colors.RED,
                            tooltip="Delete contact",
                            on_click=lambda e, cid=contact_id, cname=name: self.show_delete_dialog(cid, cname)
                        )
                    ])
                ]),
                padding=15
            ),
            elevation=1
        )
    
    def show_delete_dialog(self, contact_id, contact_name):
        """Show confirmation dialog before deleting a contact."""
        self.contact_to_delete = contact_id
        self.delete_dialog.content = ft.Text(f"Are you sure you want to delete '{contact_name}'?")
        self.delete_dialog.open = True
        self.page.update()
    
    def close_delete_dialog(self, e):
        """Close the delete confirmation dialog."""
        self.delete_dialog.open = False
        self.contact_to_delete = None
        self.page.update()
    
    def confirm_delete(self, e):
        """Confirm and execute contact deletion."""
        if self.contact_to_delete:
            try:
                delete_contact_db(self.contact_to_delete)
                self.load_contacts(self.search_field.value if self.search_field.value else None)
                
                snack_bar = ft.SnackBar(
                    content=ft.Text("Contact deleted successfully!"),
                    bgcolor=ft.Colors.GREEN
                )
                self.page.snack_bar = snack_bar
                snack_bar.open = True
            except Exception as ex:
                snack_bar = ft.SnackBar(
                    content=ft.Text(f"Error deleting contact: {str(ex)}"),
                    bgcolor=ft.Colors.RED
                )
                self.page.snack_bar = snack_bar
                snack_bar.open = True
        
        self.close_delete_dialog(e)
    
    def on_search_change(self, e):
        """Handle search field changes for real-time filtering."""
        search_term = e.control.value.strip() if e.control.value else None
        self.load_contacts(search_term)
    
    def toggle_theme(self, e):
        """Toggle between light and dark theme."""
        if e.control.value:
            self.page.theme_mode = ft.ThemeMode.DARK
        else:
            self.page.theme_mode = ft.ThemeMode.LIGHT
        
        self.page.update()


def create_contact_app(page: ft.Page):
    """Create and initialize the contact book application."""
    app = ContactBookApp(page)
    return app