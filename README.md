# Enigma Simulator

A Python-based simulation of the legendary Enigma machine, the cipher device famously used during World War II. This project lets you encrypt and decrypt messages, experiment with rotor configurations, and get hands-on experience with historical cryptography with how the encryption happens in it

---

## About
- The Enigma Simulator is an interactive program that replicates the behavior of the real Enigma machine:

-  Step rotors and encrypt letters as the machine would

- Configure the plugboard to swap letters before and after encryption

- Experiment with different reflector types for varied cipher behavior

- See the encryption process in real time

- This project is designed for learners, hobbyists, and anyone fascinated by cryptography history

**Note:** There are some known flaws in the current plugboard implementation. These may affect certain letter pairings. A fix is planned in a future update.

---

## Features
- **Custom Rotor Setup:** Choose which rotors to use and set their starting positions

- **Plugboard Configuration:** Pair letters to modify the cipher path (with minor known issues)

- **Reflector Options:** Select from multiple reflectors to change encryption behavior

- **Interactive Simulation:** Type messages and watch them encrypt letter by letter

- **Educational:** Step-by-step visualization of rotor movements and letter flow

---

## Prerequisites
- Python 3.8 or greater
- pygame

---
## Setup
#### 1. Clone the repository:
```bash
git clone https://github.com/justaguy1337/Enigma-Simulator.git
```

#### 2. Navigate into the project folder:
```bash
cd Enigma-Simulator
```

#### 3. Install dependencies:
```bash
pip install pygame
```

#### 4. Run the simulator:
```bash
python3 main.py
```

### Controls
- Keys Left , Down , Right Arrow for changing rotor position
- Use the Dropdown box to change Reflector and Rotors
  
---

## Usage
1. *Start the program*

2. *Configure your Enigma machine:*

    - Select rotors and their starting positions

    - Set up plugboard connections (beware of loop connectivity)

    - Pick a reflector

3. *Enter the message to encrypt*

4. *View the encrypted output*

5. *To decrypt, use the same settings and enter the ciphertext*

---

## Resources
- [Enigma Machine – Wikipedia](https://en.wikipedia.org/wiki/Enigma_machine)
- [Enigma Breaking Rotors](https://en.wikipedia.org/wiki/Enigma_rotor_details)
- [Implementing Enigma](https://medium.com/analytics-vidhya/how-to-build-an-enigma-machine-virtualisation-in-python-b5476a1fd922)
