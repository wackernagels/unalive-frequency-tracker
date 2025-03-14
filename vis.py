import plotly.express as px
import plotly.graph_objects as go
import plotly as p
import pandas as pd

#reading our data in
df = pd.read_csv('cleaned_data.csv')
df['date']= pd.to_datetime(df["date"])

#initializing the empty graph
postvis= go.Figure()

#adding in scatterplot for unalive
postvis.add_trace(
    go.Scatter(x=df['date'],
               y=df['unalive'],
               name='unalive', 
               line_shape='spline')
)
#scatterplot for kill
postvis.add_trace(
    go.Scatter(x=df['date'],
               y=df['kill'],
               name='kill',
               line_shape='spline')
)
#murder
postvis.add_trace(
    go.Scatter(x=df['date'],
               y=df['murder'],
               name='murder',
               line_shape='spline')
)
#suicide
postvis.add_trace(
    go.Scatter(x=df['date'],
               y=df['suicide'],
               name='suicide',
               line_shape='spline')
)

#updating the layout
postvis.update_layout(
    #adding title to vis
    title= 'Number of Posts on r/offmychest Containing Certain Words, 2019-2024',
    #setting range of axis
    yaxis_range=[0, 70],
    #adding axis label and slider for specifying time range
    xaxis=dict(
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
        title=dict(
            text="Number of Posts"
        )
    ),
    updatemenus=[
        dict(
            type="buttons",
            buttons=[
                dict(label="2019",
                     method="relayout",
                     args=["xaxis", {'range':('2019-01-01', '2019-12-31'),
                                    'rangeslider':dict(visible=True),}]),
                dict(label="2020",
                     method="relayout",
                     args=["xaxis", {'range':('2020-01-01', '2020-12-31'),
                                    'rangeslider':dict(visible=True),}]),
                dict(label="2021",
                     method="relayout",
                     args=["xaxis", {'range':('2021-01-01', '2021-12-31'),
                                    'rangeslider':dict(visible=True),}]),
                dict(label="2022",
                     method="relayout",
                     args=["xaxis", {'range':('2022-01-01', '2022-12-31'),
                                    'rangeslider':dict(visible=True),}]),
                dict(label="2023",
                     method="relayout",
                     args=["xaxis", {'range':('2023-01-01', '2023-12-31'),
                                    'rangeslider':dict(visible=True),}]),
                dict(label="2024",
                     method="relayout",
                     args=["xaxis", {'range':('2024-01-01', '2024-12-31'),
                                    'rangeslider':dict(visible=True),}])]
        )],
)

#adding buttons to set slider for certain years
postvis.update_layout(
    
)

#adding hover for the graph
postvis.update_traces(mode="lines", hovertemplate=None)
postvis.update_layout(hovermode="x unified")

#-----------END updating postvis visuals---------

#showing post vis
#postvis.show()
postvis.write_html("vis.html")

#scatterplot to show frequency of words vs posts?
#wordvis= px.scatter(df_bar, x="Fruit", y="Amount", color="City", barmode="group")
