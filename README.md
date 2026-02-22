# Smart-Parking-System

## Overview

The Smart Parking System is an automated parking management solution that detects vehicle presence in parking slots and displays their availability in real time. The system integrates hardware (Arduino and IR sensors) with software (Python GUI) to provide a user-friendly interface for monitoring parking spaces.

This project aims to reduce the time spent searching for parking, improve space utilization, and enhance overall efficiency in parking management.

---

## Objectives

- Detect vehicle presence automatically using sensors
- Display real-time parking slot status
- Reduce traffic congestion caused by parking search
- Provide a simple and intuitive user interface
- Improve parking space utilization

---

## System Components

### Hardware

- Arduino Uno (microcontroller)
- IR Sensors (6 units)
- Power supply
- USB connection to computer

### Software

- Python
- Tkinter (GUI framework)
- PySerial (for serial communication)
- PIL (for image processing)

---

## Working Principle

1. IR sensors monitor each parking slot continuously.
2. When a vehicle is present, reflected infrared light changes the sensor output.
3. Arduino processes sensor signals and determines slot status.
4. Data is sent to the computer via serial communication.
5. The Python GUI updates instantly to display slot availability.

---

## Graphical User Interface

The GUI displays parking slots visually:

- Occupied Slot → Car image with red background
- Empty Slot → "Empty!!!" text with green background
- Automatic real-time updates

---

## Pin Configuration

Each IR sensor is connected to Arduino digital pins:

- Sensor 1 → D2
- Sensor 2 → D3
- Sensor 3 → D4
- Sensor 4 → D5
- Sensor 5 → D6
- Sensor 6 → D7

All VCC pins are connected to 5V, and all GND pins to Arduino GND.

---

## Key Features

- Real-time parking status monitoring
- Automatic vehicle detection
- Visual representation of slot availability
- User-friendly interface
- Efficient space management
- Scalable system design

---

## Applications

- Shopping malls
- Office buildings
- Public parking areas
- Smart city infrastructure
- Event parking management

---

## Advantages

- Saves time for drivers
- Reduces traffic congestion
- Improves parking efficiency
- Low-cost implementation
- Easy to install and expand

---

## Future Enhancements

- Mobile application integration
- IoT-based cloud monitoring
- Online slot reservation system
- Automatic billing system
- Camera-based vehicle detection

---

## Technologies Used

- Arduino
- Embedded C (Arduino code)
- Python
- Tkinter
- Serial Communication

---

## Conclusion

The Smart Parking System demonstrates how hardware and software can be integrated to solve real-world problems efficiently. By providing real-time parking information through an intuitive interface, the system enhances convenience, reduces search time, and improves parking management.
