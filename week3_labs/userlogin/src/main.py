import flet as ft
import mysql.connector
from db_connection import connect_db

def main(page: ft.Page):
    # Configure the page
    page.window_center = True
    page.window_frameless = True
    page.title = "User Login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_height = 350
    page.window_width = 400
    page.bgcolor = ft.Colors.WHITE
    
    # Create UI controls
    login_title = ft.Text(
        "User Login",
        text_align=ft.TextAlign.CENTER,
        size=20,
        weight=ft.FontWeight.BOLD,
        font_family="Arial",
        color="#000000"  # Black text
    )
    
    username_field = ft.TextField(
        label="User name",
        hint_text="Enter your user name", 
        hint_style=ft.TextStyle(color="#000000"),  # Black hint text
        helper_text="This is your unique identifier",
        helper_style=ft.TextStyle(color="#000000"),  # Black helper text
        width=300,
        autofocus=True,
        disabled=False,
        prefix_icon=ft.Icon(ft.Icons.PERSON, color="#000000"),
        bgcolor=ft.Colors.LIGHT_BLUE_ACCENT,
        label_style=ft.TextStyle(color="#000000"),  # Black label text
        text_style=ft.TextStyle(color="#000000")    # Black input text
    )
    
    password_field = ft.TextField(
        label="Password",
        hint_text="Enter your password",
        hint_style=ft.TextStyle(color="#000000"),  # Black hint text
        helper_text="This is your secret key",
        helper_style=ft.TextStyle(color="#000000"),  # Black helper text
        width=300,
        disabled=False,
        password=True,
        can_reveal_password=True,
        prefix_icon=ft.Icon(ft.Icons.LOCK, color="#000000"),
        bgcolor=ft.Colors.LIGHT_BLUE_ACCENT,
        label_style=ft.TextStyle(color="#000000"),  # Black label text
        text_style=ft.TextStyle(color="#000000")    # Black input text
    )
    
    async def login_click(e):
        # Define dialogs
        success_dialog = ft.AlertDialog(
            title=ft.Text("Login Successful", color="WHITE"),  # Black text
            content=ft.Text(
                f"Welcome, {username_field.value}!",
                text_align=ft.TextAlign.CENTER
            ),
            actions=[
                ft.TextButton("OK", on_click=lambda _: page.close(success_dialog))
            ],
            actions_alignment=ft.MainAxisAlignment.CENTER,
            icon=ft.Icon(ft.Icons.CHECK_CIRCLE, color=ft.Colors.GREEN)
        )
        
        failure_dialog = ft.AlertDialog(
            title=ft.Text("Login Failed", color="WHITE"),
            content=ft.Text(
                "Invalid username or password",
                text_align=ft.TextAlign.CENTER
            ),
            actions=[
                ft.TextButton("OK", on_click=lambda _: page.close(failure_dialog))
            ],
            actions_alignment=ft.MainAxisAlignment.CENTER,
            icon=ft.Icon(ft.Icons.ERROR, color=ft.Colors.RED)
        )
        
        invalid_input_dialog = ft.AlertDialog(
            title=ft.Text("Input Error", color="WHITE"),
            content=ft.Text(
                "Please enter username and password",
                text_align=ft.TextAlign.CENTER
            ),
            actions=[
                ft.TextButton("OK", on_click=lambda _: page.close(invalid_input_dialog))
            ],
            actions_alignment=ft.MainAxisAlignment.CENTER,
            icon=ft.Icon(ft.Icons.INFO, color=ft.Colors.BLUE)
        )
        
        database_error_dialog = ft.AlertDialog(
            title=ft.Text("Database Error", color="WHITE"),
            content=ft.Text(
                "An error occurred while connecting to the database",
                text_align=ft.TextAlign.CENTER
            ),
            actions=[
                ft.TextButton("OK", on_click=lambda _: page.close(database_error_dialog))
            ],
            actions_alignment=ft.MainAxisAlignment.CENTER
        )
        
        # Validation and database logic
        if not username_field.value or not password_field.value:
            page.open(invalid_input_dialog)
            return
        
        try:
            # Establish database connection
            connection = connect_db()
            cursor = connection.cursor()
            
            # Execute parameterized query to prevent SQL injection
            query = "SELECT * FROM users WHERE username = %s AND password = %s"
            cursor.execute(query, (username_field.value, password_field.value))
            
            # Fetch result
            result = cursor.fetchone()
            
            # Close database connection
            cursor.close()
            connection.close()
            
            # Check if user was found
            if result:
                page.open(success_dialog)
            else:
                page.open(failure_dialog)
            
            page.update()
            
        except mysql.connector.Error as e:
            print(f"Database error: {e}")
            page.open(database_error_dialog)
            page.update()
    
    # Create login button
    login_button = ft.ElevatedButton(
        text="Login",
        on_click=login_click,
        width=100,
        icon=ft.Icon(ft.Icons.LOGIN, color="#000000"),
        style=ft.ButtonStyle(
            color=ft.Colors.BLACK,  # Black text
            bgcolor=ft.Colors.WHITE  # White background for the button
        )
    )
    
    # Create the form container with border and title
    form_container = ft.Container(
        content=ft.Column(
            [
                # Title inside the container
                ft.Container(
                    content=login_title,
                    padding=ft.padding.only(bottom=20),
                    alignment=ft.alignment.center
                ),
                # Form fields
                username_field,
                password_field,
                # Login button with top margin
                ft.Container(
                    content=login_button,
                    alignment=ft.alignment.center,
                    margin=ft.margin.only(top=10)
                )
            ],
            spacing=15,  # Spacing between elements
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        padding=ft.padding.all(20),
        border=ft.border.all(2, "#000000"),  # Black border
        border_radius=10,  # Rounded corners
        bgcolor=ft.Colors.YELLOW,  # White background for the form
        width=400,  # Fixed width
        margin=ft.margin.symmetric(horizontal=40, vertical=20)  # Margins
    )
    
    # Add the form container to the page
    page.add(
        ft.Container(height=20),  # Add some space at the top
        form_container
    )

# Start the Flet app
ft.app(target=main)