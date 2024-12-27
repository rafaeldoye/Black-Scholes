# Black-Scholes Option Pricing with Greeks Analysis
This Python program calculates the price of options using the Black-Scholes model and provides a detailed sensitivity analysis of Greeks, including Delta, Gamma, Vega, Theta, and Rho. It also allows users to update parameters interactively to observe changes in the Greeks and option prices.



# Features

- **Option Pricing**: Computes the price of European call and put options using the Black-Scholes formula.
- **Greeks Analysis**: Calculates the sensitivities (Delta, Gamma, Vega, Theta, Rho) for a given option.
- **Interactive Mode**: Allows users to update parameters (stock price, strike price, maturity, risk-free rate, volatility) to see real-time updates to Greeks and option prices.
- **User-Friendly Input**: Guides users through input steps for accurate calculations.



## **How It Works**

1. **User Inputs**:
   - Option type: Call or Put
   - Current stock price (S)
   - Strike price (K)
   - Maturity date (YYYY-MM-DD)
   - Risk-free interest rate (r) as a decimal (e.g., `0.05` for 5%)
   - Volatility (σ) as a decimal (e.g., `0.2` for 20%)

2. **Black-Scholes Model**:
   - Computes the option price using the following formula:
     - Call option price: 
     - Put option price: 

3. **Sensitivity Analysis (Greeks)**:
   - Delta: Sensitivity to stock price changes.
   - Gamma: Sensitivity of Delta to stock price changes.
   - Vega: Sensitivity to volatility changes.
   - Theta: Sensitivity to time decay.
   - Rho: Sensitivity to changes in the risk-free rate.

4. **Interactive Parameter Updates**:
   - Modify parameters to see updated option prices and Greeks.

---

## **Requirements**

- Python 3.x
- Libraries:
  - `numpy`
  - `scipy`

Install required libraries using pip:
```bash
pip install numpy scipy
```

---

## **Usage**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/black-scholes-option-pricing.git
   cd black-scholes-option-pricing
   ```

2. **Run the Program**:
   ```bash
   python black_scholes.py
   ```

3. **Follow the Prompts**:
   - Enter the required inputs when prompted (option type, stock price, strike price, etc.).
   - View the calculated option price and Greeks.

4. **Update Parameters**:
   - Choose to update parameters interactively and observe how the option price and Greeks change.

---

## **Example Output**

### Initial Results:
```plaintext
Enter option type (call/put): call
Enter current stock price (S): 100
Enter strike price (K): 105
Enter maturity date (YYYY-MM-DD): 2025-01-01
Enter risk-free interest rate (r) as a decimal (e.g., 0.05 for 5%): 0.03
Enter volatility (sigma) as a decimal (e.g., 0.2 for 20%): 0.25

Option Price:
10.5724

Sensitivity Analysis of Greeks:
Delta: 0.5834
Gamma: 0.0158
Vega: 39.4745
Theta: -0.0452
Rho: 22.9174
```

### Updated Results:
```plaintext
Do you want to update any parameters to see the new Greeks? (yes/no): yes

Which parameter would you like to update?
1. Stock price (S)
2. Strike price (K)
3. Maturity date
4. Risk-free interest rate (r)
5. Volatility (sigma)
Enter the number of your choice: 1
Enter new stock price (S): 110

Updated Option Price:
15.8924

Updated Sensitivity Analysis of Greeks:
Delta: 0.6835
Gamma: 0.0137
Vega: 37.2604
Theta: -0.0387
Rho: 31.2875
