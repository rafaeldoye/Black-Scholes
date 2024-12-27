import numpy as np
from scipy.stats import norm
from datetime import datetime

# Black-Scholes Option Pricing Model
def black_scholes(S, K, T, r, sigma, option_type="call"):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == "call":
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")
    
    return price

# Greeks calculations
def delta(S, K, T, r, sigma, option_type="call"):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    if option_type == "call":
        return norm.cdf(d1)
    elif option_type == "put":
        return norm.cdf(d1) - 1

def gamma(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    return norm.pdf(d1) / (S * sigma * np.sqrt(T))

def vega(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    return S * norm.pdf(d1) * np.sqrt(T)

def theta(S, K, T, r, sigma, option_type="call"):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    if option_type == "call":
        term1 = -(S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T))
        term2 = -r * K * np.exp(-r * T) * norm.cdf(d2)
        return term1 + term2
    elif option_type == "put":
        term1 = -(S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T))
        term2 = r * K * np.exp(-r * T) * norm.cdf(-d2)
        return term1 + term2

def rho(S, K, T, r, sigma, option_type="call"):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    if option_type == "call":
        return K * T * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        return -K * T * np.exp(-r * T) * norm.cdf(-d2)

# Sensitivity Analysis
def sensitivity_analysis(S, K, T, r, sigma, option_type="call"):
    d = delta(S, K, T, r, sigma, option_type)
    g = gamma(S, K, T, r, sigma)
    v = vega(S, K, T, r, sigma)
    t = theta(S, K, T, r, sigma, option_type)
    rh = rho(S, K, T, r, sigma, option_type)

    return {
        "Delta": d,
        "Gamma": g,
        "Vega": v,
        "Theta": t,
        "Rho": rh
    }

# Example Usage
if __name__ == "__main__":
    # User inputs
    option_type = input("Enter option type (call/put): ").strip().lower()
    S = float(input("Enter current stock price (S): "))
    K = float(input("Enter strike price (K): "))
    maturity_date = input("Enter maturity date (YYYY-MM-DD): ")
    r = float(input("Enter risk-free interest rate (r) as a decimal (e.g., 0.05 for 5%): "))
    sigma = float(input("Enter volatility (sigma) as a decimal (e.g., 0.2 for 20%): "))

    # Calculate time to maturity
    today = datetime.today()
    maturity = datetime.strptime(maturity_date, "%Y-%m-%d")
    T = (maturity - today).days / 365.0

    # Perform sensitivity analysis
    greeks = sensitivity_analysis(S, K, T, r, sigma, option_type)
    option_price = black_scholes(S, K, T, r, sigma, option_type)

    # Output initial results
    print("\nOption Price:")
    print(f"{option_price:.4f}")
    print("\nSensitivity Analysis of Greeks:")
    for greek, value in greeks.items():
        print(f"{greek}: {value:.4f}")

    # Update parameters and recalculate
    while True:
        update = input("\nDo you want to update any parameters to see the new Greeks? (yes/no): ").strip().lower()
        if update == "no":
            break
        elif update == "yes":
            print("\nWhich parameter would you like to update?")
            print("1. Stock price (S)")
            print("2. Strike price (K)")
            print("3. Maturity date")
            print("4. Risk-free interest rate (r)")
            print("5. Volatility (sigma)")
            choice = input("Enter the number of your choice: ").strip()

            if choice == "1":
                S = float(input("Enter new stock price (S): "))
            elif choice == "2":
                K = float(input("Enter new strike price (K): "))
            elif choice == "3":
                maturity_date = input("Enter new maturity date (YYYY-MM-DD): ")
                maturity = datetime.strptime(maturity_date, "%Y-%m-%d")
                T = (maturity - today).days / 365.0
            elif choice == "4":
                r = float(input("Enter new risk-free interest rate (r) as a decimal: "))
            elif choice == "5":
                sigma = float(input("Enter new volatility (sigma) as a decimal: "))
            else:
                print("Invalid choice. Please try again.")
                continue

            # Recalculate Greeks and option price
            greeks = sensitivity_analysis(S, K, T, r, sigma, option_type)
            option_price = black_scholes(S, K, T, r, sigma, option_type)

            print("\nUpdated Option Price:")
            print(f"{option_price:.4f}")
            print("\nUpdated Sensitivity Analysis of Greeks:")
            for greek, value in greeks.items():
                print(f"{greek}: {value:.4f}")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
