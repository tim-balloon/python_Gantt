import plotly.express as px
import pandas as pd

df = pd.DataFrame([

    dict(Task="Flight", Start='2026-04-01', Finish='2026-04-30', Resource="Collab.", Label='Packing<br>planning<br>&org'),
    dict(Task="Flight", Start='2026-06-01', Finish='2026-06-30', Resource="Collab.", Label='Palestine<br>integration'),
    dict(Task="Flight", Start='2026-08-01', Finish='2026-08-30', Resource="Collab.", Label='Ship MCM'),
    dict(Task="Flight", Start='2026-07-01', Finish='2026-08-30', Resource="Collab.", Label='Personal prep.'),
    dict(Task="Flight", Start='2026-11-01', Finish='2026-11-30', Resource="Collab.", Label='Arrive MCM'),
    dict(Task="Flight", Start='2026-12-01', Finish='2026-12-30', Resource="Collab.", Label='Declare<br>flight ready'),
    dict(Task="Flight", Start='2027-01-01', Finish='2027-01-30', Resource="Collab.", Label='FLIGHT'),
    dict(Task="Flight", Start='2027-02-01', Finish='2027-02-28', Resource="Collab.", Label='Pack<br>&leave'),
    dict(Task="Flight", Start='2028-09-01', Finish='2028-09-30', Resource="Collab.", Label='End<br>of<br>Grant'),

    dict(Task="Map<br>Making", Start='2026-07-01', Finish='2027-03-30', Resource="Map making team", Label='Dev. Mapmaker'),
    dict(Task="Map<br>Making", Start='2026-09-01', Finish='2026-09-30', Resource="", Label='Namap<br>ready'),
    dict(Task="Map<br>Making", Start='2024-11-01', Finish='2024-11-30', Resource="Map making team", Label='read<br>other<br>data<br>format'),
    dict(Task="Map<br>Making", Start='2024-12-01', Finish='2025-01-30', Resource="Map making team", Label='Implement<br>freqs'),
    dict(Task="Map<br>Making", Start='2025-02-01', Finish='2025-02-28', Resource="Map making team", Label='Discuss<br>in-flight<br>plots'),
    dict(Task="Map<br>Making", Start='2026-02-01', Finish='2026-02-28', Resource="Map making team", Label='Lock-in<br>scan<br>patterns<br>&pointings'),
    dict(Task="Map<br>Making", Start='2027-8-01', Finish='2027-8-30', Resource="Map making team", Label='1st<br>[CII]<br>maps'),

    dict(Task="Forecast suite", Start='2026-09-01', Finish='2027-03-30', Resource="Forecast", Label='forecasts<br>available<br>on<br>repo'),
    dict(Task="Calibration Strategy", Start='2024-11-01', Finish='2024-12-30', Resource="Analysis", Label='What<br>do<br>we<br>need'),
    dict(Task="Calibration Strategy", Start='2025-04-01', Finish='2025-09-30', Resource="Analysis", Label='Raw (I-Q)<br>to<br>power'),
    dict(Task="Calibration Strategy", Start='2027-03-01', Finish='2027-06-30', Resource="Analysis", Label='Raw data <br>&Instru perfs.'),
    dict(Task="Science Analysis", Start='2027-05-01', Finish='2027-05-30', Resource="Analysis", Label='What<br>null test<br>jacknife'),
    dict(Task="Science Analysis", Start='2027-08-01', Finish='2027-10-30', Resource="Analysis", Label='Power spectra pipeline'),
    
    dict(Task="SMG obs. forecast", Start='2024-11-01', Finish='2025-01-30', Resource="PointObs", Label='Forecast<br>integration<br>time'),
    dict(Task="SMG obs. forecast", Start='2025-02-01', Finish='2025-02-28', Resource="PointObs", Label='CO<br>z=0<br>targets'),
    dict(Task="SMG obs. forecast", Start='2026-07-01', Finish='2026-07-30', Resource="PointObs", Label='Review+<br>&Publication'),

    #dict(Task="Final map making", Start='2027-04-01', Finish='2027-04-30', Resource="Analysis", Label='We start build data map.'),
    #dict(Task="Final map making", Start='2027-09-01', Finish='2027-09-30', Resource="Analysis", Label='1st TIM CII maps'),
    dict(Task="Publication", Start='2027-04-01', Finish='2027-06-30', Resource="Collab.", Label='Decide<br>series<br>papers'),
    dict(Task="Publication", Start='2027-11-01', Finish='2028-01-30', Resource="Collab.", Label='Writing<br>time'),
    dict(Task="Publication", Start='2028-02-15', Finish='2028-03-30', Resource="Collab.", Label='Collab.<br>Review'),
    dict(Task="Publication", Start='2028-04-01', Finish='2028-05-30', Resource="Collab.", Label='Published<br>papers'),
    dict(Task="Publication", Start='2028-06-01', Finish='2028-07-30', Resource="Collab.", Label='LIM28'),

    #dict(Task="Science extraction", Start='2028-06-15', Finish='2028-08-30', Resource="Analysis", Label='Process the science cubes'),
      
])

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Resource", text='Label')
fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up
# Set tighter x-axis limits if needed
fig.update_xaxes(title='', range=['2024-10-01', '2028-09-30'])

# Show, center, and increase the font size of labels inside the bars
fig.update_traces(textposition="inside", texttemplate="%{text}", insidetextanchor="middle",textangle=0,
                  textfont=dict(size=10))  # Increase font size to 14

# Update layout for compact view
fig.update_layout(margin=dict(t=30, l=30, b=30, r=30), height=600)


fig.show()


