import numpy as np
import matplotlib.pyplot as plt
import gradio as gr


def cagr_compare(beginning_value=20.0, annual_growth=20.0, years=30, interest_rate=0.00):


    # Arrays to store the results
    years_array = np.arange(1, years + 1)
    with_interest = (beginning_value + annual_growth * years_array).astype("f4")

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
    ax1.grid(True)

    # Plotting CAGR
    ax2.plot(years_array, with_interest_cagr, label="CAGR With Interest", color="blue")
    ax2.plot(years_array, without_interest_cagr, label="CAGR Without Interest", color="red")
    ax2.set_title("Compound Annual Growth Rate (CAGR) Over Time")
    ax2.set_xlabel("Years")
    ax2.set_ylabel("CAGR")
    ax2.legend()
    ax2.grid(True)

    plt.tight_layout()
    
    return fig

def cagr_compare_new(beginning_value=20.0, annual_growth=20.0, years=30, interest_rate=0.00):
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


if __name__ == "__main__":
    # Creating Gradio interface
    interface = gr.Interface(
        fn=cagr_compare_new,
        inputs=[
            gr.Slider(1, 100, value=20.0, label="Beginning Value", step=0.1),
            gr.Slider(1, 100, value=20.0, label="Annual Growth", step=0.1),
            gr.Slider(1, 50, value=30, label="Years", step=1),
            gr.Slider(0, 0.2, value=0.00, label="Interest Rate", step=0.01),
        ],
        outputs=gr.Plot(),
        title="CAGR Comparison",
        description="This tool compares the compound annual growth rate (CAGR) with and without interest over a specified number of years.",
    )
    interface.launch()