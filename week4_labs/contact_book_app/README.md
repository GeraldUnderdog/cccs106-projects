# Contact Book App

A modern contact management application built with Flet, featuring all the advanced learning tasks implemented.

## Features

### Core Functionality
- Add, view, and delete contacts
- Store contact information (name, phone, email)
- SQLite database for persistent storage
- Modern, responsive UI with cards and icons

### Advanced Learning Tasks Implemented

#### 1. Input Validation 
- **Feature**: Prevents users from adding contacts with empty names
- **Implementation**: When "Add Contact" is clicked, validates that the name field is not empty
- **User Experience**: Shows error message "Name cannot be empty" directly on the name input field
- **Why**: Teaches graceful handling of user input errors

#### 2. Confirmation on Delete 
- **Feature**: Shows confirmation dialog before deleting any contact
- **Implementation**: Custom AlertDialog with "Cancel" and "Delete" buttons
- **User Experience**: Displays "Are you sure you want to delete '[Contact Name]'?" message
- **Why**: Prevents accidental data loss and follows standard UX practices

#### 3. Search/Filter Functionality 
- **Feature**: Real-time search and filtering of contacts
- **Implementation**: Search TextField at the top that filters contacts as you type
- **Database**: Uses SQL `LIKE` clause with `WHERE name LIKE ?` for efficient searching
- **User Experience**: Instant filtering without needing to press a search button
- **Why**: Introduces real-time UI updates and advanced SQL queries

#### 4. Theming (Dark Mode) 
- **Feature**: Toggle between light and dark themes
- **Implementation**: Switch control in the header that changes `page.theme_mode`
- **User Experience**: Smooth transition between `ThemeMode.LIGHT` and `ThemeMode.DARK`
- **Why**: Teaches application theming and user preference management

#### 5. Refined UI 
- **Feature**: Modern card-based design with icons
- **Implementation**: 
  - Each contact displayed in a `ft.Card` instead of simple ListTile
  - Phone icon () next to phone numbers
  - Email icon () next to email addresses
  - Delete button with trash icon
  - Elevated buttons with proper styling
- **User Experience**: Visually appealing, professional-looking interface
- **Why**: Explores more Flet UI components for better visual design

## Additional Features

- **Success/Error Messages**: SnackBar notifications for all operations
- **Empty State Handling**: Friendly messages when no contacts exist or no search results
- **Form Clearing**: Clear button to reset all input fields
- **Responsive Design**: Proper spacing, padding, and layout
- **Error Handling**: Try-catch blocks for all database operations

## Installation

1. Make sure you have Python 3.7+ installed
2. Install dependencies:
   ```bash
   pip install flet
   ```

## Usage

Run the application:
```bash
cd src
python main.py
```

## How to Use

1. **Adding Contacts**: Fill in the name (required), phone, and email fields, then click "Add Contact"
2. **Searching**: Type in the search box to filter contacts in real-time
3. **Deleting**: Click the red trash icon on any contact card and confirm deletion
4. **Theme Toggle**: Use the "Dark Mode" switch in the top-right corner
5. **Clearing Form**: Click "Clear" to reset all input fields

## Project Structure

```
contact_book_app/
├── src/
│   ├── main.py          # Application entry point
│   ├── app_logic.py     # UI components and business logic
│   ├── database.py      # Database operations with search support
│   ├── assets/          # Static assets (if needed)
│   └── storage/         # Database storage directory (auto-created)
├── README.md
└── pyproject.toml
```

## Learning Outcomes

This implementation demonstrates:
- **Input validation** and error handling
- **Modal dialogs** and user confirmations
- **Real-time search** with database queries
- **Theme management** and UI state
- **Modern UI design** with cards and icons
- **Database operations** with SQLite
- **Event handling** and user interactions
- **Code organization** and separation of concerns

## Technical Details

- **Framework**: Flet (Python UI framework)
- **Database**: SQLite with parameterized queries
- **Architecture**: Modular design with separate database, UI, and main modules
- **UI Components**: Cards, TextFields, Buttons, Icons, Dialogs, SnackBars
- **Features**: Real-time search, theme switching, input validation, confirmation dialogs

## Run the app

### uv

Run as a desktop app:

```
uv run flet run
```

Run as a web app:

```
uv run flet run --web
```

### Poetry

Install dependencies from `pyproject.toml`:

```
poetry install
```

Run as a desktop app:

```
poetry run flet run
```

Run as a web app:

```
poetry run flet run --web
```

For more details on running the app, refer to the [Getting Started Guide](https://flet.dev/docs/getting-started/).

## Build the app

### Android

```
flet build apk -v
```

For more details on building and signing `.apk` or `.aab`, refer to the [Android Packaging Guide](https://flet.dev/docs/publish/android/).

### iOS

```
flet build ipa -v
```

For more details on building and signing `.ipa`, refer to the [iOS Packaging Guide](https://flet.dev/docs/publish/ios/).

### macOS

```
flet build macos -v
```

For more details on building macOS package, refer to the [macOS Packaging Guide](https://flet.dev/docs/publish/macos/).

### Linux

```
flet build linux -v
```

For more details on building Linux package, refer to the [Linux Packaging Guide](https://flet.dev/docs/publish/linux/).

### Windows

```
flet build windows -v
```

For more details on building Windows package, refer to the [Windows Packaging Guide](https://flet.dev/docs/publish/windows/).