# Hotel Booking System

A simple command-line hotel booking system built with Python.

The system allows users to manage hotels, rooms, customers and bookings while the program is running.

## Features

- Display all hotels
- Display available rooms
- Display customers
- Register new customers
- Create new bookings
- Display existing bookings
- Cancel bookings
- Automatically generate unique booking IDs
- Track room availability
- Manage relationships between hotels, rooms, customers and bookings
- Validate customer age
- Validate customer names
- Validate booking dates
- Prevent invalid date ranges
- Handle invalid menu input
- Handle invalid hotel, customer and booking IDs
- Prevent booking unavailable rooms

## Project Structure

```text
Hotel-Booking/
│
├── book_system.py
├── booking.py
├── customer.py
├── hotel.py
├── room.py
└── README.md
```

## Classes

### Hotel

- Stores hotel information
- Contains rooms and bookings
- Checks room availability
- Saves bookings
- Cancels bookings

### Room

- Stores room information
- Tracks whether a room is available

### Customer

- Stores customer information such as ID, name and age

### Booking

- Connects a hotel, room and customer
- Stores booking dates and price
- Generates a unique booking ID

## Validation

The system validates user input to prevent invalid actions, including:

- Empty customer names
- Invalid customer ages
- Invalid menu options
- Invalid hotel IDs
- Invalid customer IDs
- Invalid booking IDs
- Invalid date formats
- End dates that are before or equal to start dates
- Booking unavailable rooms

## How to Run

Make sure Python 3 is installed.

Open the project folder in a terminal and run:

```bash
python3 book_system.py
```

The program will display a menu where you can choose different actions.

## Data

The project uses Python lists and dictionaries to create the initial data.

No database or permanent data storage is required. All changes only exist while the program is running.

## Technologies

- Python 3
- Object-Oriented Programming
- Lists
- Dictionaries
- Functions
- Loops
- Conditional statements
- List comprehensions
- `next()`
- UUID
- `datetime`