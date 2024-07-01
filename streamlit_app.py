import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def cagr_compare(beginning_value=20.0, annual_growth=20.0, years=30, interest_rate=0.00):
    # Arrays to store the results
    years_array = np.arange(1, years + 1)
    with_interest = beginning_value + annual_growth * years_array
    with_interest = with_interest.astype("f4")
    
    without_interest = with_interest.copy()

    for y in range(years - 1):
        with_interest[y + 1:] += with_interest[y] * interest_rate

    calc_cagr_values = lambda ending_values: ((ending_values / beginning_value) ** (1 / years_array)) - 1

    with_interest_cagr = calc_cagr_values(with_interest)
    without_interest_cagr = calc_cagr_values(without_interest)

    # Plotting the results on the same figure
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 12))

    # Plotting value growth
    ax1.plot(years_array, with_interest, label="With Interest", color="blue")
    ax1.plot(years_array, without_interest, label="Without Interest", color="red")
    ax1.set_title("Value Growth Over Time")
    ax1.set_xlabel("Years")
    ax1.set_ylabel("Value")
    ax1.legend()
    ax1.grid(True, which='both', linestyle='--', linewidth=0.5)
    ax1.minorticks_on()

    # Annotate value growth plot
    for i in range(0, years, max(1, years // 10)):
        ax1.annotate(f'{with_interest[i]:.1f}', (years_array[i], with_interest[i]), textcoords="offset points", xytext=(0,10), ha='center')
        ax1.annotate(f'{without_interest[i]:.1f}', (years_array[i], without_interest[i]), textcoords="offset points", xytext=(0,-15), ha='center')

    # Plotting CAGR
    ax2.plot(years_array, with_interest_cagr, label="CAGR With Interest", color="blue")
    ax2.plot(years_array, without_interest_cagr, label="CAGR Without Interest", color="red")
    ax2.set_title("Compound Annual Growth Rate (CAGR) Over Time")
    ax2.set_xlabel("Years")
    ax2.set_ylabel("CAGR")
    ax2.legend()
    ax2.grid(True, which='both', linestyle='--', linewidth=0.5)
    ax2.minorticks_on()

    # Annotate CAGR plot
    for i in range(0, years, max(1, years // 10)):
        ax2.annotate(f'{with_interest_cagr[i]:.4f}', (years_array[i], with_interest_cagr[i]), textcoords="offset points", xytext=(0,10), ha='center')
        ax2.annotate(f'{without_interest_cagr[i]:.4f}', (years_array[i], without_interest_cagr[i]), textcoords="offset points", xytext=(0,-15), ha='center')

    plt.tight_layout()
    
    return fig
def main():
    st.title("CAGR Comparison Tool")
    st.write("This tool compares the compound annual growth rate (CAGR) with and without interest over a specified number of years.")

    # Creating sliders
    beginning_value = st.slider("Beginning Value", min_value=1.0, max_value=2000.0, value=20.0, step=1.)
    annual_growth = st.slider("Annual Growth", min_value=1.0, max_value=200.0, value=20.0, step=0.1)
    years = st.slider("Years", min_value=1, max_value=50, value=30)
    interest_rate = st.slider("Interest Rate", min_value=0.0, max_value=0.20, value=0.00, step=0.01)

    # Button to generate plot
    if st.button('Calculate CAGR'):
        fig = cagr_compare(beginning_value, annual_growth, years, interest_rate)
        st.pyplot(fig)

if __name__ == "__main__":
    main()
