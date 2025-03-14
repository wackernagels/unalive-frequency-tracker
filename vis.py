import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

#reading our data in
df = pd.read_csv('cleaned_data.csv')
df['date']= pd.to_datetime(df["date"])

#initializing the empty graph
postvis= make_subplots(rows=2,
                       cols=1,
                       vertical_spacing= 0.05,
                       shared_xaxes=True)

#adding in line plot format for unalive
postvis.add_trace(
    go.Scatter(x=df['date'],
               y=df['unalive'],
               name='unalive', 
               line_shape='spline'),
    row=1, col=1,
)
#scatterplot for kill
postvis.add_trace(
    go.Scatter(x=df['date'],
               y=df['kill'],
               name='kill',
               line_shape='spline'),
    row=1, col=1,
)
#murder
postvis.add_trace(
    go.Scatter(x=df['date'],
               y=df['murder'],
               name='murder',
               line_shape='spline'),
    row=1, col=1,
)
#suicide
postvis.add_trace(
    go.Scatter(x=df['date'],
               y=df['suicide'],
               name='suicide',
               line_shape='spline'),
    row=1, col=1,
)

#adding hover for the graph
postvis.update_traces(mode="lines", hovertemplate=None)
postvis.update_layout(hovermode="x unified")

#adding bar chart vis
postvis.add_trace(
    go.Bar(
        x=df['date'],
        y=df['unalive'],
        name='unalive',
        marker_color='#636EFA'),
    row=2, col=1,
)
postvis.add_trace(
    go.Bar(
        x=df['date'],
        y=df['kill'],
        name='kill',
        marker_color='#EF553B'),
    row=2, col=1,
)
postvis.add_trace(
    go.Bar(
        x=df['date'],
        y=df['murder'],
        name='murder',
        marker_color='#00CC96'),
    row=2, col=1,
)
postvis.add_trace(
    go.Bar(
        x=df['date'],
        y=df['suicide'],
        name='suicide',
        marker_color='#AB63FA'),
    row=2, col=1,
)

postvis.update_layout(barmode='stack')

postvis.update_layout(
    plot_bgcolor='#f4f4f4',
    paper_bgcolor='white',
    #adding title to vis
    title= 'Number of Posts on r/offmychest Containing Killing-Related Words, 2019-2024',
    #setting range of axis
    yaxis_range=[0, 70],
    #adding axis label and slider for specifying time range
    xaxis2=dict(
        title=dict(
            text="Time"),
        #adding slider for dates
        rangeslider=dict(
            visible=True
        ),
        type="date"
    ),
    #labeling axis
    yaxis=dict(
        gridcolor='lightgrey',
        title=dict(
            text="Number of Posts"
        )
    ),
    yaxis2=dict(
        gridcolor='lightgrey',
        title=dict(
            text="Number of Posts"
        )
    ),
)



#-----------END updating postvis visuals---------

#showing post vis
#postvis.show()
postvis.write_html("vis.html")

#scatterplot to show frequency of words vs posts?
#wordvis= px.scatter(df_bar, x="Fruit", y="Amount", color="City", barmode="group")
