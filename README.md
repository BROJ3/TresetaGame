# TresetaGame
A Python representation of the old Italian card game "Triestine" (Tressette) using Object-Oriented Programming (OOP).

## **Features**
### **Implemented Mechanics**
- **Object-Oriented Structure**
  - Classes for `Deck`, `Player`, `Card`, and `Game Logic`.
  - Encapsulation of card logic, shuffling, and dealing.
  
- **Game Flow & Turn Management**
  - Alternating turns between players.
  - Enforcing suit-following rules.
  - Keeping track of rounds and the last-hand winner.

- **Card Handling**
  - Shuffling and dealing a deck of 40 cards.
  - Moving cards through different stages:
    - `Deck` → `Player Hands` → `Playing Stack` → `Scoring Stack`
  - Automatic winner determination per round.

- **Scoring System**
  - Tracks points based on traditional Tressette rules.
  - Awards extra points to the last-hand winner.

- **Game End Condition**
  - Ends when all cards have been played.
  - Displays total player scores.

---

### **Future Improvements**
✅ **Planned Features**
- [ ] **GUI Development** (e.g., `tkinter` or `pygame`)
- [ ] **AI Opponent (Bot Player)**
- [ ] **Machine Learning Integration** (AI learning card strategies)
- [ ] **Online Multiplayer Mode**

This project demonstrates OOP principles, structured game flow, and logic-based decision-making in Python.
