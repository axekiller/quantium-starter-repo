import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load the output data
df = pd.read_csv("data/output.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

app = dash.Dash(__name__)

app.layout = html.Div([

    html.H1("Soul Foods – Pink Morsel Sales Visualiser",
            style={
                "textAlign": "center",
                "color": "#ff6b6b",
                "fontFamily": "Arial, sans-serif",
                "padding": "20px",
                "backgroundColor": "#1a1a2e",
                "margin": "0"
            }),

    html.Div([
        html.Label("Filter by Region:",
                   style={"color": "white", "fontFamily": "Arial, sans-serif",
                          "fontSize": "16px", "marginBottom": "10px"}),
        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "South", "value": "south"},
                {"label": "East", "value": "east"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            inline=True,
            style={"color": "white", "fontFamily": "Arial, sans-serif"},
            labelStyle={"marginRight": "20px", "fontSize": "15px"}
        )
    ], style={
        "backgroundColor": "#16213e",
        "padding": "20px 40px",
        "borderBottom": "2px solid #ff6b6b"
    }),

    dcc.Graph(id="sales-chart"),

], style={"backgroundColor": "#1a1a2e", "minHeight": "100vh", "margin": "0"})


@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(region):
    if region == "all":
        filtered = df.groupby("date", as_index=False)["sales"].sum()
    else:
        filtered = df[df["region"] == region].groupby("date", as_index=False)["sales"].sum()

    fig = px.line(filtered, x="date", y="sales",
                  labels={"date": "Date", "sales": "Total Sales ($)"},
                  title=f"Pink Morsel Sales — {region.capitalize()}")

    fig.update_traces(line_color="#ff6b6b", line_width=2)
    fig.update_layout(
        plot_bgcolor="#16213e",
        paper_bgcolor="#1a1a2e",
        font_color="white",
        title_font_size=20,
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor="#2a2a4a")
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)