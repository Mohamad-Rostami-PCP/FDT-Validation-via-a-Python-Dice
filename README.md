
# 🎲 Fluctuation–Dissipation Validation via Dice Simulation

This project uses dice simulations to **numerically validate the Fluctuation–Dissipation Theorem (FDT)**.  
By rolling dice many times, the probabilities of outcomes and their fluctuations are compared with theoretical predictions.

---

## 📂 Code Structure
- **main.py** → generates random dice outcomes, computes probabilities, RMS fluctuations, and compares with theory.

---

## 🔑 Important Variables
- `N_throws` → number of dice throws  
- `faces` → number of sides (default: 6)  
- `bins` → histogram bins  

---

## ⚙️ How to Interact
1. Open **main.py**  
2. Change `N_throws` (e.g., from 10^3 to 10^6) to see how fluctuations shrink.  
3. Run:
   ```bash
   python main.py


---

## 🧠 Physical/Statistical Intuition

* The variance of probabilities scales as:

  $$
  \sigma \sim \frac{1}{\sqrt{N}}
  $$
* More dice → smoother probability distributions.
* Small `N` → large statistical fluctuations.

---

## 🧮 Numerical Models

* **Monte Carlo random sampling**
* **Law of Large Numbers**
* **Fluctuation–Dissipation scaling** (1/√N law)

```
