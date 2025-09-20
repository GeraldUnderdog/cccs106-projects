import flet as ft
from app_logic import create_contact_app


def main(page: ft.Page):
    """Main entry point for the Contact Book application."""
    create_contact_app(page)


if __name__ == "__main__":
    ft.app(main)
