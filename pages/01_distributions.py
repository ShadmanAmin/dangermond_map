import solara
import plotly.express as px
import numpy as np
import scipy.stats as stats
import scipy

@solara.component
def Page():
    #Reactive states for slider values
    mu1, set_mean1 = solara.use_state(0.0)
    mu2, set_mean2 = solara.use_state(0.0)
    sigma1, set_std1 = solara.use_state(1.0)
    sigma2, set_std2 = solara.use_state(1.0)
    w1, set_weight1 = solara.use_state(0.5)

    with solara.Column():
        with solara.Sidebar():
            solara.Markdown("## Normal Distribution")
            solara.SliderFloat(label="Mean 1", value=mu1, min=-10.0, max=10.0, step=0.1, on_value=set_mean1)
            solara.SliderFloat(label = "Mean 2", value=mu2, min=-10.0, max=10.0, step=0.1, on_value=set_mean2)
            solara.SliderFloat(label="Standard Deviation 1", value=sigma1, min=0.1, max=10.0, step=0.1, on_value=set_std1)
            solara.SliderFloat(label="Standard Deviation 2", value=sigma2, min=0.1, max=10.0, step=0.1, on_value=set_std2)
            solara.SliderFloat(label="Weight 1", value=w1, min=0.0, max=1.0, step=0.01, on_value=set_weight1)

        #Main Content

        population_1 = stats.Normal(mu=mu1, sigma=sigma1)
        population_2 = stats.Normal(mu=mu2, sigma=sigma2)
        mixture = stats.Mixture([population_1, population_2], weights=[w1, 1-w1])
        

        data = mixture.sample(100000)
        fig_hist = px.histogram(data, nbins = 30, title="Histogram")
        fig_hist.update_layout(
            xaxis_title="Value",
            yaxis_title="Frequency",
            width = 600,
        )

        solara.Markdown("# Main Content Area")

        solara.FigurePlotly(fig_hist)

        solara.Markdown("## Mixture Distribution Stats")
        solara.Markdown(f"**Mean:** {mixture.mean()}")
        solara.Markdown(f"**Standard Deviation:** {mixture.standard_deviation()}")
        solara.Markdown(f"**Skewness:** {mixture.skewness()}")
        solara.Markdown(f"**Kurtosis:** {mixture.kurtosis()}")
        solara.Markdown(f"**Entropy:** {mixture.entropy()}")
        solara.Markdown(f"**Weight 1:** {w1}")
        solara.Markdown(f"**Weight 2:** {1-w1}")
        solara.Markdown(f"**Mean 1:** {mu1}")
        solara.Markdown(f"**Mean 2:** {mu2}")
        solara.Markdown(f"**Standard Deviation 1:** {sigma1}")
        solara.Markdown(f"**Standard Deviation 2:** {sigma2}")